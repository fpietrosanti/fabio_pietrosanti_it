# Stato del progetto e come riprenderlo da un altro computer

Ultimo aggiornamento: 2026-10-21.

## In una riga
Sito personale di Fabio "naif" Pietrosanti (石风翱), pubblicato su **https://fabio.pietrosanti.it** (GitHub Pages,
repo `fpietrosanti/fabio_pietrosanti_it`), in **inglese e cinese**, generato dai dati di questo repo.

## Ripartire da zero su una macchina nuova

```bash
git clone https://github.com/fpietrosanti/fabio_pietrosanti_it.git
cd fabio_pietrosanti_it
pip install pillow img2pdf segno          # opzionali: opencv-python-headless, yt-dlp
python tools/build_site.py --lang en && python tools/build_site.py --lang zh
python tools/check_langs.py && python tools/check_linkedin_coherence.py
```
Il clone basta per **ricostruire e ripubblicare il sito**: dati, testi, copie leggere, strumenti e documentazione
sono tutti versionati qui. Quello che il clone non porta con sé:

| Cosa | Dove sta | Come si riottiene |
|---|---|---|
| Video e audio (>10 MB, ~49 GB) | Google Drive, cartella condivisa **Archivio-homepage** | `rclone copy gdrive: <cartella>` dopo aver configurato il remote; i link sono in `data/drive_links.json` |
| Libreria privata completa (originali byte-esatti) | repo privato `fpietrosanti/fabio_pietrosanti_it-library` | clonarlo accanto a questo, cartella `../fabio_pietrosanti_it-copies` |
| Credenziali Drive (token OAuth) | `%APPDATA%\rclone\rclone.conf` sul computer | `rclone authorize drive` una volta, poi `rclone config create gdrive drive token '<token>' root_folder_id 1VDL0d2m7b3Vb2GtbwClFAbpfO9T_vtpM` |
| Sessione LinkedIn | browser di Fabio | serve solo per aggiornare il profilo (vedi repo `linkedin-i18n`) |

## Com'è fatto

- `data/media.json` — l'archivio (oltre 1.000 voci verificate), generato da `tools/merge_media.py` a partire da
  `data/research/raw/*.json` più le decisioni in `data/research/decisions.json`.
- `data/linkedin/en.json`, `zh-CN.json` — testi che vengono da LinkedIn (headline, About, esperienze). **L'inglese è il master.**
- `site/content.en.json`, `content.zh.json` — testi scritti a mano del sito. Stessa struttura nelle due lingue.
- `data/projects.json`, `data/books.json`, `data/tags.json`, `data/live_urls.json`, `data/drive_links.json` — registri.
- `copies/` — copie offline pubblicate (fino a 10 MB), generate da `tools/publish_copies.py`.
- `past/` — siti del passato ricostruiti dal Web Archive.
- `index.html`, `zh/index.html` — generati: **non modificarli a mano**, si rigenerano da `tools/site_template.html`.

## Regole che non vanno perse

1. **LinkedIn è il master** per headline, About ed esperienze: il sito li copia, non li riscrive.
   `tools/check_linkedin_coherence.py` lo verifica.
2. **Inglese master, cinese allineato**: `tools/check_langs.py` pretende stesse chiavi, stessi link, stessi conteggi.
3. **Limite di 1 GB** per un sito GitHub Pages: in `copies/` solo file fino a 10 MB, il resto su Drive.
4. Ogni voce dell'archivio deve avere la sua copia offline (libreria privata) e, quando è pubblicabile, il link
   alla copia locale o a Drive.
5. Niente dati personali (indirizzi, telefoni, documenti sanitari) nei repo pubblici.

## Lavori automatici
- `archivio-ricerca-google` (ogni 4 ore) e `archivio-ricerca-profonda` (notte): continuano la ricerca d'archivio.
- `archivio-upload-drive-2` (01:00): carica su Drive i file oltre 10 MB, aggiorna i link, ricostruisce e pubblica.
  È ripartibile: ogni esecuzione riprende da dove si era interrotta.

## Stato dell'upload su Drive
- Da caricare: **192 file, 49,1 GB**. Caricati finora: vedi `data/drive_links.json` (si aggiorna da solo).
- Spazio su Drive: 75 GB totali, ~65 GB liberi al 2026-10-21.

## Cose aperte
- Spostamento delle copie fino a 10 MB nel repo pubblico (da 254 MB a ~700 MB): lo fa il lavoro notturno.
- Ripristino del sito Hermes: quando sarà online, mappare gli URL definitivi come fatto per infosecurity.ch
  (`data/live_urls.json`) e indicizzare progetti, paper e talk.
- Fase finale: tag cloud degli interessi, timeline per aree, una foto per anno, aggiornamento di LinkedIn.
