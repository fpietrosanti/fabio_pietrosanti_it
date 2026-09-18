"""Build past/index.html: the landing page for Fabio's archived old websites.

Reads past/*/manifest.json written by tools/wayback_mirror.py. Site descriptions live in SITES
below; a mirror without an entry is still listed, with its title from the manifest.
"""
import html
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAST = ROOT / "past"

SITES = {
    "osxcrypt.org": {
        "order": 4,
        "title": "OSXCrypt — TrueCrypt for macOS",
        "host": "osxcrypt.org",
        "text": "Il sito del progetto OSXCrypt (2007–2008), il porting open source di TrueCrypt per Mac OS X con Orlando Bassotto e Matteo Flora: blog, download, finanziatori e forum. Dal 2016 il dominio è passato ad altri.",
    },
    "madoka": {
        "order": 1,
        "title": "Comitato Pro Ignoranza e Disinformazione",
        "host": "panservice.it/people/madoka",
        "text": "Il primo sito, goliardico, ospitato da Panservice: testi e racconti del «comitato».",
    },
    "naif": {
        "order": 2,
        "title": "Fabio Pietrosanti — naif",
        "host": "naif.itapac.net",
        "text": "Homepage personale degli anni in I.NET: post tecnici su Sikurezza.org, advisory "
                "(Cisco PIX, BIND, Mailstudio), codice, curriculum, il server di casa.",
    },
    "naif2005": {
        "order": 3,
        "title": "Fabio Pietrosanti — consulenza sicurezza",
        "host": "naif.itapac.net",
        "text": "La versione professionale e bilingue: competenze, servizi, media e referenze.",
    },
}


def main():
    cards = []
    for manifest in sorted(PAST.glob("*/manifest.json")):
        m = json.load(io.open(manifest, encoding="utf-8"))
        folder = manifest.parent.name
        meta = SITES.get(m["name"], {"order": 99, "title": m["title"], "host": m["scope"], "text": ""})
        start = next((p for p in m["pages"] if p["url"].rstrip("/") == m["start"].rstrip("/").lower() or p["url"] == m["start"]), None)
        start = start or next(p for p in m["pages"] if p.get("local"))
        saved = sum(1 for p in m["pages"] if p.get("local"))
        missing = len(m["pages"]) - saved
        caps = sorted(p["capture"] for p in m["pages"] if p.get("capture") and p.get("local"))
        span = f"{caps[0][:4]}–{caps[-1][:4]}" if caps and caps[0][:4] != caps[-1][:4] else (caps[0][:4] if caps else "")
        cards.append((meta["order"], f"""
    <article class="card">
      <p class="years">{span}</p>
      <h2><a href="{folder}/{start['local']}">{html.escape(meta['title'])}</a></h2>
      <p class="host">{html.escape(meta['host'])}</p>
      <p>{html.escape(meta['text'])}</p>
      <p class="meta">{saved} file recuperati dal Web Archive (catture {span}){f', {missing} non archiviati' if missing else ''}</p>
    </article>"""))
    body = "".join(c for _, c in sorted(cards))
    page = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Siti del passato — Fabio Pietrosanti</title>
<style>
  :root {{ --bg:#faf8f3; --fg:#1d1b17; --muted:#6b665c; --accent:#b0600f; --card:#fff; --line:#e5dfd3; }}
  @media (prefers-color-scheme: dark) {{ :root {{ --bg:#15130f; --fg:#ece6da; --muted:#a39c8f; --accent:#f0a24b; --card:#1f1c17; --line:#35302a; }} }}
  body {{ margin:0; background:var(--bg); color:var(--fg); font:17px/1.55 Georgia, 'Times New Roman', serif; }}
  main {{ max-width:760px; margin:0 auto; padding:48px 16px 64px; }}
  h1 {{ font-size:2rem; margin:0 0 .3rem; }}
  .lead {{ color:var(--muted); margin:0 0 2rem; }}
  .card {{ background:var(--card); border:1px solid var(--line); border-radius:6px; padding:20px 22px; margin:0 0 18px; }}
  .card h2 {{ margin:.1rem 0 .1rem; font-size:1.3rem; }}
  .card a {{ color:var(--accent); }}
  .years {{ margin:0; font:600 .8rem/1 system-ui, sans-serif; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); }}
  .host {{ margin:0 0 .6rem; font:.9rem ui-monospace, Consolas, monospace; color:var(--muted); }}
  .meta {{ margin:.6rem 0 0; font:.8rem system-ui, sans-serif; color:var(--muted); }}
  footer {{ color:var(--muted); font:.85rem system-ui, sans-serif; margin-top:2rem; }}
</style>
</head>
<body>
<main>
  <h1>Siti del passato</h1>
  <p class="lead">I miei siti web di un'altra epoca, ricostruiti dalle copie del
  <a href="https://web.archive.org/">Web Archive</a> e resi di nuovo navigabili così com'erano.</p>
  {body}
  <footer>Ogni pagina archiviata ha in cima una barra con la data della copia e il link all'originale sul Web Archive.
  Torna a <a href="https://fabio.pietrosanti.it/">fabio.pietrosanti.it</a>.</footer>
</main>
</body>
</html>
"""
    (PAST / "index.html").write_text(page, encoding="utf-8")
    print("wrote past/index.html with", len(cards), "sites")


if __name__ == "__main__":
    main()
