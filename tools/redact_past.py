"""Redact private contact data from the archived old websites in past/.

The archives are published in a public repository, so home addresses and phone numbers
found in old contact pages are replaced before committing. Run after tools/wayback_mirror.py.
Keep the rules generic enough to catch the same data if a page is re-crawled.
"""
import re
from pathlib import Path

PAST = Path(__file__).resolve().parent.parent / "past"
NOTE = b"[rimosso da questa copia d'archivio]"
RULES = [
    # street address line followed by postal code (Italian style)
    (re.compile(rb"Via\s+Aretusa[^<\r\n]*"), NOTE),
    # any Italian phone number written as +39 ...
    (re.compile(rb"\+39[\d\s./-]{6,}\d"), NOTE),
]


def main():
    changed = 0
    for f in PAST.rglob("*"):
        if f.suffix.lower() not in (".html", ".htm", ".txt") or not f.is_file():
            continue
        data = f.read_bytes()
        new = data
        for rx, repl in RULES:
            new = rx.sub(repl, new)
        if new != data:
            f.write_bytes(new)
            changed += 1
            print("redacted", f.relative_to(PAST))
    print("files changed:", changed)


if __name__ == "__main__":
    main()
