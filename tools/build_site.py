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
    "writing": {"article_by", "blog_post", "book_chapter", "paper"},
    "research": {"research", "report", "patent", "project", "wiki", "book", "thesis", "other"},
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
            "g": it.get("tags") or [],
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

    pats = "".join(
        f'<div class="pat"><h4>{esc(x["title"])}</h4><div class="pref">{esc(x["refs"])}</div>'
        f'<div class="meta">{esc(x["dates"])}<br>{esc(x["who"])}</div><div class="plinks">'
        + " ".join(f'<a href="{esc(u)}" rel="noopener">{esc(n)}</a>' for n, u in x["links"])
        + (f' <a class="loc" href="{esc(x["local"])}">local copy (PDF)</a>' if x.get("local") else "") + "</div></div>"
        for x in c.get("patents", []))
    pat_html = f'<div class="pats" id="patents"><h3 class="subh">{esc(c.get("patents_title", "Patents"))}</h3>{pats}</div>' if pats else ""
    tagdefs = load(ROOT / "data/tags.json")
    tagged = [i for i in items if i["g"]]
    order = ["ijf", "dig", "newsroom-leaks", "transparency", "source-protection", "own-investigations"]
    strands = []
    for k in [k for k in order if k in tagdefs]:
        sel = [i for i in tagged if k in i["g"]]
        if not sel:
            continue
        ys = [i["y"] for i in sel if i["y"]]
        strands.append(f'<tr class="strand" data-tag="{esc(k)}" tabindex="0"><th>{esc(tagdefs[k]["label_en"])}</th>'
                       f'<td class="n">{len(sel)}</td><td class="yr2">{min(ys)}–{max(ys)}</td>'
                       f'<td class="wh">{esc(tagdefs[k].get("about_en") or "")}</td></tr>')
    truth = ("".join(f"<p>{x}</p>" for x in c.get("truth_intro", []))
             + ('<table class="strands"><thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead><tbody>%s</tbody></table>'
                % (esc(c["truth_table"]["strand"]), esc(c["truth_table"]["items"]), esc(c["truth_table"]["years"]),
                   esc(c["truth_table"]["what"]), "".join(strands)))
             + f'<p class="note">{esc(c.get("truth_strands_note", ""))}</p>') if strands else ""
    # focus / evidence / quotes / artifacts
    ident = c["identity"]
    focus = "".join(
        f'<article class="foc{" now" if x.get("now") else ""}"><div class="fk">{esc(x["k"])}'
        f'<span>{(esc(c.get("focus_badge", "focus now")) + " · ") if x.get("now") else ""}since {esc(x["since"])}</span></div>'
        f'<p>{esc(x["text"])}</p><div class="plinks">'
        + " ".join(f'<a href="{esc(u)}" rel="noopener">{esc(n)}</a>' for n, u in x["links"]) + "</div></article>"
        for x in c.get("focus_now", []))
    steps = c.get("evidence_steps", [])
    evidence = "".join(
        f'<article class="ev"><header><span class="evy">{esc(x["year"])}</span><h4>{esc(x["case"])}</h4></header><ol>'
        + "".join(f'<li><b>{esc(steps[n] if n < len(steps) else "")}</b><span>{esc(t)}</span></li>'
                  for n, t in enumerate(x["steps"]))
        + f'</ol><a class="evl" href="{esc(x["link"][1])}" rel="noopener">{esc(x["link"][0])} →</a></article>'
        for x in c.get("evidence", []))
    quotes = "".join(
        f'<figure class="q"><blockquote>“{esc(x["t"])}”</blockquote>'
        f'<figcaption>{esc(x["who"])} · {esc(x["when"])}</figcaption></figure>' for x in c.get("quotes", []))
    arts = []
    hosted = load(ROOT / "site/copies.json") if (ROOT / "site/copies.json").exists() else {}
    by_url = {i["url"]: i for i in load(ROOT / "data/media.json")}
    for u, path in hosted.items():
        cover = Path(path).parent / "slides" / "slide-001.jpg"
        if (ROOT / cover).exists() and u in by_url:
            it = by_url[u]
            arts.append((it.get("year") or 0, it.get("title") or "", str(cover).replace("\\", "/"),
                         str(Path(path).parent / "slides" / "slides.pdf").replace("\\", "/"), it["url"]))
    artifacts = "".join(
        f'<a class="art" href="{esc(src)}" rel="noopener"><img loading="lazy" src="{esc(img)}" alt="">' 
        f'<span class="ay">{y}</span><span class="at">{esc(t)}</span></a>'
        for y, t, img, pdf, src in sorted(arts))
    bui = c.get("books_ui", {})
    book_list = load(ROOT / "data/books.json") if (ROOT / "data/books.json").exists() else []
    books = "".join(
        f'<article class="book"><div class="by">{esc(str(b["year"]))}'
        f'<span class="how">{esc(bui.get("how", {}).get(b["how"], b["how"]))}</span></div>'
        f'<h4>{esc(b["title"])}</h4><div class="bmeta">{esc(b["authors"])} · {esc(b["publisher"])}'
        + (f' · {esc(b["pages"])}' if b.get("pages") else "") + f'</div><p>{esc(b["summary_en"])}</p><div class="plinks">'
        + " ".join(f'<a href="{esc(u)}" rel="noopener">{esc(bui.get("source", "source"))} {n + 1}</a>' for n, u in enumerate(b["urls"][:3]))
        + "</div></article>"
        for b in sorted(book_list, key=lambda b: (b["year"], b["title"])))
    books_html = (f'<div class="books">{books}</div><p class="note">{esc(bui.get("note", ""))}</p>') if books else ""
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
        "H_WORK": head("work", 4), "EXP": "".join(exp), "PATENTS": pat_html, "H_PROJECTS": head("projects", 5), "PROJECTS": proj_html,
        "H_ARCHIVE": head("archive", 7), "SEARCH": esc(ui["search"]), "CATS": cat_btns, "HIST": hist,
        "NICK": esc(ident["nick"]), "ZH": esc(ident["zh"]), "ZHNOTE": esc(ident["zh_note"]),
        "ROLES": "".join(f'<span{" class=\"first\"" if n == 0 else ""}>{esc(r)}</span>'
                         for n, r in enumerate(ident["roles"])),
        "ROLENOTE": esc(ident["role_note"]),
        "H_FOCUS": head("focus", 3), "FOCUS": focus, "QUOTES": quotes,
        "EVIDENCE": evidence, "EVTITLE": esc(c["evidence_title"][0]), "EVSUB": esc(c["evidence_title"][1]),
        "H_ARTIFACTS": head("artifacts", 10), "ARTIFACTS": artifacts,
        "H_BOOKS": head("books", 12) if "books" in st else "", "BOOKS": books_html,
        "H_TRUTH": head("truth", 6), "TRUTH": truth, "TAGS": json.dumps(
            {k: v["label_en"] for k, v in tagdefs.items() if not k.startswith("_")}, ensure_ascii=False),
        "H_COMM": head("communities", 8), "COMM": comm, "H_PAST": head("past", 9), "PAST": past,
        "H_CONTACT": head("contact", 11), "SYNC": esc(sync), "DRAFT": esc(c["footer"]["draft"]),
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
