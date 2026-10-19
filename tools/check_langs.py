"""Check that the Italian and Chinese versions stay aligned with the English master.

English is the master for structure and facts:
  - site/content.<lang>.json must have exactly the same keys, list lengths and inline HTML as content.en.json;
  - every URL must be identical (translations never change links);
  - data/linkedin/<it|zh-CN>.json must cover every experience id of the EN LinkedIn snapshot;
  - the built pages must exist and carry the same number of archive items, projects, books and patents.

Exit code 1 on any mismatch. Usage: python tools/check_langs.py
"""
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ["it", "zh"]
LI_FILE = {"it": "it", "zh": "zh-CN"}
URL = re.compile(r'https?://[^\s"<>)]+')
TAG = re.compile(r"<[a-z/][^>]*>")


def walk(a, b, path, problems, lang):
    if type(a) is not type(b):
        problems.append(f"{lang}: {path}: type {type(b).__name__} instead of {type(a).__name__}")
        return
    if isinstance(a, dict):
        for k in a:
            if k not in b:
                problems.append(f"{lang}: {path}.{k}: missing")
            else:
                walk(a[k], b[k], f"{path}.{k}", problems, lang)
        for k in b:
            if k not in a:
                problems.append(f"{lang}: {path}.{k}: not in the English master")
    elif isinstance(a, list):
        if len(a) != len(b):
            problems.append(f"{lang}: {path}: {len(b)} items instead of {len(a)}")
            return
        for n, (x, y) in enumerate(zip(a, b)):
            walk(x, y, f"{path}[{n}]", problems, lang)
    elif isinstance(a, str):
        if URL.findall(a) != URL.findall(b):
            problems.append(f"{lang}: {path}: links differ ({URL.findall(a)} vs {URL.findall(b)})")
        if TAG.findall(a) != TAG.findall(b):
            problems.append(f"{lang}: {path}: inline HTML differs")
        if a and not b.strip():
            problems.append(f"{lang}: {path}: empty translation")


def count(page, pattern):
    return len(re.findall(pattern, page))


def main():
    en = json.load(io.open(ROOT / "site/content.en.json", encoding="utf-8"))
    en_li = json.load(io.open(ROOT / "data/linkedin/en.json", encoding="utf-8"))
    en_page = (ROOT / "index.html").read_text(encoding="utf-8")
    problems = []
    for lang in LANGS:
        cp = ROOT / f"site/content.{lang}.json"
        if not cp.exists():
            problems.append(f"{lang}: site/content.{lang}.json missing")
            continue
        walk(en, json.load(io.open(cp, encoding="utf-8")), "", problems, lang)
        lp = ROOT / f"data/linkedin/{LI_FILE[lang]}.json"
        if not lp.exists():
            problems.append(f"{lang}: data/linkedin/{LI_FILE[lang]}.json missing")
        else:
            tr = json.load(io.open(lp, encoding="utf-8"))
            have = {e["id"] for e in tr.get("experience", [])}
            missing = [e["org"] for e in en_li["experience"] if e["id"] not in have]
            if missing:
                problems.append(f"{lang}: LinkedIn translation missing {len(missing)} positions: {missing[:3]}…")
            if not tr.get("about"):
                problems.append(f"{lang}: LinkedIn translation has no About")
        pg = ROOT / lang / "index.html"
        if not pg.exists():
            problems.append(f"{lang}: {lang}/index.html not built")
            continue
        page = pg.read_text(encoding="utf-8")
        for what, pattern in (("archive items", r'"u":'), ("projects", r'<tr[^>]*><td class="py"'),
                              ("patents", r'class="pat"'), ("jobs", r'class="job')):
            a, b = count(en_page, pattern), count(page, pattern)
            if a != b:
                problems.append(f"{lang}: {what}: {b} instead of {a}")
    print(f"Language alignment: {'OK — it and zh match the English master' if not problems else f'{len(problems)} problem(s)'}")
    for p in problems:
        print("  -", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
