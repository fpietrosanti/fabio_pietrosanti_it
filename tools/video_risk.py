"""Valuta ogni video dell'inventario su due assi: diritti/Content ID (YouTube) e censura (Cina).

Le valutazioni sono una PRIMA PASSATA automatica, da rivedere a mano: servono a ordinare
173 video per priorita', non a decidere al posto di una persona.

Assi
  rights  : chi detiene la registrazione -> own_free | free_license | third_party | broadcaster | unknown
  cid     : rischio di rivendicazione Content ID su YouTube -> basso | medio | alto
  cn      : rischio di blocco/censura su Bilibili -> basso | medio | alto | critico

Uso: python tools/video_risk.py
"""
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BROADCAST = re.compile(r"(?i)\brai\b|rai ?[0-9]|sky ?tg|la ?7|la7|mediaset|tg1|tg24|la stampa|"
                       r"corriere|repubblica|sole 24|tgcom|euronews")
FREE_LIC = re.compile(r"(?i)\bccc\b|chaos communication|33c3|fosdem|peertube|linux day|"
                      r"hackmeeting|endsummercamp|ohm2013|e-privacy|winston smith|debconf")
PLATFORM = re.compile(r"(?i)youtube|vimeo|dailymotion|facebook")
RADIORAD = re.compile(r"(?i)radio radicale")

# temi che su una piattaforma cinese passano la revisione con difficolta' crescente
CN_CRIT = re.compile(r"(?i)whistleblow|globaleaks|anonimat|anonymity|\btor\b|censur|censor|"
                     r"sorveglianza di stato|dissident|hong kong|tibet|uygh|xinjiang|"
                     r"freedom of (the )?press|liberta' di stampa|liberta di stampa|leak")
CN_HIGH = re.compile(r"(?i)sorveglianz|surveillance|spyware|trojan|captatore|intercettazion|"
                     r"diritti umani|human rights|attivis|activis|giornalismo d'inchiesta|"
                     r"investigative journalism|corruzion|corruption|anticorruzione|"
                     r"trasparenz|transparency|foia|accesso civico|democrazi|democracy|"
                     r"voto elettronico|e-voting|elezion|election")
CN_MED = re.compile(r"(?i)privacy|crittograf|encryption|gdpr|dati personali|data protection|"
                    r"sovranit|sovereignt|cloud act|hacker|hacking|sicurezza|security|"
                    r"digital rights|diritti digitali|open source|software libero|free software")
CN_CHINA = re.compile(r"(?i)\bcina\b|\bchina\b|cinese|chinese|shenzhen|huawei|tiktok")


def rights_of(x):
    o, u, lic = x["outlet"], x["source_url"], x["embedded_license"]
    if "creativecommons" in (lic or "").lower():
        return "own_free", "licenza CC nei metadati del file"
    if BROADCAST.search(o):
        return "broadcaster", "registrazione di un'emittente"
    if RADIORAD.search(o):
        # Radio Radicale registra e-privacy e molti convegni: la registrazione e' loro,
        # e va riconosciuta prima del tema dell'evento, che e' di mondo libero.
        return "third_party", "archivio Radio Radicale: registrazione loro, gia' online"
    if FREE_LIC.search(o) or FREE_LIC.search(x["title"]):
        return "free_license", "evento del mondo free software/hacker: licenza libera probabile, da confermare"
    if PLATFORM.search(o) or PLATFORM.search(u):
        return "third_party", "gia' pubblicato da terzi sul loro canale"
    return "unknown", "da accertare"


def cid_of(rights):
    return {"broadcaster": "alto", "third_party": "medio",
            "free_license": "basso", "own_free": "basso", "unknown": "medio"}[rights]


def cn_of(x):
    blob = " ".join((x["title"], x["outlet"], x["note"], x["type"]))
    if CN_CRIT.search(blob):
        return "critico", "temi che la revisione preventiva cinese intercetta per definizione"
    if CN_CHINA.search(blob):
        return "critico", "parla direttamente di Cina"
    if CN_HIGH.search(blob):
        return "alto", "sorveglianza, diritti, trasparenza o processi elettorali"
    if CN_MED.search(blob):
        return "medio", "privacy/sicurezza/sovranita': dipende da come e' inquadrato"
    return "basso", "tema tecnico o neutro"


def main():
    inv = json.load(io.open(ROOT / "data/video_inventory.json", encoding="utf-8"))
    for x in inv:
        x["rights"], x["rights_why"] = rights_of(x)
        x["cid_risk"] = cid_of(x["rights"])
        x["cn_risk"], x["cn_why"] = cn_of(x)
    json.dump(inv, io.open(ROOT / "data/video_risk.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    def tally(k):
        c = {}
        for x in inv:
            c[x[k]] = c.get(x[k], 0) + 1
        return " · ".join(f"{a}: {b}" for a, b in sorted(c.items(), key=lambda t: -t[1]))
    print("diritti    ", tally("rights"))
    print("Content ID ", tally("cid_risk"))
    print("Cina       ", tally("cn_risk"))
    ok = [x for x in inv if x["rights"] in ("own_free", "free_license")]
    print(f"\npubblicabili da noi su YouTube: {len(ok)} video, {sum(x['duration'] for x in ok)/3600:.1f} ore")
    cn = [x for x in ok if x["cn_risk"] in ("basso", "medio")]
    print(f"di questi, candidabili a Bilibili: {len(cn)} video, {sum(x['duration'] for x in cn)/3600:.1f} ore")


if __name__ == "__main__":
    main()
