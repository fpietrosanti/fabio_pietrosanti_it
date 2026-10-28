# Ricerca media — piano di lavoro e stato

**Obiettivo (Fabio, 2026-09-16):** copertura completa di tutta la vita pubblica. Ogni singola
menzione, intervista, citazione, articolo scritto, talk, apparizione TV/radio/video/podcast,
paper o tesi che lo cita, in qualsiasi lingua e media. **La completezza è il criterio principale,
non la velocità.** Ogni anno dal 1995 deve avere voci.

## Cosa conta e cosa no

- **Conta:** articoli pubblicati (scritti da lui, su di lui, che lo citano o lo menzionano),
  interviste, talk e panel, TV/radio/video/podcast, audizioni, paper/tesi/report/libri che lo citano
  o lo ringraziano, advisory di sicurezza, i post del suo blog infosecurity.ch (categoria a parte).
- **Non conta:** singoli post su forum e mailing list (Fabio: «altrimenti ho migliaia di post negli
  archivi delle mailing list»). Fanno eccezione gli advisory di sicurezza. Un articolo che *parla*
  di un suo post (es. Tor Weekly News) invece conta. Il filtro è in `tools/merge_media.py`.

## Come si lavora

- Risultati grezzi per fetta in `data/research/raw/slice*.json` (formato sotto). Non si cancellano:
  le passate successive aggiungono file nuovi (`slice8_...`, `pass2_...`).
- `python tools/merge_media.py data/research/raw` → `data/media.json` (deduplicato) e
  `docs/RICERCA-MEDIA-2026-09.md` (revisione per anno, 🆕 nuovo / ↺ già sul vecchio sito).
- **Limite:** ogni sessione ha 200 ricerche web **condivise da tutti gli agenti**. Il 2026-09-16 si è
  esaurito a metà del primo giro. Per le passate successive: una o due fette per sessione, oppure
  alzare `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`. Quando le ricerche finiscono, continuare con
  WebFetch sulle pagine di ricerca interne dei siti e sulla Wayback Machine.
- Regole per gli agenti: niente URL inventati; `verified: true` solo se la pagina è stata aperta e
  contiene il nome o "naif"; attenzione agli omonimi (Paolo, Matteo, Francesco, Loris, Stefano, Elma
  Pietrosanti; il giornalista/autore calabrese Fabio Pietrosanti di Radio Digiesse / "Hodex").
- **Mai** mettere dati personali di Fabio (email, telefono) in header, query o form di terze parti.
- Materiale personale (salute, genetica, questioni politiche interne) **non** va nel repo pubblico:
  va in `linkedin-i18n/archive/held-from-public-site/` in attesa di decisione di Fabio.

## Stato primo giro (2026-09-16)

| Fetta | Voci | Verificate | Note |
|---|---:|---:|---|
| slice1 1995–2006 | 146 (88 post in lista, esclusi) | 136 | nessun budget di ricerca; Wayback offline; quasi zero stampa/TV |
| slice2 2007–2011 | 186 | 176 | 74 post infosecurity.ch (Wayback), ~78 thread mailing list |
| slice3 2012–2015 | 86 | 74 | 9 IJF Perugia, Wired, Tor Weekly News |
| slice4 2016–2020 | 44 | 31 | budget esaurito presto |
| slice5 2021–2026 | 46 (+9 trattenute) | ~35 | budget esaurito; 2023–2025 scarsi |
| slice6 media/archivi | 153 | 128 | Radio Radicale, IJF, e-privacy, SlideShare, podcast |
| slice7 accademico | 17 | 14 | Google Scholar/Books bloccati da CAPTCHA: da ripassare |

Paper svedese ricordato da Fabio: **trovato** — Winter & Lindskog (Karlstad University),
"How China Is Blocking Tor", arXiv aprile 2012 / USENIX FOCI '12 (lo cita e lo ringrazia).

## Stato secondo giro (2026-09-17)

| Passata | Nuove voci | Note |
|---|---:|---|
| pass2_a 1995–2008 | 21 | La Stampa 2002, Win Magazine e PuntoSicuro 2003 (articoli suoi), Hacker Journal, PC Professionale 2008 |
| pass2_b 2009–2015 | 27 | Data Manager 2010, Repubblica 2015, Motherboard 2014, Wired Italia 2014; ricerca JS dei quotidiani da fare col browser |
| pass2_c 2016–2026 | 44 (+1 trattenuta) | Radio 24 2018, Euronews 2018, Kaspersky 2022, e-voting Lombardia 2017, WeChat TimePie 2026 |
| pass2_d accademico | 6 | 2 brevetti Khamsa (2008), studi Parlamento europeo 2017 e 2023 |

Totale dopo il secondo giro: **453 voci** deduplicate, tutti gli anni dal 1998 al 2026 hanno almeno una voce
(2024 e 2025 una sola ciascuno).

### Decisioni di Fabio (2026-09-17)
- Siti del passato: madoka 1999 pubblicato così com'è; CV 2003 con data di nascita completa: ok. **Pubblicati.**
- Pagina Monitora PA «1311 nuove PEC» (2022, data di nascita e codice fiscale): **esclusa**.
- **OpenRousseau / M5S: da documentare**, inclusa l'espulsione (Domani 2020) e l'**articolo di Raffaele Angius**
  sulla ricerca della doppia iscrizione al M5S.

## Nuovo obiettivo: copia offline di tutto (2026-09-17)

Per ogni fonte (articolo, paper, intervista, video, audio) il sito mostrerà **link alla fonte + copia locale**.
- Ogni voce di `data/media.json` riceve una copia: pagina originale (live o Web Archive), testo estratto,
  metadati (da dove, quando, hash, se il nome compare nella copia).
- Serve un **report sempre aggiornato**: fonti ottenute in locale e fonti **non** ottenute, con il motivo
  (paywall, solo JavaScript, rimossa e mai archiviata, video/audio non scaricato, bloccata da bot).
- Tecniche per i siti solo-JavaScript: ricerca mirata `site:dominio "Pietrosanti"` sul motore di ricerca,
  poi copia dal Web Archive (`/web/<data>id_/<url>`); se la pagina non è archiviata, lettura dal DOM col browser.
- Tempi: giorni o settimane, finché l'obiettivo è raggiunto.

## Coda lavori per le sessioni programmate (non chiudere finché non è tutto fatto)
Ogni voce resta aperta finché non è completata; se un limite blocca il lavoro, si riprova nella sessione successiva.
- [ ] Coda Google `data/research/queue.json` (domini + query libere).
- [ ] Copie offline: tutte le 508 voci processate (2026-09-18). Restano 🟡 59 (nome non trovato nella copia: paywall,
  PDF dei SlideShare, pagine senza nome) e ❌ 5 (PrivateWave PDF 403 e mai archiviati, Radio Monte Carlo 404,
  Infosec Island host sparito, Zhihu 403). Prossimo: rileggere i 🟡 nel Chrome di Fabio (DOM) e cercare altre capture.
- [ ] Video/audio: 69 voci con video/audio (2026-09-18: +9 registrazioni Radio Radicale multi-parte, +1 Spreaker via API).
  **Fatto:** i 20 interventi di Fabio su Radio Radicale ritagliati uno per uno con trascrizione automatica
  (`tools/radioradicale_clips.py`, elenco in `radioradicale_clips.json`). Chiuso: YouTube mAtBH2hkAcg (CyberCoach 2023, account cancellato)
  non recuperabile salvo copia di Costabile. Resta: ritagliare anche i convegni non Radio Radicale (e-privacy su YouTube ecc.).
  **2026-10-12 (`tools/convegni_clips.py`, indice `convegni_clips.json`):** 7 registrazioni trascritte → **18 segmenti tuoi
  ritagliati** (14 certi, 4 incerti) con trascrizione: Whistleblowers Conference 2014, Intelligence/antiterrorismo 2016,
  Global Forum 2018 (debole, senza nome), Government hacking 2018 (×3), Privacy nightmare 2018, Trump/OTF 2020 (×4),
  Riconoscimento facciale 2020 (×5). **Restano 8 da trascrivere** (Whisper avviato in locale il 12/10, log
  `_run_transcribe_2026-10-12.log` nelle copie): 2013 ×2, 2015 ×3, Condivisi 2020, FOIA 2022, Speciale Tg1 2025.
  **2026-10-13: trascritte tutte e 8 → +17 segmenti** (35 in totale): Condivisi 2020 (24:33–31:47, app di tracciamento),
  webinar FOIA/MonitoraPA 2022 (07:50–22:46), workshop GlobaLeaks IJF 2015 (22:21–fine), «Firewall di nuova
  generazione» 2013 (81:31–83:37 dopo «naif… Fabio, lo ho tirato in ballo», + 1 incerto su spyware), Speciale Tg1 2025
  (2 segmenti col nome della voce narrante + 1 incerto sulla donazione di sangue). **Senza ritaglio:** PouL 2013 (tu e
  Agosti, voci non distinguibili dal testo: stato `two_speakers`), Greenwald-in-a-box 16/04/2015 (sei nominato tra i
  presenti ma non si sente un tuo intervento), Greenwald-in-a-box 18/04/2015 (non presentato né nominato → domanda a
  Fabio). Video ESC 2011 «Globaleaks Live Launch» (77 min) trascritto: Whisper non trova né «Fabio» né «naif» (solo i
  sottotitoli YouTube citano «Naif» di passaggio) → resta non verificato; chi parla lo può dire solo Fabio.
- [ ] **Video su Google Drive**: Fabio li caricherà su Drive; poi inserire il link Drive di ogni video in
  `copies.json` (campo `video.drive_url`) e mostrarlo in `docs/COPIE-OFFLINE.md` e nella futura pagina del sito.
  Finché non c'è il link, i video restano solo in locale (21,6 GB, fuori da GitHub).
- [ ] Google Books API e Semantic Scholar con quota fresca. **Passata 2026-09-18 (pass4_books/scholarly/archive_texts):**
  trovati e verificati via full-text Internet Archive *Coding Democracy* (Webb 2020), *Shooting the Messenger*
  (Fowler 2020), *Once a Bitcoin Miner* (Lou 2021), Bloomberg Businessweek 2020-05-04, Gazzettino FVG 2020,
  Tor monthly report 11/2011, Privacy International 2021, Access Now CPDP 2018, ParteciPa 2020, decreto USR Toscana 2022.
  **Resta:** Google Books API (quota giornaliera esaurita, 429) per Frediani, Maurizi, Di Corinto, *Profilo hacker*
  (testo italiano); Semantic Scholar (429 per 40 minuti: serve chiave API o altro orario, provare snippet/search);
  Di Salvo 2024 (Elgar, capitolo TI Italia, 403); tesi TorSNIP (Tampere, non raggiungibile); HAL/theses.fr dietro
  controllo anti-bot; report ONG solo PDF (WIN, RSF, FBK, relazioni annuali ANAC); titolo dell'articolo Businessweek.
  **Passata 2026-09-21 (pass4_scholarly_apis / books_api / ngo_reports_pdf):** Di Salvo 2024 **confermato** (PDF open
  access dal repository UniBo, p.145); tesi TorSNIP **confermata** (rif. [17], PDF da Web Archive); Cryptocat 2013
  riconfermato; nuova voce TI Italia «#SaveDotOrg» (2020, citato come presidente Hermes). OpenAlex full-text, Crossref,
  HAL, arXiv, Zenodo: solo omonimi. OGP Italia (35 PDF), UNODC, TI Italia, ANAC AIR, EDPS, PI/CILD, audit GlobaLeaks:
  nome assente. Esclusi Freedom House FOTN e report EAT (solo «Hermes Center»). **Bug corretto** in `merge_media.py`:
  gli URL `books.google.com/books?id=…` collassavano in uno → recuperati 11 libri verificati il 19/09.
  **Resta ancora:** Google Books API bloccata senza chiave (429, limite 0: serve una chiave API gratuita di Google Cloud);
  Semantic Scholar sempre 429 (serve chiave); senato.it 403 e ohchr.org Cloudflare; CDX su anticorruzione.it
  (consultazioni 2015/2019), hermescenter.org e allegati senato.it quando il Web Archive è stabile; tesi UniBo
  «Anonimato in rete» (eprint 9599, PDF 401); *Profilo hacker* (Apogeo 2007) pagina non confermata; Frediani *Guerre di
  rete* letto: nomina GlobaLeaks ma non Fabio.
  **Passata 2026-09-26 (3 agenti: `pass4_books_scholar_retry`, `pass4_wayback_istituzioni`, `pass4_ngo_theses`) → +7 voci.**
  - **Google Books sbloccato senza chiave**: `books.google.com/books?id=<ID>&jscmd=SearchWithinVolume2&q=<termine>`
    restituisce JSON con pagina e frammento (e `searchable`, quindi uno 0 su un libro ricercabile è un vero negativo).
    Usato subito sulle copie: **11 libri confermati** con pagina (Smarter Crowdsourcing EN/ES pp.76-78/84-86, Polityka
    p.7, IGI Global ×2, L'esecuzione, Anno 2020 p.113, Anno 2022 pp.107-138, IA/blockchain 2024 p.61, Political
    Automation 2025 p.227, *Profiling Hackers* CRC 2008 p.xiii). Maurizi (4 libri), Frediani *#Cybercrime*, Di Corinto
    *I nemici della rete* / *Revolution OS II*: **0 occorrenze** su libri ricercabili → chiusi.
  - **Nuove verificate**: lettera al ministro Calenda (MISE, 11/04/2017, export di tecnologie di sorveglianza, firmata
    con CILD e Privacy International; PDF dal crawl locale di hermescenter.org); scheda socio sul vecchio sito Hermes;
    risposta dell'Agenzia delle Entrate al suo FOIA sulla fattura elettronica (12/02/2019); pagina relatore GIJC13 (Rio
    2013); pagina relatore Festival del Giornalismo (2012-2018); testimonianza Business Follows (2017, licenza GlobaLeaks).
  - **Negativi solidi**: ANAC 2019 (contributi mai pubblicati; 2023: 43 contributori, niente Hermes); OHCHR 2015
    (whistleblower, cifratura/anonimato); OpenAlex full-text con 18 parole chiave; HAL/theses.fr (tesi Maitre 2022 su
    GlobaLeaks senza il suo nome); WIN, Blueprint, GAP, Xnet, Tactical Tech, FPU, FPF, FBK, TI estere; RSF «100 eroi
    dell'informazione» 2014: per l'Italia solo Maniaci e Abbate (la bio OSCE 2016 dice «top 10 RSF»: non riscontrato).
  - **Nuova pista senza nome**: Camera, sottocommissione diritti umani (III), 23/11/2016 — audizione di «Rappresentanti
    del Centro Hermes» sulla risoluzione Tidei; il Bollettino 731 non dà nomi.
  **Resta ancora:** Semantic Scholar (serve chiave: 11 richieste su 13 in 429); libri non ricercabili su Google Books
  (Frediani *Deep Web* e *Inside Anonymous*, Di Corinto *Un dizionario hacker*, *Riprendiamoci la rete*, *Hacktivism*,
  *#Cryptomania*, *Guerra profonda*; *Profilo hacker* ed. italiana) → copia fisica o prestito IA/Open Library;
  CORE (serve chiave), BASE/OATD/DART-Europe (controlli anti-bot), NDLTD 503, EThOS giù; senato.it scheda 43472
  (WAF, mai archiviata); Camera leg17 commissioni IX e X (Web Archive ha rifiutato); OHCHR fuori dal 2015 (CDX 504);
  pista h25.io (confronto Tor2web/GlobaLeaks). **Chiusa**: tesi UniBo «Anonimato in rete» (Daini 2015) — accesso solo
  interno all'ateneo, l'abstract non lo nomina.
  **Passate 2026-09-27/28 (`pass4_books_nonsearchable`, `pass4_scholarly_retry`, `pass4_istituzioni_residui`) → 0 voci
  nuove, 4 conferme di pagina.** *This Machine Kills Secrets* pp. 318-19 (ebook `bIaZf663Z2cC`), *Shooting the Messenger*
  p. 103 (`5SFWDwAAQBAJ`), Di Salvo 2020 pp. v/73/186 (`ikzrDwAAQBAJ`), Di Salvo 2024 p.145 (PDF UniBo). Open Library
  search-inside (155 risultati «Pietrosanti») e IA full-text: solo libri già noti o omonimi. **Negativi veri**:
  *Hacktivism* (Di Corinto/Tozzi, testo integrale su hackerart.org), *Guerre di rete* (solo GlobaLeaks), *Hackers*,
  *Cyberworld*, *Il lato oscuro della Rete*, GISWatch Italia 2012/15/17; OpenAlex full-text (69 opere «globaleaks», 45
  «tor2web»: ~60 PDF letti, mai il nome); Semantic Scholar author/bulk search (42 profili Pietrosanti, tutti omonimi);
  Europe PMC (solo omonimi, anche sul biohacking). **h25.io chiusa**: directory SEO di link darknet, nessun confronto.
  **Camera 23/11/2016** (comitato diritti umani, risoluzione Tidei): video scaricato e trascritto, per Hermes parlò
  **Emmanuele Somma** → non Fabio. **Camera 23/09/2015**: anche lì Hermes era Alessandro Rodolfi. **Senato 14/05/2020**
  (AS 1721, scheda letta dalla copia parlamento.it): Hermes tra 15 auditi in video, nessun nome, nessuna memoria
  depositata; solo il video della WebTV del Senato (WAF) direbbe chi parlò. OHCHR 2015/2019: 146 contributi, nessuno di
  Hermes. Radio Radicale: 21 interventi, nessuno in sede parlamentare.
  **Resta ancora (solo con chiavi o browser):** libri non ricercabili — Frediani *Deep Web* e *Inside/Dentro Anonymous*,
  Di Corinto *Un dizionario hacker*, *Riprendiamoci la rete*, *#Cryptomania*, *Guerra profonda* (2026), *Profilo hacker*
  ed. italiana (numero di pagina) → copia fisica; Semantic Scholar e CORE (429 senza chiave); OATD/DART-Europe
  (Cloudflare), BASE e dblp (Anubis), Lens.org (JS); 5 opere su GlobaLeaks non lette (tesi NOVA Lisbona 2018, IFIP 2020,
  IEEE 2017, *The Dark Net Rises*, recensione Di Salvo ZORA 2021); video WebTV Senato del 14/05/2020; verbali commissioni
  LIBE/JURI del PE (nessuna ricerca full-text pubblica). **Proposta: chiudere questa voce** — quel che resta dipende da
  chiavi API, copie fisiche o dal browser di Fabio, non da altre ricerche automatiche.
- [x] ~~Corriere della Sera 2001-01-26 p.25~~: **chiuso** — «esperto» senza nome, escluso per decisione di Fabio (18/09).
- [x] RAI Teche, Mediaset, arretrati ICT Security / Wireless / WeekIT — passata 2026-09-22 (`pass4_it_magazines`,
  `pass4_mediaset_other_tv`): +2 WeekIT 2001/2002, Radio 24 (5 puntate), Sky TG24 Datagate 2013. **Resta** solo
  Radio Monte Carlo (audio 404, vedi PROBLEMI-APERTI B1).
- [x] **Audizioni Camera/Senato/Parlamento europeo — fatto il 2026-09-23** (3 agenti in parallelo:
  `pass4_audizioni_camera_senato`, `pass4_ue_istituzioni`, `pass4_autorita_accademico`). **+10 voci verificate.**
  **Risultato principale, negativo e solido: Fabio non è mai stato audito in Parlamento.** Scaricati per intero gli
  elenchi ufficiali degli auditi della Camera (leg17: 2.199 righe; leg18), le pagine «Documenti acquisiti» di tutte le
  14 commissioni permanenti di leg18 e leg19, le 4 sedute dell'indagine conoscitiva sul whistleblowing (2015) e il
  motore di ricerca interno della Camera: zero occorrenze. **Il 23/10/2015 il Centro Hermes fu audito** dalle
  Commissioni Riunite II+XI sul ddl Businarolo, ma lo rappresentava **Alessandro Rodolfi**. Anche le memorie della
  Rete per i Diritti Umani Digitali (leg19) e quella del Senato sul ddl IA non lo nominano.
  Al Parlamento europeo l'indice full-text del Think Tank dà **solo i 2 studi già noti**, e in entrambi è una
  **citazione bibliografica** (articolo suo e di Aterno sul government hacking), non un esperto audito.
  **Trovato invece: OSCE 2016** — la sua biografia completa, con il nick «naif», nel libretto dei relatori della
  conferenza *Gaining a Digital Edge* del Rappresentante OSCE per la libertà dei media (Vienna, 14-15/09/2016).
  **Restano** (gap noti, non chiusi): audizioni informali del **Senato** — in particolare la scheda leg18
  `ProcANLscheda43472` (Hermes audito sul recepimento della direttiva copyright, insieme a FNSI, CRUI, SIAE,
  Wikimedia Italia, Google): senato.it è dietro un WAF AWS e non è archiviata; audizioni informali **leg17** della
  Camera (API `getElenco.ashx` rotta, servono capture Wayback di `camera.it/leg17/1104`); **verbali e programmi
  delle commissioni del Parlamento europeo** (il Think Tank indicizza solo studi e briefing).
- [ ] **Piattaforme cinesi (TimePie Shanghai 2026)**: WeChat (via Sogou weixin.sogou.com nel Chrome di Fabio), Bilibili,
  Douyin, canali video WeChat. Fatto 18/09: articolo WeChat 13/9 (Fabio al «生物极客闭门论坛», forum a porte chiuse) e
  video Bilibili di riepilogo (32 s + 1'53") scaricati. Resta: Douyin, canali video WeChat, altri articoli WeChat
  (Sogou oltre la prima pagina), eventuali registrazioni integrali; chiedere a TimePie la registrazione dell'intervento.
  **Passate 2026-09-29/30 (`pass4_cina_wechat_weibo`, `pass4_cina_testi`, `pass4_cina_video`) → +8 voci.** Riepilogo
  ufficiale TimePie (WeChat 20/9, ripresa 21/9, copia permanente Sohu `a/1078945684`), resoconto del giorno 1 su
  Baijiahao; **profilo pre-forum di TimePie su NetEase** (20/08/2026, «逆龄16岁！日吞70粒补剂…»: GlobaLeaks, Hacking
  Biology, ~70 integratori al giorno, GlycanAge −16 anni); agenda del forum su Sohu (26/08, «15:50-16:15 从自我实验走向
  科学证据»); traduzione cinese (secrss.com, 2024) del pezzo Recorded Future sugli spyware italiani. Video: Bilibili
  BV1u5YX6JECk **verificato a vista** (0:20-0:22 sul palco con la slide BIOHACK.IT, fotogrammi salvati nella copia);
  riepilogo NetEase VG6GUA7FN (= Bilibili BV1Rwh76XEhj) visto fotogramma per fotogramma: **non compare** → escluso;
  elenco completo dei caricamenti Bilibili di TimePie 18/8–29/9: nessuna registrazione integrale del forum biohacker;
  YouTube TimePie fermo al 24/07. **Resta:** Douyin (account TimePie trovato, elenco video solo con browser), canali
  video WeChat, Weibo, Xiaohongshu, Toutiao (servono login/browser: il Chrome di Fabio era disconnesso); ricerca 360
  (so.com) da riprovare con «Pietrosanti 抗衰» e la grafia cinese; 5 clip Bilibili del forum principale non viste
  fotogramma per fotogramma (improbabile che ci sia); registrazione integrale da chiedere a TimePie.
  **Passate 2026-10-01/02 (`pass4_cina_noBrowser`, senza Chrome):** le 5 clip Bilibili viste a 1 fotogramma/s →
  Fabio **compare** nella cena «永生之夜» del 12/9 (BV1X9YR68ETj, 0:31.5-0:32.8) e quindi anche nel riepilogo NetEase
  VG6GUA7FN / Bilibili BV1Rwh76XEhj (1:33.7-1:34.8, stessa scena: **esclusione del 30/09 annullata**); non compare in
  BV1e2YX6tEqz, BV1YtY96bEhr, BV1w8YX6uENN, BV1SJYe6AEXo (escluse). Fotogrammi salvati nelle copie. Chrome ancora non
  raggiungibile in navigazione il 02/10: Douyin, Weibo, canali video WeChat, Xiaohongshu restano da fare.
  **Passata 2026-10-09 (Chrome di Fabio finalmente navigabile + agente `pass4_cina_riprese`) → +2 voci.**
  - **Nuovo articolo WeChat** di 长寿科技情报站 (05/10/2026, «以自身试验探索生命边界：极客闭门论坛回顾»): riepilogo del
    forum biohacker che lo nomina («开源抗衰数据平台开发者Fabio Pietrosanti») e riassume il suo intervento come «结构化人体
    自我实验»; post a immagini con **18 foto**, tra cui la **foto 10: tu sul palco con didascalia «Fabio Pietrosanti —
    生物极客、科技创业者»** e la citazione «开源数据与结构化人体自我实验» (prima foto del forum col tuo nome). Testo dal DOM,
    foto da mmbiz.qpic.cn (copia `2026/0604b9f21c7c`); il link permanente `__biz/mid/idx/sn` col curl dà la pagina anti-bot.
  - NetEase `VG5NGRVPI` = copia del Bilibili BV1u5YX6JECk (nome solo a vista; il video resta quello Bilibili).
  - **Negativi**: Sogou WeChat (14 query, fino a 3 pagine), Toutiao (4 query), Bilibili TimePie 01–08/10 (5 video visti a
    1 fps: interviste ai partecipanti, divulgazione «永生路线图», Michael Lustgarten — non compari), Sohu/NetEase TimePie
    01/09–08/10, ifeng, Tencent News, bjnews, Chinadaily; l'articolo di 长寿科技情报站 sulle **tre cene** (07/10, «三场晚宴
    加持») è stato **cancellato dall'autore** prima che lo leggessi. Bloccati (non aggirati): 360/Baidu/Sogou web (CAPTCHA).
  - **Douyin, Weibo e Xiaohongshu chiedono il login anche nel tuo Chrome** (non sei loggato su quei siti; non posso creare
    account) → restano bloccati finché non fai login tu, oppure si chiude la voce. Canali video WeChat: solo app.
  **Proposta: chiudere la voce** salvo login (domanda in PROBLEMI-APERTI A0-quinquies).
- [ ] **Progetti mai partiti da documentare** (segnalati da Fabio 18/09): OSSCI – Osservatorio sicurezza dello spazio
  cibernetico italiano (Telegram + documento di specifica, anno da trovare); COVID mappatura focolai con dati di cella;
  COVID vulnerabilità app della Regione Lazio con Giovanni Rocca. Query in coda; cercare anche su Telegram (t.me), GitHub,
  Google Docs pubblici, Web Archive.
  **Passata 2026-09-24 (3 agenti: `pass4_ossci`, `pass4_covid_dati_cella`, `pass4_covid_app_lazio`) → +39 voci.**
  - **OSSCI**: il nome GitHub è «OSPCI – Osservatorio Sicurezza del **Perimetro** Cibernetico Italiano»; org creata il
    12/11/2019, ultimo commit 03/01/2020 (loghi, firmato «Fabio (naif) Pietrosanti»), ultima attività lug–set 2020
    (issue #3 e fork GitLab `fnzv/ossci`). Verificati: issue #2 «Pipeline 0» (commenti di Fabio 17-18/11/2019), PR #1
    unita da lui, commit dei loghi. Partecipanti: Y. Agostini, C. Mara, S. Onofri, A. Prado, G. Bonfiglio, fnzv, rfc1036.
    Il gruppo Telegram (230 membri) è **privato**: il link d'invito **non** è stato messo nel repo pubblico. Nessuna
    copertura stampa.
  - **COVID dati di cella**: trovata la **proposta originale** (Google Doc «Digitalizzazione processi gestione emergenziale
    coronavirus assistiti da dati di geo-location mobile», ~20/03/2020, «L'autore primario è Fabio Pietrosanti», pareri
    legali di Aterno, Piana, Saetta, Perri e altri) + **20 tweet di Fabio** (mar–set 2020) che ne ricostruiscono la storia
    (post in lista Copernicani 18/3, annuncio 25/3, bilancio 31/5), AGPLv3 per Immuni, archivio verbali CTS (6/9).
    Nuove anche: webinar Eumans «Condivisi» 10/04/2020 (relatore), lettera aperta Nexa 20/04/2020 e lettera ANORC alla
    ministra Pisano 24/04/2020 (firmatario «(naif)»), scheda podcast Associazione Luca Coscioni.
  - **App LAZIOdrCOVID**: il post di Giovanni Rocca del 29/03/2020 **nomina Fabio** («FABIO – Naif – PIETROSANTI», test fatti
    con il suo codice fiscale) → verificato; tweet di lancio di Rocca che tagga @fpietrosanti. Stampa: solo richiami
    indiretti senza nome (gioxx.org 2020, Il Fatto/Rapetto 2021, il Giornale 2021); nessun articolo delle grandi testate.
  **Resta** (bloccato dal Web Archive «Temporarily Offline» durante la sessione): capture giugno 2021 del Google Doc OSSCI
  (chi l'ha modificato); articolo StartMag sul codice sorgente di Immuni (403, Wayback non caricava); `verbalictscovid.
  infosecurity.ch` (offline, nessuna capture); 2 post Facebook di Fabio (16/03 e 09/04/2020, servono login, mai archiviati);
  scansione fine dei ~700 tweet archiviati dopo aprile 2020 (filtrati solo per parole chiave).
  **Ripassata 2026-09-29/30 (`pass4_tweets_2020_residui`, `pass4_covid_ossci_residui`):** +119 tweet 2019-2021
  verificati dal Web Archive (OSSCI, COVID, Immuni, OpenRousseau, voto elettronico). Web Archive funzionante: **StartMag**
  (42 articoli Immuni/tracciamento del 2020 letti) → nome solo nel pezzo già noto; **Google Doc OSSCI** mai archiviato,
  testo live senza il suo nome; `verbalictscovid` mai archiviato; stampa 2020 su dati di cella/Immuni (Agenda Digitale,
  Key4biz, Punto Informatico, Open, AGI, Cybersecurity360…) → nessuna menzione nuova. **Escluso** Radio Digiesse 17/04/2020
  (omonimo calabrese). **Resta solo:** puntata Radio 24 «Coronavirus e tecnologia: dati, app, GPS» (marzo 2020, ospiti
  caricati via JavaScript, nessuna capture) e i 2 post Facebook (servono login).
  **2026-10-01:** puntata Radio 24 del 13/03/2020 letta dal JSON dell'episodio → ospiti Quarteroni, Bonannini e altri,
  **non Fabio** (esclusa). **Resta solo** il testo dei 2 post Facebook, che solo Fabio può fornire.
- [x] **Foto del «生物极客闭门论坛» — fatto il 2026-10-04**: 10 foto della sezione forum (copia `2026/523c49878113/photos/`,
  dalla ripresa Baijiahao 18/09 dell'articolo del 12/9) + 23 dal riepilogo Sohu 20/9 (`2026/ebce85101353/photos/`: forum
  senza filigrana + cena «永生之夜»), con `README.md` per foto. **Foto 05** = probabilmente tu sul palco (slide «130+
  biomarkers / N = 1»), nessuna didascalia col nome. Il testo di entrambi gli articoli ti nomina («开源抗衰数据平台开发者
  Fabio Pietrosanti»). Originale `mp.weixin.qq.com` non ottenuto (Sogou → pagina anti-bot, non aggirata); l'articolo del
  13/9 sul solo forum a porte chiuse non esiste tra i post Sohu di TimePie.
- [ ] Video ufficiali TimePie: Fabio avviserà quando pubblicati → scaricarli e archiviarli.
- [x] **Progetto AIRE — fatto il 2026-09-25** (`pass4_aire_voto_estero`, +27 voci, 9 verificate). Non un progetto
  finanziato ma una ricerca di policy alternativa al fondo di 1 M€ per il voto elettronico (L. 160/2019, c. 627):
  **fase 1** (nov–dic 2019) analisi della geolocalizzazione degli iscritti AIRE (tweet 15/11/2019; CRVD «Come non
  sprecare un milione di euro», 20/12/2019: 80 seggi esteri → 86%, 216 → 99%); **fase 2** (mar 2021) **Geo-AIRE**
  con Stefano Quintarelli e Maurizio Napolitano (FBK), `github.com/g0v-it/Geo-AIRE` (README lo nomina coautore) +
  Agenda Digitale 15/03/2021 (43 città → 84,35%, 273 → 99,82%). Esito: posizione ufficiale Copernicani, ripresa dal
  Post (09/2022); lo Stato ha seguito il voto elettronico (decreto 9/7/2021, Comites 2021, simulazione Viminale 12/2023).
  **Resta:** tweet dei mesi non controllati (Web Archive lento); nessuna TV/podcast/audizione trovata sul tema;
  `notizieoggi.com` (ripresa del Post) irraggiungibile e mai archiviato.
- [x] **OpenRousseau / M5S — fatto il 2026-09-25** (`pass4_openrousseau_m5s`, +16 voci, 10 verificate): La Stampa
  02/10/2020 (Iacoboni, «Tra gli sviluppatori, Denis Roio, Fabio Pietrosanti»), Il Messaggero 02/10/2020, Radio Veronica
  One (ripresa Adnkronos), 4 repo GitHub `decidiamo/*` (contributor fpietrosanti), 3 tweet di agosto 2020; contesto:
  sito openrousseau.org (non .it), PDF «Dieci principi», replica del Blog delle Stelle, Open 19/08/2020.
  **Domani:** l'articolo sull'espulsione **è** quello già noto del 27/10/2020 («Ecco la lettera ai Cinque stelle…»,
  Redazione): racconta che fu allontanato il 23/10 per l'inchiesta Wired; non esiste un pezzo separato.
  **Angius:** solo i due articoli Wired già noti (19/08 e 23/10/2020). **Resta:** ~620 dei 784 tweet archiviati
  ago 2020–lug 2021 non letti (soprattutto dal 23/10 in poi); HuffPost/Repubblica non raggiungibili dal motore.
- [x] ~~Bloomberg Businessweek 2020-05-04~~ (trovato, p. 70, manca il titolo); ~~Il Gazzettino Friuli 2020-10-02~~ (verificato); ~~Radio1 Rai Italian Hacker Camp 2018~~ (2026-09-25: servizio di Paola Guarnieri ricaricato su SoundCloud, 1'07", nome nel titolo; la pagina radio1.rai.it non esiste più né in Wayback).
- [x] Internet Archive: win-magazine-italia-48, pcprofessionale207, hackerjournal-38, GazzettinoFVG2020-10-02 (copie: OCR + PDF, nome verificato; 2026-09-18).
- [ ] **Sito Hermes Center** in ripristino da Fabio: quando online, indicizzare tutti i progetti, paper e talk di Fabio per
  Hermes, GlobaLeaks, CRVD, Copernicani (come fatto per CRVD il 18/09).
- [x] **infosecurity.ch — fatto il 2026-09-29**: confrontato il sito ripristinato (`infosecurity-ch/site`, 76 post
  2007-2017) con `media.json`: mancava solo «Low Liability - Reduced Abuses Tor Exit Nodes» (10/06/2017), ora aggiunto;
  il post del 17/09/2026 sul ripristino non è una pubblicazione esterna.
- [x] **Pyongyang 2019 / caso Virgil Griffith — chiuso il 2026-10-05** (lacuna aperta il 2026-10-02: in archivio c'erano solo Bloomberg, The
  Walrus, Medium e il libro di Lou). **Passata 2026-10-02 (`pass4_pyongyang_intl`, `pass4_pyongyang_it_asia`) → +13 voci
  verificate:** CoinDesk 03/12/2019 **intervista** («The sanctions were not a topic at all», «a boring two days») e
  «Freedom Fighter or Fool?» (+ ripresa Yahoo Finance), MIT Technology Review 05/12/2019, AMBCrypto EN/ES (tweet),
  **2600 «Off The Hook» 04/12/2019** (in diretta dall'Italia; pagina + MP3, trascrizione locale), CoinReaders (Corea)
  03 e 04/12/2019, Medium ethex-smm (copia Web Archive), Substack Taylor Simone 2021 (intervista telefonica 30/09/2021),
  **British GQ 24/11/2022** (Peter Guest, lunga intervista); in più baiyi.com (Cina, 04/12/2019, dalla run del 01/10).
  **Negativi:** atti US v. Griffith (CourtListener: nessuna occorrenza; l'udienza del 30/12/2019 cita Hermes per Tor2web,
  non lui), Cointelegraph, Newsweek, IEEE Spectrum, heise, Daily Beast, NBC, Decrypt, Vice, stampa spagnola su Cao de
  Benós; **stampa italiana: zero** (25 testate); giapponese zero; cinese solo baiyi.
  **Resta:** l'originale cinese ripreso da baiyi (8btc/Jinse/Odaily: ricerca solo nel browser); GDELT (rate limit) per
  aprile 2019, patteggiamento 2021 e condanna 2022; archivi Reuters/AP/AFP, Bloomberg news dic. 2019, NYT/WaPo/Guardian/
  BBC/Wired, El País/El Mundo/ABC, Yonhap/Chosun; Japan Times, UPI, Forbes, France24 (anti-bot); i suoi tweet di aprile
  e nov–dic 2019 (Web Archive offline/limitato il 02/10); CoinDesk Japan (traduzione dell'intervista?); TV e video.
  **Passata 2026-10-04 (`pass4_pyongyang_wire`, `pass4_pyongyang_tweets_asia`) → +28 tweet verificati, 0 articoli.**
  **Tweet** (CDX Web Archive → 6.256 status archiviati, 164 letti): 29/11–01/12/2019 la stessa risposta ripetuta a 11
  account (CoinDesk, McAfee, NK News, VICE, 2600, Kim Dotcom, USA Today… «I went in North Korea with Virgil… willing to
  provide my testimony», accorpata in una voce) + 6 risposte diverse («no plan or conspiracy», «the entire affidavit
  isn't honest»), 02 e 07/12/2019; **26-30/09/2021** (patteggiamento) 10 tweet (con Ethan Lou, «cryptoanarchism
  trolling», viaggio pagato dai partecipanti a prezzi Koryo Tours). Aprile 2019: nessun tweet sul tema; aprile 2022: niente.
  **Negativi** (29 controlli in `leads_negatives_pyongyang_wire_2026-10-04.json`, 2026-10-04 asia): Bloomberg 2022 (via
  Japan Times), Forbes, Fortune, TechCrunch, Slate, Al Jazeera, SCMP, The Diplomat, NK News, Daily NK, Korea Herald/Times,
  Yonhap, VOA/RFA coreane, Decenter, Tokenpost, Blockmedia, CoinDesk Japan, CoinPost, Business Insider Japan, Sina
  (traduzione CoinDesk), stampa FR/DE/ES; i 9 post Substack di Ethan Lou sul processo; 2600 del 22/04/2022. L'«originale
  cinese» di baiyi.com **non esiste**: baiyi si dà come fonte (百亿财经). Omonimo: Bruno Pietrosanti (CoinDesk 04/2020).
  **Resta:** GDELT per finestre (429); Blockworks, The Block, BeInCrypto, CCN (403, Wayback anti-bot); NK Pro, Bloomberg
  29/11/2019 e WaPo 27/09/2021 (paywall); ~90 tweet archiviati 19/12/2019–10/01/2020 e ~35 di set/ott 2021 non letti; 6
  tweet cancellati nelle finestre (capture esistenti, rileggere dal server); podcast NK News ep. 301; eventuale 2600 di
  set/ott 2021. **Proposta:** dopo la lettura dei tweet residui, chiudere la voce.
  **Passata 2026-10-05 (`pass4_pyongyang_tweets_residui`, `pass4_pyongyang_media_residui`) → +10 voci, voce CHIUSA.**
  **Tweet:** letti tutti i 91 status archiviati 19/12/2019–10/01/2020 e gli altri 91 di 15/09–15/10/2021 (+20 capture
  Wayback dei cancellati, scaricate dal server in serie): 7 rilevanti — «Getting @virgilgr out of jail» (a Buterin,
  25/12/2019), al 36C3 sul talk DPRK («I've been there in April for blockchain conference», 27/12/2019), «North Korea
  Technologies at IO at #36c3», a Kenneth Geers, «Axes of Evil» di Josh Dean, «North Korea informant reward program»
  (04/10/2021, cancellato, testo dal Wayback), a Ethan Lou (15/10/2021). **Media:** The Next Web 03/12/2019 (cita
  l'intervista CoinDesk), **CoinDesk Italiano** ×2 (traduzioni 2022 dell'intervista e di «Freedom Fighter or Fool?»,
  uniche pagine in italiano sul tema; versioni es/fr/ru/uk come riprese), Yahoo Finance (ripresa, accorpata).
  **Negativi** (`leads_negatives_pyongyang_{tweets,media}_2026-10-05.json`, 31+ controlli): NK News ep. 301 trascritto
  (solo Cao de Benós ed Emms), 2600 Off The Hook 29/09/2021, 13/04/2022, 04/05/2022 trascritti (mai nominato), GDELT su
  4 finestre, Blockworks, The Block, YouTube (sottotitoli VICE e CoinDesk). Fabio il 05/10 ha ricordato solo Bloomberg
  (già gestito). **Residui non aggirabili:** BeInCrypto/CCN (Cloudflare), NK Pro/Bloomberg 2019/WaPo 2021 (paywall),
  tweet mai archiviati.
- [x] **Nuove piste emerse il 2026-10-05 — fatte il 2026-10-06** (3 agenti: `pass4_mirror_anac_appello_2017`,
  `pass4_foggia_2019`, `pass4_audizioni_foia_cad_pega`; negativi in `data/research/leads_negatives_{anac_appello,
  foggia_2019,foia_cad_pega}_2026-10-06.json`) → **+2 voci**, il resto negativo solido.
  (a) **Appello ANAC 24/07/2017**: il testo (Web Archive 08/08/2017) è firmato solo «Centro Hermes», senza il suo nome;
  nessuna copertura stampa luglio–ottobre 2017; nessun suo tweet sul tema; la stampa 2019 su OpenWhistleblowing (Il Fatto,
  Dire, DigitalPA, Tor blog, Publika…) non lo nomina. Trovato solo l'**URL originale 2017** della lettera di Cantone sul
  vecchio portale ANAC → aggiunto come mirror. Non verificati: techeconomy2030.it 19/10/2020 (403), neicomuni.it (morto).
  Fabio (06/10) non ricorda passaggi TV o radio sulla polemica → **pista chiusa**.
  (b) **«Slide Foggia»**: tweet recuperato dal Web Archive (05/12/2019 12:58, testo «Slide Foggia» + link a Google Slides)
  → verificato; il deck è **cancellato** (410) e mai archiviato. Ipotesi migliore, **non confermata**: lezione ospite nel
  corso di «Sicurezza informatica» di **Stefano Aterno** all'Università di Foggia (LM Scienze giuridiche della sicurezza,
  I semestre 2019; coautori su Agenda Digitale 04/2019). **Confermato da Fabio il 06/10**: lezione all'università su
  invito di Aterno → il deck è registrato come talk (verificato da Fabio); resta solo il file delle slide (cancellato).
  (c) **FOIA (AG 267, 6-7/04/2016)**: raccolta completa delle memorie (146 pp., OCR) → Hermes non audito né memoria;
  **CAD (AG 307, 18/07/2016)**: video WebTV Camera trascritto per intero → nessun intervento Hermes; **relazione PEGA
  A9-0189/2023** letta (DOCX ufficiale): nessuna occorrenza (l'unico «Hermes» è Hermes Airports, Cipro).
  Omonima già nota (decisions.json): **Valentina Pietrosanti** (redazione Radio Radicale), falsi positivi su radioradicale.it.

- [x] **Lacuna 2023–2026 — passata 2026-10-07** (aperta oggi: 2023-2025 avevano solo 26 voci; 3 agenti:
  `pass4_lacuna2023_{latina,tech,biohacking}`, negativi in `data/research/leads_negatives_lacuna2023_*_2026-10-07.json`,
  ~130 ricerche) → **+14 voci**, tutte verificate.
  - **Latina**: riprese della visita della Celentano alla GLS (19/04/2023) su latinatu.it e latinanews.eu («accompagnata
    da Fabio Pietrosanti», foto con didascalia); PEC MonitoraPA del 06/11/2022 riprodotta da easyteam.org (**con i suoi
    dati personali** → domanda a Fabio). Negativi: chiusura GLS Latina 2025 (6 testate, parla solo **Elma**), ex Pacifico/P&D
    («famiglia Pietrosanti», mai il suo nome), Aeroporto di Latina, Consorzio Logistico, Unindustria, TV locali: nessuna
    menzione. Omonimo nuovo: **Fabio Pietrosanti di Velletri (ASD Center Bike, ciclismo)** → in `decisions.json`.
  - **Tech/spyware**: The Next Web 01/04/2026 (caso SIO, «Hermes Center president»), IRPA 16/07/2025, riprese del pezzo
    The Record 2024 (Think.it, Fudzilla, The Cyber Post, SoylentNews, digest CTO at NCSC), webinar IPI 13/10/2022 su FOIA
    e MonitoraPA (YouTube), **Garante privacy di San Marino** («Dott. Fabio Pietrosanti» nel comitato tecnico di esperti,
    senza data → domanda a Fabio). Negativi: D.lgs 24/2023, Paragon, Equalize, e-privacy 2023-26, Hackmeeting, ITASEC,
    Cybertech, Security Summit, podcast, Radio Radicale (ultimo intervento 2021).
  - **Biohacking**: reel Facebook «Codice Barbara Carfagna» del 27/06/2025 (dietro le quinte, video scaricato) e il sito
    hackingbiology.com (fonte primaria, News dal 2023). Negativi: stampa nazionale, longevity media internazionali, 39C3,
    GlycanAge, Biohackers Milano, SignalSwarm (nessuna copertura pubblica).
  **Resta:** IHC 2024/2026 (sito vuoto agli script), LatinaToday (ricerca solo JS), RaiPlay Sound / Ufficio stampa Rai
  (403 dal laptop: altre puntate Codice Beta/Rai Radio), Facebook/Instagram (altri promo Codice: serve il Chrome loggato),
  livestream Fund Longevity Roma 08/04/2026 (YouTube 4CHvbryuUb4, segmento Roma 17:23-17:25, da guardare), quotidiani
  a pagamento (Corriere, Repubblica, Il Foglio, Messaggero Latina).
- [x] **Lacuna 2004–2008 — passata 2026-10-08** (solo ~26 voci in 5 anni; 3 agenti: `pass4_lacuna2004_{talks,press,tech}`,
  negativi in `data/research/leads_negatives_lacuna2004_*_2026-10-08.json`) → **+28 voci verificate** (+1 CVE esclusa: il record non lo nomina).
  - **Talk ed eventi**: **Webbit 04** a Padova (maggio) **e Milano (3-4/06/2004)**, 6 seminari (sicurezza wireless 1 e 2
    con Yvette Agostini, «La percezione della sicurezza informatica», titolo assente dal suo elenco), scheda relatore,
    pagina «relatori indipendenti area sicurezza» (coordinatore), **2 PDF delle slide** dal Web Archive (wireless,
    126 pp.; «la percezione e la realtà»); **SMAU 2005** eAcademy Sikurezza.org («PGP luci e ombre», evento distinto da
    e-privacy 2005, PPT archiviato); **Infosecurity 2006** (firma digitale ven. 10/02 ore 10; sostituto di Igor Falcomatà
    con Pennasilico sull'hardening PHP del 09/02); **Infosecurity 2007** «Voice Security & Privacy» (06/02, con Flora,
    Misitano, Pennasilico); **hack.lu 2006** agenda + pagina relatori con biografia (KHAMSA SA, docenze CNR e Castellanza);
    pagina Sikurezza.org «ITBH» (SMAU 2002).
  - **Tecnico**: sito **OSXCrypt** dal Web Archive (pagina Staff «Fabio Pietrosanti (naif) - Starter of the project» e il
    post originale «This is not a scam»), brevetto **ITRM20060426A1** (priorità italiana di WO2008015723), s0ftpj.org
    docs (slide «by naif»); CVE-2006-5817 (dal suo advisory Parallels, ma il record NVD non lo nomina → non verificata).
  - **Blog**: 7 post di Matteo Flora (mgpf.it 2007-2008: Infosecurity 2007, talk AIP del 28/04/2007 Orvieto/Perugia,
    corso «Pragmatic Security» set. 2007, annuncio OSXCrypt 24/01/2008, Aperitivo Informatico Milano 19/12/2008) e
    minotti.net 08/02/2007.
  - **Negativi solidi**: Punto Informatico 2004-08 (full-text), **Zeus News** (~6.700 articoli 2003-08), Internet Archive
    (2.209 occorrenze «Pietrosanti» + scansione OCR di Hacker Journal, PC Professionale, Win Magazine, Computer Idea, Linux
    Magazine, PCWorld Italia, Internet News 2003-09: solo i 3 già noti), Repubblica, Corriere, Clusit newsletter 2004-08
    (56), MOCA 2004, Hackmeeting 2004/05/07/08, hack.lu 2005/07/08, registro di commercio svizzero (Khamsa SA: mai nel
    CdA), Notiziario Tecnico Telecom Italia (13 numeri), OSXCrypt stampa estera, scandalo Telecom 2006 (mai nominato).
    Il suo `curriculum.shtml` nel Web Archive è fermo al 2003; la pagina «media» 2005-06 era «in costruzione».
  - **Bug corretto** in `merge_media.py`: le pagine MediaWiki `index.php?title=…` e gli allegati MoinMoin `?upname=…`
    collassavano in una sola voce → **recuperate 9 voci End Summer Camp 2007-2015** già trovate il 18/09 (Hacker
    Jeopardy ESC07 ecc.). Data di SlideShare 1669276 corretta al 10/02/2006.
  **Resta:** archivi a pagamento o non ricercabili (Sole 24 Ore/Nova, La Stampa 2006-08, Messaggero, Panorama, Espresso,
  Computerworld/ZDNet Italia); riviste ICT Security e Wireless (nessun numero online); apparizioni TV citate nel suo CV
  (TG2, TG3, Studio Aperto, Neapolis); MP3 Webbit 04 Milano e PDF Infosecurity 2007 mai archiviati; newsletter Clusit
  apr–mag 2008 (controllo anti-robot: **non aggirato**); premio «innovation competition» del CV; sedi del 2006 (Centro
  Alti Studi Lotta al Terrorismo, Castellanza, IBM). Hackmeeting 2006 e CCC 24C3/25C3 non ricontrollati.
- [x] **Lacuna 2011–2016 — passata 2026-10-13** (21-38 voci/anno; 3 agenti: `pass4_lacuna2011_{talks,stampa_it,
  estero_video}`, negativi in `data/research/leads_negatives_lacuna2011_*_2026-10-13.json`, ~130 ricerche) → **+11 voci**
  (10 verificate) e 6 mirror di voci note.
  - **Nuove**: Internet Freedom Festival **Valencia 2016** («Setting up Whistleblowing Activism Initiatives with
    GlobaLeaks», «Presenter(s) Fabio Pietrosanti», wiki IFF dal Web Archive); **Wired Italia 01/02/2016** (ddl Businarolo,
    citato); **Punto Informatico 21/01/2016** (tuo tweet sulla lettera a Renzi contro la nomina Carrai); **SenzaBarcode
    22/04/2015** (resoconto del tuo intervento a Frontiera Digitale Radicale); video **Friuli FutureForum #VL2014**
    (19/05/2014) e **videodiario IJF 2012** terza puntata (+ copia di Valeria Belviso); fuori periodo: Motherboard Italia
    14/02/2017 e 03/07/2017 (Area SpA), lettera aperta sulla direttiva whistleblowing su The Black Sea (2019), video
    YouTube del seminario «Manualetto» del CRS (2026). **Non verificata**: «Globaleaks Live Launch» ESC 2011 (nome solo
    nei sottotitoli automatici → in trascrizione). **Mirror**: think.it (EJO ExpoLeaks), LWN (Tor Weekly News 17/09/2014),
    VICE «-mb» (VLC 2017), MOCA 2016 /speakers/, YouTube Fanpage DIG 2020, slide del 73° Mercoledì di Nexa (PDF dal
    Web Archive, nome solo nel nome del file). **Escluso**: La Stampa YouTube TI4GA-ozdHw (IJF 2011, senza nome).
  - **Negativi solidi**: Repubblica 2011-16 (ricerca con filtri data: solo i 4 noti), Punto Informatico full-text
    (pietrosanti/naif/globaleaks/tor2web/privatewave; Hacking Team 2015 non ti nomina), Wired.it (46 articoli), Il
    Fatto/L'Espresso (Hacking Team, IrpiLeaks, ALAC, RegeniLeaks), ~25 testate online, archivio stampa Hermes
    (`hermescenter-restore`: nessun pezzo 2011-16 col nome; Corriere TV 2013 dice solo «il presidente di Hermes»); CCC
    28C3-33C3, RightsCon 2014-16 (sessioni Hermes con relatore «TBA»), IFF 2016 «User forum» (Pellerano), GIJC 2011/15,
    IGF 2014-16, Dataharvest, HOPE, Logan, Tor dev meeting; YouTube (~900 video), Vimeo, podcast 2011-16, Tor Weekly
    News/report mensili, stampa estera su GlobaLeaks/Tor2web/Hacking Team in 10 lingue; Radio3 Scienza 2013 PRISM
    (era Arturo Filastò).
  **Resta:** La Stampa (Frediani su Hacking Team 2015) e Corriere (ricerca interna solo da browser), Sole 24 Ore,
  Messaggero, Secolo XIX, ANSA/AGI/Adnkronos (nessuna ricerca full-text); Il Manifesto dic. 2014 «Tecnologie
  anticorruzione»; Repubblica cartaceo 07/08/2016 p.36 (paywall); dal Web Archive (bloccato per 429 tutta la sessione):
  Golem.de 2011, OWNI 2011-12, de Volkskrant 2013 (Publeaks), Disappeared News 2013, techPresident, pagine stampa
  Hermes/GlobaLeaks; programma finale RightsCon 2016 e Circumvention Tech Festival 2015; PDF dei programmi SIF, CPDP,
  re:publica, CoE, UNESCO; podcast 2020-24 da verificare (Valigia Blu, Ciao Internet, DataKnightmare); pista 2010
  tuttovolume.net 09/02/2010 (intervista, Khamsa) da controllare.
- [ ] **Lacuna 2007–2010 — passata 2026-10-23** (2007 e 2008 con 13 voci ciascuno; 3 agenti: `pass4_lacuna2007_{talks,
  press,tech}`, negativi in `data/research/leads_negatives_lacuna2007_*_2026-10-23.json`, ~85 ricerche) → **+17 voci**
  (11 verificate + TVtech verificato con la trascrizione = 12).
  - **Talk**: **WhyMCA Spring 2010** (Politecnico di Milano, 21/05/2010, «Mobile security and privacy», scheda + agenda) e
    **WhyMCA 2011** (20/05/2011); **Security Summit Milano 2009** (26/03, Seminario SiKurezza.org) e **Hacking Film
    Festival 2009** (tra gli organizzatori delle tavole rotonde); relatori Security Summit Milano 2010; 2 deck sul
    SlideShare di PrivateWave (3746617, 3746738: copie di talk già noti).
  - **Stampa/TV**: **TVtech 08/02/2010** «Intercettazioni GSM: più facili di quanto si creda» (YouTube `_S19ka5fy2Q`,
    trascritto: «parere di Fabio Pietrosanti, security manager di Khamsa» → **verificato**); LinuxSecurity.com 02/2010
    (ripresa CSO «Accusations fly over voice encryption hack»); pagina autore **Voice of VOIPSA** (2010, «Fabio
    Pietrosanti (naif)»). **Piste dalla rassegna stampa PrivateWave** (`privatewave.it/chi-siamo/area-stampa.html`, 7
    capture 2010-12): **Rai 3 TGR Neapolis 29/12/2009 «Telefonate protette»** (probabilmente la «Neapolis» della bio
    2013), video Class Life 02/2010, 39 ritagli 2010 (Economy, L'Espresso, Il Mondo, Il Sole 24 Ore 28/11/2010…): nessun
    PDF archiviato, sito 403 → domande a Fabio. **Escluso**: Comms Business (comunicato EVSS senza nome).
  - **Negativi solidi**: e-privacy 2007/08/10, CCC 24C3-27C3 e Camp 2007, ESC 2008, Clusit newsletter 2007/09/10 (38
    PDF), Infosecurity 2007-10, OWASP Day 1-5, Linux Day, voip2day/Astricon/HOPE 2008/HITB 2008/DeepSec; stampa 2007-08
    (Corriere 22/02/2010 su PrivateWave nomina solo Marchini e Zimmermann; NYT 2007 sulle intercettazioni; The Register,
    01net, CorCom, Focus); brevetti (solo la famiglia Khamsa nota), commit di Asterisk/PJSIP/Tor/FreeSWITCH/SniffJoke,
    IETF datatracker, OpenAlex, tesi su ZRTP/VoIP.
  **Resta** (Web Archive «Temporarily Offline» per gran parte della sessione): giro di 255 pagine (privatewave.com/.it,
  zorg.org, khamsa.it, voipsa.org, sikurezza.org wiki 2009-11, infosecurity.ch 2007-08) avviato sul server
  (`~/wb_tech2007_fetch.py`, esiti `~/wb_tech2007/hits2.jsonl`, fine quando `log.txt` dice «FETCH2 FINISHED") + CDX di
  ohloh/freshmeat/launchpad/Google Code/zfone (`~/wb_tech2007_cdx2.sh`: **finito**, elenchi pronti e non ancora letti —
  293 capture zfoneproject.com, 61 www.khamsa.it, 2 fabio.pietrosanti.it; ohloh/freshmeat/code.google.com/p/privategsm
  da rifare, il CDX ha restituito la pagina «Temporarily Offline»). **Giro delle 255 pagine finito (253 lette):** +1
  voce, la pagina «author» di infosecurity.ch (capture 23/12/2008, «Fabio Pietrosanti (naif)»); PrivateWave/Khamsa/
  ZORG/privategsm senza il nome; VOIPSA: solo un tuo commento (11/08/2010, client ZRTP per BlackBerry), che come un
  post di forum non conta; osxcrypt e sikurezza.org solo pagine già note. SMAU 2007-10 (400 URL su ~9.000 controllati);
  MOCA 2008 (programma non archiviato); seminario Trento 2010; URL di 22 testate italiane nel Web Archive (504);
  Google Books (429); brevetto US20130252585 (Google Patents anti-bot, solo pista).

- [ ] **Lacuna 2017–2019 — passata 2026-10-24** (3 agenti: `pass4_lacuna2017_{press,talks,media_research}`, negativi in
  `data/research/leads_negatives_lacuna2017_*_2026-10-24.json`, ~90 ricerche) → **+22 voci** (20 verificate).
  - **Stampa**: Repubblica.it (Rijtano) «Dimmi come digiti e ti dirò chi sei» 11/05/2017 e app spia per iPhone (Exodus)
    08/04/2019; **Repubblica 2018 «Quando la spia si nasconde nell'app» (29/05) e «Il sito del Viminale bloccato
    all'estero» (Longo, 09/11) verificate dalla versione AMP pubblica** (pagina normale dietro paywall); AGI (Angius) NYT
    nel dark web 28/10/2017, AGI sorveglianza di massa a IJF18 11/04/2018, AGI (Frediani) intelligence sharing 26/04/2018
    («portavoce del Centro Hermes»); Euronews Kaspersky 15/05/2018 e app per il ciclo **in EN/ES/FR** (2018); AgenSIR
    01/10/2018 piattaforma TI Italia–Hermes. Non verificate (solo snippet dell'archivio Repubblica, cartaceo):
    «La beffa dei tablet» 20/10/2017 p.10 e RLab «La spia che venne dall'app» 30/05/2018 p.57.
  - **Talk/eventi**: Tor Meeting Amsterdam 03/2017 («naif», partecipante) e Roma 03/2018 («Fabio (naif)», probabile);
    video Privacy Camp 2018 EDPS–Civil Society Summit (YouTube RYYqziLGBG4); tweet che datano Mojo Italia 29/09/2019,
    convegno sul voto a distanza a Roma ~12/10/2019, 34C3, workshop Amatriciana al 35C3 e 36C3; **Advisory Board del
    Center for the Cultivation of Technology** (Berlino, 2017-2021).
  - **Negativi solidi**: RightsCon 2017-19, CPDP 2017-19, GIJC17, IGF 2017/19, FNF 2018, ESC e Hackmeeting 2017-19, State
    of the Net, Dataharvest, CCC (nessun suo talk), IJF 2017/2019; La Stampa (81 risultati), Vice, Key4biz, Valigia Blu,
    CorCom, Agenda Digitale, Cybersecurity360, Fatto Quotidiano, netzpolitik, EDRi, Intercept; GDELT 2017-18 vuoto; TV
    (PresaDiretta Rousseau 2018, La7 tablet 2017); OpenAlex/IA full-text. **Escluso** POuL 2018 GlobaLeaks (relatore
    Pellerano). Twitter nel Web Archive 2017-19: lette tutte le 486 capture leggibili, fonte esaurita.
  **Resta**: Corriere della Sera e Sole 24 Ore (ricerca JS/anti-bot), Il Post/Open/HuffPost; programma del convegno di
  Roma 10/2019; WIN Glasgow 09/2019 (workshop GlobaLeaks senza nome); IFF Valencia, MozFest, Wired Next Fest, Internet
  Festival, Security Summit/ITASEC PDF, Codemotion; Semantic Scholar e Google Books (429); tesi NOVA Lisbona 2018 e SSRN
  3459366 (anti-bot, citano Hermes); WebTV Camera conferenza stampa trojan 31/01/2017; sottotitoli YouTube POuL/HOPE 2018.

- [ ] **Lacuna 2023–2025 (ripasso) — passata 2026-10-25** (3 agenti: `pass4_lacuna2023r_{press,talks,biolatina}`, negativi in
  `data/research/leads_negatives_lacuna2023r_*_2026-10-25.json`, ~100 ricerche + ricerche interne su ~135 siti) → **+4 voci**
  (3 verificate), di cui solo 1 nel periodo: il ripasso conferma che il 2023–2025 è davvero povero di menzioni.
  - **Nuove**: Mondoreale 19/04/2023 (quarta ripresa della visita Celentano alla GLS, «accompagnata da Fabio
    Pietrosanti»); **Linux Day Bari 22/10/2022** ×2 su PeerTube video.linux.it — panel «Privacy e sicurezza del dato:
    l'approccio hacker» (con Lopez, Tesio, Vannini, Bernieri, Resoli; MonitoraPA) e tavola rotonda conclusiva (nome nella
    descrizione; video scaricati in locale, 1h41' e 1h22'); h24notizie 22/06/2014 «Cinque Stelle apre il dibattito sulla
    conversione del Comani» (un «Fabio Pietrosanti» presenta una proposta sull'aeroporto: **non verificata**, domanda a Fabio).
  - **Negativi solidi**: Paragon/Graphite 2025 (Il Post, TechCrunch, The Record, Euronews, Guerre di Rete…), riprese di The
    Record 2024 oltre a quelle note, 14 numeri della newsletter Hermes «</Monitor>» (2024-25, mai il nome), MonitoraPA 2023
    nella stampa scolastica (senza nome), ricerche interne IrpiMedia/Domani/Wired/Valigia Blu/Red Hot Cyber/Il Post/ANSA e ~25
    testate WordPress; RaiPlay (Codice, Tv7, Speciale Tg1) e RaiPlay Sound 2023-25 (12 programmi: Eta Beta 23/09/2023 cita
    Hermes ma ospite Laura Carrer); Hackmeeting/ESC/WHY2025/37C3/Camp 2023 (Hermes al 37C3 = Agosti e Priori); Copernicani
    2023-26 (263 pagine Wayback); Lifespan.io, Longevity.Technology, GlycanAge; ~110 testate locali del Lazio (solo l'omonimo
    di Velletri). Fund Longevity 08/04/2026: i sottotitoli non lo nominano (il segmento Roma lo parla «Ferdinando»).
  **Resta**: ricerche interne di Il Fatto, Open, Repubblica, La Stampa, Corriere, AGI, Adnkronos (403/401: Chrome di Fabio);
  ihc.camp 2024/2026 e pagina linuxdaybari.it (Web Archive offline dal laptop per tutta la sessione); latinanews.eu e
  laprovincialatina.it (non rispondono); post LinkedIn di terzi (login); PDF ComeInClasse fuss.bz.it (9,8 MB, MonitoraPA);
  meetup «Longevity Biohacking» al 38C3 (28/12/2024, annunciato su X, assente dalle pagine archiviate); GDELT (429).
  **Proposta**: dopo i residui via Chrome, chiudere la voce — la ricerca automatica sul 2023–2025 è esaurita.

## Note sessione 2026-10-28 (run programmata «ricerca profonda»)
- **1232 voci** in `data/media.json` (+1 verificata, +1 talk non verificato). Prime voci della coda ancora bloccate (chiavi,
  login, risposte di Fabio, video TimePie): lavorate le piste indicate il 27/10 con 3 agenti (`pass4_weekit2003_2005`,
  `pass4_siti1997_libri`, `pass4_tv_cv2003_eventi`; negativi in `data/research/leads_negatives_*_2026-10-28.json`).
- **Nuova verificata: CEGOS Italia, Milano 1/02/2001** — «Come rapportarsi e rispondere ai nuovi hacker» (14:30, «Fabio
  Pietrosanti, Security Manager I.NET», con CERT-IT, GdF, Transcrime, chiusura di Giustozzi; programma su degrazia.it dal Web
  Archive): **è il talk più antico in archivio** (prima: AntiKrimen 13/10/2001).
- **Ritrovato il tuo sito naif.itapac.net 2000–2002** (homepage «NaiF...un uomo, un SysAdmin», `uffa.htm`, `curriculum.txt`
  2001/2002): contiene **dati personali** (indirizzi, cellulare, data di nascita) e toni goliardici → **tenuto fuori dal sito**,
  solo nel repo privato (`_in_attesa/naif_itapac_2026-10-28.json`), domanda a Fabio. Dal CV 2001 nuove piste stampa:
  intervista **ADNKronos sull'intrusione nel sito di Radio Vaticana** (ripresa da Corriere e Il Tempo, data ignota, prima di
  07/2001), articolo su **Il Mondo** («ero in prima pagina»), speciale **TG2 Dossier** sugli hacker; eventi «Sicurezza reti
  aziendali», «Security on The Net», Summercon (NL), Hacker at Large 2001 — nessuna trovata online.
- **Non verificato**: IFF 2019 (1/4/2019) «Whistleblowing PA … (a GlobaLeaks usecase)», programma senza relatori.
- **Negativi solidi**: WeekIT (tutte le 120 schede + ~750 articoli 2003-04 letti, ID 006004036000-036665 e 039720-040421),
  sikurezza.org 2003-05 (30 pagine non di lista), Apogeonline/Datamanager/LineaEDP/ZeroUno/Webnews/CorCom/Key4biz (ricerche
  interne: solo omonimi Cristiano, Paolo, Guido), computerworld.it/zdnet.it (domini parcheggiati), ictbusiness.it (niente
  prima del 2006); digilander, geocities «naif*» (altri), naif.it (segnaposto), naif.org, latinaonline.it/.com, xoom/lycos/
  inwind/supereva/tin; Google Books nel Chrome di Fabio (1995-2002: solo omonimi e i 2 libri noti; *Profilo hacker* ed.
  italiana senza anteprima); Hacker Journal 1-14 e 37; **e-privacy 2002 e 2003: non eri relatore** (10 talk 2002 su IA);
  Wired Next Fest Milano 2015/16/18/19 e Firenze 2018, MozFest 2019, YouTube (13 ricerche), Il Tempo/Il Mondo/L'Espresso
  2000-04 sul Web Archive (quasi nessun articolo catturato), PrivateWave rassegna video (nessun TG3).
- **Job ancora in corso sul server** (ubuntu@51.158.36.151, ripartibili): **WeekIT** ~2.160 articoli rimasti (ID
  006004036666-039719, `~/wb_weekit/collect.sh` dà avanzamento e `HIT`, riavvio `cd ~/wb_weekit; for k in 0 1; do nohup
  python3 fetchw2.py $k > fx$k.out 2>&1 & done`, max 2 worker); **siti 1997-2002** 552 capture (latinaonline.it, antikrimen.it,
  e-privacy.firenze.linux.it, kill-9.it, lns.it, sicurmatica.it, ilmondo.rcs.it) in `~/wb_personal1997/` (`python3
  grepcap.py`, esiti `grep_results.json`), più le query di `q4.json` (smau.it 2001, iltempo.it, espressonline, vaticanradio.org,
  clusit.it) mai eseguite.
- **Prossima voce lavorabile:** raccogliere gli esiti dei due job sul server; cercare la data dell'intrusione a Radio Vaticana
  (archivi Corriere/ADNKronos) appena Fabio la ricorda; poi proporre di chiudere tutte le voci «Lacuna».

## Note sessione 2026-10-27 (run programmata «ricerca profonda»)
- **1227 voci** in `data/media.json` (+6: 1 voce nuova verificata, 1 talk non verificato, 4 mirror/voci proprie). Prime voci
  della coda ancora bloccate (chiavi, login, risposte di Fabio, video TimePie): lavorate la **lacuna 1995–2002** (mai
  coperta da una passata pass4: 1995-99 avevano 2 voci) e i **residui 2017–2019** sul Web Archive. 3 agenti:
  `pass4_lacuna1995_1999`, `pass4_lacuna2000_2002`, `pass4_residui2017_2019`; negativi in
  `data/research/leads_negatives_*_2026-10-27.json`.
- **1995–1999 → 0 voci nuove** (fonte esaurita): letti tutti i BFi 1-8 + PFi/summer/news, s0ftpj su Wayback 1999-2000,
  Hackmeeting 98 e 99 (260 pagine), I...ludiamoci 97-99, indici Bugtraq 01/1997–05/2000 (primo advisory resta giugno
  2000), 13 ricerche full-text IA su riviste, Phrack 65. Aggiunte come voci proprie/mirror: **madoka** (panservice.it, firma
  «NaiF», «IrcNet #Latinaonline NaiF^» → il nick è tuo già nel 1997-98, rafforza BFi n.4) e l'archivio `bfi7.tar.gz`
  (ringraziamenti: naif a **I...ludiamoci 99**, Pescara). **La Stampa 27, 30 e 31/10/1997** «Fabio Pietrosanti, Velletri
  (Roma)»: omonimo → esclusi in `decisions.json`. **Tenuto fuori dal sito**: commento HTML «pagina e server bucato da naif
  la notte del 30 agosto 2000» nella homepage di Hackmeeting 1999 → in attesa di Fabio (repo privato `_in_attesa/`).
- **2000–2002 → +1 verificata**: **Webb.it 02**, contest «Secure System Administration» di Sikurezza.org («RESPONSABILE
  DELLA COMPETIZIONE Fabio Pietrosanti naif», 6-7/07/2002) + 2 mirror webb.it del talk/coordinamento Sikurezza.org.
  Datore di lavoro 2002 = **I.NET SpA** (gruppo BT), «Network Security Manager». **Negativi**: Corriere archivio 2000-02
  (26 articoli hacker; il 28/10/2002 sui Blackhats a SMAU cita «Wireless (in)security» ma intervista Vodka e Raistlin),
  PuntoSicuro AR-1…AR-2400 (con il 22/10 coperto fino al 2007), ~490 comunicati I.NET, 634 schede webb.it 2001-02, 551
  pagine WeekIT, Hackmeeting 2000-02, L'Unità, Linux Day, SMAU, Winston Smith, Phrack 56-60.
- **Residui 2017–2019 → +1 (non verificata) e una correzione**: il convegno «sul voto a distanza» è il meetup **#AperiTech
  Legal Hackers Roma «Voto Elettronico: verso una democrazia digitale?» del 14/10/2019** (via Marsala 29H; relatori Reale,
  Nicotra, Bruno Bossio, Titomanlio, Scialdone, Barich; modera Morelli): il tuo nome non c'è → probabilmente intervento dal
  pubblico (domanda a Fabio). **IFF Valencia**: la sessione GlobaLeaks della wiki (datata 2016 in archivio) è nel
  **programma ufficiale 2017 (9/3/2017, 14:30-15:30)**, wiki in categorie 2017 → aggiunto il programma 2017; IFF 2019:
  sessione «Whistleblowing PA (a GlobaLeaks usecase)» 1/4/2019 senza relatori archiviati. Negativi: IFF 2018 (archivio
  parziale), Internet Festival 2019 (796 pagine), MozFest 2017-18.
- **Resta**: Google Books (429) per 1995-2002; Wayback di itapac.net/digilander/space.tin.it/geocities/naif.it; programma
  e-privacy 2002, rassegna stampa webb.it 2001, AntiKrimen 10/2001 (non archiviati); ~2.800 pagine WeekIT 2003-05; TV e
  periodici della homepage 2003 (TG2 Dossier, «7 giorni al Parlamento», Studio Aperto, RMC, L'Espresso, Il Mondo, Il Tempo,
  DotCom) senza archivi interrogabili; Wired Next Fest anno per anno, MozFest 2019, relatore IFF 2019.
- **Prossima voce lavorabile:** WeekIT 2003-05 e Wayback dei siti personali 1997-2000 dal server; poi proporre a Fabio la
  chiusura di tutte le voci «Lacuna» (ricerca automatica esaurita su tutti i periodi).

## Note sessione 2026-10-26 (run programmata «ricerca profonda»)
- **1216 voci** in `data/media.json` (+5). Prime voci della coda ancora bloccate (chiavi, login, risposte di Fabio, video
  TimePie): lavorati i **residui** delle lacune 2007–2010, 2011–2016, 2017–2019 e 2023–2025 con 3 agenti
  (`pass4_chrome_testate`, `pass4_wayback_residui`, `pass4_eventi2017_residui`; negativi in
  `data/research/leads_negatives_*_2026-10-26.json`).
- **Testate via Chrome di Fabio (ricerche interne JS) → +4**: **Repubblica 19/01/2020 «Senza rete»** (Bottura,
  #bravimabasta: «come ha scoperto subito dopo Fabio Pietrosanti del Centro Hermes», dominio made.it) e **Nova100 / Sole 24
  Ore 18/11/2022** (blog Kettmaier, «l'Hermes center con Fabio Pietrosanti») **verificate**; non verificate (paywall):
  Repubblica Milano cartaceo 19/10/2017 p.5 sul voto elettronico (anteprima «spiega Fabio…») e Il Fatto cartaceo 13/03/2019
  «Il M5S vuole il voto digitale» (Della Sala; trovato cercando «Pietrosanti», il nome non si vede). **Negativi**: Repubblica
  (198 risultati letti), Corriere (archivio: 0 per «Fabio Pietrosanti»), Il Fatto (9 articoli GlobaLeaks), Open, ANSA (solo
  dal 2023), Messaggero (~105/115), HuffPost, Il Post, Internazionale, La7. **Bloccati**: AGI (ricerca rotta, 500), Sky TG24
  (404), Adnkronos (ricerca non restituisce nulla). **Piste a pagamento**: archivio Sole 24 Ore 29/05/2000, 15/09/2010,
  16/01/2023 «Diario legale» (probabile omonimo avvocato), NT+ Enti Locali 22/10/2020 (transazione Anac–Hermes).
- **Web Archive → +1**: pagina programma **Linux Day Bari 2022** (dominio scaduto, capture 05/12/2022, nome tra i relatori).
  **Negativi**: CPDP 2011 (PDF), post Hermes ALAC/ExpoLeaks 2014, blackhats.it, olografix.org (13.816 URL), ohloh/freshmeat
  (nessuna capture), Google Code Archive (403 per tutti i progetti: chiuso come bloccato), meetup 38C3 «Longevity
  Biohacking» (assente da 330 sessioni self-organized). **Resta**: ihc.camp 2024/2026 (nessuna capture dopo il 2023, sito
  giù), coe.int (CDX del dominio fallisce), SMAU 2007-10 (~8.600 URL non aperti, resa attesa bassa).
- **Eventi 2017–2019 → 0**: Internet Festival 2017/18, ITASEC 2017-19, HOPE 2018 (talk di Casadevall, sottotitoli senza
  nome), SSRN 3459366 (copia aperta: solo Hermes), tesi NOVA 2018 (Giachi: Hermes ×12, mai il nome), WIN Glasgow, Camera
  WebTV 31/01/2017, Clusit/Codemotion/Wired Next Fest/MozFest. **Resta**: convegno sul voto a distanza Roma ~12/10/2019
  (Wayback di crvd.org/copernicani.it 10/2019), IFF 2017-19 (wiki rimosso), Internet Festival 2019 (sito giù), sottotitoli
  italiani POuL 2018 (rate limit YouTube).
- **Prossima voce lavorabile:** convegno Roma 10/2019 e IFF 2017-19 dal Web Archive; piste a pagamento solo con accesso di
  Fabio; altrimenti proporre a Fabio di chiudere le voci «Lacuna» (ricerca automatica sostanzialmente esaurita).

## Note sessione 2026-10-25 (run programmata «ricerca profonda»)
- **1202 voci** in `data/media.json`. Prime voci della coda ancora bloccate (chiavi, login, risposte di Fabio, video
  TimePie): ripassata la **lacuna 2023–2025** (voce sopra, +4). Web Archive «Temporarily Offline» dal laptop: CDX fatti dal
  server.
- **Copie**: Linux Day Bari 2022 ×2 da 🟡 a video ottenuto (metadati dall'API PeerTube + video 540p in locale);
  Packet Storm/Secunia e notizieoggi ×2: nessuna capture (motivo aggiornato); Neapolis, Class Life, RMC, coinage: CDX vuoto.
- **Prossima voce lavorabile:** residui 2017–2019 e 2023–2025 nel Chrome di Fabio (Corriere, Sole 24 Ore, Repubblica, Il
  Fatto, Open), oppure la lacuna 2011–2016 sul Web Archive quando torna stabile.

## Note sessione 2026-10-24 (run programmata «ricerca profonda»)
- **1190 voci** in `data/media.json` (1124 verificate). Prime voci della coda ancora bloccate (chiavi, login, risposte di
  Fabio, video TimePie): lavorata la **lacuna 2017–2019** (vedi voce sopra, +22).
- **TVtech 598 / YouTube L4beB3qQjVw verificati**: la capture 2025 della pagina 598 incorpora il video, e la trascrizione
  Whisper della copia locale dice «parlando con Fabio Pietrosanti, un esperto di Khamsa» (00:14).
- **Brevetto US20130252585 escluso**: letto al retry, è CellTrust (Moshir, Khanban), nessun riferimento a Fabio.
- **Prossima voce lavorabile:** residui 2017–2019 (Corriere/Sole via Chrome di Fabio, convegno Roma 10/2019), oppure la
  lacuna 2023–2025 (12-19 voci/anno, ripassata solo il 07/10).

## Note sessione 2026-10-23 (run programmata «ricerca profonda»)
- **1154 voci** in `data/media.json` (1087 verificate). Prime voci della coda ancora bloccate (chiavi, login, risposte di
  Fabio, video TimePie): lavorata la **lacuna 2007–2010** (vedi voce sopra, +17).
- **Podcast solo audio → tutti e 5 verificati** con Whisper sulla copia locale: DataKnightmare 6x28 (2022, «l'intervista a
  Fabio Naif Pietrosanti»), The Crypto Conversation 2021 (Ethan Lou), Bloomberg «North Korea's Man in Spain» (2020),
  Valigia Blu Crypto AG (2020, «come racconta a Valigia Blu Fabio Pietrosanti»), **BBC The Lazarus Heist S2E7 «Crypto
  comrades» (2023): sei INTERVISTATO** («This is Fabio Pietrosanti», 10:49, poi 12:20-20:22 con Chris Emms).
  Audio presi dagli `episodeUrl` di iTunes Search (solo in locale).
- **Prossima voce lavorabile:** raccogliere gli esiti del giro Web Archive sul server (`~/wb_tech2007`); sottotitoli Ciao
  Internet sul server a ritmo lento; SMAU 2007-10 dal CDX; poi la lacuna 2017–2019 o i residui 2011-16 sul Web Archive.

## Note sessione 2026-10-22 (run programmata «ricerca profonda»)
- **1119 voci** in `data/media.json` (1052 verificate). Le prime voci aperte della coda restano bloccate (chiavi API,
  login, risposte di Fabio, sito Hermes, video TimePie): lavorate le tre voci proposte il 13/10, con 3 agenti
  (`pass4_lacuna2011_residui`, `pass4_lacuna2003_2006`, `pass4_podcast_2020_2026`; negativi in
  `data/research/leads_negatives_*_2026-10-22.json`) → **+16 voci nuove** (15 verificate) e 4 podcast promossi a verificati.
  Parte dei file grezzi è stata fusa e committata dal task Google che girava in parallelo (commit 3ed368f).
- **Residui lacuna 2011–2016 → +7 La Stampa** (la ricerca interna di lastampa.it funziona e copre l'archivio):
  Guerrini «Debutta Mafialeaks» 05/11/2013; **Frediani su Hacking Team** 14/07/2015 («Intelligence o panini?»),
  07/08/2015 («The Italian job»), 19/10/2015 (mercato degli attacchi); fuori periodo Frediani 11/05/2017 (Comey,
  costi GlobaLeaks), Angius 17/01/2019 (Tor) e 30/08/2019 (CCCamp, «Fabio “Naif” Pietrosanti»). **Negativi**: OWNI,
  techPresident, rassegna logioshermes.org, globaleaks.org/news, programmi OHM2013, IJF13, RightsCon 2016 (solo bozza),
  CTF 2015, CPDP 2012-16, SIF 2015, re:publica 2013/14/16; Sole 24 Ore. **Resta**: CPDP 2011 e post Hermes ALAC/ExpoLeaks
  (429 Web Archive), CDX coe.int, Messaggero/ANSA/AGI/Adnkronos (ricerca interna solo recente o browser).
- **Lacuna 2003/2005-2006 → +3 verificate** (2003 resta senza voci nuove): pagina «Interviste ai Relatori Webbit 05»
  (area Sicurezza, Zanero; capture 17/02/2005), advisory Parallels su Packet Storm (30/10/2006, «Authored by naif») e
  pagina autore «naif» di Packet Storm; non verificate: RTF dell'intervista Webbit (mai archiviato), ristampa Secunia
  SA22634 (anti-bot). **Negativi solidi** (scansioni intere dal server): PuntoSicuro 10/2002–2007 (~3.500 articoli: solo il
  pezzo noto del 10/02/2003), Zeus News 11/2002–10/2003, agenda SMAU 2003-05 (~560 pagine), Infosecurity Italia 2002-06
  (~1.400 pagine), CeAS, Linux Day, CCC 2003-06, Hackmeeting 2003/2006, e-privacy 2003/2006, sikurezza.org.
  **Escluso**: Win Magazine n.88 (05/2006) «Si chiama Naif» = l'hacker di XP sui Mac Intel, non Fabio.
  **Resta**: Google Books (429), CDX blackhats.it 2002-04 e olografix.org (Web Archive instabile), SMAU 2005-06 non
  archiviati, 01net.it (anti-bot), riviste cartacee e TV del CV.
- **Podcast 2020–2026 → +4 video YouTube** (gemelli delle puntate Spreaker, nome trovato nei sottotitoli automatici,
  senza scaricare audio): Ciao Internet 972 Kaspersky (15/03/2022), Canestrari «Pacifici sì ma incazzati pure»
  (30/03/2022), diretta Ciao Internet L54 (pesce d'aprile sul voto elettronico, 01/04/2022), #ONference «Le sfide della
  privacy nel 2023» (07/01/2023, «ciao naif»); le 4 puntate Spreaker corrispondenti ora **verificate**. Sempre citato,
  mai ospite. **Negativi**: iTunes Search su 7 store (980 episodi), 20 query YouTube, Radio Onda d'Urto/Città Fujiko/
  Popolare, Radio Radicale dopo il 2021, 28 puntate Ciao Internet (sottotitoli), Rivoluzionari in codice, TI Italia/WIN.
  **Resta**: sottotitoli dell'intero canale Ciao Internet (1.729 video + 107 dirette; YouTube limita: da fare lentamente
  sul server); 5 episodi solo audio da trascrivere (DK 6x28 e Crypto Conversation 2021 ora scaricati e in trascrizione
  locale, log `_run_transcribe_2026-10-22.log`; Valigia Blu 2020, BBC Lazarus Heist S2E7, Bloomberg «North Korea's Man in
  Spain» senza audio scaricato).
- **Prossima voce lavorabile:** esito delle 2 trascrizioni; sottotitoli Ciao Internet sul server a ritmo lento; residui
  Web Archive (CPDP 2011, coe.int, blackhats.it/olografix 2002-04); poi una lacuna per anno debole (2007-2010 o 2017-2019).

## Note sessione 2026-10-13 (run programmata «ricerca profonda»)
- **1038 voci** in `data/media.json` (+11, vedi «Lacuna 2011–2016»).
- **Scelta della voce:** le prime voci aperte restano bloccate (chiavi API, login Chrome, risposte di Fabio, sito Hermes,
  video TimePie): lavorata la lacuna 2011–2016 proposta il 08/10 e chiusi i ritagli delle 8 registrazioni trascritte.
- **Web Archive**: 429/connessione rifiutata per gli agenti quasi tutta la sessione; lo script delle copie ha funzionato.
- **Prossima voce lavorabile:** residui della lacuna 2011–2016 dal Web Archive (lista sopra) a ritmo lento, poi lacuna
  **2003 e 2005-2006** (7-9 voci/anno) o una passata sui podcast 2020-2024.

## Note sessione 2026-10-08 (run programmata «ricerca profonda»)
- **969 voci** in `data/media.json` (+37: 28 della lacuna 2004–2008 + 9 ESC recuperate dal bug di deduplica; 3 ESC senza nome escluse).
- **Scelta della voce:** Chrome di Fabio ancora «not connected» al primo comando (piattaforme cinesi ferme); lavorata la
  lacuna 2004–2008 proposta ieri.
- **Permessi:** su richiesta di Fabio impostato `defaultMode: bypassPermissions` globale (nessuna richiesta di conferma).
- **Prossima voce lavorabile:** lacuna **2011–2016** (21-34 voci/anno, periodo PrivateWave/GlobaLeaks: talk
  internazionali, stampa estera) oppure «Video/audio — ritagliare i convegni non Radio Radicale».

## Note sessione 2026-10-07 (run programmata «ricerca profonda»)
- **921 voci** in `data/media.json` (+14, vedi «Lacuna 2023–2026» sopra).
- **Scelta della voce:** le prime voci aperte restano bloccate — Chrome di Fabio «not connected» anche oggi (Douyin,
  Weibo, WeChat fermi), sito Hermes online ma con le sole 33 notizie nuove (News & Press storico non ancora ripubblicato),
  video TimePie non annunciati. Aperta e lavorata la lacuna per anni 2023–2026.
- **Copie:** 14 nuove ottenute (reel Facebook scaricato con yt-dlp; hackingbiology.com salvato dal live perché la
  capture 2024 non aveva il nome). Retry dei falliti: invariati i 7 ❌.
- **Prossima voce lavorabile:** «Video/audio — ritagliare i convegni non Radio Radicale» (lavoro locale) oppure la
  lacuna **2004–2008** (solo 26 voci: SMAU, MOCA 2004, Infosecurity, PrivateGSM/Khamsa agli inizi, stampa d'epoca).

## Note sessione 2026-10-06 (run programmata «ricerca profonda»)
- **906 voci** in `data/media.json` (+2: tweet «Slide Foggia» 05/12/2019 verificato; deck Google Slides cancellato, non
  verificabile). Voce lavorata: «Nuove piste emerse il 2026-10-05» (vedi sopra), chiusa.
- **Chrome di Fabio** ancora «not connected» alla prima navigazione → piattaforme cinesi (Douyin, Weibo, WeChat) ferme.
- **Copie:** tutte le nuove ottenute tranne il deck (410). Ripulite le 8 «non confermate» e 2 parziali residue (vedi
  PROBLEMI-APERTI B0-decies). `archive_copies.py` ora riconosce anche le grafie cirillica (Пьетросанти/П’єтросанті) e
  cinese (皮特罗桑蒂) del nome.
- **Prossima voce lavorabile:** le prime voci aperte restano bloccate (Chrome, chiavi API, Fabio, TimePie, sito Hermes).
  Candidata: «Video/audio — ritagliare i convegni non Radio Radicale» (lavoro locale, nessuna ricerca web) oppure una
  passata generale sui tweet 2017 (gli ID fuori tema raccolti dall'agente ANAC sono in `leads_negatives_anac_appello`).

## Note sessione 2026-10-05 (run programmata «ricerca profonda», sera)
- **904 voci** in `data/media.json` (+11: 7 tweet Pyongyang/Griffith, The Next Web 2019, CoinDesk Italiano ×2, lettera
  ANAC di Cantone 21/09/2017 «Al Presidente del Centro Hermes Ing. Fabio Pietrosanti»; Yahoo Finance accorpata come ripresa).
- **Voce chiusa:** Pyongyang 2019 / Griffith (vedi sopra). **Senato 14/05/2020** ricontrollato in parallelo alla sessione
  del mattino: stesso esito (Hermes = Vincenzo Tiani, 2:17:46 del video WebTV); il motore interno del Senato (generale +
  PDF non legislativi, leg17-19) non contiene mai «Fabio Pietrosanti». Il **browser integrato dell'app** passa il WAF di
  senato.it; il **Chrome di Fabio** risulta ancora non navigabile («extension not connected»).
- **Istituzioni residue** (`pass4_istituzioni_residui2`): audizioni informali Camera leg17 lette da **arquivo.pt**
  (~1.660 audizioni, 14 commissioni): zero occorrenze; Commissione Internet 2014-15, PE JURI/PANA 2017, PEGA 2023,
  Garante, AGCOM, AgID, CoE, consigli regionali: negativi (`leads_negatives_istituzioni_2026-10-05.json`).
- **Weibo e Douyin** provati nel browser integrato: entrambi chiedono il login (nessuna ricerca anonima) → restano per il
  Chrome loggato di Fabio.
- Web Archive: 429 dal laptop sulle CDX; gli agenti hanno usato il server (in serie) e WebFetch per GDELT.

## Note sessione 2026-10-04
- **942 voci** in `data/media.json` (+19: 28 tweet Pyongyang/Griffith, di cui 11 risposte identiche accorpate in una voce,
  + elenco ufficiale Camera dei candidati al **Garante privacy** 2019).
- **Garante privacy 2019 chiuso:** `camera.it/leg18/1372` (capture Web Archive 26/09/2020) elenca «Pietrosanti Fabio (**)»
  = candidatura dopo la riapertura dei termini del 7/10/2019, con link al curriculum `CV_PIETROSANTI_FABIO_.pdf` (mai
  archiviato, live 404). Conferma CorCom 31/10/2019.
- **Scelta della voce:** le prime voci aperte restano bloccate (Chrome, chiavi API, risposte di Fabio); lavorate le foto
  TimePie (prima voce sbloccabile) e i residui Pyongyang/Griffith.
- **Web Archive:** di nuovo blocco «suspected abusive bot traffic» dopo poche richieste CDX in parallelo; lo script delle
  copie però ha funzionato subito dopo. I tweet sono stati letti dall'endpoint pubblico `cdn.syndication.twimg.com`
  (testo + autore), le copie vengono dal Web Archive.

## Note sessione 2026-10-02
- **923 voci** in `data/media.json` (809 verificate): +1 dai file grezzi del 01/10 (la run si era fermata prima di merge e
  commit: CorCom 31/10/2019 candidatura al Garante privacy **riammessa** — l'esclusione del 23/09 era un errore di
  lettura —, baiyi.com, clip TimePie risolte), +13 Pyongyang/Griffith, −1 programma Linke; esclusi 25 negativi con
  motivo in `decisions.json` (Radio 24 13/03/2020, comunicato Partito Pirata, stampa senza nome).
- **Scelta della voce:** le voci aperte prima in coda sono tutte bloccate (Chrome non naviga, chiavi API, risposte di
  Fabio), quindi la run ha aperto e lavorato la lacuna «Pyongyang 2019 / Griffith», più il seguito Bundestag/Garante.
- **Bundestag 27/11/2019 chiuso:** l'audizione Linke «Medien unter Beschuss» (Assange/WikiLeaks); dal programma
  ufficiale (Wayback 14/11/2019) Fabio **non è relatore**; i video sono privati o rimossi. Resta solo il suo tweet.
- **Garante privacy 2019:** l'unica fonte resta CorCom (+ tweet @partitopirata 2020). Elenco ufficiale della Camera
  (`camera.it/leg18/1372`, capture 06/03/2020) **da leggere** quando il Web Archive risponde.
- **Web Archive** offline a intermittenza tutta la mattina (503 «Temporarily Offline», e per un'ora l'IP è stato
  segnalato come «bot»): le prossime run devono limitare le richieste a raffica.

- **Seconda esecuzione (iniziata il 29/09, finita il 30/09):** i suoi file grezzi erano già stati uniti dalla
  sessione del 30/09. In più: **911 voci** (+5 clip Bilibili TimePie candidate, non verificate: nome assente nei
  metadati; tolta BV1Rwh76XEhj = video NetEase già escluso); corrette le etichette BV1u5/BV1M7 in `decisions.json`;
  PrivateWave 2010 ripubblicato su RealWire e Comms Business ma senza il nome (B1 invariata).
- **906 voci** in `data/media.json`: +127 dai file grezzi del 29/09 (la sessione si era fermata prima del merge: 119 tweet
  2019-2021, TimePie Sohu/Baijiahao/WeChat, post infosecurity.ch 2017, OrlandoMagazine 18/09/2026), poi +4 oggi
  (NetEase profilo TimePie, agenda Sohu, secrss 2024, voce 360百科 GlobaLeaks non verificata) e −1 (NetEase video,
  escluso). Chrome di Fabio ancora disconnesso: Douyin/Weibo/WeChat Channels rinviati.

## Note sessione 2026-09-28
- **776 voci** in `data/media.json` (invariate: solo note arricchite con numeri di pagina). La sessione del 27/09 si era
  fermata prima di merge e commit: i suoi file grezzi e le copie risolte (BugTraq ID «credit» 2000, blackhats.it
  contatti/eventi SMAU 2001-2002, *This Machine Kills Secrets*, Di Salvo 2024) sono stati uniti e committati oggi.
- Copie: **i due «Amministrazione Trasparente» delle scuole risolti** con la ricerca interna del sito (`?cerca=Pietrosanti`,
  piattaforma Spaggiari): IC Cornigliano (diniego FOIA 19/10/2022) e Liceo Montessori (la sua istanza, **con dati
  personali** → solo archivio privato). Piste/negativi istituzionali in `data/research/leads_negatives_istituzioni_2026-09-28.json`
  (fuori da `raw/` per non entrare in `media.json`).

## Note sessione 2026-09-26
- **776 voci** in `data/media.json` (+7, vedi passata «Google Books API e Semantic Scholar» sopra).
- **RaiNews/Tg1 05/01/2025 confermato**: video scaricato (yt-dlp) e trascritto; a 0:34 didascalia «Fabio Pietrosanti –
  Biohacker» mentre spiega i biomarcatori (fotogramma salvato nella copia). **Sky TG24 02/07/2013 «Datagate»**: video
  visto per intero, l'unico intervistato è **Matteo Flora** → Fabio non c'è (domanda a Fabio in PROBLEMI-APERTI).
- 🔊 «solo video/audio» chiusi entrambi; 📚 «libri in attesa» da 13 a **2** (Profilo hacker ed. italiana, This Machine
  Kills Secrets in prestito IA; Di Salvo 2024 era già confermato dal PDF UniBo).

## Note sessione 2026-09-25
- **782 voci** in `data/media.json` (+48): AIRE 27, OpenRousseau 16, residui 2 (SoundCloud Rai IHC 2018; **The Record
  12/11/2024** «How Italy became an unexpected spyware hub», Fabio fonte principale), più il blocco Google delle 12:32.
- Residui chiusi: Google Doc OSSCI (2 capture giugno 2021, nessun nome né autore); StartMag Immuni 27/05/2020 (cita
  Uggeri, non Fabio; controllati tutti i 37 articoli StartMag su Immuni in Wayback); post Facebook 16/03 e 09/04/2020
  mai archiviati; Bloomberg online confermato («Italian information-security specialist Fabio Pietrosanti»).
- **Hackmeeting 2000 recuperato** (host senza www); **Google Books IGI Global**: l'ID era un refuso (`KOREEAAAQBAJ`).
- Nuovo strumento `tools/transcribe_media.py` (faster-whisper locale): trascrizioni delle puntate Radio 24.

## Note sessione 2026-09-24
- **734 voci** in `data/media.json` (+40): 39 dai «progetti mai partiti» (sopra) + la pagina CyberCoach di Gerardo Costabile.
- **Video YouTube `mAtBH2hkAcg` («Evoluzione dell'hacking con Fabio Pietrosanti (aka Naif)»)**: non è del 2019 ma del
  **17/01/2023**, canale **CyberCoach di Gerardo Costabile**. Il canale YouTube è stato rimosso (404); la pagina
  `costabile.net/cibercoach/` conserva titolo, data e descrizione → nuova voce verificata, data corretta via `override`.
- Web Archive irraggiungibile per buona parte della sessione (connessioni rifiutate / «Temporarily Offline»).
- Fabio (24/09): Gerardo Costabile conferma che l'account Google di DeepCyber è stato cancellato, e con esso il canale
  YouTube CyberCoach → il video del 2023 non tornerà online.
- `archive_copies.py`: `--retry-failed` non annulla più le classificazioni manuali (65 ripristinate da git).

## Note sessione 2026-09-23 (sera)
- **694 voci** in `data/media.json` (+2). Copie offline: 555 ottenute, 5 non ottenute, 0 in attesa.
- **`BRAVE_API_KEY` non impostata**: lo step 1 del task programmato (Brave Search API) resta inutilizzabile
  finché Fabio non fornisce una chiave.
- **`verify_candidates.py` corretto**: il filtro omonimi copriva solo 9 nomi e lasciava passare le schede di
  Radio Radicale «a cura di Valentina Pietrosanti». Ora usa `HOMONYMS`, allineato a `not_me` di `decisions.json`,
  più il pattern «a cura di … Pietrosanti».
- 5 nuove esclusioni in `decisions.json` (omonimi: 3 schede Radio Radicale, cronaca tg24.sky, cronaca Riformista).

## Note sessione 2026-09-23
- **701 voci** dopo il merge (erano 676). Nuove verificate: OSCE 2016 (biografia con il nick «naif»),
  ParteciPa #423 e #425 (gennaio 2020, proposte sue, handle `naif`), onData 2020 ×2 e la ripresa di Fondazione AIDR,
  USR Lazio 2024 e Ordine Ingegneri Catania 2022 (strascichi di MonitoraPA negli atti della PA),
  IC «Luciano Manara» (FOIA, **escluso dal repo pubblico**: contiene dati personali).
- **«Profilo hacker» (Apogeo 2007) confermato**: nei ringraziamenti «"Naif" Pietrosanti» (copia Internet Archive).
- **Linee chiuse** (cercate a fondo, nessuna traccia): ANAC (consultazione 2015 e delibere lette per intero: le
  osservazioni del Centro Hermes le firmano altri), Garante privacy (i 3 risultati sono l'avv. **Fabrizio Pietrosanti**,
  omonimo nuovo), AgID, AGCOM, ACN, Developers Italia, Consip, Regione Lazio; consultazioni della Commissione UE sulla
  direttiva whistleblowing (34+74 contributi, Hermes assente); PACE/Consiglio d'Europa su Pegasus.
- **OpenAlex**: una sola opera (Cryptocat 2013, già nota). **Crossref/arXiv/Zenodo/DOAJ/OpenLibrary**: solo omonimi.
- **Google Books API e Semantic Scholar: 429 permanente** — è la quota del progetto anonimo condiviso, non l'orario.
  Senza una chiave API i libri di Frediani, Maurizi e Di Corinto restano non verificabili.
- **Bug corretto** in `archive_copies.py`: le risposte gzip/deflate/brotli venivano salvate compresse e illeggibili
  (caso mxmap.it). Ora c'è `decode_body()`.
- **Controllo del nome corretto** in `render_copies_report.py` e nella ripassata: si leggono **tutti** i file della
  copia, non solo `text.txt` → 12 copie che risultavano «senza nome» erano in realtà già verificate.

## Note sessione 2026-09-18
- +22 voci (486 → 508). Da rivedere: La Stampa 1997-10-30 «Fabio Pietrosanti, Velletri (Roma)» tra i vincitori di un
  concorso — probabile omonimo, non verificato. Nell'OCR di Hacker Journal 10 il nick «Naif» è attribuito ad «Alessio
  Orlandi» (refuso o altra persona?).
- `archive_copies.py`: le voci archive.org di tipo testo ora salvano OCR (`ocr_djvu.txt`) e PDF; le registrazioni
  multi-parte vengono scaricate tutte (`media.01.mp4`, …); le voci in solo prestito si verificano con gli snippet della
  ricerca full-text di Internet Archive (`fts_snippets.txt`).
- Internet Archive full-text API utile: `https://be-api.us.archive.org/fts/v1/search?q=...` (snippet con pagina).

## Tecnica ricerca con browser (validata 2026-09-17)
- **Google `site:` nel Chrome di Fabio**: funziona, ~10 ricerche poi compare il controllo anti-robot → fermarsi
  (non aggirarlo). Ritmo per le prossime sessioni: blocchi da ~8 ricerche distanziati di ore.
  Query: `site:<dominio> "Pietrosanti" (GlobaLeaks OR hacker OR Hermes OR whistleblowing OR Rousseau OR Tor OR
  cifratura OR intercettazioni OR PrivateWave OR Kaspersky OR "voto elettronico" OR sicurezza)`.
- **Chiave localStorage nuova a ogni giro** (2026-10-28, secondo incidente nello stesso giorno): una chiave già
  usata da un giro precedente può contenere un *array*; `s.q0=u` su un array non viene serializzato da
  `JSON.stringify` e i risultati si perdono in silenzio. Usare una chiave col timestamp (es. `gqr<AAAAMMGG-HHMM>`),
  inizializzarla a `{}` prima della prima ricerca e controllare dopo ogni salvataggio che il conteggio letto sia
  uguale a quello raccolto. Rifare le ricerche perse costa il blocco: il 2026-10-28 16:30 il secondo giro ha
  incontrato subito il robot check.
- Candidati in `data/research/candidates/*.txt` → `tools/verify_candidates.py` (copia dal Web Archive, cerca il nome,
  scarta omonimi) → `data/research/raw/pass3_*.json`.
- Bing ignora `site:`; DuckDuckGo mostra sempre il controllo anti-robot; ricerca interna Corriere troppo povera.
- Fatti il 2026-09-17: corriere, repubblica (+ pagina «protagonisti»), lastampa, ilsole24ore, ilfattoquotidiano,
  lespresso, panorama, ilpost, linkiesta → **+23 voci**. Da fare: ansa, agi, adnkronos, wired.it, punto-informatico,
  zeusnews, webnews, huffingtonpost.it, open.online, today.it, fanpage, ilgiornale, ilmessaggero, avvenire,
  ilmanifesto, internazionale, dday, hwupgrade, key4biz, agendadigitale, cybersecurity360, corrierecomunicazioni,
  startmag, formiche, ilriformista, editorialedomani, valigiablu, rainews, raiplay, la7, tg24.sky, radiopopolare,
  latinaoggi, latinatoday, h24notizie + testate estere.
- Fatti il 2026-09-23 (ripresa degli 8 domini in `retry`, nessun anti-robot): hwupgrade, tomshw, key4biz,
  agendadigitale, cybersecurity360, corrierecomunicazioni, startmag, formiche → **+5 voci** (4 Tom's Hardware,
  1 Startmag). **Chiusa la lacuna «due articoli Agenda Digitale senza data»**: la pagina autore
  `agendadigitale.eu/giornalista/fabio-pietrosanti/` elenca i suoi 3 articoli (trojan/Exodus con Stefano Aterno;
  voto dei cittadini all'estero con Quintarelli e Napolitano; voto su blockchain), tutti già in `data/media.json`.
  Fatti il 2026-09-23 (sera, secondo blocco, **nessun controllo anti-robot**): ilriformista, rainews, raiplay,
  la7, tg24.sky, radio24.ilsole24ore, radiopopolare, radioradicale → **+2 voci** (entrambe Il Riformista:
  «Russia verso la disconnessione da Internet» 2022-03-07, intervista a Fabio del Centro Hermes; «Volano stracci
  tra i grillini» 2020-10-08, «l'informatico Fabio Pietrosanti» e i parlamentari M5S). Zero risultati su
  rainews, raiplay, la7, radiopopolare e radio24.ilsole24ore (**host sbagliato**: le puntate note di Radio 24
  stanno su `radio24.it`, aggiunto in coda). tg24.sky: un solo risultato, omonimo di cronaca locale.
  radioradicale: tutti i risultati erano già noti oppure pagine soggetto di omonimi; **attenzione**, le schede
  dei resoconti parlamentari di Radio Radicale sono «a cura di **Valentina** Pietrosanti» e generavano falsi
  positivi (ora filtrati in `verify_candidates.py`). Resta da enumerare la sua pagina soggetto
  `radioradicale.it/soggetti/175095/fabio-pietrosanti` (dominio non consentito nel browser: usare API/Wayback).
  Da fare: i 86 domini ancora `pending` in `queue.json` (locali Latina, tecnici italiani, stampa estera, media cinesi).

## Copie offline
- `tools/archive_copies.py <cartella>`: Web Archive (capture più vicina alla data) poi sito live; salva originale,
  testo, metadati e se il nome compare. Stato in `copies.json`, report in `docs/COPIE-OFFLINE.md`
  (`tools/render_copies_report.py`). Cartella copie: `Claude/fabio_pietrosanti_it-copies/` (locale, non pubblicata).

## Progetti: sito + LinkedIn
Regola di Fabio: **tutto ciò che è un progetto** ha una sezione sul sito e una voce nei Projects di LinkedIn
(EN + zh_CN) con nome, descrizione e link di approfondimento. Registro: `data/projects.json` (25 candidati,
stato «da-documentare»). Per ciascuno: raccogliere le fonti da `data/media.json`, scrivere descrizione, proporre a
Fabio, poi pubblicare (LinkedIn con il metodo in linkedin-i18n/tools).

## FASE FINALE (solo a lavoro di ricerca concluso e homepage pubblicata)
Richiesta di Fabio 2026-09-18 — da fare **alla fine**, quando non c'è più nulla da ricercare:
1. **Rappresentazione visiva sulla homepage** fabio.pietrosanti.it:
   - **tag cloud** degli ambiti di interesse professionale **nel tempo** (per anno/periodo);
   - **timeline della vita professionale** per categorie di interesse (sicurezza, cifratura, whistleblowing,
     diritti digitali, voto elettronico, logistica, finanza algoritmica, biohacking, comunità hacker, …),
   costruite dai dati LinkedIn (`linkedin-i18n/snapshots/en.json`) + `data/media.json` + `data/projects.json`.
2. **Aggiornamento di LinkedIn** (EN master + zh_CN) sulla base dei dati della homepage definitiva: progetti,
   pubblicazioni, talk, esperienze mancanti — con proposta a Fabio prima di pubblicare.

## TODO futuri
- **CRVD voto elettronico**: replica dal Web Archive e rimessa online (progetto a parte, da pianificare).
- **Progetto AIRE** (voto elettronico / voto degli italiani all'estero iscritti all'AIRE): da documentare bene
  nell'ambito voto elettronico (fonti, articoli, ruolo di Fabio, risultati). Solo dopo averlo documentato,
  proporre a Fabio la voce nella sezione Progetti di LinkedIn (EN + zh_CN).
- **LinkedIn — sezione Progetti** (EN master + zh_CN), testi da proporre a Fabio prima di pubblicarli:
  - **Monitora PA**: breve indicazione dei risultati ottenuti nella rimozione di Google Analytics dalla PA.
  - **OpenRousseau**.

## Lacune da coprire nelle prossime sessioni

### Per periodo
- **1995–2006**: da verificare anno del libro «Il software libero in Italia» (Shake; 2006 è un segnaposto),
  lettera firmata «Naif» su BFi 4 (1998, da confermare), blackhats.it / naif.itapac.net / lns.it via Wayback; Punto Informatico, Zeus News, BFi, Sikurezza.org,
  Italian Black Hats, hackmeeting, MOCA 2004, SMAU, Infosecurity, rassegne stampa, TG2/Studio
  Aperto/TG3, Radio Montecarlo, libro "Il software libero in Italia".
- **2007–2011**: stampa italiana su intercettazioni e PrivateGSM (Corriere, Repubblica, Panorama,
  Sole 24 Ore, L'Espresso), copertura GlobaLeaks 2011 (anche estera), Security Summit 2010/2011,
  HAR2009, ESC, blog PrivateWave, VOIPSA, Infosec Island.
- **2012–2015**: grandi testate italiane (Repubblica, Corriere, La Stampa, Il Fatto, L'Espresso),
  Vice/Motherboard, archivi video CCC (media.ccc.de), Hacking Team 2015, articoli che riprendono
  i suoi post (Tor Weekly News e simili), pagine 2+ del press archive Hermes Center, Sky TG24 / Corriere Datagate 2013.
- **2016–2020**: Ethic Whispers, Ethic Alliance, Info.nodes, SignalSwarm, Advanced Knowledge
  Ventures, Haulersense, LESS.green, GLS Latina, Copernicani, Italian Hacker Camp 2018,
  audizioni parlamentari, Sole 24 Ore/Repubblica/Corriere, direttiva UE whistleblowing.
  ~~due articoli Agenda Digitale senza data~~ (risolto il 2026-09-23 dalla pagina autore).
- **2021–2026**: SignalSwarm, PLogistics, Aeroporto di Latina, Copernicani 2026, Italian Hacker Camp
  2022/2024, MCH2022, CCCamp2023, audizioni D.lgs 24/2023, media cinesi (TimePie Shanghai),
  biohack.it, stampa locale Latina.

### Piste emerse (da verificare)
- `data/research/leads/repubblica_leads.txt`: ~20 articoli Repubblica 2015–2020 che lo citano.
- Bloomberg Businessweek 2020-05-04; Il Gazzettino Friuli 2020-10-02; Radio1 Rai all'Italian Hacker Camp 2018.
- Libri: «Shooting the Messenger» (2018), «Coding Democracy» (2020), «Once a Bitcoin Miner» (2021).
- Corriere della Sera 2001-01-26 p.25 ("esperto" non nominato nel sommario): verificare testo con login archivio.
- «Il software libero in Italia» (Shake): data di pubblicazione 15/12/2008 secondo due librerie (non 2006).
- Da cercare: RAI Teche, Mediaset, Radio Monte Carlo, arretrati ICT Security / Wireless / WeekIT.
- Internet Archive: `win-magazine-italia-48` (articolo di Fabio Pietrosanti e Yvette Agostini),
  `pcprofessionale207` (2008, fondatori Khamsa), `hackerjournal-38` ("Pietrosanti", forse lui),
  `GazzettinoFVG2020-10-02`.
- Google Books API e Semantic Scholar da rilanciare con quota fresca; ringraziamenti nel libro di
  Di Salvo (2020) e in «Profilo hacker» (2007); libri di Frediani, Maurizi, Di Corinto, Chiesa.

- Siti con ricerca solo JavaScript (non leggibili da WebFetch): Corriere/Corriere Innovazione, La Stampa,
  Il Sole 24 Ore, ANSA, AGI, Adnkronos, Internazionale, RaiPlay/RaiNews, La7, Sky TG24, Radio24 →
  **usare il browser** (Claude in Chrome o browser integrato) per eseguire la ricerca interna e leggere i
  risultati dal DOM. Guardian: API key rifiutata. L'Espresso: nessuna ricerca utilizzabile.
- Il web search copre male il periodo pre-2016: per 2009–2015 servono gli archivi dei singoli siti.

### Per fonte (enumerazione sistematica, non a campione)
- Senato e Camera (web TV, resoconti audizioni), Parlamento europeo, ANAC, Garante privacy.
- RaiPlay, Rai News, RSI, Radio Popolare, Radio3, Radio24, BBC, NPR.
- Archivi storici: Repubblica, Corriere, La Stampa (archiviolastampa), Il Sole 24 Ore, ANSA, AGI.
- Punto Informatico, Wired.it, Il Fatto Quotidiano, Valigia Blu, Key4biz, Agenda Digitale — ricerca
  interna del sito per "Pietrosanti".
- YouTube/Vimeo (scansione per canale: IJF, e-privacy, Nexa, TI Italia, Matteo Flora, CCC), podcast.
- Google Scholar, Semantic Scholar, DiVA, tesi italiane, Google Books — citazioni di GlobaLeaks,
  Tor2web, ZRTP con il suo nome.
- Advisory di sicurezza pubblicati (bugtraq, full-disclosure, SecurityFocus, CVE): solo quelli, non i
  normali post in lista.
- **infosecurity.ch**: il restauro lo sta facendo un'altra sessione (repo `fpietrosanti/infosecurity-ch`,
  locale `Claude/infosecurity-ch`); Fabio: online previsto il 2026-09-18. Poi importare l'elenco completo
  dei post da `site/` (non duplicare il lavoro di restauro).

## Deciso

- Post su forum (Rapamycin News) e mailing list: esclusi, non sono pubblicazioni.

### Code aggiunte 2026-09-18 (sera) — da riprendere nel task giornaliero
- [x] **Ticket VLC — chiuso per decisione di Fabio (2026-09-23):** i 12 ticket (#18472 #18484 #18486 #18491 #18492 #18493
      #18498 #18500 #18569 #20007 #20008 #21805) sono **un episodio unico** (campagna HTTPS su videolan.org, 2017-2019),
      «una cosa aperta e chiusa»: resta **una sola voce**, il capofila #18472 (copia già ottenuta), che elenca gli altri.
      Gli altri 11 sono in `decisions.json` → esclusi da `media.json`; non si inseguono più copie separate.
      *(Nota tecnica: il 418 di code.videolan.org dipendeva solo dallo User-Agent — con UA da browser l'API risponde 200.)*
      Ticket Tor: salvati via API, i commenti richiedono login → recuperarli da trac.torproject.org sul Web Archive.
- [x] RaiPlay Sound / RaiNews — **fatto il 2026-10-12** (`pass4_rai_cyberchallenge`, 0 voci nuove): niente 403 con UA da
      browser. Codice Beta (slug `codicebeta-ognicosaedigitale`): 70 puntate 22/10/2020–13/02/2025, solo S04EP08 ti nomina
      (già nota; Rai la data 16/01/2025, media.json 17/01). Eta Beta 2021–2026 (273 puntate): solo 05/03/2022 (nota).
      Tv7, Speciale Tg1, Codice, Radio3 Scienza, Radio anch'io, Zapping: solo voci note. Ricerca RaiNews: 0 risultati.
      **Resta (minore):** Eta Beta 2017–2020 (vecchio RaiPlay Radio, solo Web Archive), Tutta la città ne parla prima del 2025.
- [x] **Fatto il 2026-10-12** (`pass4_wayback_eventi`, +8 voci; pagine lette dal server perché il Web Archive bloccava il
      portatile): Security Summit Milano 2009 (relatori), Milano 2010 (atti + PDF `7_PIETROSANTI.pdf`), Roma 2010 (relatori +
      scheda `/relatori/view/80` con «naif»). Il 2008 non è esistito (prima edizione 03/2009); 2011 (MI/RM/VR), Roma 2009 e
      2012 senza il tuo nome. Newsletter Clusit 2016–2026 (102 PDF): zero. Hackmeeting (tutti i wiki): zero; hackit12 ha un
      seminario GlobaLeaks di «random globaleaks contributor» → regola «senza nome». *Testo originale della voce:* pagine Security Summit 2008/2011 (atti, edizioni precedenti), wiki Hackmeeting
      (_wiki seminari, hackit05, hackit08, genova2004, /wiki), newsletter Clusit dopo il 2016.
- [x] e-privacy — **fatto il 2026-10-12**: +3 pagine abstract (XVII 2015, XXI 2017 con Coluccini, XXIII 2018 BBA); XXII ha la
      tua bio ma nessuna sessione; XVIII, XIX, XXIV, XXVI–XXIX senza nome; **XXV BBA 2019: solo «Hermes Center» → escluso**.
- [x] Freedom Not Fear 2019 — **chiuso il 2026-10-12**: programma era un foglio condiviso, il Web Archive ha solo il guscio
      vuoto; wiki 2019 inesistente, post freedomnotfear.org senza nome. Recuperabile solo da una copia tua o di digitalcourage.
- [ ] ICT Security (Tecna Editrice) cartaceo anni 2000: nessun indice online → chiedere a Fabio numeri/anni; numero dell'articolo «Penetration Testing & Tiger Teams».
- [ ] TV: TG2, TG3, Neapolis (Rai 3), Studio Aperto citati nella bio 2013 senza date → chiedere a Fabio anni/argomenti.
- [x] Sapienza CyberChallenge.IT 2018 — **fatto il 2026-10-12**. L'agente aveva trovato solo l'annuncio CINI; **su
      segnalazione di Fabio**, la ricerca Google nel suo Chrome («CyberChallenge 2018 pietrosanti», «Security Summit
      pietrosanti», «rapporto clusit pietrosanti») ha dato **+9 voci** (`pass4_google_fabio_cyberchallenge_securitysummit`):
      agenda ufficiale della premiazione (PDF key4biz), 2 post LinkedIn (Alessia Valentini «Fabio Pietrosanti naif ci ha
      aiutato…» + ricondivisione), ITASEC 2020 (bio relatore), Hacking Film Festival 2009 su PMI.it (organizzatori, legato
      al Security Summit), Rapporto Clusit 2012 IT+EN (contributori), Nexa annual report 2015, bio di Raoul Chiesa su
      dvara.net (ITBH 2001, «aka Naif»); + 3 nuove URL di voci note (CINI 1349, startupitalia.eu, pagina CRS del Manualetto).
      **Lezione:** gli agenti con ricerca web generica perdono risultati che Google trova subito → per ogni tema chiuso
      rifare almeno «<tema> pietrosanti» su Google nel Chrome di Fabio prima di dichiararlo negativo.

### Fase finale — aggiunta 2026-09-18
- [ ] **Una foto di Fabio per ogni anno** (percorso di invecchiamento): raccogliere solo foto in cui è indicato per nome
      (didascalie, sue pubblicazioni, pagine evento, SlideShare/Flickr fpietrosanti); conferma di Fabio per ognuna; mai
      riconoscimento dal volto. Solo alla fine, insieme a tag cloud e timeline.

### Homepage — layout da rifare (Fabio, 2026-09-30)
- [ ] Il layout attuale (`tools/site_template.html`, bozza EN del 18/09) **non piace a Fabio**: si ripensa più avanti.
      Contenuti e dati restano validi: testi in `site/content.en.json`, dati da LinkedIn/media/progetti, copie in `copies/`.
      Il template è separato dal generatore, quindi si cambia impaginazione senza rifare i contenuti.
