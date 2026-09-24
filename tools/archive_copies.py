"""Make an offline copy of every source in data/media.json and report what was obtained.

For each item:
  1. Web Archive capture nearest to the item's date  (https://web.archive.org/web/<ts>id_/<url>)
  2. otherwise the live page
Saves under <out>/<year>/<id>/:
  original.<ext>   exact bytes (HTML without the Wayback toolbar, or PDF, image, ...)
  text.txt         extracted text (HTML and plain text only)
  meta.json        source url, method, capture timestamp, content type, size, sha256, name_found
Video/audio platforms are not downloaded here: they are recorded as "media-not-downloaded".

Writes <out>/copies.json (status per item) and prints a summary. docs are rendered by
tools/render_copies_report.py.

Usage: python tools/archive_copies.py <out_dir> [--only YEAR|ID ...] [--limit N] [--retry-failed]
"""
import gzip
import hashlib
import html
import io
import json
import re
import subprocess
import sys
import tarfile
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36"
DELAY = 1.5
MEDIA_HOSTS = ("youtube.com", "youtu.be", "vimeo.com", "media.ccc.de", "spreaker.com", "open.spotify.com",
               "podcasts.apple.com", "radioradicale.it", "raiplay.it", "archive.org/details")
NAME_RE = re.compile(rb"pietrosanti|\bnaif\b|\xe7\x9f\xb3\s?\xe9\xa3\x8e\xe7\xbf\xb1", re.I)  # also 石风翱 in UTF-8
WAYBACK_ERROR = re.compile(rb"Wayback Machine has not archived that URL|Hrm\.|This URL has been excluded", re.I)


def item_id(it):
    return hashlib.sha1((it.get("url") or it.get("title") or "").encode("utf-8")).hexdigest()[:12]


def ts_for(it):
    d = re.sub(r"[^0-9]", "", str(it.get("date") or it.get("year") or ""))
    return (d + "0101000000")[:14] if d else "20100101000000"


def decode_body(data, enc, ctype):
    """Some servers answer gzip/deflate/brotli even without Accept-Encoding: decode, or the copy is unreadable."""
    enc = (enc or "").lower()
    try:
        if enc == "gzip" or (not enc and data[:2] == b"\x1f\x8b" and "html" in (ctype or "")):
            return gzip.decompress(data)
        if enc == "deflate":
            import zlib
            try:
                return zlib.decompress(data)
            except zlib.error:
                return zlib.decompress(data, -zlib.MAX_WBITS)
        if enc == "br":
            try:
                import brotli
                return brotli.decompress(data)
            except ImportError:
                pass
    except Exception:
        pass
    return data


def get(url, timeout=90):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "it,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        ctype = r.headers.get("Content-Type", "")
        return decode_body(r.read(), r.headers.get("Content-Encoding", ""), ctype), ctype, r.geturl(), r.status


def try_fetch(url, attempts=3):
    last = None
    for a in range(attempts):
        try:
            return get(url) + (None,)
        except urllib.error.HTTPError as e:
            if e.code in (403, 404, 410, 451):
                return None, "", url, e.code, f"http {e.code}"
            last = f"http {e.code}"
        except Exception as e:  # timeouts, resets, TLS
            last = type(e).__name__
        time.sleep(4 * (a + 1))
    return None, "", url, None, last


def ext_for(ctype, url, data):
    c = (ctype or "").lower()
    if "pdf" in c or data[:5] == b"%PDF-":
        return "pdf"
    if "html" in c:
        return "html"
    if "text/plain" in c:
        return "txt"
    m = re.search(r"\.([a-z0-9]{2,5})$", urlsplit(url).path.lower())
    return m.group(1) if m else "bin"


def name_in(data, ext):
    """Look for his name/nick also inside gzip/tar archives (BFi issues) and PDFs (via pdftotext when present).
    Returns None for a PDF that cannot be read."""
    if data[:2] == b"\x1f\x8b":
        try:
            data = gzip.decompress(data)
        except (OSError, EOFError):
            pass
    try:
        with tarfile.open(fileobj=io.BytesIO(data)) as tf:
            return any(NAME_RE.search(tf.extractfile(m).read()) for m in tf.getmembers() if m.isfile())
    except (tarfile.TarError, EOFError, OSError):
        pass
    if ext == "pdf":
        # pdftotext cannot read a PDF from stdin on the Windows (mingw) build: go through a temp file
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            src = Path(td) / "in.pdf"
            src.write_bytes(data)
            try:
                data = subprocess.run(["pdftotext", "-q", str(src), "-"], capture_output=True, timeout=120).stdout
            except (OSError, subprocess.SubprocessError):
                return None
        if not data.strip():
            return None
    return bool(NAME_RE.search(data))


def html_text(data):
    t = data.decode("utf-8", "replace") if b"charset=utf-8" in data[:3000].lower() or not re.search(rb"charset=(iso-8859|windows-125)", data[:3000], re.I) else data.decode("latin-1")
    t = re.sub(r"(?is)<(script|style|noscript|svg).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</(p|div|li|h\d|tr)>", "\n", t)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    t = re.sub(r"[ \t\r\f\v]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n\n", t).strip()


def copy_item(it, out):
    url = (it.get("url") or "").strip()
    rec = {"id": item_id(it), "url": url, "year": it.get("year"), "title": it.get("title"), "type": it.get("type"),
           "outlet": it.get("outlet"), "status": None, "method": None, "capture": None, "reason": None,
           "local": None, "name_found": None, "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    if not url.startswith(("http://", "https://")):
        rec.update(status="missing", reason="no url")
        return rec
    is_media = any(h in url for h in MEDIA_HOSTS)
    target = url
    m = re.match(r"https?://web\.archive\.org/web/(\d+)[a-z_]*/(.+)$", url)
    if m:
        target = m.group(2)
    # 1) Web Archive
    wb = f"https://web.archive.org/web/{ts_for(it)}id_/{target}"
    data, ctype, final, status, err = try_fetch(wb)
    time.sleep(DELAY)
    method = None
    if data and not WAYBACK_ERROR.search(data[:5000]) and "/web/" in final:
        method = "wayback"
        rec["capture"] = (re.search(r"/web/(\d{14})", final) or [None, None])[1]
    else:
        # 2) live page
        data, ctype, final, status, err = try_fetch(target)
        time.sleep(DELAY)
        if data:
            method = "live"
    folder = out / str(it.get("year") or "undated") / rec["id"]
    video = None
    scan = archive_org_text(target, folder) if "archive.org/details/" in target else None
    if scan is not None:
        is_media = False
        rec["scan"] = scan
    if is_media:
        key = media_key(target)
        if key in SHARED_MEDIA:
            video = dict(SHARED_MEDIA[key])
        else:
            video = download_media(target, folder)
            if video.get("file"):
                SHARED_MEDIA[key] = dict(video, same_as=str(folder.relative_to(out)).replace("\\", "/"))
    if not data:
        if video and video.get("file"):
            rec.update(status="video-obtained", method="yt-dlp", reason="video saved, page copy not obtained: " + (err or f"http {status}"),
                       local=str(folder.relative_to(out)).replace("\\", "/"), video=video)
        else:
            rec.update(status="not-obtained", reason=(err or f"http {status}") + (f"; video: {video.get('error')}" if video else ""), video=video)
        return rec
    ext = ext_for(ctype, final, data)
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"original.{ext}").write_bytes(data)
    text = None
    if ext == "html":
        text = html_text(data)
    elif ext == "txt":
        text = data.decode("utf-8", "replace")
    if text is not None:
        (folder / "text.txt").write_text(text, encoding="utf-8")
    name_found = name_in(data, ext)
    if scan and "file" in scan:
        name_found = scan["name_found"]
    js_shell = ext == "html" and text is not None and len(text) < 400
    meta = {"source_url": url, "fetched_url": final, "method": method, "capture": rec["capture"],
            "content_type": ctype, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            "name_found": name_found, "fetched_at": rec["checked_at"]}
    (folder / "meta.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False), encoding="utf-8")
    status = "obtained"
    reason = None
    if js_shell:
        status, reason = "partial", "page is a JavaScript shell with almost no text: needs browser capture"
    elif name_found is False:
        status, reason = "obtained-unconfirmed", "copy saved but his name/nick not found in it (paywall, wrong capture or JS)"
    if is_media:
        if video and video.get("file"):
            status, reason = "video-obtained", None
        else:
            status = "page-only"
            reason = "page copy saved; video/audio not downloaded: " + ((video or {}).get("error") or "unknown")
    rec.update(status=status, method=method, reason=reason, local=str(folder.relative_to(out)).replace("\\", "/"),
               name_found=name_found, video=video)
    return rec


def archive_org_text(url, folder):
    """archive.org texts item (scanned magazine/book): save its OCR text (_djvu.txt), and the PDF when public
    and under 60 MB. Returns {file, bytes, name_found} or None when the item is not a texts item."""
    m = re.match(r"https?://archive\.org/details/([^/?#]+)", url)
    if not m:
        return None
    data, *_ , err = try_fetch(f"https://archive.org/metadata/{m.group(1)}")
    if not data:
        return None
    md = json.loads(data)
    if md.get("metadata", {}).get("mediatype") != "texts":
        return None
    files = md.get("files", [])
    txt = next((f["name"] for f in files if f["name"].endswith("_djvu.txt")), None)
    if not txt:
        return {"error": "texts item without OCR text"}
    base = f"https://archive.org/download/{m.group(1)}/"
    t, *_ , err = try_fetch(base + urllib.request.quote(txt))
    if not t:
        return {"error": f"OCR text not downloadable ({err}); lending-only item?"}
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "ocr_djvu.txt").write_bytes(t)
    res = {"file": "ocr_djvu.txt", "bytes": len(t), "name_found": bool(NAME_RE.search(t))}
    pdf = next((f for f in files if f["name"].lower().endswith(".pdf") and int(f.get("size") or 0) < 60_000_000), None)
    if pdf and not md.get("metadata", {}).get("access-restricted-item"):
        p, *_ = try_fetch(base + urllib.request.quote(pdf["name"]))
        if p:
            (folder / "original.pdf").write_bytes(p)
            res["pdf"] = "original.pdf"
    return res


SHARED_MEDIA = {}  # media_key -> video record already downloaded (two URLs of the same recording)


def media_key(url):
    m = re.search(r"radioradicale\.it/scheda/(\d+)", url)
    return f"radioradicale:{m.group(1)}" if m else url


def download_media(url, folder):
    """Download video/audio with yt-dlp into folder/media.*; returns {file, bytes, title} or {error}.
    Multi-part recordings (e.g. Radio Radicale conferences) are saved as media.01.mp4, media.02.mp4, ..."""
    r = _yt_dlp(url, folder, ["--no-playlist"], "media.%(ext)s")
    if "error" in r and "playlist" in r["error"].lower():
        r = _yt_dlp(url, folder, ["--yes-playlist"], "media.%(playlist_index)02d.%(ext)s")
    return r


def _yt_dlp(url, folder, mode, template):
    import shutil
    import subprocess
    folder.mkdir(parents=True, exist_ok=True)
    import os
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        found = sorted((Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft/WinGet/Packages").glob("Gyan.FFmpeg*/*/bin/ffmpeg.exe"))
        ffmpeg = str(found[-1]) if found else None
    fmt = "bv*[height<=720]+ba/b[height<=720]/bv*+ba/b" if ffmpeg else "b[height<=720]/b"
    extra = ["--ffmpeg-location", ffmpeg, "--merge-output-format", "mp4"] if ffmpeg else []
    cmd = [sys.executable, "-m", "yt_dlp", *mode, "--no-progress", "-f", fmt, *extra,
           "--write-info-json", "--write-description", "--write-subs", "--sub-langs", "it,en",
           "--write-thumbnail", "-o", str(folder / template), url]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=3600, encoding="utf-8", errors="replace")
    except Exception as e:
        return {"error": f"yt-dlp failed to run: {type(e).__name__}"}
    files = [f for f in folder.glob("media.*") if f.suffix.lower() not in (".json", ".description", ".vtt", ".srt", ".jpg", ".webp", ".png", ".part")]
    if p.returncode == 0 and files:
        f = max(files, key=lambda x: x.stat().st_size)
        res = {"file": f.name, "bytes": f.stat().st_size}
        if len(files) > 1:
            res.update(parts=sorted(x.name for x in files), bytes=sum(x.stat().st_size for x in files))
        return res
    err = (p.stderr or p.stdout or "").strip().splitlines()
    return {"error": (err[-1] if err else f"exit {p.returncode}")[:300]}


# Statuses set by hand after reviewing a copy (see docs/PROBLEMI-APERTI.md B3-bis)
CLASSIFIED = {"obtained-org-only", "obtained-book-pending", "obtained-media-only", "obtained-name-absent",
              "obtained-stub", "closed-by-decision"}


def main():
    args = sys.argv[1:]
    out = Path(args.pop(0))
    only, limit, retry = set(), None, False
    while args:
        a = args.pop(0)
        if a == "--only":
            while args and not args[0].startswith("--"):
                only.add(args.pop(0))
        elif a == "--limit":
            limit = int(args.pop(0))
        elif a == "--retry-failed":
            retry = True
    out.mkdir(parents=True, exist_ok=True)
    state_path = out / "copies.json"
    state = {r["id"]: r for r in json.load(io.open(state_path, encoding="utf-8"))} if state_path.exists() else {}
    items = json.load(io.open(ROOT / "data/media.json", encoding="utf-8"))
    for r in state.values():
        v = r.get("video") or {}
        if r["status"] == "video-obtained" and v.get("file") and "same_as" not in v:
            SHARED_MEDIA.setdefault(media_key(r["url"]), dict(v, same_as=r["local"]))
    done = 0
    for it in items:
        iid = item_id(it)
        if only and str(it.get("year")) not in only and iid not in only:
            continue
        prev = state.get(iid)
        if prev and prev["status"] in ("obtained", "video-obtained"):
            continue
        if prev and prev["status"] != "media-not-downloaded" and not retry:
            continue
        rec = copy_item(it, out)
        if prev and prev["status"] in CLASSIFIED and rec["status"] not in ("obtained", "video-obtained"):
            continue  # a retry that did not find the name must not undo a manual classification
        state[iid] = rec
        print(f"{rec['status']:<22} {rec.get('method') or '':<8} {it.get('year')} {rec['url'][:90]}", flush=True)
        json.dump(sorted(state.values(), key=lambda r: (r["year"] or 0, r["url"])), io.open(state_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        done += 1
        if limit and done >= limit:
            break
    from collections import Counter
    print("SUMMARY", dict(Counter(r["status"] for r in state.values())))


if __name__ == "__main__":
    main()
