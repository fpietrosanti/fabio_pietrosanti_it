"""Measure Fabio's participation in the Tor community.

1. Issues he opened on the Tor Project GitLab (includes migrated Trac tickets, author "naif").
2. His posts on the Tor mailing lists (Mailman 2 pipermail archives, author index per month) and on the old
   or-talk list (archives.seul.org).

Writes data/research/tor_community.json (per list/year counts, first/last post, thread subjects, issues)
and docs/TOR-COMMUNITY.md. Individual posts are NOT added to media.json (Fabio's rule): this is a summary of
community participation.

Usage: python tools/tor_community.py
"""
import html
import io
import json
import re
import sys
import time
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from archive_copies import UA  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
LISTS = ["tor-talk", "tor-relays", "tor-dev", "tor-onions", "tor-project", "tor-teachers", "tor-community-team",
         "tor-mirrors", "tor-reports", "tor-censorship-events", "tor-scaling", "tor-announce", "network-health",
         "anti-censorship-team", "tor-qa", "tor-consensus-health"]
ME = re.compile(r"Fabio Pietrosanti|naif", re.I)
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]


def get(url):
    for a in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
        except Exception:
            pass
        time.sleep(3 * (a + 1))
    return None


def mailman_list(name, base="https://lists.torproject.org/pipermail"):
    idx = get(f"{base}/{name}/")
    if not idx:
        return None
    months = re.findall(r'href="(\d{4}-[A-Za-z]+)/(?:thread|author|date)\.html"', idx)
    months = list(dict.fromkeys(months))
    posts = []
    for m in months:
        page = get(f"{base}/{name}/{m}/author.html")
        time.sleep(0.4)
        if not page:
            continue
        for href, subj, who in re.findall(r'<LI><A HREF="(\d+\.html)">(.*?)\s*</A>.*?<I>(.*?)\s*</I>', page, re.S | re.I):
            if ME.search(who):
                y, mon = m.split("-")
                posts.append({"list": name, "year": int(y), "month": MONTHS.index(mon) + 1 if mon in MONTHS else 0,
                              "subject": re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", subj))).strip(),
                              "url": f"{base}/{name}/{m}/{href}"})
    return posts


def main():
    out = {"lists": {}, "issues": []}
    for name in LISTS:
        posts = mailman_list(name)
        if posts is None:
            print("no archive", name)
            continue
        out["lists"][name] = posts
        print(name, len(posts))
    # old or-talk (2003-2010) on archives.seul.org
    ortalk = []
    idx = get("http://archives.seul.org/or/talk/")
    if idx:
        for m in dict.fromkeys(re.findall(r'href="([A-Z][a-z]{2}-\d{4})/', idx)):
            page = get(f"http://archives.seul.org/or/talk/{m}/maillist.html")
            time.sleep(0.4)
            if not page:
                continue
            for href, subj, who in re.findall(r'<li><strong><a name="\d+" href="(msg\d+\.html)">(.*?)</a></strong>.*?<em>(.*?)</em>', page, re.S | re.I):
                if ME.search(who):
                    mon, y = m.split("-")
                    ortalk.append({"list": "or-talk", "year": int(y), "month": 0, "subject": html.unescape(subj).strip(),
                                   "url": f"http://archives.seul.org/or/talk/{m}/{href}"})
        out["lists"]["or-talk"] = ortalk
        print("or-talk", len(ortalk))
    # issues
    issues = []
    for page in range(1, 6):
        t = get(f"https://gitlab.torproject.org/api/v4/groups/tpo/issues?author_username=naif&scope=all&state=all&per_page=100&page={page}")
        batch = json.loads(t) if t else []
        if not batch:
            break
        issues += [{"date": i["created_at"][:10], "closed": (i.get("closed_at") or "")[:10], "ref": i["references"]["full"],
                    "title": i["title"], "url": i["web_url"], "milestone": (i.get("milestone") or {}).get("title")} for i in batch]
    out["issues"] = sorted({i["url"]: i for i in issues}.values(), key=lambda i: i["date"])
    json.dump(out, io.open(ROOT / "data/research/tor_community.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    allp = [p for v in out["lists"].values() for p in v]
    per = defaultdict(Counter)
    for p in allp:
        per[p["list"]][p["year"]] += 1
    years = sorted({p["year"] for p in allp} | {int(i["date"][:4]) for i in out["issues"]})
    L = ["# Partecipazione alla Tor Community", "",
         "Generato da `tools/tor_community.py` (archivi pubblici delle mailing list Tor + ticket GitLab/Trac aperti da «naif»).",
         "I singoli post non entrano nell'elenco media: qui c'è il riepilogo della partecipazione.", "",
         f"- **Post in mailing list:** {len(allp)} (primo: {min((p['year'], p['month']) for p in allp) if allp else '-'}, "
         f"ultimo: {max((p['year'], p['month']) for p in allp) if allp else '-'})",
         f"- **Ticket aperti:** {len(out['issues'])} ({out['issues'][0]['date'] if out['issues'] else '-'} → {out['issues'][-1]['date'] if out['issues'] else '-'})",
         "", "## Per anno", "", "| Anno | " + " | ".join(per) + " | Ticket |", "|---|" + "---:|" * (len(per) + 1)]
    for y in years:
        L.append(f"| {y} | " + " | ".join(str(per[l][y] or "") for l in per) + f" | {sum(1 for i in out['issues'] if i['date'].startswith(str(y))) or ''} |")
    L += ["", "## Ticket", ""]
    for i in out["issues"]:
        L.append(f"- {i['date']} [{i['ref']}]({i['url']}) — {i['title']}" + (f" · milestone {i['milestone']}" if i["milestone"] else ""))
    L += ["", "## Discussioni principali (per numero di messaggi)", ""]
    subj = Counter((p["list"], re.sub(r"^(re:\s*|\[tor-[a-z-]+\]\s*)+", "", p["subject"], flags=re.I)) for p in allp)
    for (lst, s), n in subj.most_common(60):
        L.append(f"- {lst}: {s} ({n})")
    io.open(ROOT / "docs/TOR-COMMUNITY.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("posts", len(allp), "issues", len(out["issues"]))


if __name__ == "__main__":
    main()
