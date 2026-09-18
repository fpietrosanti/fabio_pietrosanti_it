"""Check that the homepage says exactly what LinkedIn (the master) says.

Compares data/linkedin/<lang>.json with the built page: headline, every About paragraph, and for every
experience entry its title, organisation and dates. Exit code 1 on any mismatch.

Refresh data/linkedin/*.json from the private linkedin-i18n repo (snapshots/) after each LinkedIn sync, then rebuild.
Usage: python tools/check_linkedin_coherence.py [--lang en]
"""
import html
import io
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_site import ym  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def norm(s):
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def main():
    lang = sys.argv[sys.argv.index("--lang") + 1] if "--lang" in sys.argv else "en"
    li = json.load(io.open(ROOT / f"data/linkedin/{lang}.json", encoding="utf-8"))
    page = (ROOT / ("index.html" if lang == "en" else f"{lang}/index.html")).read_text(encoding="utf-8")
    text = norm(re.sub(r"<[^>]+>", " ", page))
    problems = []
    if norm(li["intro"]["headline"]) not in text:
        problems.append("headline differs")
    for n, p in enumerate(li["about"]):
        if norm(p) not in text:
            problems.append(f"About paragraph {n + 1} differs: {p[:60]}…")
    for e in li["experience"]:
        m = re.search(r'data-li-id="%s">(.*?)</li>' % re.escape(e["id"]), page, re.S)
        if not m:
            problems.append(f"experience missing: {e['title']} — {e['org']}")
            continue
        block = norm(re.sub(r"<[^>]+>", " ", m.group(1)))
        for label, val in (("title", e["title"]), ("org", e["org"]), ("start", ym(e["start"])), ("end", ym(e["end"]))):
            if norm(val) not in block:
                problems.append(f"experience {e['org']}: {label} '{val}' not on page")
        for p in e.get("description") or []:
            if p.strip() and norm(p) not in block:
                problems.append(f"experience {e['org']}: description paragraph differs: {p[:50]}…")
    ids = set(re.findall(r'data-li-id="([^"]+)"', page))
    extra = ids - {e["id"] for e in li["experience"]}
    if extra:
        problems.append(f"page has experience entries not on LinkedIn: {sorted(extra)}")
    print(f"LinkedIn coherence ({lang}, snapshot {li.get('extracted')}): "
          + ("OK — headline, About and %d positions identical" % len(li["experience"]) if not problems else f"{len(problems)} problem(s)"))
    for p in problems:
        print("  -", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
