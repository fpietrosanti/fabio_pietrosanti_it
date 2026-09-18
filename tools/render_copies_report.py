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
    "video-obtained": "🎬 Video/audio scaricato (+ pagina)",
    "page-only": "🎞️ Solo pagina/link: video/audio non scaricabile",
    "media-not-downloaded": "⏳ Video/audio: non ancora processato",
    "not-obtained": "❌ Non ottenuta",
    "missing": "❌ Senza URL",
}
GOOD = {"obtained", "video-obtained"}
OWN_TYPES = {"article_by", "blog_post", "slides", "research", "project", "patent"}
OWN_HOSTS = ("infosecurity.ch", "naif.itapac.net", "pietrosanti.it", "slideshare.net/fpietrosanti", "github.com/fpietrosanti",
             "biohack.it", "monitora-pa.it", "globaleaks.org", "hermescenter.org", "logioshermes.org")


def licence(r):
    u = (r.get("url") or "").lower()
    if r.get("type") in OWN_TYPES or any(h in u for h in OWN_HOSTS):
        return "propria"
    return "terzi"


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
        "privata (`fabio_pietrosanti_it-copies/`, repo privato fpietrosanti/fabio_pietrosanti_it-library); questo report dice cosa è fatto, cosa è parziale e cosa manca.",
        "",
        "## Totali",
        "",
        f"- Voci in `data/media.json`: **{len(media)}**; già processate: **{len(recs)}**; ancora da processare: **{len(pending)}**",
        f"- Licenza delle copie ottenute: **{sum(1 for r in recs if r['status'] in GOOD|{'obtained-unconfirmed','page-only','partial'} and licence(r)=='propria')}** materiale proprio (ripubblicabile), "
        f"**{sum(1 for r in recs if r['status'] in GOOD|{'obtained-unconfirmed','page-only','partial'} and licence(r)=='terzi')}** di terzi (**solo archivio privato**, mai linkate dal sito)",
    ]
    for k, lab in LABEL.items():
        if st.get(k):
            L.append(f"- {lab}: **{st[k]}**")
    L += ["", "## Per anno", "", "| Anno | ✅ | 🎬 | 🟡 | 🟠 | 🎞️ | ⏳ | ❌ |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for y in sorted(by_year, key=lambda v: v or 0):
        c = by_year[y]
        L.append(f"| {y or 's.d.'} | {c['obtained']} | {c['video-obtained']} | {c['obtained-unconfirmed']} | {c['partial']} | {c['page-only']} | {c['media-not-downloaded']} | {c['not-obtained'] + c['missing']} |")
    L += ["", "## Da completare (non ancora processate)", ""]
    for m in sorted(pending, key=lambda m: (m.get("year") or 0))[:400]:
        L.append(f"- ⏳ **{m.get('year')}** · {(m.get('outlet') or '')[:40]} — [{(m.get('title') or m.get('url'))[:90]}]({m.get('url')})")
    L += ["", "## Fonti NON ottenute o incomplete", "", "Da recuperare con altre tecniche (browser, download media, richiesta di salvataggio al Web Archive).", ""]
    for r in sorted((r for r in recs if r["status"] not in GOOD), key=lambda r: (r["status"], r["year"] or 0)):
        L.append(f"- {LABEL[r['status']].split(' ')[0]} **{r['year']}** · {(r.get('outlet') or '')[:40]} — [{(r.get('title') or r['url'])[:90]}]({r['url']}) · licenza: {licence(r)}  \n  {r.get('reason') or ''}")
    clips_path = copies / "radioradicale_clips.json"
    if clips_path.exists():
        clips = json.load(io.open(clips_path, encoding="utf-8"))
        ok = [c for c in clips if c.get("clip")]
        L += ["", "## Interventi di Fabio ritagliati da Radio Radicale", "",
              f"Solo il suo intervento (video + trascrizione automatica), da `tools/radioradicale_clips.py`: **{len(ok)}** di {len(clips)}.", ""]
        for c in sorted(clips, key=lambda c: (c["scheda"], c["intervention"])):
            dur = f"{(c['end'] - c['start']) // 60}′{(c['end'] - c['start']) % 60:02d}″" if c.get("end") is not None and c.get("start") is not None else "fino a fine parte"
            if c.get("clip"):
                L.append(f"- 🎬 [scheda {c['scheda']}, intervento {c['intervention']}]({c['url']}) · {dur} · `{c['local']}/{c['clip']}` ({c.get('bytes', 0) / 1e6:,.0f} MB)")
            else:
                L.append(f"- ❌ [scheda {c['scheda']}, intervento {c['intervention']}]({c['url']}) · {c.get('error', '')}")
    L += ["", "## Fonti ottenute in locale", ""]
    for r in sorted((r for r in recs if r["status"] in GOOD), key=lambda r: (r["year"] or 0, r["url"])):
        via = f"Web Archive {r['capture'][:8]}" if r.get("method") == "wayback" and r.get("capture") else r.get("method")
        v = r.get("video") or {}
        if v.get("drive_url"):
            via += f" · [video su Drive]({v['drive_url']})"
        elif v.get("file"):
            via += f" · video locale `{v['file']}` ({v.get('bytes', 0) / 1e6:,.0f} MB, da caricare su Drive)"
        L.append(f"- **{r['year']}** · {(r.get('outlet') or '')[:40]} — [{(r.get('title') or r['url'])[:90]}]({r['url']}) · copia: `{r['local']}` ({via}) · licenza: {licence(r)}")
    io.open(ROOT / "docs/COPIE-OFFLINE.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("wrote docs/COPIE-OFFLINE.md", dict(st), "pending", len(pending))


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    main()
