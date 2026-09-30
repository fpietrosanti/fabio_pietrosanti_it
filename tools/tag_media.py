"""Propose tags for data/media.json (investigative-journalism strands) and write data/tags.json.

data/tags.json is the curated source of truth: {tag: {label_it, label_en, about, urls: [...]}}.
tools/merge_media.py applies it, so tags survive every rebuild of media.json.

This script only PROPOSES: it matches rules against the verified items, keeps any URL already curated,
and prints what changed. Review the printout, edit data/tags.json by hand where it is wrong.

Usage: python tools/tag_media.py [--write]
"""
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

RULES = {
    "ijf": (r"journalism festival|festival del giornalismo|\bIJF\b|#ijf|MOJO ITALIA", None),
    "dig": (r"\bDIG Festival\b|\bDIG Awards?\b|dig raddoppia|Backstair", None),
    "newsroom-leaks": (r"globaleaks|publeaks|irpileaks|irpi|nawaat|expoleaks|backstair|greenwald-in-a-box|"
                       r"take care of your sources|abbi cura delle tue fonti|leaksite|whistleblowing platform|"
                       r"piattaforma di whistleblowing", None),
    "transparency": (r"transparency international|anti-?corruption|anticorruzione|ALAC|allerta anticorruzione|"
                     r"whistleblowing.*(ANAC|corruzione)|ANAC", None),
    "source-protection": (r"intercettazion|wiretap|source protection|proteggere le fonti|protect the next snowden|"
                          r"proteggere i prossimi snowden|sicurezza digitale per giornalisti|crypto for journalists|"
                          r"comunicazioni confidenziali|secure communications|dissidenza|digital repression|firewall", None),
    # his own investigations: only pieces he authored/filed/presented, not press coverage of them
    "own-investigations": (r"ifuriosi|open ?rousseau|votare due volte|kaspersky-risks|monitora ?pa|monitorapa|securstar|"
                           r"infosecurityguard|phonecrypt|robots ?txt abuses|accesso civico|istanza di riesame|"
                           r"richiesta FOIA|FOIA su|FOIA sul|FOIA al|FOIA a |perimetro cibernetico|geo-aire|"
                           r"come non sprecare un milione|voto online\? no, grazie", None),
}
SKIP = re.compile(r"(?i)hacker journal|journalism\.medium")


def main():
    media = [i for i in json.load(io.open(ROOT / "data/media.json", encoding="utf-8")) if i.get("verified")]
    path = ROOT / "data/tags.json"
    cur = json.load(io.open(path, encoding="utf-8")) if path.exists() else {}
    out = {}
    for tag, (rx, _) in RULES.items():
        prev = cur.get(tag, {})
        urls = list(prev.get("urls", []))
        found = []
        for it in media:
            hay = f"{it['title']} {it['outlet']} {it['note']}"
            if SKIP.search(hay) or it["url"] in urls:
                continue
            if tag == "own-investigations" and (it["type"] in ("mentioned", "quoted", "interview", "radio", "tv", "podcast")
                                                or it.get("role") in ("subject", "interviewee", "quoted")):
                continue
            if re.search(rx, hay, re.I):
                found.append(it["url"])
        out[tag] = {
            "label_it": prev.get("label_it", tag),
            "label_en": prev.get("label_en", tag),
            "about": prev.get("about", ""),
            "urls": sorted(set(urls + found)),
        }
        print(f"{tag}: {len(urls)} curated + {len(found)} new = {len(out[tag]['urls'])}")
        for u in found[:200]:
            it = next(i for i in media if i["url"] == u)
            print(f"   + {it['date']} | {it['type'][:9]} | {it['outlet'][:36]} | {it['title'][:64]}")
    if "--write" in sys.argv:
        json.dump(out, io.open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("wrote data/tags.json")


if __name__ == "__main__":
    main()
