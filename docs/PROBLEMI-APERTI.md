# Problemi aperti: ricerca e copie offline

Aggiornato il 2026-09-18. Da discutere con Fabio: dove siamo bloccati, perché, e cosa proponiamo.
Stato generale: **513 voci** trovate; copie processate per tutte quelle esistenti al 18/09 (dettaglio in `COPIE-OFFLINE.md`).

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

### B1. Non ottenute (5)
| Anno | Fonte | Motivo | Proposta |
|---|---|---|---|
| 2010 | PrivateWave press release EN (PDF) | 403 sul sito, mai archiviato dal Web Archive | Fabio ha i PDF originali di PrivateWave? |
| 2010 | PrivateWave press release ES (PDF) | idem | idem |
| 2010 | Radio Monte Carlo, audio intervista | 404, nessuna copia archiviata | Chiedere a RMC o cercare registrazioni personali |
| 2011 | Infosec Island, «ZRTP Voice Encryption is Finally a Standard» | sito chiuso, non archiviato | Cercare ripubblicazioni del testo (PrivateWave blog, mailing list) |
| 2026 | Zhihu (cinese) sul TimePie Forum | 403 anti-bot | Aprirlo nel Chrome di Fabio |

### B2. Video non scaricabile (1)
- YouTube `mAtBH2hkAcg` (2019): «video non disponibile». Pagina salvata. Proposta: cercare lo stesso intervento su altri canali o chiedere all'organizzatore.

### B3. Copie ottenute ma senza il tuo nome dentro (59) — da rivedere
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
