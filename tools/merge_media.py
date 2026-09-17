"""Merge web-research results about Fabio Pietrosanti into one deduplicated list,
compare it with what the old Blogger site already listed, and render a review
document grouped by year.

Usage:
  python tools/merge_media.py <dir with slice*.json>

Writes:
  data/media.json                        merged, deduplicated items (source for the site)
  data/media-baseline-blogger-2013.json  items listed on the old site (parsed from the archive)
  docs/RICERCA-MEDIA-2026-09.md          review: per year, NEW vs already on the old site
"""
import glob
import io
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / "archive/blogger-2026-09-16/content-post-2013-10.md"
MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
TYPE_LABEL = {
    "talk": "Talk", "article_by": "Articolo scritto", "interview": "Intervista", "quoted": "Citato",
    "research": "Ricerca", "paper": "Paper", "book": "Libro", "tv": "TV", "radio": "Radio",
    "video": "Video", "podcast": "Podcast", "slides": "Slide", "project": "Progetto",
    "press_release": "Comunicato", "hearing": "Audizione", "wiki": "Wiki", "other": "Altro",
    "mentioned": "Menzionato", "blog_post": "Post sul blog infosecurity.ch", "thesis": "Tesi", "report": "Report", "book_chapter": "Capitolo di libro", "patent": "Brevetto",
}


def norm_url(u):
    if not u:
        return ""
    s = urlsplit(u.strip())
    host = s.netloc.lower().removeprefix("www.").removeprefix("m.")
    if host in ("web.archive.org",):
        m = re.search(r"/web/\d+[a-z_]*/(.+)$", s.path)
        if m:
            return norm_url(m.group(1) if "://" in m.group(1) else "http://" + m.group(1))
    path = s.path.rstrip("/")
    if host.endswith("youtube.com") and "v=" in s.query:
        return "youtube/" + re.search(r"v=([\w-]+)", s.query).group(1)
    if host == "youtu.be":
        return "youtube/" + path.strip("/")
    return host + path


def norm_title(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def parse_baseline():
    text = io.open(ARCHIVE, encoding="utf-8").read()
    items = []
    for section, kind in (("## Conference / Pubblication", "talk"), ("## Security Research", "research")):
        block = text.split(section, 1)[1].split("\n## ", 1)[0]
        for line in block.splitlines():
            line = line.strip()
            if not line.startswith("- ") or line.startswith("- TODO"):
                continue
            body = line[2:]
            urls = re.findall(r"\]\((https?://[^)]+)\)", body)
            plain = re.sub(r"\[([^\]]*)\]\([^)]+\)", r"\1", body)
            m = re.match(r"(\d{1,2})?\s*([A-Za-z]{3,})?\s*(\d{4})\s*,?\s*(.*)", plain)
            year = int(m.group(3)) if m else None
            month = MONTHS.get((m.group(2) or "")[:3].lower()) if m else None
            day = int(m.group(1)) if m and m.group(1) else None
            date = f"{year}" + (f"-{month:02d}" if month else "") + (f"-{day:02d}" if day and month else "")
            items.append({
                "date": date, "year": year,
                "type": "article_by" if "article" in plain.lower() and kind == "talk" else kind,
                "title": (m.group(4) if m else plain).strip(" ,:"),
                "urls": urls, "source": "blogger-2013",
            })
    return items


def matches_baseline(item, baseline):
    u = norm_url(item.get("url"))
    t = norm_title(item.get("title"))
    for b in baseline:
        if u and any(norm_url(x) == u for x in b["urls"]):
            return True
        if item.get("year") == b["year"]:
            bt = norm_title(b["title"])
            words = [w for w in bt.split() if len(w) > 4]
            if words and sum(w in t or w in norm_title(item.get("outlet", "")) + " " + norm_title(item.get("note", "")) for w in words) >= max(2, len(words) // 2):
                return True
    return False


def year_of(item):
    y = item.get("year")
    if isinstance(y, int):
        return y
    m = re.match(r"(\d{4})", str(item.get("date") or ""))
    return int(m.group(1)) if m else None


# Hosts never merged into the public data: personal material held back until Fabio decides
# (kept in the private linkedin-i18n repo, archive/held-from-public-site/).
HELD_HOSTS = {"rapamycin.news"}

# Individual forum and mailing-list posts are NOT publications (Fabio, 2026-09-16: "otherwise I have
# thousands of posts on mailing list archives"). Security advisories stay: they are research.
POST_HOSTS = {
    "seclists.org", "marc.info", "archive.torproject.org", "mailman.stanford.edu", "mail-archive.com",
    "groups.google.com", "forum.italia.it",
}
POST_PATHS = ("voipsa.org/pipermail",)


def is_list_or_forum_post(item):
    u = norm_url(item.get("url"))
    host = u.split("/")[0]
    if item.get("type") == "research":
        return False
    return host in POST_HOSTS or host.startswith("lists.") or u.startswith(POST_PATHS)


def merge(files):
    raw = []
    for f in files:
        try:
            data = json.load(io.open(f, encoding="utf-8"))
        except Exception as exc:  # a malformed slice must not block the others
            print(f"SKIP {f}: {exc}")
            continue
        for it in data:
            if norm_url(it.get("url")).split("/")[0] in HELD_HOSTS or is_list_or_forum_post(it):
                continue
            if norm_url(it.get("url")).startswith("infosecurity.ch") and it.get("type") == "article_by":
                it["type"] = "blog_post"
            it["_slice"] = Path(f).stem
            raw.append(it)
    by_key = {}
    for it in raw:
        it["year"] = year_of(it)
        key = norm_url(it.get("url")) or f"{it['year']}|{norm_title(it.get('title'))}"
        if key in by_key:
            old = by_key[key]
            # keep the more precise / verified record, remember all slices that found it
            better = (bool(it.get("verified")), len(str(it.get("date") or ""))) > (bool(old.get("verified")), len(str(old.get("date") or "")))
            slices = sorted(set(old.get("_slices", [old["_slice"]]) + [it["_slice"]]))
            if better:
                it["_slices"] = slices
                by_key[key] = it
            else:
                old["_slices"] = slices
        else:
            it["_slices"] = [it["_slice"]]
            by_key[key] = it
    # second pass: same year + same normalized title from different URLs (syndication)
    seen, out = {}, []
    for it in by_key.values():
        tk = (it["year"], norm_title(it.get("title"))[:60])
        if tk[1] and tk in seen and it.get("type") == seen[tk].get("type"):
            seen[tk].setdefault("mirrors", []).append(it.get("url"))
            continue
        seen[tk] = it
        out.append(it)
    return raw, out


def render(items, baseline, raw_count):
    years = sorted({i["year"] for i in items if i["year"]} | {b["year"] for b in baseline if b["year"]})
    first, last = min(years), max(years)
    by_year = defaultdict(list)
    for i in items:
        by_year[i["year"]].append(i)
    new_items = [i for i in items if not i["on_old_site"]]
    lines = [
        "# Ricerca online — articoli, interviste, ricerche, talk e media su Fabio Pietrosanti",
        "",
        "Generato da `tools/merge_media.py` unendo tutte le passate di ricerca in `data/research/raw/`.",
        "Confronto con il vecchio sito (Blogger, ultimo aggiornamento ottobre 2013).",
        "",
        "## Riepilogo",
        "",
        f"- Risultati grezzi dalle ricerche: **{raw_count}**; dopo deduplica: **{len(items)}**",
        f"- Già presenti sul vecchio sito: **{len(items) - len(new_items)}** (su {len(baseline)} voci elencate lì)",
        f"- **Nuovi rispetto al vecchio sito: {len(new_items)}**",
        f"- Verificati aprendo la pagina: **{sum(1 for i in items if i.get('verified'))}**; solo da risultato di ricerca: **{sum(1 for i in items if not i.get('verified'))}**",
        "",
        "Per tipo (nuovi): " + ", ".join(f"{TYPE_LABEL.get(t, t)} {n}" for t, n in Counter(i.get("type") for i in new_items).most_common()),
        "",
        "### Copertura per anno",
        "",
        "| Anno | Vecchio sito | Trovati | di cui nuovi |",
        "|---|---:|---:|---:|",
    ]
    empty = []
    for y in range(first, last + 1):
        old = sum(1 for b in baseline if b["year"] == y)
        found = len(by_year.get(y, []))
        new = sum(1 for i in by_year.get(y, []) if not i["on_old_site"])
        if found == 0:
            empty.append(y)
        lines.append(f"| {y} | {old} | {found} | {new} |")
    lines += ["", "Anni senza nessun risultato: " + (", ".join(map(str, empty)) if empty else "nessuno"), ""]
    undated = [i for i in items if not i["year"]]
    for y in range(last, first - 1, -1):
        rows = sorted(by_year.get(y, []), key=lambda i: str(i.get("date") or ""), reverse=True)
        if not rows:
            continue
        n_new = sum(1 for i in rows if not i["on_old_site"])
        lines += [f"## {y} — {len(rows)} voci, {n_new} nuove", ""]
        for i in rows:
            badge = "🆕 " if not i["on_old_site"] else "↺ "
            ver = "" if i.get("verified") else " _(non verificato)_"
            title = (i.get("title") or "").replace("|", "/").strip()
            url = i.get("url") or ""
            link = f"[{title}]({url})" if url else title
            lines.append(
                f"- {badge}**{i.get('date') or y}** · {TYPE_LABEL.get(i.get('type'), i.get('type'))} · "
                f"{i.get('outlet', '')} — {link}{ver}"
                + (f"  \n  {i['note']}" if i.get("note") else "")
            )
        lines.append("")
    if undated:
        lines += ["## Senza data", ""]
        for i in undated:
            lines.append(f"- 🆕 {TYPE_LABEL.get(i.get('type'), i.get('type'))} · {i.get('outlet', '')} — [{i.get('title')}]({i.get('url')})")
        lines.append("")
    lines += ["---", "", "Legenda: 🆕 nuovo rispetto al vecchio sito · ↺ già citato sul vecchio sito."]
    return "\n".join(lines) + "\n"


def main():
    src = Path(sys.argv[1])
    files = sorted(glob.glob(str(src / "*.json")))
    baseline = parse_baseline()
    raw, items = merge(files)
    for i in items:
        i["on_old_site"] = bool(i.get("known")) or matches_baseline(i, baseline)
        i.pop("_slice", None)
    items.sort(key=lambda i: (i["year"] or 0, str(i.get("date") or "")))
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "docs").mkdir(exist_ok=True)
    json.dump(baseline, io.open(ROOT / "data/media-baseline-blogger-2013.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(items, io.open(ROOT / "data/media.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    io.open(ROOT / "docs/RICERCA-MEDIA-2026-09.md", "w", encoding="utf-8").write(render(items, baseline, len(raw)))
    print(f"files={len(files)} raw={len(raw)} merged={len(items)} baseline={len(baseline)} new={sum(1 for i in items if not i['on_old_site'])}")


if __name__ == "__main__":
    main()
