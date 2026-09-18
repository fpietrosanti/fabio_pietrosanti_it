"""Cut Fabio's own interventions out of Radio Radicale recordings (video clip + transcript).

Radio Radicale lists a speaker's interventions on the "soggetti" page as scheda links with ?i=<intervention id>.
Each scheda page embeds a map "int<id>": {"file": <part index>, "offset": <seconds>} and a playlist of parts
(HLS stream + automatic transcript .vtt). An intervention runs from its offset to the next intervention's offset
in the same part (or to the end of the part).

Saves into the copies folder of the matching media.json item (<out>/<year>/<id>/):
  fabio_int<id>.mp4      the clip (stream copy, no re-encode)
  fabio_int<id>.txt      transcript lines of the clip (automatic transcription by Radio Radicale)
and records everything in <out>/radioradicale_clips.json.

Usage: python tools/radioradicale_clips.py <out_dir> [<soggetti page url>]
"""
import io
import json
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from archive_copies import UA, get, item_id  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SOGGETTI = "https://www.radioradicale.it/soggetti/175095/fabio-pietrosanti"


def ffmpeg_path():
    import os
    p = shutil.which("ffmpeg")
    if p:
        return p
    found = sorted((Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft/WinGet/Packages").glob("Gyan.FFmpeg*/*/bin/ffmpeg.exe"))
    return str(found[-1]) if found else None


def page(url):
    return get(url)[0].decode("utf-8", "replace")


def playlist_of(html):
    i = html.index('"playlist":[') + len('"playlist":')
    return json.JSONDecoder().raw_decode(html[i:])[0]


def vtt_seconds(t):
    h, m, s = t.replace(",", ".").split(":") if t.count(":") == 2 else ("0", *t.split(":"))
    return int(h) * 3600 + int(m) * 60 + float(s)


def vtt_slice(vtt, start, end):
    out = []
    for block in re.split(r"\n\s*\n", vtt):
        m = re.search(r"([\d:.,]+)\s*-->\s*([\d:.,]+)", block)
        if not m:
            continue
        a = vtt_seconds(m.group(1))
        if a >= start and (end is None or a < end):
            text = " ".join(block[m.end():].split())
            if text:
                out.append(f"[{int(a - start) // 60:02d}:{int(a - start) % 60:02d}] {text}")
    return "\n".join(out)


def main():
    out = Path(sys.argv[1])
    soggetti = sys.argv[2] if len(sys.argv) > 2 else SOGGETTI
    ffmpeg = ffmpeg_path()
    items = json.load(io.open(ROOT / "data/media.json", encoding="utf-8"))
    by_scheda = {}
    for it in items:
        m = re.search(r"radioradicale\.it/scheda/(\d+)", it.get("url") or "")
        if m:
            by_scheda.setdefault(m.group(1), it)
    links = sorted(set(re.findall(r'scheda/(\d+)/[^"?]*\?i=(\d+)', page(soggetti))))
    state_path = out / "radioradicale_clips.json"
    state = {r["intervention"]: r for r in json.load(io.open(state_path, encoding="utf-8"))} if state_path.exists() else {}
    for scheda, iid in links:
        if state.get(iid, {}).get("clip"):
            continue
        rec = {"intervention": iid, "scheda": scheda, "url": f"https://www.radioradicale.it/scheda/{scheda}?i={iid}"}
        it = by_scheda.get(scheda)
        if not it:
            rec["error"] = "scheda not in data/media.json"
            state[iid] = rec
            print("SKIP", scheda, iid, rec["error"])
            continue
        folder = out / str(it.get("year") or "undated") / item_id(it)
        folder.mkdir(parents=True, exist_ok=True)
        rec["item_url"], rec["local"] = it["url"], str(folder.relative_to(out)).replace("\\", "/")
        try:
            html = page(rec["url"])
            ints = {k: (int(f), int(o)) for k, f, o in re.findall(r'"int(\d+)":\{"file":(\d+),"offset":(\d+)', html)}
            f, start = ints[iid]
            later = [o for (ff, o) in ints.values() if ff == f and o > start]
            end = min(later) if later else None
            part = playlist_of(html)[f]
            src = part["sources"][0]["src"]
            rec.update(part=f, start=start, end=end, stream=src)
            clip = folder / f"fabio_int{iid}.mp4"
            cmd = [ffmpeg, "-y", "-loglevel", "error", "-user_agent", UA, "-ss", str(start), "-i", src]
            if end is not None:
                cmd += ["-t", str(end - start)]
            cmd += ["-c", "copy", str(clip)]
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=3600, encoding="utf-8", errors="replace")
            if p.returncode == 0 and clip.exists() and clip.stat().st_size > 0:
                rec.update(clip=clip.name, bytes=clip.stat().st_size)
            else:
                rec["error"] = (p.stderr or "ffmpeg failed").strip()[-300:]
            subs = part.get("subtitles") or []
            if subs:
                vtt = get(urllib.request.urljoin("https://www.radioradicale.it/", subs[0]["src"]))[0].decode("utf-8", "replace")
                text = vtt_slice(vtt, start, end)
                (folder / f"fabio_int{iid}.txt").write_text(
                    f"Radio Radicale, scheda {scheda}, intervento {iid}, parte {f}, da {start}s a {end}s\n"
                    f"Trascrizione automatica di Radio Radicale.\n\n{text}\n", encoding="utf-8")
                rec["transcript"] = f"fabio_int{iid}.txt"
        except Exception as e:
            rec["error"] = f"{type(e).__name__}: {e}"[:300]
        state[iid] = rec
        print("OK  " if rec.get("clip") else "FAIL", scheda, iid, rec.get("start"), rec.get("end"), rec.get("error", ""), flush=True)
        json.dump(sorted(state.values(), key=lambda r: (r["scheda"], r["intervention"])),
                  io.open(state_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("CLIPS", sum(1 for r in state.values() if r.get("clip")), "of", len(state))


if __name__ == "__main__":
    main()
