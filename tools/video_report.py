"""Scrive docs/VIDEO-PUBBLICAZIONE.md: la scheda di ogni video con i due rating di rischio.

Deduplica per fonte (lo stesso talk e' spesso in piu' formati) e ordina per anno.
Rieseguibile: si rigenera da video_risk.json + video_liveness.json.
"""
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
R = {"basso": "🟢 basso", "medio": "🟡 medio", "alto": "🟠 alto", "critico": "🔴 critico"}
RIGHTS = {"own_free": "nostro / CC", "free_license": "licenza libera (da confermare)",
          "third_party": "di terzi, gia' online", "broadcaster": "emittente", "unknown": "da accertare"}


def main():
    inv = json.load(io.open(ROOT / "data/video_risk.json", encoding="utf-8"))
    live = json.load(io.open(ROOT / "data/video_liveness.json", encoding="utf-8"))
    seen, rows = {}, []
    for x in sorted(inv, key=lambda y: (-(y.get("year") or 0), y["title"])):
        key = x["source_url"] or x["file"]
        if key in seen:
            seen[key] += 1
            continue
        seen[key] = 1
        rows.append(x)

    out = [
        "# Video d'archivio: cosa si puo' pubblicare, dove e con quale rischio",
        "",
        f"Generato da `tools/video_report.py`. {len(inv)} file, {len(rows)} registrazioni distinte "
        f"(lo stesso intervento e' spesso archiviato in piu' formati), "
        f"{sum(x['duration'] for x in inv)/3600:.0f} ore, "
        f"{sum(x['size'] for x in inv)/2**30:.0f} GB.",
        "",
        "**I due rating sono una prima passata automatica.** Ordinano il lavoro, non lo decidono: "
        "la colonna diritti va confermata caso per caso prima di caricare qualunque cosa.",
        "",
        "| Anno | Durata | Registrazione | Diritti | Content ID | Cina | Fonte |",
        "|---|---|---|---|---|---|---|",
    ]
    for x in rows:
        st = live.get(x["source_url"], "")
        src = "viva" if st.startswith("vivo") else ("assente" if "nessuna" in st else "non raggiungibile")
        out.append(
            f"| {x.get('year') or '—'} | {x['duration']//60}′ | {(x['title'] or '(senza titolo)')[:70]} "
            f"| {RIGHTS[x['rights']]} | {R[x['cid_risk']]} | {R[x['cn_risk']]} | {x['outlet'][:40]} ({src}) |")
    io.open(ROOT / "docs/VIDEO-PUBBLICAZIONE.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"scritto docs/VIDEO-PUBBLICAZIONE.md — {len(rows)} registrazioni distinte")


if __name__ == "__main__":
    main()
