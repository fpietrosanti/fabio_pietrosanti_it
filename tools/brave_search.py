"""Run the pending entries of data/research/queue.json through the Brave Search API.

Needs an API key in the environment variable BRAVE_API_KEY (Fabio creates it at
https://api-dashboard.search.brave.com/ ; free tier ~2,000 queries/month, 1 query/second).
Brave supports site: and quoted phrases, and has no CAPTCHA, so it complements the Google
searches done in Fabio's Chrome.

Writes candidate URLs to data/research/candidates/brave-<timestamp>.txt, marks queue entries
"done-brave" and prints the command to verify them.

Usage: python tools/brave_search.py [--max N]
"""
import io
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOPIC = ('(GlobaLeaks OR hacker OR Hermes OR whistleblowing OR Rousseau OR Tor OR cifratura OR intercettazioni '
         'OR PrivateWave OR Kaspersky OR "voto elettronico" OR sicurezza)')


def brave(q, offset=0):
    url = "https://api.search.brave.com/res/v1/web/search?" + urllib.parse.urlencode({"q": q, "count": 20, "offset": offset})
    req = urllib.request.Request(url, headers={"Accept": "application/json", "X-Subscription-Token": os.environ["BRAVE_API_KEY"]})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    return [x["url"] for x in data.get("web", {}).get("results", [])]


def main():
    if not os.environ.get("BRAVE_API_KEY"):
        sys.exit("BRAVE_API_KEY not set: nothing to do")
    maxq = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 40
    qpath = ROOT / "data/research/queue.json"
    q = json.load(io.open(qpath, encoding="utf-8"))
    todo = [("d", e) for e in q["domains"] if not e.get("brave")] + [("q", e) for e in q["queries"] if not e.get("brave")]
    found, n = [], 0
    for kind, e in todo:
        if n >= maxq:
            break
        query = f'site:{e["domain"]} "Pietrosanti" {TOPIC}' if kind == "d" else e["query"]
        urls = []
        for page in range(int(e.get("pages", 1)) if kind == "q" else 2):
            try:
                res = brave(query, page)
            except Exception as ex:  # quota or network: stop, the next run resumes
                print("STOP", type(ex).__name__, ex)
                n = maxq
                break
            n += 1
            urls += res
            time.sleep(1.2)
            if len(res) < 20:
                break
        e["brave"] = {"date": datetime.now().strftime("%Y-%m-%d"), "found": len(urls)}
        found += urls
        print(f"{len(urls):3} {query[:90]}")
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M")
    out = ROOT / f"data/research/candidates/brave-{stamp}.txt"
    out.write_text("# Brave Search API " + stamp + "\n" + "\n".join(dict.fromkeys(found)) + "\n", encoding="utf-8")
    q["history"].append({"date": stamp, "engine": "brave", "queries": n, "candidates": len(set(found))})
    json.dump(q, io.open(qpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"candidates: {len(set(found))} -> {out.name}\nnext: python tools/verify_candidates.py {out.as_posix()} pass3_brave_{stamp}")


if __name__ == "__main__":
    main()
