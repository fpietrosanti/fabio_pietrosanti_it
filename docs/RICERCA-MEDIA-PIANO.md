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
  (b) **«Slide Foggia»**: tweet recuperato dal Web Archive (05/12/2019 12:58, testo «Slide Foggia» + link a Google Slides)
  → verificato; il deck è **cancellato** (410) e mai archiviato. Ipotesi migliore, **non confermata**: lezione ospite nel
  corso di «Sicurezza informatica» di **Stefano Aterno** all'Università di Foggia (LM Scienze giuridiche della sicurezza,
  I semestre 2019; coautori su Agenda Digitale 04/2019). Nessuna pagina UniFG lo nomina → domanda per Fabio.
  (c) **FOIA (AG 267, 6-7/04/2016)**: raccolta completa delle memorie (146 pp., OCR) → Hermes non audito né memoria;
  **CAD (AG 307, 18/07/2016)**: video WebTV Camera trascritto per intero → nessun intervento Hermes; **relazione PEGA
  A9-0189/2023** letta (DOCX ufficiale): nessuna occorrenza (l'unico «Hermes» è Hermes Airports, Cipro).
  Omonima già nota (decisions.json): **Valentina Pietrosanti** (redazione Radio Radicale), falsi positivi su radioradicale.it.

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
- [ ] RaiPlay Sound / RaiNews: 403 a metà ricerca → rifare lista puntate Codice Beta e ricerca RaiNews «Pietrosanti».
- [ ] Web Archive (rifiutava connessioni): pagine Security Summit 2008/2011 (atti, edizioni precedenti), wiki Hackmeeting
      (_wiki seminari, hackit05, hackit08, genova2004, /wiki), newsletter Clusit dopo il 2016.
- [ ] e-privacy: cartelle materiali 2015+ chiuse (403) → cercare file per nome dalle pagine edizione; verificare XXV BBA (solo «Hermes Center»).
- [ ] Freedom Not Fear 2019: programma su calc.digitalcourage.de non recuperabile.
- [ ] ICT Security (Tecna Editrice) cartaceo anni 2000: nessun indice online → chiedere a Fabio numeri/anni; numero dell'articolo «Penetration Testing & Tiger Teams».
- [ ] TV: TG2, TG3, Neapolis (Rai 3), Studio Aperto citati nella bio 2013 senza date → chiedere a Fabio anni/argomenti.
- [ ] Sapienza CyberChallenge.IT 2018: cercare video/foto (YouTube CINI, Sapienza).

### Fase finale — aggiunta 2026-09-18
- [ ] **Una foto di Fabio per ogni anno** (percorso di invecchiamento): raccogliere solo foto in cui è indicato per nome
      (didascalie, sue pubblicazioni, pagine evento, SlideShare/Flickr fpietrosanti); conferma di Fabio per ognuna; mai
      riconoscimento dal volto. Solo alla fine, insieme a tag cloud e timeline.

### Homepage — layout da rifare (Fabio, 2026-09-30)
- [ ] Il layout attuale (`tools/site_template.html`, bozza EN del 18/09) **non piace a Fabio**: si ripensa più avanti.
      Contenuti e dati restano validi: testi in `site/content.en.json`, dati da LinkedIn/media/progetti, copie in `copies/`.
      Il template è separato dal generatore, quindi si cambia impaginazione senza rifare i contenuti.
