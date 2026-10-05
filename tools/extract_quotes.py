"""Extract candidate quotes about / by Fabio from the offline copies, for him to choose from.

Two kinds:
  SAID BY HIM   — quoted sentences near his name ("...", dice/spiega/afferma Pietrosanti; Pietrosanti: "...")
  SAID ABOUT HIM — how sources describe him (noun phrases right before/after the name:
                   "il noto hacker Fabio Naif", "hacker etico e cyberdefender professionista", ...)

Reads <library>/<year>/<id>/text.txt (byte-exact text of every local copy) plus the notes in data/media.json,
and writes docs/CITAZIONI.md, grouped by kind and sorted by date, each with outlet, date and source link.

Usage: python tools/extract_quotes.py [--max-per-item 4]
"""
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT.parent / "fabio_pietrosanti_it-copies"
NAME = re.compile(r"(Fabio\s+(?:«|\"|')?naif(?:»|\"|')?\s+)?Pietrosanti|\bnaif\b|石风翱", re.I)
# a quoted chunk: “…” «…» "…" '…'
QUOTED = re.compile(r"[“\"«](?P<q>[^”\"»]{25,320})[”\"»]")
VERB = re.compile(r"(?i)\b(dice|spiega|afferma|racconta|sostiene|commenta|aggiunge|precisa|osserva|conclude|ricorda|"
                  r"says|said|explains|told|adds|argues|notes)\b")
DESCR = re.compile(r"(?i)((?:il|lo|la|l'|un|uno|una|the|a|an)\s+[^.,;:()]{0,70}?"
                   r"(?:hacker|esperto|informatico|ricercatore|attivista|presidente|fondatore|co-?fondatore|direttore|"
                   r"imprenditore|cyberdefender|specialista|consulente|researcher|expert|founder|president|activist)"
                   r"[^.,;:()]{0,60}?)\s*(?:,\s*)?(?:Fabio\s+)?Pietrosanti")
DESCR2 = re.compile(r"(?i)(?:Fabio\s+)?Pietrosanti[^.,;:()]{0,10},\s*((?:hacker|esperto|informatico|ricercatore|attivista|"
                    r"presidente|fondatore|co-?fondatore|direttore|imprenditore|cyberdefender|consulente|researcher|"
                    r"expert|founder|president|activist)[^.;:()]{0,90})")
CLEAN = re.compile(r"\s+")


def tidy(s):
    return CLEAN.sub(" ", s).strip("  -–—·|")


def main():
    cap = int(sys.argv[sys.argv.index("--max-per-item") + 1]) if "--max-per-item" in sys.argv else 4
    media = {i["url"]: i for i in json.load(io.open(ROOT / "data/media.json", encoding="utf-8"))}
    copies = json.load(io.open(LIB / "copies.json", encoding="utf-8")) if (LIB / "copies.json").exists() else []
    said, about, seen = [], [], set()

    def add(bucket, text, rec):
        t = tidy(text)
        key = re.sub(r"\W+", "", t.lower())[:80]
        if len(t) < 20 or key in seen:
            return
        seen.add(key)
        bucket.append((rec.get("date") or str(rec.get("year") or ""), rec.get("outlet") or "", t, rec.get("url") or ""))

    for r in copies:
        it = media.get(r["url"])
        if not it or not it.get("verified") or not r.get("local"):
            continue
        f = LIB / r["local"] / "text.txt"
        if not f.exists():
            continue
        txt = f.read_text(encoding="utf-8", errors="replace")
        if not NAME.search(txt):
            continue
        n = 0
        for m in NAME.finditer(txt):
            win = txt[max(0, m.start() - 400):m.end() + 400]
            for d in list(DESCR.finditer(win)) + list(DESCR2.finditer(win)):
                add(about, d.group(1), it)
            for q in QUOTED.finditer(win):
                near = win[max(0, q.start() - 120):q.end() + 120]
                if NAME.search(near) and (VERB.search(near) or abs(q.start() - (m.start() - max(0, m.start() - 400))) < 160):
                    add(said, q.group("q"), it)
                    n += 1
                    if n >= cap:
                        break
            if n >= cap:
                break

    for it in media.values():
        if not it.get("verified"):
            continue
        for q in QUOTED.finditer(it.get("note") or ""):
            add(said, q.group("q"), it)
        for d in DESCR.finditer(it.get("note") or ""):
            add(about, d.group(1), it)

    def block(title, rows, note):
        L = [f"## {title}", "", note, ""]
        for date, outlet, text, url in sorted(rows, reverse=True):
            L.append(f"- **{date or '—'}** · {outlet[:60]} — «{text}»  \n  <{url}>")
        return L

    L = ["# Citazioni — estratto per la scelta", "",
         "Generato da `tools/extract_quotes.py` dalle copie offline (testo degli articoli) e dalle note dell'elenco media.",
         "Non è una selezione: è tutto quello che le fonti dicono. Segna quelle che vuoi sul sito e le metto nella sezione citazioni.",
         ""]
    L += block("Come ti descrivono", about, f"{len(about)} descrizioni trovate.")
    L += [""]
    L += block("Tue frasi citate", said, f"{len(said)} virgolettati trovati (alcuni possono essere di altri: controlla la fonte).")
    io.open(ROOT / "docs/CITAZIONI.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"docs/CITAZIONI.md: {len(about)} descrizioni, {len(said)} virgolettati")


if __name__ == "__main__":
    main()
