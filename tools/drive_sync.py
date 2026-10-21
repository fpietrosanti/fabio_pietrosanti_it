"""Upload the heavy offline copies to Google Drive and record their links. Resumable by design.

What it does, in order (every step is idempotent — re-running after any interruption resumes):
  1. rclone copy of every file larger than --min-size from the private library to the shared Drive folder
     "Archivio-homepage", keeping the <year>/<id>/<file> layout. rclone skips what is already there, so a
     crash, a reboot or a lost connection costs nothing.
  2. rclone lsjson of the folder -> data/drive_links.json in the site repo: {relative path: {id, url, size}}.
     The site reads it to offer "copy on Drive" next to the source link.
  3. prints what is still missing, so a scheduled run can simply be repeated until the count is zero.

The rclone remote is called "gdrive" and is configured once with the Drive OAuth token (kept in
%APPDATA%\\rclone\\rclone.conf, never in the repo). Set RCLONE if the binary is not on PATH.

Usage: python tools/drive_sync.py [--min-size 10M] [--dry-run] [--links-only]
"""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT.parent / "fabio_pietrosanti_it-copies"
REMOTE = "gdrive:"
LINKS = ROOT / "data/drive_links.json"
LOG = LIB / "_drive_sync.log"


def rclone_bin():
    env = os.environ.get("RCLONE")
    if env and Path(env).exists():
        return env
    found = shutil.which("rclone")
    if found:
        return found
    for p in Path(os.environ["LOCALAPPDATA"]).glob("Microsoft/WinGet/Packages/Rclone.Rclone*/*/rclone.exe"):
        return str(p)
    sys.exit("rclone not found: install it or set RCLONE=<path to rclone.exe>")


def run(args, **kw):
    return subprocess.run(args, text=True, capture_output=True, **kw)


def main():
    rc = rclone_bin()
    size = sys.argv[sys.argv.index("--min-size") + 1] if "--min-size" in sys.argv else "10M"
    if "--links-only" not in sys.argv:
        args = [rc, "copy", str(LIB), REMOTE,
                "--min-size", size,
                "--exclude", ".git/**", "--exclude", "_*.log",
                "--drive-chunk-size", "128M", "--transfers", "4", "--checkers", "8",
                "--retries", "20", "--low-level-retries", "20", "--retries-sleep", "20s",
                "--drive-stop-on-upload-limit", "--timeout", "10m",
                "--log-file", str(LOG), "--log-level", "INFO", "--stats", "5m", "--stats-one-line"]
        if "--dry-run" in sys.argv:
            args.append("--dry-run")
        print("uploading (resumable, safe to re-run)…")
        r = run(args)
        print("rclone copy exit", r.returncode)
        if r.returncode:
            print((r.stderr or "")[-400:])

    r = run([rc, "lsjson", "-R", "--files-only", "--no-modtime", REMOTE])
    if r.returncode:
        sys.exit("lsjson failed: " + (r.stderr or "")[-300:])
    links = {}
    for f in json.loads(r.stdout or "[]"):
        links[f["Path"].replace("\\", "/")] = {"id": f["ID"], "size": f["Size"],
                                               "url": f"https://drive.google.com/file/d/{f['ID']}/view"}
    LINKS.parent.mkdir(exist_ok=True)
    LINKS.write_text(json.dumps(links, ensure_ascii=False, indent=1), encoding="utf-8")

    # what is still missing locally -> remote
    want, missing, total = 0, [], 0
    lim = int(size[:-1]) * (1024 ** {"K": 1, "M": 2, "G": 3}[size[-1].upper()])
    for p in LIB.rglob("*"):
        if not p.is_file() or ".git" in p.parts or p.name.startswith("_"):
            continue
        if p.stat().st_size < lim:
            continue
        want += 1
        total += p.stat().st_size
        rel = str(p.relative_to(LIB)).replace("\\", "/")
        if rel not in links:
            missing.append(rel)
    print(f"data/drive_links.json: {len(links)} files on Drive")
    print(f"to upload: {want} files, {total / 1e9:.1f} GB · still missing: {len(missing)}")
    for m in missing[:10]:
        print("   -", m)
    sys.exit(2 if missing else 0)


if __name__ == "__main__":
    main()
