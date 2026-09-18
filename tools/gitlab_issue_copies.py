"""Offline copies of GitLab issues (code.videolan.org, gitlab.torproject.org) and GitHub issues via their APIs.

GitLab "work_items" pages need JavaScript (the copy tool gets HTTP 418 or an empty shell), so the issue and all
its notes are fetched from the REST API and saved as original.json + text.txt. GitHub issues are fetched the same
way (issue + comments) to have a complete thread even when the HTML copy is truncated.

Also relabels direct video files (*.mp4/*.webm) already saved as original.<ext> to "video-obtained".

Usage: python tools/gitlab_issue_copies.py <copies_dir>
"""
import datetime
import hashlib
import io
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from archive_copies import NAME_RE, UA  # noqa: E402

GITLAB = re.compile(r"https://(code\.videolan\.org|gitlab\.torproject\.org)/(.+?)/-/(?:work_items|issues)/(\d+)")
GITHUB = re.compile(r"https://github\.com/([^/]+/[^/]+)/issues/(\d+)")


def api(url):
    for a in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(3 * (a + 1))
    raise err


def pages(url):
    out, page = [], 1
    while True:
        batch = api(f"{url}{'&' if '?' in url else '?'}per_page=100&page={page}")
        out += batch
        if len(batch) < 100:
            return out
        page += 1


def gitlab(host, path, iid):
    base = f"https://{host}/api/v4/projects/{urllib.parse.quote(path, safe='')}/issues/{iid}"
    issue = api(base)
    try:
        notes = pages(base + "/notes?sort=asc")
    except Exception:  # noqa: BLE001  gitlab.torproject.org answers 401 to anonymous /notes
        notes = None
    lines = [f"{issue['title']}", f"{issue['web_url']}", f"opened {issue['created_at']} by {issue['author']['username']}"
             f" · state {issue['state']}" + (f" · closed {issue['closed_at']}" if issue.get("closed_at") else ""), "",
             issue.get("description") or ""]
    if notes is None:
        lines += ["", "[comments not saved: the API requires login for notes]"]
    for n in notes or []:
        lines += ["", f"--- {n['created_at']} {n['author']['username']}{' (system)' if n.get('system') else ''}", n["body"]]
    return {"issue": issue, "notes": notes}, "\n".join(lines)


def github(repo, num):
    base = f"https://api.github.com/repos/{repo}/issues/{num}"
    issue = api(base)
    comments = pages(base + "/comments")
    lines = [issue["title"], issue["html_url"], f"opened {issue['created_at']} by {issue['user']['login']} · state {issue['state']}",
             "", issue.get("body") or ""]
    for c in comments:
        lines += ["", f"--- {c['created_at']} {c['user']['login']}", c["body"] or ""]
    return {"issue": issue, "comments": comments}, "\n".join(lines)


def main():
    out = Path(sys.argv[1])
    state_p = out / "copies.json"
    state = json.load(io.open(state_p, encoding="utf-8"))
    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    for r in state:
        url = r["url"]
        if r.get("local") and re.search(r"\.(mp4|webm|mkv|mp3|ogg)$", url, re.I) and r["status"] != "video-obtained":
            if any((out / r["local"]).glob("original.*")):
                r.update(status="video-obtained", reason="direct media file downloaded (original.*); speaker named on the event page")
                print("video", url)
            continue
        m, g = GITLAB.match(url), GITHUB.match(url)
        if not (m or g) or r["status"] in ("obtained",) and (out / (r.get("local") or "x") / "original.json").exists():
            continue
        try:
            data, text = gitlab(*m.groups()) if m else github(*g.groups())
        except Exception as e:  # noqa: BLE001
            print("FAIL", url, e)
            continue
        folder = out / str(r.get("year") or "undated") / r["id"]
        folder.mkdir(parents=True, exist_ok=True)
        raw = json.dumps(data, ensure_ascii=False, indent=1).encode("utf-8")
        (folder / "original.json").write_bytes(raw)
        (folder / "text.txt").write_text(text, encoding="utf-8")
        found = bool(NAME_RE.search(text.encode("utf-8")))
        meta = {"source_url": url, "fetched_url": "api", "method": "api", "capture": None, "content_type": "application/json",
                "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "name_found": found, "fetched_at": now}
        (folder / "meta.json").write_text(json.dumps(meta, indent=1), encoding="utf-8")
        r.update(status="obtained" if found else "obtained-unconfirmed", method="api", capture=None, name_found=found,
                 local=str(folder.relative_to(out)).replace("\\", "/"), checked_at=now,
                 reason=("comments need login (issue text only)" if isinstance(data.get("notes", []), type(None)) else None)
                 if found else "issue saved via API; author/nick not in text")
        print(r["status"], url)
        time.sleep(1)
    json.dump(state, io.open(state_p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
