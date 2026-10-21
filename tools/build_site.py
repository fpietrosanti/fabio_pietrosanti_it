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


def ym(s, ui=None):
    ui = ui or {}
    if not s:
        return ui.get("present", "Present")
    y, m = s.split("-")[:2]
    months = ui.get("months") or MONTHS
    return f"{months[int(m) - 1]} {y}"


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


def media_items(ui=None):
    media = load(ROOT / "data/media.json")
    copies = {}
    if (LIB / "copies.json").exists():
        for r in load(LIB / "copies.json"):
            copies[r["url"]] = r
    hosted = load(ROOT / "site/copies.json") if (ROOT / "site/copies.json").exists() else {}
    drive = load(ROOT / "data/drive_links.json") if (ROOT / "data/drive_links.json").exists() else {}
    wbmap = load(ROOT / "data/wayback.json") if (ROOT / "data/wayback.json").exists() else {}
    by_folder = {}
    for rel, info in drive.items():
        by_folder.setdefault(rel.rsplit("/", 1)[0], []).append(info)
    out = []
    for it in media:
        if not it.get("verified") or it.get("hermes_activity"):
            continue
        url = it.get("live_url") or it["url"]
        rec = copies.get(it["url"]) or {}
        copy = hosted.get(it["url"]) or ""
        folder = (rec.get("local") or "").replace("\\", "/")
        dr = sorted(by_folder.get(folder, []), key=lambda x: -int(x["size"]))
        drive_url = dr[0]["url"] if dr else ""
        wb = ""
        cap = rec.get("capture") if rec.get("method") == "wayback" else wbmap.get(it["url"])
        if cap and "web.archive.org" not in url:
            wb = f"https://web.archive.org/web/{cap}/{it['url']}"
        out.append({
            "d": it.get("date") or (str(it["year"]) if it.get("year") else ""),
            "y": it.get("year") or 0,
            "t": it.get("title") or "",
            "o": it.get("outlet") or "",
            "k": ((ui or {}).get("types") or {}).get(TYPE_LABEL.get(it["type"], it["type"]),
                                                      TYPE_LABEL.get(it["type"], it["type"])),
            "c": cat_of(it["type"]),
            "l": (it.get("language") or "").lower()[:2],
            "u": url,
            "g": it.get("tags") or [],
            "a": copy,
            "dv": drive_url,
            "w": wb,
        })
    out.sort(key=lambda x: (x["y"], x["d"]), reverse=True)
    return out


LANGS = [("en", "English", ""), ("zh", "中文", "zh/")]
LI_FILE = {"en": "en", "zh": "zh-CN"}


def linkedin_for(lang):
    """EN snapshot is the master; a translation file overlays headline/About/title/description by id."""
    base = load(ROOT / "data/linkedin/en.json")
    if lang == "en":
        return base
    tr = load(ROOT / f"data/linkedin/{LI_FILE[lang]}.json")
    out = json.loads(json.dumps(base))
    out["intro"]["headline"] = tr["intro"].get("headline") or out["intro"]["headline"]
    out["about"] = tr.get("about") or out["about"]
    by_id = {e["id"]: e for e in tr.get("experience", [])}
    for e in out["experience"]:
        t = by_id.get(e["id"])
        if t:
            e["title"] = t.get("title") or e["title"]
            if t.get("description"):
                e["description"] = t["description"]
    for key in ("patents", "volunteering"):
        if tr.get(key):
            out[key] = tr[key]
    return out


def build(lang="en"):
    li = linkedin_for(lang)
    c = load(ROOT / f"site/content.{lang}.json")
    projects = load(ROOT / "data/projects.json")["projects"]
    uiL = c.get("ui") or {}
    items = media_items(uiL)
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
        meta = " · ".join(x for x in [f'{ym(e["start"], uiL)} – {ym(e["end"], uiL)}', e.get("employment_type"), e.get("location"),
                                       e.get("location_type")] if x)
        desc = "".join(f"<p>{linkify(p)}</p>" for p in (e.get("description") or []) if p.strip())
        cur = "" if e["end"] else " current"
        exp.append(f'''<li class="job{cur}" data-li-id="{esc(e["id"])}">
  <div class="when">{esc(ym(e["start"], uiL))}<span>{esc(ym(e["end"], uiL))}</span></div>
  <div class="what"><h3><span class="li-title">{esc(e["title"])}</span></h3><div class="org li-org">{esc(e["org"])}</div>
  <div class="meta">{esc(meta)}</div>{f'<details><summary>{esc(uiL.get("details", "Details"))}</summary>{desc}</details>' if desc else ''}</div></li>''')

    # story
    story = []
    for ch in c["story"]:
        body = "".join(f"<p>{p}</p>" for p in ch["body"])
        story.append(f'<article class="chapter"><div class="yrs">{esc(ch["years"])}</div><div><h3>{esc(ch["title"])}</h3>{body}</div></article>')

    # identity, focus, artifacts, books, contact, donor
    ident = c["identity"]
    pre = "" if lang == "en" else "../"
    portrait = (f'<img class="portrait" src="{pre}assets/portrait.png" '
                f'srcset="{pre}assets/portrait.png 1x, {pre}assets/portrait@2x.png 2x" '
                'alt="Fabio Pietrosanti" width="152" height="152" fetchpriority="high">'
                ) if (ROOT / "assets/portrait.png").exists() else ""
    focus = "".join(
        f'<article class="foc{" now" if x.get("now") else ""}"><div class="fk">{esc(x["k"])}'
        f'<span>{(esc(c.get("focus_badge", "focus now")) + " · ") if x.get("now") else ""}since {esc(x["since"])}</span></div>'
        f'<p>{esc(x["text"])}</p><div class="plinks">'
        + " ".join(f'<a href="{esc(u)}" rel="noopener">{esc(n)}</a>' for n, u in x["links"]) + "</div></article>"
        for x in c.get("focus_now", []))
    arts = []
    hosted = load(ROOT / "site/copies.json") if (ROOT / "site/copies.json").exists() else {}
    by_url = {i["url"]: i for i in load(ROOT / "data/media.json")}
    for u, path in hosted.items():
        cover = Path(path).parent / "slides" / "slide-001.jpg"
        if (ROOT / cover).exists() and u in by_url:
            it = by_url[u]
            arts.append((it.get("year") or 0, it.get("title") or "", str(cover).replace("\\", "/"), u))
    artifacts = "".join(
        f'<a class="art" href="{esc(src)}" rel="noopener"><img loading="lazy" src="{esc(img)}" alt="">'
        f'<span class="ay">{y}</span><span class="at">{esc(t)}</span></a>' for y, t, img, src in sorted(arts))
    bui = c.get("books_ui", {})
    book_list = load(ROOT / "data/books.json") if (ROOT / "data/books.json").exists() else []
    btab = c.get("books_table", {})
    brows = "".join(
        f'<tr><td class="py">{esc(str(b["year"]))}</td><th>{esc(b["title"])}</th>'
        f'<td class="bh">{esc(bui.get("how", {}).get(b["how"], b["how"]))}</td>'
        f'<td class="ba">{esc(b["authors"])}<span>{esc(b["publisher"])}</span></td>'
        f'<td class="pd">{esc(b["summary_en"])}</td><td class="pl">'
        + " ".join(f'<a href="{esc(u)}" rel="noopener">{n + 1}</a>' for n, u in enumerate(b["urls"][:3])) + "</td></tr>"
        for b in sorted(book_list, key=lambda b: (b["year"], b["title"])))
    books_html = ('<table class="ptable btable"><thead><tr>'
                  + "".join(f"<th>{esc(btab.get(k, k))}</th>" for k in ("year", "title", "how", "authors", "what", "links"))
                  + f'</tr></thead><tbody>{brows}</tbody></table>'
                  + f'<p class="note">{esc(bui.get("note", ""))}</p>') if book_list else ""
    contact = "".join(f"<p>{linkify(x)}</p>" for x in c.get("contact_lines", []))
    wc = c.get("wechat") or {}
    wechat = (f'<div class="wechat"><img src="{pre}assets/wechat@1x.png" '
              f'srcset="{pre}assets/wechat@1x.png 1x, {pre}assets/wechat.png 2x" '
              'alt="WeChat QR code" width="132" height="132" loading="lazy">'
              f'<div><span class="wk">{esc(wc["label"])}</span><b>{esc(wc["handle"])}</b>'
              f'<p>{esc(wc["note"])}</p></div></div>') if wc and (ROOT / "assets/wechat.png").exists() else ""
    dn = c.get("donor") or {}
    donor = (f'<div class="donor"><span class="dk">{esc(dn.get("kicker", ""))}</span>'
             f'<h3>{esc(dn.get("title", ""))}</h3><p>{esc(dn.get("text", ""))}</p>'
             f'<a href="{esc(dn["link"][1])}" rel="noopener">{esc(dn["link"][0])} →</a></div>') if dn else ""

    appts = "".join(
        f'<div class="pat appt"><h4>{esc(a["role"])}</h4><div class="pref">{esc(a["org"])} · {esc(a["since"])}</div>'
        f'<div class="meta">{esc(a["note"])}</div>'
        f'<div class="plinks"><a href="{esc(a["url"])}" rel="noopener">source</a></div></div>'
        for a in c.get("appointments", []))
    appt_html = (f'<div class="pats"><h3 class="subh">{esc(c.get("appointments_title", ""))}</h3>{appts}</div>') if appts else ""

    # patents
    pats = "".join(
        f'<div class="pat"><h4>{esc(x["title"])}</h4><div class="pref">{esc(x["refs"])}</div>'
        f'<div class="meta">{esc(x["dates"])}<br>{esc(x["who"])}</div><div class="plinks">'
        + " ".join(f'<a href="{esc(u)}" rel="noopener">{esc(n)}</a>' for n, u in x["links"])
        + (f' <a class="loc" href="{esc(x["local"])}">local copy (PDF)</a>' if x.get("local") else "") + "</div></div>"
        for x in c.get("patents", []))
    pat_html = f'<div class="pats" id="patents"><h3 class="subh">{esc(c.get("patents_title", "Patents"))}</h3>{pats}</div>' if pats else ""

    # projects: compact table, all data
    ptab = c.get("projects_table", {})
    never_mark = f' <em>({esc(c["never_started_marker"])})</em>' 
    prows = []
    for p_ in sorted(projects, key=lambda p: int(p["start_year"] or 0)):
        area = c["areas"].get(p_["area"], p_["area"])
        desc, link = c["projects"].get(p_["name"], ["", ""])
        name = c["project_titles"].get(p_["name"], p_["name"])
        never = "mai partito" in p_["name"] or "never started" in desc
        src = [x for x in p_.get("sources", []) if isinstance(x, str) and x.startswith("http")][:3]
        links = ([f'<a href="{esc(link)}" rel="noopener">site</a>'] if link and link.startswith("http") else []) +                 [f'<a href="{esc(x)}" rel="noopener">{n + 1}</a>' for n, x in enumerate(src)]
        prows.append(f'<tr{" class=\"never\"" if never else ""}><td class="py">{esc(str(p_["start_year"]))}</td>'
                     f'<th>{esc(name)}{f" <em>({esc(c[chr(34)+chr(34)] if False else c["never_started_marker"])})</em>" if never else ""}</th>'
                     f'<td class="pa">{esc(area)}</td><td class="pd">{esc(desc)}</td>'
                     f'<td class="pl">{" ".join(links)}</td></tr>')
    proj_html = ('<table class="ptable"><thead><tr>'
                 + "".join(f"<th>{esc(ptab.get(k, k))}</th>" for k in ("year", "name", "area", "what", "links"))
                 + f'</tr></thead><tbody>{"".join(prows)}</tbody></table>')

    comm = "".join(f'<div class="comm"><h4>{esc(n)}</h4><p>{esc(t)}</p></div>' for n, t in c["communities"])
    past = "".join(f'<li><a href="{esc(u)}">{esc(n)}</a></li>' for n, u in c["past_sites"])
    nav = "".join(f'<a href="#{k}">{esc(v)}</a>' for k, v in c["nav"])
    base = "" if lang == "en" else "../"
    langsw = "".join(
        f'<a class="lang{" on" if code == lang else ""}" href="{esc(base + path) or "./"}" hreflang="{code}">{esc(label)}</a>'
        for code, label, path in LANGS)
    alts = "".join(f'<link rel="alternate" hreflang="{code}" href="https://fabio.pietrosanti.it/{path}">'
                   for code, _l, path in LANGS)
    hero_links = "".join(f'<a href="{esc(u)}" rel="noopener">{esc(n)}</a>' for n, u in c["hero"]["links"])
    stats_html = "".join(f'<div class="stat"><b data-n="{n}">{n}</b><span>{esc(l)}</span></div>' for n, l in stats)
    ymin, ymax = min(years), max(years)
    peak = max(years.values())
    hist = "".join(f'<button class="bar" data-y="{y}" title="{y}: {years.get(y, 0)}" style="--h:{years.get(y, 0) / peak:.3f}"><i></i><span>{str(y)[2:]}</span></button>'
                   for y in range(ymin, ymax + 1))
    ui = c["archive_ui"]
    order_t = ["ijf", "dig", "newsroom-leaks", "transparency", "source-protection", "own-investigations"]
    tagdefs = load(ROOT / "data/tags.json")
    tagchips = "".join(
        f'<button class="chip" data-tag="{esc(k)}">{esc(tagdefs[k].get("label_" + lang) or tagdefs[k]["label_en"])} '
        f'<small>{sum(1 for i in items if k in i["g"])}</small></button>'
        for k in order_t if k in tagdefs and any(k in i["g"] for i in items))
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
        "H_WORK": head("work", 4), "EXP": "".join(exp), "APPOINT": appt_html, "PATENTS": pat_html, "H_PROJECTS": head("projects", 5), "PROJECTS": proj_html,
        "H_ARCHIVE": head("archive", 6), "SEARCH": esc(ui["search"]), "CATS": cat_btns, "TAGCHIPS": tagchips, "HIST": hist,
        "NICK": esc(ident["nick"]), "ZH": esc(ident["zh"]), "ZHNOTE": esc(ident["zh_note"]),
        "ROLES": "".join(f'<span{" class=\"first\"" if n == 0 else ""}>{esc(r)}</span>'
                         for n, r in enumerate(ident["roles"])),
        "ROLENOTE": esc(ident["role_note"]),
        "H_FOCUS": head("focus", 3), "FOCUS": focus, "CONTACT": contact,
        "H_ARTIFACTS": head("artifacts", 8), "ARTIFACTS": artifacts,
        "H_BOOKS": head("books", 7) if "books" in st else "", "BOOKS": books_html,
        "TAGS": json.dumps({k: (v.get("label_" + lang) or v["label_en"]) for k, v in tagdefs.items()
                            if not k.startswith("_")}, ensure_ascii=False),
        "H_COMM": head("communities", 9), "COMM": comm, "H_PAST": head("past", 10), "PAST": past,
        "H_CONTACT": head("contact", 11), "DONOR": donor, "SYNC": esc(sync), "DRAFT": esc(c["footer"]["draft"]),
        "PORTRAIT": portrait, "WECHAT": wechat, "MORE": esc(uiL.get("more", "Show more")), "FOOTLINKS": hero_links, "LANGSW": langsw, "ALTS": alts, "BASE": base, "DATA": data_json, "UI": ui_json, "YEAR": str(date.today().year), "LOCATION": esc(intro.get("location", "")),
    }.items():
        page = page.replace("{{" + k + "}}", v)
    if lang != "en":
        page = page.replace('href="copies/', 'href="../copies/').replace('src="copies/', 'src="../copies/')
        page = page.replace('href="past/', 'href="../past/')
    out = ROOT / ("index.html" if lang == "en" else f"{lang}/index.html")
    out.parent.mkdir(exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}: {len(page) // 1024} KB, {len(items)} archive items, {len(projects)} projects")


TEMPLATE = (Path(__file__).resolve().parent / "site_template.html").read_text(encoding="utf-8")

if __name__ == "__main__":
    lang = sys.argv[sys.argv.index("--lang") + 1] if "--lang" in sys.argv else "en"
    build(lang)
