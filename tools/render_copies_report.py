"""Render the offline-copy status report from <copies_dir>/copies.json.

Writes docs/COPIE-OFFLINE.md in the site repo: totals, per-year coverage, and two lists —
sources obtained locally and sources NOT obtained (with the reason), so gaps are always visible.

Usage: python tools/render_copies_report.py <copies_dir>
"""
import io
import json
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LABEL = {
    "obtained": "✅ Copia locale, nome verificato nella copia",
    "obtained-unconfirmed": "🟡 Copia locale, nome NON trovato nella copia (paywall, JavaScript o capture sbagliata)",
    "partial": "🟠 Solo guscio JavaScript: serve cattura col browser",
    "media-not-downloaded": "🎞️ Video/audio: non ancora scaricato",
    "not-obtained": "❌ Non ottenuta",
    "missing": "❌ Senza URL",
}
GOOD = {"obtained"}


def main():
    copies = Path(sys.argv[1])
    recs = json.load(io.open(copies / "copies.json", encoding="utf-8"))
    media = json.load(io.open(ROOT / "data/media.json", encoding="utf-8"))
    from archive_copies import item_id  # noqa: E402
    done_ids = {r["id"] for r in recs}
    pending = [m for m in media if item_id(m) not in done_ids]
    st = Counter(r["status"] for r in recs)
    by_year = defaultdict(Counter)
    for r in recs:
        by_year[r["year"]][r["status"]] += 1
    L = [
        "# Copie offline delle fonti — stato",
        "",
        f"Aggiornato il {date.today().isoformat()} da `tools/render_copies_report.py`. Le copie stanno in una cartella locale",
        "non pubblicata (`fabio_pietrosanti_it-copies/`); questo report dice cosa abbiamo e cosa manca.",
        "",
        "## Totali",
        "",
        f"- Voci in `data/media.json`: **{len(media)}**; già processate: **{len(recs)}**; ancora da processare: **{len(pending)}**",
    ]
    for k, lab in LABEL.items():
        if st.get(k):
            L.append(f"- {lab}: **{st[k]}**")
    L += ["", "## Per anno", "", "| Anno | ✅ | 🟡 | 🟠 | 🎞️ | ❌ |", "|---|---:|---:|---:|---:|---:|"]
    for y in sorted(by_year, key=lambda v: v or 0):
        c = by_year[y]
        L.append(f"| {y or 's.d.'} | {c['obtained']} | {c['obtained-unconfirmed']} | {c['partial']} | {c['media-not-downloaded']} | {c['not-obtained'] + c['missing']} |")
    L += ["", "## Fonti NON ottenute o incomplete", "", "Da recuperare con altre tecniche (browser, download media, richiesta di salvataggio al Web Archive).", ""]
    for r in sorted((r for r in recs if r["status"] not in GOOD), key=lambda r: (r["status"], r["year"] or 0)):
        L.append(f"- {LABEL[r['status']].split(' ')[0]} **{r['year']}** · {(r.get('outlet') or '')[:40]} — [{(r.get('title') or r['url'])[:90]}]({r['url']})  \n  {r.get('reason') or ''}")
    L += ["", "## Fonti ottenute in locale", ""]
    for r in sorted((r for r in recs if r["status"] in GOOD), key=lambda r: (r["year"] or 0, r["url"])):
        via = f"Web Archive {r['capture'][:8]}" if r.get("method") == "wayback" and r.get("capture") else r.get("method")
        L.append(f"- **{r['year']}** · {(r.get('outlet') or '')[:40]} — [{(r.get('title') or r['url'])[:90]}]({r['url']}) · copia: `{r['local']}` ({via})")
    io.open(ROOT / "docs/COPIE-OFFLINE.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("wrote docs/COPIE-OFFLINE.md", dict(st), "pending", len(pending))


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    main()
