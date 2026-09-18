"""Build the single-page homepage (index.html) from the data files.

Sources
  data/linkedin/en.json      LinkedIn master (headline, About, experience) — copied verbatim, never rewritten
  site/content.en.json       hand-written homepage text (story, project descriptions, UI strings)
  data/projects.json         project registry
  data/media.json            talks, press, writing, research (only verified items are published)
  ../fabio_pietrosanti_it-copies/copies.json   offline-copy status (Web Archive capture used for "archived copy")
  site/copies.json           optional: light copies hosted in this repo / heavy files on Google Drive

Usage: python tools/build_site.py [--lang en]
Then:  python tools/check_linkedin_coherence.py
"""
import html
import io
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT.parent / "fabio_pietrosanti_it-copies"
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

CATS = {
    "talks": {"talk", "workshop", "panel", "slides", "village", "hearing"},
    "press": {"interview", "quoted", "mentioned", "newspaper", "press_release"},
    "av": {"tv", "radio", "podcast", "video"},
    "writing": {"article_by", "blog_post", "book_chapter", "paper", "thesis"},
    "research": {"research", "report", "patent", "project", "wiki", "book", "other"},
}
TYPE_LABEL = {
    "talk": "talk", "workshop": "workshop", "panel": "panel", "slides": "slides", "village": "camp", "hearing": "hearing",
    "interview": "interview", "quoted": "quoted", "mentioned": "mention", "newspaper": "newspaper",
    "press_release": "press release", "tv": "TV", "radio": "radio", "podcast": "podcast", "video": "video",
    "article_by": "article", "blog_post": "blog", "book_chapter": "book chapter", "paper": "paper", "thesis": "thesis",
    "research": "code / ticket", "report": "report", "patent": "patent", "project": "project", "wiki": "wiki",
    "book": "book", "other": "other",
}


def esc(s):
    return html.escape(s or "", quote=True)


def ym(s):
    if not s:
        return "Present"
    y, m = s.split("-")[:2]
    return f"{MONTHS[int(m) - 1]} {y}"


def linkify(text):
    t = esc(text)
    return re.sub(r"(https?://[^\s<)]+[^\s<).,;])", r'<a href="\1" rel="noopener">\1</a>', t)


def cat_of(t):
    for k, v in CATS.items():
        if t in v:
            return k
    return "research"


def load(p):
    return json.load(io.open(p, encoding="utf-8"))


def media_items():
    media = load(ROOT / "data/media.json")
    copies = {}
    if (LIB / "copies.json").exists():
        for r in load(LIB / "copies.json"):
            copies[r["url"]] = r
    hosted = load(ROOT / "site/copies.json") if (ROOT / "site/copies.json").exists() else {}
    out = []
    for it in media:
        if not it.get("verified") or it.get("hermes_activity"):
            continue
        url = it.get("live_url") or it["url"]
        rec = copies.get(it["url"]) or {}
        copy = hosted.get(it["url"]) or ""
        wb = ""
        if rec.get("method") == "wayback" and rec.get("capture") and "web.archive.org" not in url:
            wb = f"https://web.archive.org/web/{rec['capture']}/{it['url']}"
        out.append({
            "d": it.get("date") or (str(it["year"]) if it.get("year") else ""),
            "y": it.get("year") or 0,
            "t": it.get("title") or "",
            "o": it.get("outlet") or "",
            "k": TYPE_LABEL.get(it["type"], it["type"]),
            "c": cat_of(it["type"]),
            "l": (it.get("language") or "").lower()[:2],
            "u": url,
            "a": copy,
            "w": wb,
        })
    out.sort(key=lambda x: (x["y"], x["d"]), reverse=True)
    return out


def build(lang="en"):
    li = load(ROOT / f"data/linkedin/{lang}.json")
    c = load(ROOT / f"site/content.{lang}.json")
    projects = load(ROOT / "data/projects.json")["projects"]
    items = media_items()
    counts = Counter(i["c"] for i in items)
    years = Counter(i["y"] for i in items if i["y"])
    first_year = 1995
    stats = [
        (date.today().year - first_year, c["stats_labels"]["years"]),
        (counts["talks"], c["stats_labels"]["talks"]),
        (counts["press"] + counts["av"], c["stats_labels"]["press"]),
        (counts["writing"], c["stats_labels"]["writing"]),
        (len(projects), c["stats_labels"]["projects"]),
    ]
    st = c["section_titles"]

    def head(key, num):
        t, sub = st[key]
        return f'<header class="sh"><span class="num">{num:02d}</span><h2>{esc(t)}</h2><p>{esc(sub)}</p></header>'

    intro = li["intro"]
    about = "".join(f"<p>{esc(p)}</p>" for p in li["about"])

    # experience (verbatim from LinkedIn)
    exp = []
    for e in li["experience"]:
        meta = " · ".join(x for x in [f'{ym(e["start"])} – {ym(e["end"])}', e.get("employment_type"), e.get("location"),
                                       e.get("location_type")] if x)
        desc = "".join(f"<p>{linkify(p)}</p>" for p in (e.get("description") or []) if p.strip())
        cur = "" if e["end"] else " current"
        exp.append(f'''<li class="job{cur}" data-li-id="{esc(e["id"])}">
  <div class="when">{esc(ym(e["start"]))}<span>{esc(ym(e["end"]))}</span></div>
  <div class="what"><h3><span class="li-title">{esc(e["title"])}</span></h3><div class="org li-org">{esc(e["org"])}</div>
  <div class="meta">{esc(meta)}</div>{f'<details><summary>Details</summary>{desc}</details>' if desc else ''}</div></li>''')

    # story
    story = []
    for ch in c["story"]:
        body = "".join(f"<p>{p}</p>" for p in ch["body"])
        story.append(f'<article class="chapter"><div class="yrs">{esc(ch["years"])}</div><div><h3>{esc(ch["title"])}</h3>{body}</div></article>')

    # projects grouped by area
    groups = {}
    for p in sorted(projects, key=lambda p: int(p["start_year"] or 0), reverse=True):
        area = c["areas"].get(p["area"], p["area"])
        desc, link = c["projects"].get(p["name"], ["", ""])
        name = c["project_titles"].get(p["name"], p["name"])
        never = "mai partito" in p["name"] or "never started" in desc
        src = [s for s in p.get("sources", []) if isinstance(s, str) and s.startswith("http")][:3]
        links = ([f'<a href="{esc(link)}" rel="noopener">{esc(re.sub(r"^https?://(www\\.)?", "", link).rstrip("/")[:40])}</a>'] if link else []) + \
                [f'<a href="{esc(s)}" rel="noopener">source {n + 1}</a>' for n, s in enumerate(src)]
        groups.setdefault(area, []).append(f'''<div class="proj{' never' if never else ''}">
  <div class="py">{esc(str(p["start_year"]))}{f' · <em>{esc(c["never_started_marker"])}</em>' if never else ''}</div>
  <h4>{esc(name)}</h4><p>{esc(desc)}</p><div class="plinks">{" ".join(links)}</div></div>''')
    order = sorted(groups, key=lambda a: -len(groups[a]))
    proj_html = "".join(f'<div class="pgroup"><h3>{esc(a)}</h3><div class="pgrid">{"".join(groups[a])}</div></div>' for a in order)

    comm = "".join(f'<div class="comm"><h4>{esc(n)}</h4><p>{esc(t)}</p></div>' for n, t in c["communities"])
    past = "".join(f'<li><a href="{esc(u)}">{esc(n)}</a></li>' for n, u in c["past_sites"])
    nav = "".join(f'<a href="#{k}">{esc(v)}</a>' for k, v in c["nav"])
    hero_links = "".join(f'<a href="{esc(u)}" rel="noopener">{esc(n)}</a>' for n, u in c["hero"]["links"])
    stats_html = "".join(f'<div class="stat"><b data-n="{n}">{n}</b><span>{esc(l)}</span></div>' for n, l in stats)
    ymin, ymax = min(years), max(years)
    peak = max(years.values())
    hist = "".join(f'<button class="bar" data-y="{y}" title="{y}: {years.get(y, 0)}" style="--h:{years.get(y, 0) / peak:.3f}"><i></i><span>{str(y)[2:]}</span></button>'
                   for y in range(ymin, ymax + 1))
    ui = c["archive_ui"]
    cat_btns = f'<button class="chip on" data-c="">{esc(ui["all"])} <small>{len(items)}</small></button>' + "".join(
        f'<button class="chip" data-c="{k}">{esc(v)} <small>{counts[k]}</small></button>' for k, v in ui["cats"].items())

    data_json = json.dumps(items, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    ui_json = json.dumps(ui, ensure_ascii=False)
    sync = c["footer"]["sync"].format(date=li.get("extracted", ""))

    page = TEMPLATE
    for k, v in {
        "LANG": lang, "TITLE": esc(c["meta"]["title"]), "DESC": esc(c["meta"]["description"]), "NAV": nav,
        "KICKER": esc(c["hero"]["kicker"]), "FIRST": esc(intro["first_name"]), "LAST": esc(intro["last_name"]),
        "AKA": esc(c["hero"]["aka"]), "HEADLINE": esc(intro["headline"]), "HERO_LINKS": hero_links, "STATS": stats_html,
        "H_ABOUT": head("about", 1), "ABOUT": about, "H_STORY": head("story", 2), "STORY": "".join(story),
        "H_WORK": head("work", 3), "EXP": "".join(exp), "H_PROJECTS": head("projects", 4), "PROJECTS": proj_html,
        "H_ARCHIVE": head("archive", 5), "SEARCH": esc(ui["search"]), "CATS": cat_btns, "HIST": hist,
        "H_COMM": head("communities", 6), "COMM": comm, "H_PAST": head("past", 7), "PAST": past,
        "H_CONTACT": head("contact", 8), "SYNC": esc(sync), "DRAFT": esc(c["footer"]["draft"]),
        "DATA": data_json, "UI": ui_json, "YEAR": str(date.today().year), "LOCATION": esc(intro.get("location", "")),
    }.items():
        page = page.replace("{{" + k + "}}", v)
    out = ROOT / ("index.html" if lang == "en" else f"{lang}/index.html")
    out.parent.mkdir(exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}: {len(page) // 1024} KB, {len(items)} archive items, {len(projects)} projects")


TEMPLATE = (Path(__file__).resolve().parent / "site_template.html").read_text(encoding="utf-8")

if __name__ == "__main__":
    lang = sys.argv[sys.argv.index("--lang") + 1] if "--lang" in sys.argv else "en"
    build(lang)
