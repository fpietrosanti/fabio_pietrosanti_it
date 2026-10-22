"""Scan the restored hermescenter.org posts: find the ones that name Fabio and the campaigns he signed.

Reads the restoration map of the Hermes project (slug -> live URL), fetches every post, and classifies it:
  named      — the text says "Pietrosanti" or "naif": candidate for the personal archive
  appeal     — an open letter / appeal / position paper (riuso, ANAC, software libero, voto elettronico, …)
  activity   — everything else: Hermes activity, not personal

Writes data/research/raw/pass5_hermes_live_<date>.json (named posts, as media items) and
data/research/hermes_live_scan.json (the full classification, for review).

Usage: python tools/hermes_scan.py [--limit N]
"""
import csv
import datetime
import html
import io
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT.parent / "hermescenter-restore/baseline/mappa_ripristino.csv"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36"
NAME = re.compile(r"(?i)pietrosanti|\bnaif\b")
THEMES = [
    ("riuso", r"(?i)riuso del software|riuso\b|software reuse"),
    ("anac", r"(?i)\bANAC\b|autorit[àa] nazionale anticorruzione"),
    ("software-libero", r"(?i)software libero|free software|open source|codice aperto"),
    ("voto-elettronico", r"(?i)voto elettronico|e-?voting|voto online|urne elettroniche|smartmatic|"
                         r"referendum.{0,40}(lombardia|autonomia)|seggi|scheda elettorale|rousseau"),
    ("whistleblowing", r"(?i)whistleblow|segnalazione di illeciti"),
    ("sorveglianza", r"(?i)sorveglianza|captator|trojan|data retention|spyware"),
    ("biometria", r"(?i)riconoscimento facciale|biometri|clearview"),
    ("foia", r"(?i)\bFOIA\b|accesso civico|accesso generalizzato"),
]
APPEAL = re.compile(r"(?i)appello|lettera aperta|open letter|position paper|posizione del centro|"
                    r"consultazione|esposto|segnalazione al garante|petizione|richiesta a|"
                    r"chiediamo|sottoscriv|firmatari")


def get(url):
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=45) as r:
                return r.read().decode("utf-8", "replace")
        except Exception:
            time.sleep(2 * (attempt + 1))
    return ""


def text_of(page):
    body = re.search(r'(?is)<(?:article|main)[^>]*>(.*?)</(?:article|main)>', page)
    t = body.group(1) if body else page
    t = re.sub(r"(?is)<(script|style|nav|footer|header)[^>]*>.*?</\1>", " ", t)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t))).strip()


def main():
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 0
    rows = list(csv.DictReader(io.open(MAP, encoding="utf-8-sig")))
    if limit:
        rows = rows[:limit]
    out, named = [], []
    for n, r in enumerate(rows, 1):
        url = r["url_ripristinato"]
        page = get(url)
        body = text_of(page)
        themes = [k for k, rx in THEMES if re.search(rx, body)]
        rec = {"date": r["data"], "title": r["titolo"], "url": url, "slug": r["slug"],
               "categories": r["categorie"], "themes": themes,
               "named": bool(NAME.search(body)), "appeal": bool(APPEAL.search(body)),
               "chars": len(body)}
        out.append(rec)
        if rec["named"]:
            m = NAME.search(body)
            ctx = body[max(0, m.start() - 160):m.end() + 160]
            named.append({
                "date": r["data"], "year": int(r["data"][:4]), "type": "press_release",
                "outlet": "Hermes Center for Transparency and Digital Human Rights",
                "title": r["titolo"], "url": url, "language": "it",
                "role": "author" if re.search(r"(?i)pietrosanti.{0,40}(scrive|dichiara|spiega)", ctx) else "subject",
                "note": f"Articolo del sito Hermes (ripristinato 2026-10-22). Contesto: …{ctx.strip()}…"[:600],
                "verified": True, "known": False,
                "themes": themes, "appeal": rec["appeal"],
            })
        if n % 20 == 0:
            print(f"  {n}/{len(rows)}…", flush=True)
        time.sleep(0.3)
    stamp = datetime.date.today().isoformat()
    json.dump(out, io.open(ROOT / "data/research/hermes_live_scan.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    json.dump(named, io.open(ROOT / f"data/research/raw/pass5_hermes_live_{stamp}.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    byt = {}
    for rec in out:
        for t in rec["themes"]:
            byt[t] = byt.get(t, 0) + 1
    print(f"{len(out)} articoli · {len(named)} nominano Fabio · appelli: {sum(1 for r in out if r['appeal'])}")
    print("temi:", ", ".join(f"{k} {v}" for k, v in sorted(byt.items(), key=lambda x: -x[1])))


if __name__ == "__main__":
    main()
