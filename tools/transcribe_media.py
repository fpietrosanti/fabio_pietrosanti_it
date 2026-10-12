"""Transcribe audio/video copies locally (faster-whisper) to confirm Fabio's voice/name in media-only copies.

Usage: python tools/transcribe_media.py <copy_dir> [<copy_dir> ...] [--model small] [--lang it|en|auto]
Writes <copy_dir>/transcript.txt (with [mm:ss] timestamps) and prints the lines that mention him.
The transcript is text, so it is committed; the media file itself stays local-only.
Clips cut out of a recording (fabio_*.mp4, fabio-*.mp4 etc., see radioradicale_clips.py / convegni_clips.py) are never
taken as the copy's media file.
"""
import re
import sys
from pathlib import Path

MEDIA_EXT = (".mp3", ".m4a", ".mp4", ".webm", ".mkv", ".opus", ".ogg", ".mov")
NAME_RE = re.compile(r"pietro\s*s+ant|\bfabio\b|\bnaif\b|\bna[iï]f\b|hermes|globaleaks", re.I)


def media_file(d: Path):
    for f in sorted(d.iterdir()):
        if f.suffix.lower() in MEDIA_EXT and not f.name.lower().startswith("fabio"):
            return f
    return None


def load_model(model_name="small"):
    from faster_whisper import WhisperModel

    return WhisperModel(model_name, device="cpu", compute_type="int8")


def transcribe(model, path, lang="it", offset=0):
    """Return '[mm:ss] text' lines; timestamps are shifted by `offset` seconds. lang 'auto' = detect."""
    segments, _ = model.transcribe(str(path), language=None if lang == "auto" else lang, vad_filter=True)
    lines = []
    for s in segments:
        m, sec = divmod(int(s.start + offset), 60)
        lines.append(f"[{m:02d}:{sec:02d}] {s.text.strip()}")
    return lines


def main():
    args = sys.argv[1:]
    opts = {"--model": "small", "--lang": "it"}
    for k in list(opts):
        if k in args:
            i = args.index(k)
            opts[k] = args[i + 1]
            del args[i : i + 2]
    model_name = opts["--model"]
    model = load_model(model_name)
    for a in args:
        d = Path(a)
        f = media_file(d)
        if not f:
            print(f"{d}: no media file")
            continue
        lines = transcribe(model, f, opts["--lang"])
        (d / "transcript.txt").write_text(
            f"# Trascrizione automatica (faster-whisper {model_name}) di {f.name}\n" + "\n".join(lines) + "\n",
            encoding="utf-8",
        )
        hits = [ln for ln in lines if NAME_RE.search(ln)]
        print(f"== {d}: {len(lines)} segmenti, {len(hits)} menzioni", flush=True)
        for h in hits:
            print("   " + h, flush=True)


if __name__ == "__main__":
    main()
