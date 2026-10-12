"""Cut Fabio's own segments out of long conference/panel/TV recordings that are NOT Radio Radicale
(YouTube, archive.org e-privacy, media.ccc.de, podcasts...), with a per-clip transcript.

Companion of radioradicale_clips.py. There is no speaker index outside Radio Radicale, so the segments are
curated by hand in <out>/convegni_clips.json, from the uploader's chapters/description, the broadcaster's
subtitles (speaker colours) or the local Whisper transcript (tools/transcribe_media.py), and this script does
the mechanical part. One record per recording checked; "status" is one of:
  clip             a segment where Fabio speaks (start/end in seconds, end null = to the end); one record per segment
  uncertain        a segment cut because Fabio probably speaks there, but the evidence is weak ("reason" says why)
  whole            no cut needed: short (< ~20 min) or entirely Fabio's own talk/interview
  already_clipped  his part is already a separate copy ("see")
  to_transcribe    long multi-speaker recording, no transcript yet: segment not located
  not_found        transcribed, but no evidence that Fabio speaks in it
  no_media         the media file is not in the copy

For "clip"/"uncertain" records the script writes into the copy folder (<out>/<local>/):
  fabio_t<start>.<ext>   the clip (ffmpeg stream copy, no re-encode; media files stay local-only, git-ignored)
  fabio_t<start>.txt     the transcript of the clip, taken from (in order) the copy's transcript.txt, its
                         media.*.srt subtitles, or a fresh faster-whisper run on the clip ("lang" field)
and fills in clip/bytes/transcript in the index.

Usage: python tools/convegni_clips.py <out_dir>              cut the missing clips/transcripts
       python tools/convegni_clips.py <out_dir> --find <id>  print the lines of the copy's transcript that
                                                             mention him (with a little context)
"""
import io
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from radioradicale_clips import ffmpeg_path  # noqa: E402
from transcribe_media import NAME_RE, media_file  # noqa: E402

TS_RE = re.compile(r"^\[(\d+):(\d{2})\]\s*(.*)$")
SRT_RE = re.compile(r"(\d+):(\d+):(\d+)[,.]\d+\s*-->\s*(\d+):(\d+):(\d+)(?:[,.]\d+)?")


def mmss(t):
    return f"{int(t) // 60:02d}:{int(t) % 60:02d}"


def transcript_lines(path):
    """(seconds, text) from a transcribe_media.py transcript.txt."""
    out = []
    for ln in io.open(path, encoding="utf-8"):
        m = TS_RE.match(ln.strip())
        if m:
            out.append((int(m.group(1)) * 60 + int(m.group(2)), m.group(3)))
    return out


def srt_lines(path):
    out = []
    for block in re.split(r"\n\s*\n", io.open(path, encoding="utf-8").read()):
        m = SRT_RE.search(block)
        if m:
            t = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
            text = " ".join(re.sub(r"<[^>]+>", "", block[m.end():]).split())
            if text:
                out.append((t, text))
    return out


def slice_lines(lines, start, end):
    return [f"[{mmss(t - start)}] {x}" for t, x in lines if t >= start and (end is None or t < end)]


def duration(ffmpeg, f):
    ffprobe = str(Path(ffmpeg).with_name(Path(ffmpeg).name.replace("ffmpeg", "ffprobe")))
    p = subprocess.run([ffprobe, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                       capture_output=True, text=True)
    try:
        return round(float(p.stdout.strip()))
    except ValueError:
        return None


def find(out, cid):
    rec = next(r for r in json.load(io.open(out / "convegni_clips.json", encoding="utf-8")) if r["id"] == cid)
    lines = transcript_lines(out / rec["local"] / "transcript.txt")
    for i, (t, x) in enumerate(lines):
        if NAME_RE.search(x):
            for tt, xx in lines[max(0, i - 2): i + 3]:
                print(f"{'>' if tt == t else ' '} [{mmss(tt)}] {xx}")
            print()


def main():
    out = Path(sys.argv[1])
    if "--find" in sys.argv:
        return find(out, sys.argv[sys.argv.index("--find") + 1])
    ffmpeg = ffmpeg_path()
    index = out / "convegni_clips.json"
    recs = json.load(io.open(index, encoding="utf-8"))
    model = None
    for rec in recs:
        if rec.get("status") not in ("clip", "uncertain") or rec.get("start") is None:
            continue
        folder = out / rec["local"]
        src = media_file(folder)
        if not src:
            rec["error"] = "no media file"
            continue
        start, end = rec["start"], rec.get("end")
        clip = folder / f"fabio_t{start}{src.suffix.lower()}"
        rec["source"] = src.name
        if not (clip.exists() and clip.stat().st_size > 0):
            cmd = [ffmpeg, "-y", "-loglevel", "error", "-ss", str(start), "-i", str(src)]
            if end is not None:
                cmd += ["-t", str(end - start)]
            cmd += ["-map", "0", "-c", "copy", str(clip)]
            p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
            if p.returncode != 0:
                rec["error"] = (p.stderr or "ffmpeg failed").strip()[-300:]
                print("FAIL", rec["id"], start, rec["error"], flush=True)
                continue
        rec.update(clip=clip.name, bytes=clip.stat().st_size)
        rec.pop("error", None)
        txt = folder / f"fabio_t{start}.txt"
        if not txt.exists():
            full = folder / "transcript.txt"
            srts = sorted(folder.glob("media.*.srt"))
            if full.exists():
                how, lines = "faster-whisper small, dalla trascrizione completa transcript.txt", \
                    slice_lines(transcript_lines(full), start, end)
            elif srts:
                how, lines = f"sottotitoli dell'emittente, {srts[0].name}", slice_lines(srt_lines(srts[0]), start, end)
            else:
                from transcribe_media import load_model, transcribe
                model = model or load_model("small")
                how, lines = "faster-whisper small, sulla clip", transcribe(model, clip, rec.get("lang", "it"))
            txt.write_text(
                f"{rec['title']}\n{rec['url']}\nSegmento da {mmss(start)} a {mmss(end) if end else 'fine'} "
                f"della registrazione ({src.name}); timestamp relativi all'inizio della clip.\n"
                f"Trascrizione automatica ({how}).\n\n" + "\n".join(lines) + "\n", encoding="utf-8")
        rec["transcript"] = txt.name
        print("OK  ", rec["id"], mmss(start), mmss(end) if end else "end", clip.name, flush=True)
        json.dump(recs, io.open(index, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    json.dump(recs, io.open(index, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("CLIPS", sum(1 for r in recs if r.get("clip")), "of", sum(1 for r in recs if r.get("start") is not None))


if __name__ == "__main__":
    main()
