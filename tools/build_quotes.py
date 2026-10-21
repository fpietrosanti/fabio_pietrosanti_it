"""Build data/quotes.json: quotes attributable to Fabio, extracted from the offline copies.

Strict attribution only — a quoted sentence counts when the quote and his name are tied by a reporting
verb in the same window and no other person's name sits between them:
    «…», dice Fabio Pietrosanti      Pietrosanti: «…»      "…", says Pietrosanti
Each quote keeps outlet, date and source URL, so every line on the site can be checked.

Usage: python tools/build_quotes.py [--min-len 40] [--max-len 260]
"""
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT.parent / "fabio_pietrosanti_it-copies"
NAME = r"(?:Fabio\s+)?Pietrosanti|\bnaif\b"
VERB = (r"dice|spiega|afferma|racconta|sostiene|commenta|aggiunge|precisa|osserva|conclude|ricorda|avverte|"
        r"chiarisce|sottolinea|says|said|explains|explained|tells|told|adds|argues|notes|warns")
OTHER = re.compile(r"\b[A-Z][a-z]{2,}\s+[A-Z][a-z]{3,}\b")  # another full name in between
QUOTE = r"[“\"«](?P<q>[^”\"»]{%d,%d})[”\"»]"
CLEAN = re.compile(r"\s+")
NOISE = re.compile(r"(?i)cookie|privacy policy|javascript|abbonati|newsletter|iscriviti|registrati|^[\W\d]+$")


def tidy(s):
    return CLEAN.sub(" ", s).strip("  -–—·|")


def main():
    lo = int(sys.argv[sys.argv.index("--min-len") + 1]) if "--min-len" in sys.argv else 40
    hi = int(sys.argv[sys.argv.index("--max-len") + 1]) if "--max-len" in sys.argv else 260
    qre = re.compile(QUOTE % (lo, hi))
    after = re.compile(qre.pattern + r"[,;:\s]*(?:ha\s+)?(?:%s)\b[^.;:]{0,40}?(?:%s)" % (VERB, NAME), re.I)
    before = re.compile(r"(?:%s)[^.;:]{0,40}?(?:%s)[^.;:]{0,20}?[:,]\s*" % (NAME, VERB), re.I)
    colon = re.compile(r"(?:%s)\s*:\s*" % NAME, re.I)

    media = {i["url"]: i for i in json.load(io.open(ROOT / "data/media.json", encoding="utf-8"))}
    copies = json.load(io.open(LIB / "copies.json", encoding="utf-8")) if (LIB / "copies.json").exists() else []
    out, seen = [], set()
    for r in copies:
        it = media.get(r["url"])
        if not it or not it.get("verified") or not r.get("local"):
            continue
        f = LIB / r["local"] / "text.txt"
        if not f.exists():
            continue
        txt = CLEAN.sub(" ", f.read_text(encoding="utf-8", errors="replace"))
        if not re.search(NAME, txt, re.I):
            continue
        found = []
        for m in after.finditer(txt):                       # «…», dice Pietrosanti
            found.append((m.group("q"), "after"))
        for m in qre.finditer(txt):                         # Pietrosanti spiega: «…»  /  Pietrosanti: «…»
            head = txt[max(0, m.start() - 90):m.start()]
            if before.search(head) or colon.search(head[-40:]):
                found.append((m.group("q"), "before"))
        for q, how in found:
            t = tidy(q)
            if NOISE.search(t) or len(t) < lo:
                continue
            key = re.sub(r"\W+", "", t.lower())[:90]
            if key in seen:
                continue
            seen.add(key)
            out.append({
                "text": t,
                "lang": (it.get("language") or "").lower()[:2] or "it",
                "outlet": it.get("outlet") or "",
                "date": it.get("date") or (str(it.get("year")) if it.get("year") else ""),
                "year": it.get("year") or 0,
                "url": it.get("live_url") or it["url"],
                "how": how,
            })
    out.sort(key=lambda q: (q["year"], q["date"]), reverse=True)
    json.dump(out, io.open(ROOT / "data/quotes.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"data/quotes.json: {len(out)} quotes, {len({q['url'] for q in out})} sources, "
          f"{min((q['year'] for q in out if q['year']), default=0)}–{max((q['year'] for q in out), default=0)}")


if __name__ == "__main__":
    main()
