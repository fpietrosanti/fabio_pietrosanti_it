"""Verifica se la fonte originale di ogni video e' ancora raggiungibile.

Un video la cui fonte e' viva non va ripubblicato: si linka l'originale. Uno la cui
fonte e' morta esiste solo nel nostro archivio, ed e' li' che la ripubblicazione serve.

Scrive data/video_liveness.json. Rieseguibile.
"""
import io
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0 Safari/537.36")


def check(url):
    if not url:
        return url, "nessuna fonte"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=25) as r:
            body = r.read(200000).decode("utf-8", "replace")
            if "youtube.com" in url or "youtu.be" in url:
                low = body.lower()
                for dead in ("video unavailable", "video non disponibile",
                             "isn't available anymore", "account associated with this video has been terminated"):
                    if dead in low:
                        return url, "rimosso"
            return url, f"vivo ({r.status})"
    except Exception as e:
        return url, f"morto ({type(e).__name__}: {str(e)[:60]})"


def main():
    inv = json.load(io.open(ROOT / "data/video_inventory.json", encoding="utf-8"))
    urls = sorted({x["source_url"] for x in inv})
    with ThreadPoolExecutor(max_workers=8) as ex:
        res = dict(ex.map(check, urls))
    json.dump(res, io.open(ROOT / "data/video_liveness.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    c = {}
    for v in res.values():
        k = v.split(" ")[0]
        c[k] = c.get(k, 0) + 1
    print(f"{len(urls)} fonti · " + " · ".join(f"{a}: {b}" for a, b in sorted(c.items(), key=lambda t: -t[1])))


if __name__ == "__main__":
    main()
