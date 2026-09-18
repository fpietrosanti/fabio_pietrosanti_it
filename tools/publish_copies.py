"""Publish the light offline copies in this (public) repo, under copies/<year>/<id>/.

Fabio's decision (2026-09-18): third-party copies are public too — they are about him (right of report).
Source: the private library ../fabio_pietrosanti_it-copies (byte-exact originals).
For every verified item of data/media.json that has a local copy:
  - files up to LIGHT_MAX bytes are copied (media.* downloads and anything bigger go to Google Drive);
  - HTML originals are published as copy.html with <script>, <iframe>, event handlers and <base> removed and a
    banner with source URL and capture date; the untouched original stays in the private library;
  - text.txt and meta.json are copied as they are.
Writes site/copies.json: {source url: relative path of the page to link}.

Usage: python tools/publish_copies.py
"""
import io
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT.parent / "fabio_pietrosanti_it-copies"
OUT = ROOT / "copies"
LIGHT_MAX = 20_000_000
SKIP = re.compile(r"^media\.|\.(mp4|webm|mkv|mov|mp3|m4a|ogg|opus|wav|flac)$", re.I)
BANNER = ('<div style="all:initial;display:block;position:sticky;top:0;z-index:2147483647;background:#0d5c58;color:#fff;'
          'font:13px/1.4 system-ui,sans-serif;padding:8px 14px">Archived copy for <a style="color:#f2b134" href="/">fabio.pietrosanti.it</a>'
          ' · source: <a style="color:#f2b134" href="{url}">{url_short}</a>{cap} · scripts removed</div>')


def clean_html(raw, url, capture):
    t = raw.decode("utf-8", "replace")
    t = re.sub(r"(?is)<script\b.*?</script\s*>", "", t)
    t = re.sub(r"(?is)<script\b[^>]*/?>", "", t)
    t = re.sub(r"(?is)<iframe\b.*?</iframe\s*>", "", t)
    t = re.sub(r"(?is)<base\b[^>]*>", "", t)
    t = re.sub(r"""(?i)\son[a-z]+\s*=\s*("[^"]*"|'[^']*'|[^\s>]+)""", "", t)
    t = re.sub(r"""(?i)(href|src)\s*=\s*(["'])\s*javascript:[^"']*\2""", r'\1="#"', t)
    cap = f" · captured {capture[:4]}-{capture[4:6]}-{capture[6:8]}" if capture else ""
    banner = BANNER.format(url=url.replace('"', "%22"), url_short=re.sub(r"^https?://", "", url)[:80], cap=cap)
    m = re.search(r"(?is)<body\b[^>]*>", t)
    t = t[:m.end()] + banner + t[m.end():] if m else banner + t
    if not re.search(r"(?i)<meta[^>]+charset", t):
        t = '<meta charset="utf-8">' + t
    return t.encode("utf-8")


def main():
    media = json.load(io.open(ROOT / "data/media.json", encoding="utf-8"))
    ok = {i["url"] for i in media if i.get("verified") and not i.get("hermes_activity")}
    copies = json.load(io.open(LIB / "copies.json", encoding="utf-8"))
    index, n_files, size = {}, 0, 0
    for r in copies:
        if r["url"] not in ok or not r.get("local") or not (LIB / r["local"]).is_dir():
            continue
        src = LIB / r["local"]
        dst = OUT / r["local"]
        link = None
        for f in sorted(src.rglob("*")):
            if not f.is_file() or SKIP.search(f.name) or f.stat().st_size > LIGHT_MAX:
                continue
            rel = f.relative_to(src)
            if f.name.startswith("original.") and f.suffix.lower() in (".html", ".htm", ".shtml", ".php", ".asp", ".aspx", ""):
                target = dst / rel.parent / "copy.html"
                data = clean_html(f.read_bytes(), r["url"], r.get("capture"))
                link = link or target
            else:
                target = dst / rel
                data = f.read_bytes()
                if f.name.startswith("original.") or (f.name == "slides.pdf"):
                    link = link or target
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists() or target.read_bytes() != data:
                target.write_bytes(data)
            n_files += 1
            size += len(data)
        if not link and (dst / "text.txt").exists():
            link = dst / "text.txt"
        if link:
            index[r["url"]] = str(link.relative_to(ROOT)).replace("\\", "/")
    json.dump(index, io.open(ROOT / "site/copies.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0, sort_keys=True)
    print(f"published {len(index)} copies, {n_files} files, {size / 1e6:.0f} MB -> copies/")


if __name__ == "__main__":
    main()
