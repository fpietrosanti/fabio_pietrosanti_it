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
- Da caricare in tutto: **200 file, 52,2 GB**. Su Drive al 2026-10-27: **51 file, 8,3 GB** (`data/drive_links.json`);
  mancano **150 file** (~44 GB).
- Notte 2026-10-27 (01:07–06:31): caricati 8 file, ~1,6 GB (più ~1,9 GB di trasferimenti parziali persi
  all'arresto). Velocità 145–260 KiB/s, nessuno stallo a 0 B/s e nessun errore di quota. Stop con TaskStop
  alle 06:31: questa volta si è chiuso anche rclone e lo script, quindi link registrati con `--links-only`.
  Copie leggere pubblicate: 1139 voci, 446 MB in `copies/`. Controlli lingue e LinkedIn OK.
- Notte 2026-10-26 (01:07–06:39): caricati 7 file, ~2,8 GB (più ~0,9 GB di trasferimenti parziali persi
  all'arresto). Velocità costante 140–270 KiB/s, **nessuno stallo a 0 B/s** e nessun errore di quota; rclone
  fermato a mano alle 06:39, poi `drive_sync.py` ha registrato da solo i link. Copie leggere pubblicate:
  1128 voci, 443 MB in `copies/`. Controlli lingue e LinkedIn OK.
- Notte 2026-10-25 (01:07–05:37, con il passaggio all'ora solare): caricati 9 file, ~0,50 GB. Primo giro
  250–310 KiB/s fino alle 03:00 circa, poi in calo fino a uno stallo a 0 B/s dalle 04:00 (rete ok, API Drive
  raggiungibile); rclone fermato alle 04:18 (persi ~2,5 GB di trasferimenti parziali di file grandi), rilancio
  subito ripartito a 200–300 KiB/s con 4 file in più; fermato a mano alle 05:37. Nessun errore di quota.
  Copie leggere pubblicate: 1120 voci, 442 MB in `copies/`.
- Notte 2026-10-24 (01:07–06:40): caricati 12 file, ~2,3 GB. Velocità 110–270 KiB/s, nessuno stallo a 0 B/s e
  nessun errore di quota; rclone fermato a mano alle 06:40 (persi i trasferimenti parziali in corso), poi
  `drive_sync.py` ha registrato da solo i link (exit 2). Copie leggere pubblicate: 1105 voci, 433 MB in `copies/`.
- Notte 2026-10-23 (01:07–05:40): caricati 6 file, ~0,76 GB (più ~1,3 GB di trasferimenti parziali persi
  all'arresto). Velocità 70–250 KiB/s; dalle 04:55 stallo a 0 B/s per ~45 minuti, quindi rclone fermato a
  mano alle 05:40 e link registrati con `--links-only`. Copie leggere pubblicate: 1071 voci, 427 MB in `copies/`.
- Notte 2026-10-22 (01:07–06:00): caricati 8 file, ~0,5 GB, con stalli simili.
- Spazio su Drive: 75 GB totali, **57,95 GiB liberi** al 2026-10-27.

### Problemi aperti dell'upload
- **Banda in upload bassissima** dal computer (60–250 KiB/s, stalli ricorrenti a 0 B/s verso le 05:00; la rete risponde, ping 19 ms): verificare la linea
  oppure spostare l'upload sul server (51.158.36.151) copiando lì la libreria e la configurazione di rclone.
- rclone usa il client_id condiviso di Google Drive, che verrà ritirato nel 2026: creare un client_id proprio
  (https://rclone.org/drive/#making-your-own-client-id) e riconfigurare il remote `gdrive:`.
- `drive_sync.py` lanciato in background è uscito con codice 1 senza output mentre rclone continuava
  (processo rimasto orfano): da indagare, per ora si chiude rclone a mano e si usa `--links-only`.
  Il 2026-10-24, con `drive_sync.py` lanciato in background da Bash (non scollegato), lo stop manuale di rclone
  ha funzionato in modo pulito: lo script ha proseguito da solo con lsjson e link.
- Lo stallo notturno a 0 B/s si risolve rilanciando `drive_sync.py` (verificato il 2026-10-25): conviene
  fermare e rilanciare dopo ~15 minuti di stallo invece di aspettare.
- La sessione notturna lascia ~1 GB di trasferimenti parziali a ogni stop manuale: con 4 transfer paralleli
  a ~150 KiB/s ogni file grande resta a metà. Valutare `--transfers 2` o l'upload dal server.

## Cose aperte
- Spostamento delle copie fino a 10 MB nel repo pubblico (da 254 MB a ~700 MB): lo fa il lavoro notturno.
- Ripristino del sito Hermes: quando sarà online, mappare gli URL definitivi come fatto per infosecurity.ch
  (`data/live_urls.json`) e indicizzare progetti, paper e talk.
- Fase finale: tag cloud degli interessi, timeline per aree, una foto per anno, aggiornamento di LinkedIn.
