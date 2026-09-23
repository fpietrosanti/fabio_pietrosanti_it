# Problemi aperti: ricerca e copie offline

Aggiornato il **2026-09-23**. Da discutere con Fabio: dove siamo bloccati, perché, e cosa proponiamo.
Stato generale: **692 voci** (599 verificate); **tutte** le copie processate — 553 con il nome verificato dentro la copia,
82 video/audio scaricati, il resto suddiviso per causa nella tabella B3-bis (dettaglio in `COPIE-OFFLINE.md`).

## A0. Cose che servono da te (aggiornato 2026-09-23)

1. **⚠️ Dati personali pubblicati da una scuola.** L'Istituto Comprensivo «Luciano Manara» di Roma ha pubblicato il PDF
   della tua richiesta FOIA di MonitoraPA con **data e luogo di nascita, codice fiscale e indirizzo di residenza**
   (`istitutolucianomanara.edu.it/storico/wp-content/uploads/2023/07/FOIA-01.MIIC8C7002-1.pdf`). L'ho escluso dal repo
   pubblico applicando la decisione che avevi già preso per «1311 nuove PEC»; la copia resta solo nell'archivio privato.
   **Proposta: chiedere alla scuola la rimozione o l'oscuramento.** Probabilmente non è l'unica: la campagna MonitoraPA
   ha prodotto molte pubblicazioni di PA che ti nominano — vale la pena un giro sistematico `site:*.edu.it`.
2. **Chiave API Google Books** (gratuita, Google Cloud) e **chiave Semantic Scholar**: senza, 13 schede di libri e i
   volumi di Frediani, Maurizi e Di Corinto restano non verificabili. È il blocco più costoso rimasto.
3. **Le 28 pagine «solo organizzazione»** e le **11 «nome assente»** (tabella B3-bis): contesto o esclusione?
4. **PDF originali dei comunicati stampa PrivateWave** del 18/10/2010 (EN e ES): li hai?
5. **Senato**: senato.it è dietro un WAF e non è archiviato. Se hai un browser con sessione residenziale, la scheda
   leg18 `ProcANLscheda43472` direbbe chi rappresentò Hermes nell'audizione sulla direttiva copyright.

## A. Problemi nella RICERCA

| # | Problema | Effetto | Proposta |
|---|---|---|---|
| A1 | **Google mostra il controllo anti-robot dopo ~10 ricerche** nel Chrome di Fabio | Non si possono fare tutte le 129 testate in un colpo solo | Blocchi da 8 ricerche ogni 4 ore (task programmato). Alternativa più veloce: chiave API di Google Programmable Search (100 query/giorno gratis) o Brave Search API, creata da Fabio |
| A2 | **Il task delle 4 ore non trovava Chrome** la notte del 17/09 (poi collegato; alcune esecuzioni saltate con computer in sospensione) | Stanotte 0 ricerche; coda ferma finché non c'è una sessione manuale | Fabio: tenere Chrome aperto con l'estensione Claude collegata, e premere «Esegui ora» sul task una volta per approvare i tool. Oggi a mano: 8 ricerche, +6 voci |
| A3 | Il **web search degli agenti** copre male il periodo pre-2016 e ha 200 ricerche a sessione condivise | Anni 1995–2008 e 2023–2025 ancora scarsi | Si compensa con archivi dei singoli siti, Internet Archive full-text, e con Google site: per testata |
| A4 | Google Scholar, Google Books (interfaccia web), DuckDuckGo, HAL, theses.fr: **controlli anti-bot** | Citazioni accademiche e libri incompleti | Usiamo le API (Google Books API ha quota giornaliera: 429; Semantic Scholar: 429 senza chiave). Una **chiave API Semantic Scholar** (gratuita, da richiedere) sbloccherebbe molto |
| A5 | **Siti con ricerca solo JavaScript** (Corriere, Sole 24 Ore, ANSA, RAI, La7, Sky) | La ricerca interna del sito non è leggibile dagli agenti; quella del Corriere è comunque scarsa | Google site: nel Chrome di Fabio (funziona). RAI Teche e Mediaset restano da provare nel browser |
| A6 | **Omonimi** (Paolo Pietrosanti radicale, Matteo, Roberto, il giornalista calabrese Fabio Pietrosanti…) | Molti falsi candidati; oggi un falso positivo su Punto Informatico corretto | Filtro migliorato (ignora i footer «privacy policy»); casi dubbi elencati sotto per verifica di Fabio |
| A7 | **Archivi con login** (Corriere archivio storico, Repubblica «Rep» edicola, La Stampa archivio) | Articoli pre-2010 non leggibili | Se Fabio ha un abbonamento, lettura nel suo Chrome; altrimenti restano «da verificare» |

### Risposte di Fabio (2026-09-18) — applicate in `data/research/decisions.json`
- Paolo Pietrosanti non è Fabio. Regola: senza nome o nick «naif» non è lui.
- Corriere 2001-01-26: esperto senza nome → **escluso**. La Stampa 1997 (Velletri) → **escluso**.
- Hacker Journal n.10: «Alessio Orlandi (Naif)» = Nail, niente Mozzarella/Fastweb → **escluso**.
- BFi n.4 (1998), lettera «Naif» → **confermata**.
- Bloomberg Businessweek 2020 → **confermato e trovato**: «Wanna Do Business in Pyongyang? Call North Korea's Guy in
  Spain» (Josh Dean, 2020-05-01, conferenza blockchain di Pyongyang e programmatori nordcoreani), più The Walrus,
  Medium «No Future for the North Korea Fixer», Substack «Once a Bitcoin Miner».
- Radio Monte Carlo 2010: Fabio non ricorda → si continua a cercare nel Web Archive.

### Cosa serve da Fabio
- **Brave Search API**: creare la chiave su https://api-dashboard.search.brave.com/ (piano gratuito) e impostarla come
  variabile d'ambiente utente `BRAVE_API_KEY` (poi riavviare l'app Claude). Lo script `tools/brave_search.py` e il task
  delle 4 ore la usano da soli. Io non posso creare account.
- **Controlli anti-robot di Google**: non li posso risolvere io. Se compare, puoi risolverlo tu nella tab dedicata e il
  task riprende al giro successivo.
- **Computer acceso e app Claude aperta**: i task delle 02:52 e 06:52 UTC del 18/09 non sono partiti (probabile
  computer in sospensione). Chrome risulta collegato («Browser 1») il 18/09 alle 11:30.

## B. Problemi nelle COPIE OFFLINE

### B0. Chiuse il 2026-09-23
- **Ticket VLC (12)**: per tua decisione sono **un episodio unico** (campagna HTTPS su videolan.org, 2017-2019,
  «una cosa aperta e chiusa»). Resta la sola voce capofila **#18472**; gli altri 11 sono esclusi in `decisions.json`.
  *(Nota tecnica, per il futuro: il 418 di code.videolan.org dipendeva soltanto dallo User-Agent.)*
- **PrivateWave, comunicati stampa EN/ES del 18/10/2010**: la pagina stampa di PrivateWave è stata recuperata dal
  Web Archive (capture 2011-12-08) e **conferma i due PDF** con nome e dimensione (52,2 KB e 50,2 KB), ma i PDF non
  sono mai stati archiviati: nel Web Archive di `privatewave.com/media/` ci sono solo immagini. Resta la domanda: **hai
  tu i PDF originali di PrivateWave?**
- **Radio Monte Carlo**: confermato vicolo cieco — nel Web Archive non esiste **nessuna** capture di
  `radiomontecarlo.net` che contenga il tuo cognome.
- **derStandard.at 2010** (nuovo candidato emerso dalla pagina stampa PrivateWave): letto dalla capture 2013-09-04,
  parla di PrivateGSM e ZRTP ma **non ti nomina** → escluso per la tua regola. Resta `computerworld.ch/aktuell/news/50435`
  (mai archiviato, sito riorganizzato).

### B1. Non ottenute (5)
| Anno | Fonte | Motivo | Proposta |
|---|---|---|---|
| 2010 | PrivateWave press release EN (PDF) | 403 sul sito, mai archiviato dal Web Archive | Fabio ha i PDF originali di PrivateWave? |
| 2010 | PrivateWave press release ES (PDF) | idem | idem |
| 2010 | Radio Monte Carlo, audio intervista | 404, nessuna copia archiviata | Chiedere a RMC o cercare registrazioni personali |
| 2011 | Infosec Island, «ZRTP Voice Encryption is Finally a Standard» | sito chiuso, non archiviato | Cercare ripubblicazioni del testo (PrivateWave blog, mailing list) |
| ~~2026~~ | ~~Zhihu sul TimePie Forum~~ | **Risolto 18/09**: letto nel Chrome di Fabio, salvato l’estratto con il suo intervento | Web Archive «save» ha risposto 500: riprovare |

### B2. Video non scaricabile (1)
- YouTube `mAtBH2hkAcg` (2019): «video non disponibile». Pagina salvata. Proposta: cercare lo stesso intervento su altri canali o chiedere all'organizzatore.

### B3-bis. Ripassata del 2026-09-23 — i 🟡 sono stati sciolti in categorie precise

Il problema «59 copie senza il nome» era in realtà cinque problemi diversi. Ora ognuno ha una causa e una proposta.

| Categoria | Quante | Cosa significa | Proposta |
|---|---:|---|---|
| ✅ **Risolte** | **12** | Il nome c'era, ma in un file diverso da quello che il controllo leggeva (OCR de La Stampa 2002, programmi e-privacy che accompagnano audio/video, snippet Google Books, commit e contributor GitHub, copia restaurata di infosecurity.ch) | Fatto: il controllo ora legge **tutti** i file della copia, non solo `text.txt` |
| 🏛️ **Solo organizzazione** | **28** | Copia completa, ma la pagina parla di Hermes Center / GlobaLeaks / WhistleblowingPA / Copernicani **senza nominarti** (EDRi ×4, CCC wiki, OHM2013, e-privacy XXIV/XXV, whistleblowing.it, hermescenter.org FOIA, interoperable-europe…) | **Serve una tua decisione**: la tua regola dice «senza nome non sono io», ma qui si tratta di pagine dei *tuoi* progetti. Le tengo come *contesto del progetto* o le escludo? |
| 📚 **Libri e paper** | **13** | È solo la scheda del volume: il nome sta nel testo interno (Google Books, Springer, Elgar, archive.org in prestito) | Google Books API / PDF del capitolo — **serve una chiave API Google** (vedi A4) |
| 🔊 **Solo video/audio** | **11** | Il tuo intervento è nella registrazione, non nel testo della pagina (Sky TG24 2013, RaiNews 2025, Bilibili ×2, 5 puntate di Radio 24 + 2 podcast MP3) | Trascrizione automatica della registrazione |
| 🗂️ **Scheda d'archivio** | **3** | Maschera di ricerca dell'archivio Corriere e due pagine «Amministrazione Trasparente» di scuole che costruiscono l'elenco documenti in JavaScript (verificato anche nel browser) | Corriere: già escluso. Scuole: serve l'URL diretto del PDF dell'istanza |
| 🧩 **Bug di copia** | **1** | `mxmap.it` salvato compresso e illeggibile (gzip/brotli non decodificato) | Riscaricare con decodifica corretta |
| 🔎 **Nome davvero assente** | **11** | Copia completa e leggibile: la pagina **non** contiene né il nome né «naif» né un tuo progetto (Apogeo ×3, Corriere TV 2013, Askanews 2017, IJF 2017, StartupItalia 2018, CINI 2017, FNF 2017, Pluto LDR 2001, SecurityWeek 2019) | Per la tua regola andrebbero **escluse**: confermi? |

### B3. Copie ottenute ma senza il tuo nome dentro (59) — *superato dalla tabella qui sopra*
Cause principali: presentazioni SlideShare (il testo è nelle slide, non nella pagina), pagine di progetto (GitHub, CCC wiki)
dove compare solo «naif» in immagini o in pagine collegate, PDF non analizzati (Springer, Google Books, brevetti), pagine
d'archivio (Web Archive, archiviolastampa.it, archivio Corriere) che sono solo schede di ricerca.
Siti: SlideShare 5, Web Archive 4, EDRi 4, s0ftpj/BFi 3, Apogeonline 3, CCC events 3, GitHub 3, SecurityFocus 2,
archiviolastampa 2, winstonsmith 3, journalismfestival 2, Springer 2, monitora-pa 2, e altri 1 ciascuno.
**Proposta:** estrarre il testo dai PDF e dalle slide per confermare; per le schede d'archivio scaricare il PDF della
pagina di giornale; per il resto rilettura nel Chrome di Fabio.

### B4. Video solo in locale (69 voci, ~21,6 GB)
Non stanno su GitHub. **Da fare da Fabio:** caricarli su Google Drive; poi collego i link.

## C. Decisioni già prese (promemoria)
Copie di tutto a prescindere dalla licenza (archivio privato); materiale di terzi mai linkato dal sito; forum e mailing
list esclusi; progetti → sezione sito + LinkedIn Projects dopo approvazione.
