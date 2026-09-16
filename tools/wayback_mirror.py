"""Rebuild a navigable static copy of an old website from the Internet Archive.

Starts from one snapshot, follows every in-scope link (href/src/background/...) by asking
the Wayback Machine for the capture nearest to the start timestamp, saves the original
bytes (id_ mode, no Wayback toolbar) and rewrites links:
  - in-scope pages that were archived  -> relative local paths
  - in-scope pages never archived      -> the Wayback URL (so the link still goes somewhere)
  - external links                     -> the Wayback URL at the same timestamp
A small banner is injected in every HTML page, and a manifest.json records what was found.

Usage:
  python tools/wayback_mirror.py <name> <start_url> <timestamp> <scope_prefix> <outdir> "<banner title>"

The CDX API was offline when this was written, so discovery is by crawling only.
"""
import io
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit, quote, unquote

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36"
WB = "https://web.archive.org/web/"
LINK_RE = re.compile(rb"""(?P<attr>\b(?:href|src|background|lowsrc|action|data)\s*=\s*)(?P<q>["']?)(?P<url>[^"'\s>]+)(?P=q)""", re.I)
CSS_URL_RE = re.compile(rb"""url\(\s*(?P<q>["']?)(?P<url>[^"')\s]+)(?P=q)\s*\)""", re.I)
MAX_PAGES = 3000
DELAY = 1.2


def canon(url):
    """Normalise an original URL: lowercase host, drop :80, drop fragment."""
    s = urlsplit(url.strip())
    host = (s.hostname or "").lower()
    port = f":{s.port}" if s.port and s.port not in (80, 443) else ""
    path = s.path or "/"
    return urlunsplit(("http", host + port, path, s.query, ""))


def in_scope(url, scope):
    return canon(url).lower().startswith(scope.lower())


def local_path(url, scope_host_root):
    """Map an original URL to a path inside the output folder."""
    s = urlsplit(canon(url))
    path = unquote(s.path)
    if path.endswith("/"):
        path += "index.html"
    name = path.lstrip("/")
    if s.query:
        stem, dot, ext = name.rpartition(".")
        safe_q = re.sub(r"[^A-Za-z0-9_.-]+", "_", s.query)[:80]
        name = f"{stem}__{safe_q}.{ext}" if dot else f"{name}__{safe_q}"
    # .shtml/.php etc. served as static HTML need an .html twin name for browsers
    return name


def fetch(url, ts):
    """Return (bytes, content_type, capture_timestamp, status) for the capture nearest ts."""
    wb = f"{WB}{ts}id_/{url}"
    for attempt in range(5):
        req = urllib.request.Request(wb, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
                final = r.geturl()
                m = re.search(r"/web/(\d{14})", final)
                return data, r.headers.get("Content-Type", ""), (m.group(1) if m else ts), r.status
        except urllib.error.HTTPError as e:
            if e.code in (404, 403):
                return None, "", None, e.code
            time.sleep(5 * (attempt + 1))
        except Exception:
            time.sleep(5 * (attempt + 1))
    return None, "", None, "error"


def is_html(ctype, name, data):
    if "html" in (ctype or "").lower():
        return True
    if re.search(r"\.(s?html?|php3?|asp|cgi)$", name, re.I):
        return True
    return bool(data) and data[:600].lstrip().lower().startswith((b"<html", b"<!doctype html", b"<head", b"<body"))


def extract_links(data, base):
    out = []
    for m in LINK_RE.finditer(data):
        out.append(m.group("url").decode("latin-1"))
    for m in CSS_URL_RE.finditer(data):
        out.append(m.group("url").decode("latin-1"))
    links = []
    for u in out:
        u = u.strip()
        if not u or u.startswith(("#", "mailto:", "javascript:", "news:", "ftp:", "irc:", "data:")):
            continue
        links.append(urljoin(base, u))
    return links


def main():
    name, start, ts, scope, outdir, title = sys.argv[1:7]
    scope = canon(scope)
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    queue, seen, pages = [canon(start)], set(), {}
    while queue and len(pages) < MAX_PAGES:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        data, ctype, cap_ts, status = fetch(url, ts)
        time.sleep(DELAY)
        rel = local_path(url, scope)
        rec = {"url": url, "status": status, "capture": cap_ts, "type": ctype, "local": None}
        pages[url] = rec
        if data is None:
            print(f"MISS {status} {url}", flush=True)
            continue
        html = is_html(ctype, rel, data)
        if html and re.search(r"\.(gif|jpe?g|png|bmp|ico|mp3|wav|mid|zip|exe|pdf|swf)$", rel, re.I):
            # the nearest capture of an image/binary is an HTML error page from a later hosting
            rec["status"] = "html-instead-of-binary"
            print(f"MISS html-instead-of-binary {url}", flush=True)
            continue
        if html and not re.search(r"\.html?$", rel, re.I):
            rel = rel + ".html"
        rec["local"] = rel
        rec["html"] = html
        dest = out / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        print(f"OK   {cap_ts} {len(data):>7} {url}", flush=True)
        if html:
            for link in extract_links(data, url):
                c = canon(link)
                if in_scope(c, scope) and c not in seen and c not in queue:
                    queue.append(c)
    # rewrite pass
    for url, rec in pages.items():
        if not rec.get("html") or not rec.get("local"):
            continue
        dest = out / rec["local"]
        data = dest.read_bytes()
        here = Path(rec["local"]).parent

        def repl_target(raw):
            u = raw.decode("latin-1").strip()
            if not u or u.startswith(("#", "mailto:", "javascript:", "data:")):
                return raw
            absu = urljoin(url, u)
            frag = ("#" + urlsplit(absu).fragment) if urlsplit(absu).fragment else ""
            c = canon(absu)
            if in_scope(c, scope) and pages.get(c, {}).get("local"):
                target = Path(pages[c]["local"])
                relp = Path(*([".."] * len(here.parts))) / target if here.parts else target
                return (quote(relp.as_posix()) + frag).encode("latin-1")
            if absu.startswith(("http://", "https://")):
                cap = rec.get("capture") or ts
                return f"{WB}{cap}/{absu}".encode("latin-1")
            return raw

        data = LINK_RE.sub(lambda m: m.group("attr") + m.group("q") + repl_target(m.group("url")) + m.group("q"), data)
        data = CSS_URL_RE.sub(lambda m: b"url(" + m.group("q") + repl_target(m.group("url")) + m.group("q") + b")", data)
        cap = rec.get("capture") or ts
        date = f"{cap[:4]}-{cap[4:6]}-{cap[6:8]}"
        depth = len(here.parts) + 1
        back = "../" * depth
        banner = (
            '<div style="position:sticky;top:0;z-index:99999;background:#111;color:#eee;'
            'font:13px/1.4 Arial,sans-serif;padding:6px 10px;border-bottom:2px solid #c90">'
            f'Archivio &middot; {title} &middot; copia del {date} dal '
            f'<a style="color:#fc6" href="{WB}{cap}/{url}">Web Archive</a> &middot; '
            f'<a style="color:#fc6" href="{back}index.html">tutti i miei siti del passato</a> &middot; '
            '<a style="color:#fc6" href="https://fabio.pietrosanti.it/">fabio.pietrosanti.it</a></div>'
        ).encode("latin-1", "xmlcharrefreplace")
        m = re.search(rb"<body[^>]*>", data, re.I)
        data = data[: m.end()] + banner + data[m.end():] if m else banner + data
        dest.write_bytes(data)
    manifest = {
        "name": name, "start": start, "timestamp": ts, "scope": scope, "title": title,
        "pages": sorted(pages.values(), key=lambda r: r["url"]),
    }
    json.dump(manifest, io.open(out / "manifest.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    ok = sum(1 for r in pages.values() if r.get("local"))
    print(f"DONE {name}: {ok} saved, {len(pages) - ok} not archived")


if __name__ == "__main__":
    main()
