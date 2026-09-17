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

## Copie offline
- `tools/archive_copies.py <cartella>`: Web Archive (capture più vicina alla data) poi sito live; salva originale,
  testo, metadati e se il nome compare. Stato in `copies.json`, report in `docs/COPIE-OFFLINE.md`
  (`tools/render_copies_report.py`). Cartella copie: `Claude/fabio_pietrosanti_it-copies/` (locale, non pubblicata).

## TODO futuri
- **CRVD voto elettronico**: replica dal Web Archive e rimessa online (progetto a parte, da pianificare).
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
  audizioni parlamentari, Sole 24 Ore/Repubblica/Corriere, direttiva UE whistleblowing,
  due articoli Agenda Digitale senza data (voto elettronico, voto estero).
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
