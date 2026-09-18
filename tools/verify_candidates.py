"""Verify candidate URLs (one per line, '#' comments allowed) and turn confirmed ones into research items.

For each URL not already in data/media.json: fetch the Web Archive capture (date guessed from the URL)
or the live page, look for "Fabio Pietrosanti" / "Pietrosanti" near a known topic / "naif", and write
  data/research/raw/<name>.json            confirmed items (verified: true)
  data/research/candidates/<name>.rejected.json   URLs checked and rejected, with reason

Usage: python tools/verify_candidates.py <candidates.txt> <name>
"""
import html
import io
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from archive_copies import UA, WAYBACK_ERROR, try_fetch  # noqa: E402
from merge_media import norm_url  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TOPICS = re.compile(r"globaleaks|hermes|whistleblow|tor2web|\btor\b|hacker|privatewave|khamsa|cifratur|intercettazion|"
                    r"trojan|rousseau|voto elettronico|e-voting|kaspersky|monitora ?pa|sicurezza informatica|privacy|"
                    r"crittograf|anonimato|copernicani|biohack", re.I)
IT_MONTHS = {m: i for i, m in enumerate(["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
                                         "agosto", "settembre", "ottobre", "novembre", "dicembre"], 1)}


def date_from_url(u):
    m = re.search(r"/(20\d\d|19\d\d)[/-](\d{1,2})[/-](\d{1,2})/", u)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    m = re.search(r"/(\d\d)_([a-z]+)_(\d\d)/", u)
    if m and m.group(2) in IT_MONTHS:
        return f"20{m.group(1)}-{IT_MONTHS[m.group(2)]:02d}-{int(m.group(3)):02d}"
    m = re.search(r"/(20\d\d)-(\d\d)-(\d\d)/", u)
    if m:
        return "-".join(m.groups())
    m = re.search(r"/(20\d\d)/(\d{1,2})/", u)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}"
    return None


def text_of(data):
    t = data.decode("utf-8", "replace")
    title = re.search(r"(?is)<title[^>]*>(.*?)</title>", t)
    og = re.search(r'(?is)<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)', t)
    t2 = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", t)
    body = html.unescape(re.sub(r"<[^>]+>", " ", t2))
    return html.unescape((og or title).group(1)).strip() if (og or title) else "", re.sub(r"\s+", " ", body)


def main():
    src, name = sys.argv[1], sys.argv[2]
    known = {norm_url(i.get("url")) for i in json.load(io.open(ROOT / "data/media.json", encoding="utf-8"))}
    urls = [l.strip() for l in io.open(src, encoding="utf-8") if l.strip() and not l.startswith("#")]
    ok, rejected = [], []
    for u in urls:
        if norm_url(u) in known:
            rejected.append({"url": u, "reason": "already in media.json"})
            continue
        d = date_from_url(u)
        ts = re.sub(r"\D", "", d or "2020") + "01000000"
        data, ctype, final, status, err = try_fetch(f"https://web.archive.org/web/{ts[:14]}id_/{u}")
        method = "wayback"
        if not data or WAYBACK_ERROR.search(data[:5000]):
            data, ctype, final, status, err = try_fetch(u)
            method = "live"
        time.sleep(1.5)
        if not data:
            rejected.append({"url": u, "reason": f"not fetched: {err or status}"})
            print("FAIL", u)
            continue
        title, body = text_of(data)
        body = re.sub(r"(?i)(privacy|cookie)\s+policy|informativa (sulla )?privacy", " ", body)  # footer boilerplate must not count as a topic
        full = re.search(r"Fabio\s+Pietrosanti|Pietrosanti,?\s+Fabio|\bnaif\b", body, re.I)
        near = None
        for m in re.finditer(r"Pietrosanti", body):
            ctx = body[max(0, m.start() - 400): m.end() + 400]
            if TOPICS.search(ctx) and not re.search(r"(Paolo|Matteo|Roberto|Loris|Stefano|Elma|Enrico|Katia|Francesco)\s+Pietrosanti", ctx):
                near = ctx
                break
        if full or near:
            snippet = (full and body[max(0, full.start() - 160): full.end() + 160]) or near[300:620]
            ok.append({"date": d, "year": int(d[:4]) if d else None, "type": "mentioned", "outlet": re.sub(r"^www\.", "", u.split("/")[2]),
                       "title": title, "url": u, "language": "it", "role": "subject",
                       "note": f"verified via {method}; context: …{snippet.strip()[:220]}…", "verified": True, "known": False})
            print("OK  ", u)
        else:
            reason = "JavaScript shell or paywall (almost no text)" if len(body) < 1500 else "his name not found (homonym or different Pietrosanti)"
            rejected.append({"url": u, "reason": reason, "method": method})
            print("NO  ", u, "-", reason)
    out = ROOT / "data/research/raw" / f"{name}.json"
    json.dump(ok, io.open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    json.dump(rejected, io.open(Path(src).with_suffix(".rejected.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"confirmed {len(ok)}, rejected {len(rejected)} -> {out.name}")


if __name__ == "__main__":
    main()
