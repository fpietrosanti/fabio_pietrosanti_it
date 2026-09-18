"""Archive every SlideShare deck in data/media.json: all slide images (highest resolution available),
the transcript text, and a PDF assembled from the slides, into <copies>/<year>/<id>/slides/.

Updates copies.json: status "obtained" with name_found from the transcript, and a "slides" record.
Usage: python tools/slideshare_archive.py <copies_dir>
"""
import html
import io
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from archive_copies import NAME_RE, get, item_id  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def fetch(url):
    for a in range(3):
        try:
            return get(url)[0]
        except Exception:
            time.sleep(3 * (a + 1))
    return None


def main():
    out = Path(sys.argv[1])
    state_p = out / "copies.json"
    state = {r["id"]: r for r in json.load(io.open(state_p, encoding="utf-8"))}
    media = json.load(io.open(ROOT / "data/media.json", encoding="utf-8"))
    import img2pdf
    for it in media:
        url = it.get("url") or ""
        if not re.search(r"slideshare\.net/(slideshow/)?[^/]+/\d+", url):
            continue
        rid = item_id(it)
        folder = out / str(it.get("year") or "undated") / rid / "slides"
        if (folder / "slides.pdf").exists():
            print("skip", url)
            continue
        page = fetch(url)
        if not page:
            print("FAIL page", url)
            continue
        t = page.decode("utf-8", "replace")
        imgs = re.findall(r"https://image\.slidesharecdn\.com/([^/\"\\]+)/\d+/([^\"\\ ]+?)-(\d+)-\d+\.(jpg|png|webp)", t)
        if not imgs:
            print("no slides", url)
            continue
        base, title, _, ext = imgs[0]
        n = max(int(i[2]) for i in imgs)
        m = re.search(r'"totalSlides":(\d+)', t)
        n = max(n, int(m.group(1))) if m else n
        folder.mkdir(parents=True, exist_ok=True)
        files = []
        for k in range(1, n + 1):
            data = None
            for size, path in (("2048", "75"), ("1024", "75"), ("638", "85"), ("320", "85")):
                data = fetch(f"https://image.slidesharecdn.com/{base}/{path}/{title}-{k}-{size}.{ext}")
                if data and len(data) > 1000:
                    break
            if data:
                f = folder / f"slide-{k:03d}.{ext}"
                f.write_bytes(data)
                files.append(f)
            time.sleep(0.3)
        tr = re.search(r'(?is)<div[^>]+class="[^"]*transcript[^"]*"[^>]*>(.*?)</div>\s*</div>', t)
        text = html.unescape(re.sub(r"<[^>]+>", " ", tr.group(1))) if tr else ""
        text = re.sub(r"[ \t]+", " ", text).strip()
        (folder / "transcript.txt").write_text(text, encoding="utf-8")
        if files and ext in ("jpg", "png"):
            (folder / "slides.pdf").write_bytes(img2pdf.convert([str(f) for f in files]))
        found = bool(NAME_RE.search(text.encode("utf-8"))) or bool(NAME_RE.search(page))
        rec = state.get(rid, {"id": rid, "url": url, "year": it.get("year"), "title": it.get("title"), "type": it.get("type"), "outlet": it.get("outlet")})
        rec["slides"] = {"count": len(files), "expected": n, "pdf": "slides/slides.pdf", "transcript_chars": len(text)}
        if files:
            rec.update(status="obtained" if found else "obtained-unconfirmed", name_found=found,
                       local=str((out / str(it.get("year") or "undated") / rid).relative_to(out)).replace("\\", "/"),
                       reason=None if found else "slides saved; name not in transcript (check slide images)")
        state[rid] = rec
        print(f"{len(files)}/{n} slides, name {found}: {url}")
        json.dump(sorted(state.values(), key=lambda r: (r.get("year") or 0, r["url"])), io.open(state_p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
