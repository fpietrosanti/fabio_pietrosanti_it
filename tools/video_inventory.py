"""Inventario dei video della libreria: unisce file, voce d'archivio e metadati tecnici.

Produce data/video_inventory.json, la base su cui si fa la valutazione del rischio
(Content ID per YouTube, censura per Bilibili). Rieseguibile: ricalcola tutto da zero.

Uso: python tools/video_inventory.py
"""
import io
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT.parent / "fabio_pietrosanti_it-copies"
EXT = {".mp4", ".webm", ".mov", ".mkv", ".avi"}


def ffprobe(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration:format_tags=copyright,title,artist,album",
                        "-of", "json", str(p)], text=True, capture_output=True)
    try:
        f = json.loads(r.stdout).get("format", {})
    except Exception:
        return {}
    t = f.get("tags", {})
    return {"duration": round(float(f.get("duration", 0) or 0)),
            "embedded_license": t.get("copyright", ""),
            "embedded_title": t.get("title", ""),
            "embedded_album": t.get("album", "")}


def main():
    by_local = {}
    for r in json.load(io.open(LIB / "copies.json", encoding="utf-8")):
        if r.get("local"):
            by_local[r["local"].replace("\\", "/")] = r
    media = {x["url"]: x for x in json.load(io.open(ROOT / "data/media.json", encoding="utf-8"))}
    drive = json.load(io.open(ROOT / "data/drive_links.json", encoding="utf-8"))

    out = []
    for p in sorted(LIB.rglob("*")):
        if p.suffix.lower() not in EXT or not p.is_file():
            continue
        rel = p.relative_to(LIB).as_posix()
        folder = rel.rsplit("/", 1)[0]
        rec = by_local.get(folder, {})
        it = media.get(rec.get("url", ""), {})
        out.append({
            "file": rel,
            "size": p.stat().st_size,
            **ffprobe(p),
            "folder": folder,
            "source_url": rec.get("url", ""),
            "title": it.get("title") or rec.get("title") or "",
            "outlet": it.get("outlet") or rec.get("outlet") or "",
            "type": it.get("type") or rec.get("type") or "",
            "year": it.get("year") or rec.get("year"),
            "date": it.get("date"),
            "language": it.get("language") or "",
            "role": it.get("role") or "",
            "note": (it.get("note") or "")[:400],
            "drive": drive.get(rel, {}).get("url", ""),
        })
    json.dump(out, io.open(ROOT / "data/video_inventory.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    orphan = sum(1 for x in out if not x["source_url"])
    print(f"{len(out)} video · {sum(x['duration'] for x in out)/3600:.1f} ore · "
          f"{sum(x['size'] for x in out)/2**30:.1f} GB · senza voce d'archivio: {orphan}")


if __name__ == "__main__":
    main()
