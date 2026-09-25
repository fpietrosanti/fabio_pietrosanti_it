"""Transcribe audio/video copies locally (faster-whisper) to confirm Fabio's voice/name in media-only copies.

Usage: python tools/transcribe_media.py <copy_dir> [<copy_dir> ...] [--model small]
Writes <copy_dir>/transcript.txt (with [mm:ss] timestamps) and prints the lines that mention him.
The transcript is text, so it is committed; the media file itself stays local-only.
"""
import re
import sys
from pathlib import Path

from faster_whisper import WhisperModel

MEDIA_EXT = (".mp3", ".m4a", ".mp4", ".webm", ".mkv", ".opus", ".ogg")
NAME_RE = re.compile(r"pietro\s*sant|\bnaif\b|\bna[iï]f\b|hermes|globaleaks", re.I)


def media_file(d: Path):
    for f in sorted(d.iterdir()):
        if f.suffix.lower() in MEDIA_EXT:
            return f
    return None


def main():
    args = sys.argv[1:]
    model_name = "small"
    if "--model" in args:
        i = args.index("--model")
        model_name = args[i + 1]
        del args[i : i + 2]
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    for a in args:
        d = Path(a)
        f = media_file(d)
        if not f:
            print(f"{d}: no media file")
            continue
        segments, _ = model.transcribe(str(f), language="it", vad_filter=True)
        lines = []
        for s in segments:
            m, sec = divmod(int(s.start), 60)
            lines.append(f"[{m:02d}:{sec:02d}] {s.text.strip()}")
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
