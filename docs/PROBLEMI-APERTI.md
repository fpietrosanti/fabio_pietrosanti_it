# Problemi aperti: ricerca e copie offline

Aggiornato il **2026-10-07**. Da discutere con Fabio: dove siamo bloccati, perché, e cosa proponiamo.
Stato generale: **923 voci** (809 verificate; il dettaglio che segue è del 28/09); **tutte** le copie processate — 617 con il nome verificato dentro la copia,
85 video/audio scaricati, il resto suddiviso per causa nelle tabelle B3-bis/B3-ter (dettaglio in `COPIE-OFFLINE.md`).

## A0-ter. Nuove domande (2026-10-07)
1. **Garante privacy di San Marino**: la pagina «Chi siamo» (`garanteprivacy.sm/…/chi-siamo.html`) elenca «Dott. Fabio
   Pietrosanti» nel comitato tecnico di esperti, senza data. Sei tu? Da quando? (Registrata come voce verificata per nome.)
2. **⚠️ Terzo caso di dati personali pubblicati**: easyteam.org (fornitore software per scuole) riproduce integralmente la
   PEC MonitoraPA del 06/11/2022 con luogo e data di nascita e codice fiscale. Copia solo nell'archivio privato, nel sito
   solo il titolo. Chiedere la rimozione, come per le due scuole?
3. **Codice Beta**: la pagina News di hackingbiology.com indica il **17/05/2025**, l'URL RaiPlay Sound è del 01/2025.
   Quale data è giusta (prima messa in onda o ripubblicazione)?
4. **Fund Longevity, Roma 08/04/2026**: eri nella lista ospiti; ti hanno ripreso nel livestream globale (segmento Roma
   17:23-17:25)? Ci sono altre riprese/articoli?
5. **Omonimo nuovo**: un Fabio Pietrosanti di Velletri (ciclismo, ASD Center Bike) compare su Latina Oggi e latinanews →
   escluso. Confermi che non sei tu?

## A0-bis. Risposte di Fabio del 2026-10-05 (applicate)
- **1** dati personali delle scuole: «va bene così» → nessuna richiesta di oscuramento, copie solo nell'archivio privato. Chiuso.
- **2** libri: fatta la **sezione «Books» del sito + tag `books`** (22 libri, `data/books.json`), sintesi in italiano in `docs/LIBRI.md`.
- **3** risposta «senza nome, non sono io» → **escluse 52 voci** (solo organizzazione/progetto e nome assente: EDRi, CCC, OHM2013, e-privacy, Copernicani, OpenRousseau/OSSCI senza nome, Apogeo, Sky TG24 2013, Askanews, SecurityWeek, clip Bilibili senza di te, pagina Linke, Bloomberg Law troncato…). Copie conservate nell'archivio privato. Restano 10 pagine senza nome nel testo ma verificate per altra via (repo GitHub con tuoi commit, indice LDR, tesi TorSNIP, Freedom Not Fear 2017, tuo blog). `media.json`: 945 → 893 voci.
- **4** PDF PrivateWave: non li hai → B1 chiusa come irrecuperabile.
- **5** Senato: col browser locale ho trovato il video WebTV del 14/05/2020 (14ª Commissione, ddl 1721) e trascritto il
  tratto di Hermes (2:16–2:34): **parlò Vincenzo Tiani** da Bruxelles, non tu → A0.8(d) e A0.9(b) chiuse
  (`fabio_pietrosanti_it-copies/leads/senato_2020-05-14/`).
- **6** «tutto pubblico»: schede progetto COVID con il Google Doc, i nomi dei giuristi e l'audit LAZIOdrCOVID; OSSCI era già
  nel sito, link Telegram compreso. **6(d)**: nemmeno Costabile ha il video CyberCoach → chiuso.
- **10(a)** «Eclecticism Now!» è tuo → i post sono verificati come tuoi. **10(b)** Chrome: l'estensione risulta collegata ma
  si disconnette appena navigo (05/10, come il 02/10) → Douyin/Weibo/WeChat ancora fermi. **10(c)** WeChat desktop: non
  posso controllare app desktop (solo i browser); TimePie avviserà quando la registrazione è online. **10(d)** ok.
- **12(a)** candidatura al Garante confermata, «con intento provocatorio e un po' troll» (nota sulle voci CorCom e Camera).
  **12(b)** «sì, sono io»: cena TimePie (Bilibili ×2, NetEase) e foto 05 del forum → verificate. **12(c)** Bundestag: non
  relatore. **12(d)** «Bloomberg»: l'unica intervista resta il pezzo di Josh Dean (2020, titolo cartaceo «The Road to
  Pyongyang Starts in Spain»); nuove: **Businessweek 25/04/2024** (Brent Crane, riprende la tua citazione) e la
  **ristampa SCMP 16/05/2020**.

## A0. Cose che servono da te (aggiornato 2026-09-30)

1. **⚠️ Dati personali pubblicati da una scuola.** L'Istituto Comprensivo «Luciano Manara» di Roma ha pubblicato il PDF
   della tua richiesta FOIA di MonitoraPA con **data e luogo di nascita, codice fiscale e indirizzo di residenza**
   (`istitutolucianomanara.edu.it/storico/wp-content/uploads/2023/07/FOIA-01.MIIC8C7002-1.pdf`). L'ho escluso dal repo
   pubblico applicando la decisione che avevi già preso per «1311 nuove PEC»; la copia resta solo nell'archivio privato.
   **Proposta: chiedere alla scuola la rimozione o l'oscuramento.** Probabilmente non è l'unica: la campagna MonitoraPA
   ha prodotto molte pubblicazioni di PA che ti nominano — vale la pena un giro sistematico `site:*.edu.it`.
   **Secondo caso (28/09): Liceo Statale «Maria Montessori» di Roma** — pubblica in Amministrazione Trasparente la tua
   istanza FOIA (prot. 4020 del 20/09/2022, file `FOIA-01.RMPQ010009_privacy.pdf`, piattaforma Spaggiari) con **luogo e
   data di nascita, codice fiscale e città di residenza**, nonostante il nome del file. Copia solo nell'archivio privato;
   nel sito compare solo il titolo della pagina. Stessa proposta: chiedere l'oscuramento.
2. ~~**Chiave API Google Books**~~ **non serve più (26/09)**: la ricerca interna `jscmd=SearchWithinVolume2` funziona
   senza chiave → 11 libri confermati. Resta utile solo la **chiave Semantic Scholar** (e CORE) per le citazioni accademiche.
3. **Le 29 pagine «solo organizzazione»** e le **11 «nome assente»** (tabella B3-bis): contesto o esclusione?
4. **PDF originali dei comunicati stampa PrivateWave** del 18/10/2010 (EN e ES): li hai?
5. **Senato**: senato.it è dietro un WAF e non è archiviato. Se hai un browser con sessione residenziale, la scheda
   leg18 `ProcANLscheda43472` direbbe chi rappresentò Hermes nell'audizione sulla direttiva copyright.

6. **Nuove (24/09).** (a) **Gruppo Telegram OSSCI** (privato, 230 membri): il link d'invito l'ho tenuto fuori dal repo
   pubblico — vuoi che l'osservatorio compaia nel sito, e con quale nome (OSSCI o OSPCI, come su GitHub)?
   (b) **Proposta COVID sui dati di cella** (Google Doc, marzo 2020): i nomi dei giuristi e commentatori sono nel
   documento pubblico; li citiamo nel sito o solo «con il contributo di vari esperti»? (c) I due **post Facebook** del
   16/03 e 09/04/2020 sulla geolocalizzazione: se me ne dai il testo (o un export Facebook), completo la storia.
   (d) **Intervista CyberCoach 2023**: account DeepCyber cancellato (confermato da Costabile). Costabile ha ancora il
   file originale in locale? Se sì, basta che te lo passi e lo archivio.
   (e) ~~verbalictscovid.infosecurity.ch~~: risposto — sito temporaneo, spento volutamente.

7. ~~**Nuove (25/09)**~~ — **risposte di Fabio (25/09)**: (a) contesto AIRE/OpenRousseau: le 10 pagine dei suoi
   progetti restano come contesto, le **12 pagine generiche sono escluse** (`decisions.json`); (b) Geo-AIRE su
   LinkedIn: sì, bozza da proporre; (c) tweet di Carlo Piana: **escluso**. Bilibili TimePie: Fabio **compare** nel
   clip da 32 s del forum biohacker (BV1u5YX6JECk → confermato), **non** nel riassunto del pomeriggio da 1'54" (BV1M7YX67EsD → escluso). *(Etichette corrette il 30/09: gli ID erano giusti, le descrizioni scambiate.)*
   Testo Geo-AIRE approvato → `linkedin-i18n/docs/PROGETTI-APPROVATI-2026-09.md`, da pubblicare.

8. **Nuove (26/09).** (a) **Sky TG24 02/07/2013 «Datagate, il mondo delle spie visto da dentro»**: ho scaricato e
   guardato il video intero (2'07"): l'unico intervistato è **Matteo Flora** («Fondatore di The Fool»), tu non ci sei.
   La voce veniva solo dalla pagina News/Press di Hermes. **Escludo** (regola: senza nome non sei tu) o ricordi un altro
   servizio Sky di quei giorni? (b) **OSCE 2016**: la tua biografia dice «top 10 di Reporter senza frontiere»; nella lista
   ufficiale RSF «100 eroi dell'informazione» 2014 per l'Italia ci sono solo Maniaci e Abbate — ricordi quale classifica
   RSF era? (c) **Camera, 23/11/2016**: la sottocommissione diritti umani sentì «Rappresentanti del Centro Hermes» sulla
   risoluzione Tidei (difensori dei diritti umani) — eri tu? (d) **Senato, maggio 2020** (direttiva copyright, AS 1721):
   chi rappresentò Hermes, e hai la memoria depositata? (e) La risposta dell'Agenzia delle Entrate al tuo FOIA 2019
   contiene la tua PEC personale: è nella sola copia privata, nel sito compare solo il titolo.

9. **Nuove (28/09).** (a) ~~Camera 23/11/2016~~ **risolta da me**: ho trascritto il video, per Hermes parlò
   **Emmanuele Somma** (non tu) → A0.8(c) chiusa. (b) **Senato 14/05/2020**: Hermes compare tra i 15 auditi in
   videoconferenza, senza nome e senza memoria depositata: eri tu? (A0.8(d) resta). (c) **Proposta: chiudere la voce
   «Google Books / Semantic Scholar»** del piano: tre passate di fila senza voci nuove; restano solo 7 libri non ricercabili
   online (Frediani, Di Corinto) che si verificano solo con la copia fisica — li hai in casa, o vuoi che restino aperti?

10. **Nuove (30/09).** (a) **Blog «Eclecticism Now!»** (`eclecticismnow.wordpress.com`, firmato solo «eclecticismnow»):
   è il tuo? Ospita i tuoi FOIA e tu rilanci i post; il post «Sim Toolkit uses notes for covid-19» (29/03/2020) non
   contiene il tuo nome, quindi per la regola resterebbe «nome assente». (b) **Chrome disconnesso da giorni**: anche la
   coda Google è ferma (10+ run saltati). Douyin, Weibo, canali video WeChat e Xiaohongshu per TimePie richiedono il
   browser loggato — riconnetti l'estensione quando puoi. (c) **TimePie**: chiedere la registrazione integrale del forum
   biohacker del 12/9 (su Bilibili ci sono solo clip; YouTube fermo a luglio). (d) Il profilo TimePie su NetEase del
   20/08 («逆龄16岁…») riporta dettagli personali (~70 integratori al giorno, 600 €/mese, GlycanAge −16 anni): va bene
   citarlo nel sito così, o solo titolo e link?

11. **Nuove (30/09, seconda esecuzione).** (a) **5 clip Bilibili di TimePie** (BV1e2YX6tEqz giro del forum, BV1X9YR68ETj
   cena «永生之夜», BV1YtY96bEhr e BV1w8YX6uENN giorno 1, BV1SJYe6AEXo chiusura): il tuo nome non è nei metadati; le ho messe
   come candidate non verificate — ricordi di essere in qualcuna (la cena del 12/9 soprattutto)? (b) **Tweet del 28/11/2019**
   «Yesterday in a commitee room at Bundestag»: che evento era (audizione, workshop)? Se me lo dici cerco il programma.
   (c) **Partito Pirata, 10/07/2020**: ti candidava con Marco Calamari al collegio del Garante Privacy — vuoi che compaia nel sito?

12. **Nuove (01-02/10).** (a) **Garante privacy, ottobre 2019**: CorCom del 31/10/2019 ti elenca tra i candidati al
   collegio («Pietrosanti Fabio», voce a sé: l'esclusione del 23/09 era un mio errore di lettura, ora corretta). Confermi
   di aver presentato la candidatura? (b) **Cena TimePie del 12/9**: nella clip Bilibili BV1X9YR68ETj (0:32) e nel
   riepilogo NetEase/Bilibili (1:34) a tavola c'è un uomo con camicia di lino bianca e cordino rosso TimePie, di fronte a
   uno rosso di capelli in maglietta nera: sei tu? (fotogrammi nelle copie; ho annullato l'esclusione del NetEase).
   (c) **Bundestag 27/11/2019**: era l'audizione Linke su Assange/WikiLeaks; dal programma ufficiale non risulti tra i
   relatori — eri tra il pubblico (con Davide Dormino?) o sei intervenuto? (d) **Pyongyang/Griffith**: trovate 13 voci
   nuove (CoinDesk, 2600 «Off The Hook», MIT Technology Review, GQ 2022…). Ricordi altre interviste, TV o radio su quel
   tema, magari italiane? In Italia non ho trovato **nessun** articolo che ti nomini.

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

### B0-undecies. 2026-10-07
- Copie delle 14 voci nuove **tutte ottenute**: reel Facebook di Codice (27/06/2025, 14 s) scaricato con yt-dlp (solo
  locale); hackingbiology.com: la capture Wayback 02/2024 non conteneva il nome → salvate home, News e About dal live.
- Retry dei falliti: invariati (Radio Monte Carlo 2010, PrivateWave EN/ES, deck Foggia 410, 2 notizieoggi.com,
  coinage.it, CyberCoach solo pagina; 🟠 Sogou anti-bot).

### B0-decies. 2026-10-06
- **Risolti:** techsupportforum.com (ripresa Techworld 01/02/2010, «Fabio Pietrosanti, founder and CTO of … Khamsa»):
  curl riceveva solo una shell JavaScript; letta nel browser integrato dell'app (nessun CAPTCHA) e salvato il corpo del
  post → ottenuta. I 3 MP3 Radio 24 (mirror) sono identici byte per byte alle puntate principali, già confermate dalla
  trascrizione → ottenuti. arXiv 1306.5156 (pagina abstract) → ottenuta: il nome è nel PDF (p.6), già in archivio.
  4 clip Bilibili TimePie senza di te e la maschera dell'archivio Corriere 2001 → chiuse per decisione (copie conservate).
- **Nuovo ❌:** deck Google Slides «Slide Foggia» (05/12/2019): cancellato (410), mai archiviato.
- **Restano ❌ (motivo invariato):** Radio Monte Carlo 2010 (404, mai archiviato), PrivateWave EN/ES (chiusi da Fabio),
  coinage.it e 2 notizieoggi.com (siti morti, nessuna capture), CyberCoach YouTube (solo pagina); 🟠 Sogou (anti-bot).
- `archive_copies.py`: aggiunte al controllo del nome le grafie cirillica e cinese (miglioria proposta il 05/10).
- **Risposte di Fabio (06/10):** (a) Foggia 05/12/2019 = lezione all'Università di Foggia su invito di Stefano Aterno →
  confermata, voce «talk»; il deck resta ❌ salvo ritrovarlo nel cestino Drive / Takeout. (b) Appello ANAC 2017: nessun
  passaggio TV/radio ricordato → pista chiusa.

### B0-nonies. 2026-10-05 (sera)
- Copie delle 11 voci nuove e delle loro 10 riprese **tutte ottenute** (7 tweet dal Web Archive, ANAC PDF, The Next Web,
  CoinDesk it/es/fr/ru/uk). Le 4 versioni **ru/uk** risultavano «non confermate» perché il controllo cerca il nome solo
  in alfabeto latino: verificate a mano («Фабио Пьетросанти», «Фабіо П’єтросанті») → ottenute. *Miglioria possibile:*
  aggiungere le grafie cirillica e cinese del nome al controllo di `archive_copies.py`.
- `coinage.it` (ripresa italiana CoinDesk): sito morto, nessuna capture → resta ❌, ma è superata dalla traduzione
  italiana ufficiale di CoinDesk, ora in archivio.
- Retry dei falliti: nessun cambiamento (Radio Monte Carlo, PrivateWave EN/ES — chiusi come irrecuperabili da Fabio —,
  2 notizieoggi.com, CyberCoach solo pagina). Restano 8 «non confermate» (arXiv 2013, 3 MP3 Radio 24 già confermati
  dalla trascrizione, …) e 2 parziali (techsupportforum, Sogou).
- **Nuove domande per te:** (a) **«Slide Foggia»** — un tuo tweet cancellato del 05/12/2019 parla di slide per Foggia:
  che evento era (convegno, università, ordine professionale)? (b) **Appello del Centro Hermes ad ANAC (24/07/2017)** sulla
  gara del whistleblowing: Cantone ti rispose per lettera il 21/09/2017 (ora in archivio); ricordi articoli o interviste
  su quella polemica? Li cerco nella prossima passata.

### B0-octies. 2026-10-04
- **Copie delle mirror (05/10, su tua indicazione: «serve sempre una copia offline, inclusi i tweet»)**: `archive_copies.py`
  copiava solo l'URL principale di ogni voce; le 41 URL in `mirrors` (riprese, risposte identiche accorpate) non avevano
  copia. Corretto: ogni mirror ha ora una copia propria (`mirror_of` in `copies.json`). Esito: **34 ottenute** (tutte le
  10 risposte-tweet «I went in North Korea with Virgil», Wikipedia GlobaLeaks IT/ZH/CA/PL, Repubblica, LWN, Yahoo Finance…),
  2 video Radio Radicale, 3 MP3 Radio 24 (audio solo in locale, nome nel parlato), 2 parziali (techsupportforum, Sogou),
  **3 non ottenute**: coinage.it (ripresa CoinDesk) e 2 riprese notizieoggi.com.
- Copie delle 19 voci nuove **tutte ottenute** (28 tweet dal Web Archive). La copia automatica di `camera.it/leg18/1372`
  aveva preso una capture del 20/06/2019, **precedente** alla tua candidatura → sostituita a mano con la 20200926: nome presente.
  Il **PDF del tuo curriculum** depositato alla Camera non è mai stato archiviato (CDX vuoto, live 404): ce l'hai tu?
- **Foto TimePie** (forum biohacker 12/9): 33 file nelle copie `523c49878113` e `ebce85101353` (cartelle `photos/`).
  Domanda: **la foto 05 sei tu?** (uomo in camicia bianca davanti alla slide «130+ biomarkers / N = 1»). Se hai il link
  `mp.weixin.qq.com` dell'articolo originale del 12/9, mandamelo: Sogou porta solo alla pagina anti-bot.
- **PrivateWave 2010 (B1)**: fatto il CDX rinviato il 02/10 su `privatewave.com/.it` e `privategsm.com/.it`: solo PDF
  del 2009 (brochure) e del 2014 (manuali, licenze); la pagina «Press» (Confluence, 27/09/2012) elenca solo derstandard.at
  e computerworld.ch. **Vicolo cieco confermato**: servono i PDF originali tuoi o dell'ex ufficio stampa (Theoria).
- Radio Monte Carlo: nessuna capture neanche per `radiomontecarlo.net/audio/1032426*`. ❌ invariate (4).
- Il Web Archive ha di nuovo segnalato l'IP come «bot» dopo poche richieste CDX parallele: limitarsi a richieste in serie.

### B0-septies. 2026-10-02
- Copie delle voci nuove (01-02/10) **tutte ottenute**: CorCom, baiyi.com, CoinDesk ×2, MIT TR, AMBCrypto ×2,
  CoinReaders ×2, GQ, Medium ethex-smm, pagina e **MP3** di 2600 «Off The Hook» (trascrizione locale in `transcript.txt`).
- **Video TimePie**: BV1X9YR68ETj e BV1Rwh76XEhj scaricati (solo in locale), fotogrammi della cena salvati
  (`fabio_*.jpg`); copia NetEase riaperta da «esclusa» a «ottenuta» (vedi A0.12(b)).
- **Programma Linke** del 27/11/2019 ottenuto dal Web Archive: nome assente → escluso.
- ❌ invariate (4): PrivateWave EN/ES, Radio Monte Carlo, notizieoggi.com. Il retry e le nuove piste (CDX su
  `privategsm.*`/`privatewave.*`) non si sono potuti fare: **Web Archive offline** (503) per gran parte della sessione.

### B0-sexies. 2026-09-30
- Copie delle 131 voci nuove (29-30/09): **tutte ottenute** (i 119 tweet dal Web Archive, TimePie Sohu/NetEase,
  secrss.com dal Web Archive). Due «non confermate» sciolte a mano: post «Commissione Voto Elettronico: Rigetto FOIA»
  → **nome presente** (allegato «Risposta … FOIA Fabio Petrosanti», con refuso del Ministero); post «Sim Toolkit» →
  **nome assente** (firma solo «eclecticismnow», vedi A0.10(a)).
- Video NetEase VG6GUA7FN (riepilogo TimePie) → **escluso**: visto fotogramma per fotogramma, non compari. Bilibili
  BV1u5YX6JECk: aggiunti 3 fotogrammi di prova (slide BIOHACK.IT, primo piano) nella copia.
- **PrivateWave 2010, nuove piste (30/09 sera)**: il comunicato UK del 21/10/2010 è ripubblicato su **RealWire** (Web
  Archive 20101023) e **Comms Business** (05/11/2010, copia mabdev): testo integrale, ma **senza il tuo nome** → non
  sostituiscono i PDF EN/ES firmati. Nel Web Archive di `privatewave.com` ci sono solo 5 PDF del 2014 (manuali e licenze).
- Etichette Bilibili corrette: il clip da 32 s del forum biohacker è **BV1u5YX6JECk** (compari, confermato), il riassunto
  del pomeriggio da 1'54" è **BV1M7YX67EsD** (escluso). Gli ID in archivio erano giusti, le descrizioni scambiate.
- ❌ non ottenute invariate (4): PrivateWave EN/ES, Radio Monte Carlo, notizieoggi.com (ripassate col retry: sempre
  404/403, nessuna capture). `computerworld.ch/aktuell/news/50435` resta mai archiviato.

### B0-quinquies. 2026-09-28
- **🗂️ «Scheda d'archivio» da 3 a 1** (resta solo la maschera del Corriere, già esclusa): le due scuole erano
  «Amministrazione Trasparente» in JavaScript, ma la ricerca interna `amministrazione-trasparente?cerca=Pietrosanti`
  restituisce il link diretto al documento Spaggiari → PDF + testo salvati, nome presente (Cornigliano: diniego del
  19/10/2022 «Al sig. Fabio Pietrosanti – MONITORA PA»; Montessori: la tua istanza, con dati personali, vedi A0.1).
- Recuperati anche i lavori del 27/09 rimasti senza commit: BugTraq ID «credit» (2000, «Fabio Pietrosanti (naif)»),
  blackhats.it contatti ed eventi SMAU 2001-2002, *This Machine Kills Secrets* pp. 318-19, Di Salvo 2024 (PDF UniBo).
- **📚 libri**: resta in attesa solo *Profilo hacker* ed. italiana — Google non la rende ricercabile, nessun ebook: la
  menzione è confermata dalla copia IA e dall'ed. inglese, manca solo il numero di pagina italiano (copia fisica).
- ❌ non ottenute invariate (4): PrivateWave EN/ES, Radio Monte Carlo, notizieoggi.com — vicoli ciechi già documentati.

### B0-quater. 2026-09-26
- **🔊 «solo video/audio» chiusi entrambi.** RaiNews/Tg1 05/01/2025: video scaricato e trascritto, **didascalia «Fabio
  Pietrosanti – Biohacker»** a 0:34 (fotogramma salvato) → confermato. Sky TG24 2013: video intero visto, unico
  intervistato Matteo Flora → **nome assente**, domanda in A0.8(a).
- **📚 «libri e paper» da 13 a 3**: Google Books *search-within* senza chiave ha dato pagina e frammento per 11 volumi
  (frammenti salvati in `google_books_snippets.txt` nelle copie). Restano: *Profilo hacker* ed. italiana (Google la
  dichiara non ricercabile; il nome è confermato nell'edizione inglese CRC p.xiii e nella copia IA), *This Machine Kills
  Secrets* (prestito IA), Di Salvo 2024 (già confermato dal PDF UniBo, da riallineare la copia).
- **Lettera MISE 2017**: URL 404 e senza capture propria, recuperata dal crawl locale di hermescenter.org
  (`hermescenter-restore/archive`) → ottenuta, firma presente.

### B0-bis. Task «download rinviati» — chiuso il 2026-09-23 (sera)
Il task creato il 22/09 per rifare i download pesanti «quando torna la linea veloce» **non serve più**:
le esecuzioni ordinarie di oggi avevano già tolto il marcatore `.low-bandwidth` e smaltito tutta la lista
«Download rinviati». Verificati uno per uno gli elementi che erano in coda: **TorSNIP** (PDF da 3,2 MB + testo
estratto, `2017/4ac2264ec0cf`), **Infosec Island** ZRTP (`2011/6eef821a1b3c`), **LDR/pluto.it** «Suggerimenti»
(`2001/581a4a985147`), **askanews 2017** sui captatori (`2017/6f076ea0271b`, copia completa ma senza il tuo nome),
**PDF PrivateWave** (confermato: mai archiviati). Ci sono tutti.

La linea stasera era comunque ancora lenta (0,37–1,0 MB/s su due test), quindi **non ho riscaricato nulla**:
le uniche due cose fatte sono a costo zero di banda — la riparazione della copia `mxmap.it` (i byte gzip erano
già sul disco, bastava decomprimerli) e la correzione di questa scheda, che dava per «non ottenuto» materiale
che in realtà era stato recuperato il 19/09.

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

### B0-ter. 2026-09-25
- **Hackmeeting 2000 risolto**: `www.hackmeeting.org` dà 404, ma l'host **senza www** (certificato non corrispondente)
  serve ancora la pagina originale: «proposed by [NaiF-RooT]» con mailto `naif@itapac.net` (`2000/b60fa4817340`).
- **IGI Global risolto**: l'ID Google Books salvato era un **refuso** (`KOREEAAQBAJ` → `KOREEAAAQBAJ`); il feed
  GData legacy restituisce il frammento con il riferimento «Pietrosanti, F., & Aterno, S. (2017)».
- **Radio 24**: trascrizione automatica locale (`tools/transcribe_media.py`, faster-whisper). La puntata del 02/03/2018
  conferma: «Ne voglio parlare con Fabio Pietrosanti che è presidente… del centro Hermes» (min 40:59). Scaricati gli
  MP3 mancanti (11/2018, 02/2019, 06/2022; URL `radio24_audio/<anno>/<aammgg>-2024.mp3`). **Tutte e 7 le voci Radio 24
  confermate** (5 MP3 trascritti, 2 pagine collegate alla puntata): i 🔊 «solo video/audio» scendono da 11 a **2**
  (Sky TG24 2013, RaiNews 2025 — prossimo passo: stessa trascrizione sui video locali).
- Nuova non ottenuta: `notizieoggi.com` (ripresa del Post 2022), sito giù e mai archiviato — irrilevante (copia del Post
  già presente).

### B1. Non ottenute (4)
| Anno | Fonte | Motivo | Proposta |
|---|---|---|---|
| ~~2000~~ | ~~Hackmeeting 2000 (Hackit00), «Letteratura Cyberpunk»~~ **risolto 25/09** | Pagina live sparita (404; in HTTPS il certificato di `hackmeeting.org` non corrisponde). Nel Web Archive c'è **una sola** capture (20260827004502, 1.310 byte) e la replay risponde **500** su ogni forma di URL | Guasto lato Internet Archive, non un vicolo cieco: **riprovare fra qualche giorno** |
| 2010 | PrivateWave press release EN (PDF) | 403 sul sito, mai archiviato dal Web Archive | Fabio ha i PDF originali di PrivateWave? |
| 2010 | PrivateWave press release ES (PDF) | idem | idem |
| 2010 | Radio Monte Carlo, audio intervista | 404, nessuna copia archiviata | Chiedere a RMC o cercare registrazioni personali |
| ~~2020~~ | ~~verbalictscovid.infosecurity.ch~~ | **Chiuso il 24/09**: sito temporaneo, spento da te volutamente; i dati restano nel repo `COVID-19-Verbali-CTS-OCR` | — |
| ~~2021~~ | ~~IGI Global, *Research Anthology on Business Aspects of Cybersecurity*~~ **risolto 25/09 (ID refuso)** | La scheda Google Books (`id=KOREEAAQBAJ`) risponde 404 | Serve la **chiave API Google Books** (vedi A0.2 / A4) |
| ~~2011~~ | ~~Infosec Island, «ZRTP Voice Encryption is Finally a Standard»~~ | **Risolto il 19/09**: recuperato dal Web Archive (capture 20111206), firma «Contributed By: Fabio Pietrosanti» presente nella copia `2011/6eef821a1b3c` | — |
| ~~2026~~ | ~~Zhihu sul TimePie Forum~~ | **Risolto 18/09**: letto nel Chrome di Fabio, salvato l’estratto con il suo intervento | Web Archive «save» ha risposto 500: riprovare |

### B2. Video non scaricabile (1)
- YouTube `mAtBH2hkAcg`: «video non disponibile». **Chiarito il 24/09**: è l'intervista del **17/01/2023** per il canale
  **CyberCoach di Gerardo Costabile** (non 2019). Il canale è stato rimosso da YouTube (404) e non esistono ricopie; la
  pagina `costabile.net/cibercoach/` conserva titolo, data e descrizione (ora voce verificata).
  **Confermato da te (24/09, via Costabile):** l'account Google di DeepCyber è stato cancellato e con esso il canale
  YouTube: il video non tornerà online. Unica via: una copia locale di Costabile o tua.

### B3-ter. 2026-09-24 — copie delle voci nuove e un bug corretto
- Le 40 voci nuove hanno tutte una copia. Da **solo organizzazione** passano a **32** (+3: pagina GitHub OSSCI, issue #3,
  repo GitLab `fnzv/ossci`); **nome assente** a **16** (+5 pagine che parlano dell'audit LAZIOdrCOVID senza nominarti:
  post di Rocca del 01/04/2020, gioxx.org, tweet @mobilesecurity_, Il Fatto 2021, il Giornale 2021).
- Recuperati a mano: export del Google Doc sui dati di cella, pagina CyberCoach live, lettera Nexa live (la capture del
  21/04/2020 precedeva la tua firma).
- **Bug corretto** in `archive_copies.py`: `--retry-failed` riportava a «non confermata» le 65 copie classificate a mano
  il 23/09. Ripristinate da git; ora un nuovo tentativo sostituisce la classificazione solo se trova il tuo nome.
- **Hackmeeting 2000**: ancora irrecuperabile, oggi il Web Archive rifiutava proprio le connessioni.

### B3-bis. Ripassata del 2026-09-23 — i 🟡 sono stati sciolti in categorie precise

Il problema «59 copie senza il nome» era in realtà cinque problemi diversi. Ora ognuno ha una causa e una proposta.

| Categoria | Quante | Cosa significa | Proposta |
|---|---:|---|---|
| ✅ **Risolte** | **12** | Il nome c'era, ma in un file diverso da quello che il controllo leggeva (OCR de La Stampa 2002, programmi e-privacy che accompagnano audio/video, snippet Google Books, commit e contributor GitHub, copia restaurata di infosecurity.ch) | Fatto: il controllo ora legge **tutti** i file della copia, non solo `text.txt` |
| 🏛️ **Solo organizzazione** | **29** | Copia completa, ma la pagina parla di Hermes Center / GlobaLeaks / WhistleblowingPA / Copernicani / MxMap **senza nominarti** (EDRi ×4, CCC wiki, OHM2013, e-privacy XXIV/XXV, whistleblowing.it, hermescenter.org FOIA, interoperable-europe…) | **Serve una tua decisione**: la tua regola dice «senza nome non sono io», ma qui si tratta di pagine dei *tuoi* progetti. Le tengo come *contesto del progetto* o le escludo? |
| 📚 **Libri e paper** | **13** | È solo la scheda del volume: il nome sta nel testo interno (Google Books, Springer, Elgar, archive.org in prestito) | Google Books API / PDF del capitolo — **serve una chiave API Google** (vedi A4) |
| 🔊 **Solo video/audio** | **11** | Il tuo intervento è nella registrazione, non nel testo della pagina (Sky TG24 2013, RaiNews 2025, Bilibili ×2, 5 puntate di Radio 24 + 2 podcast MP3) | Trascrizione automatica della registrazione |
| 🗂️ **Scheda d'archivio** | **3** | Maschera di ricerca dell'archivio Corriere e due pagine «Amministrazione Trasparente» di scuole che costruiscono l'elenco documenti in JavaScript (verificato anche nel browser) | Corriere: già escluso. Scuole: serve l'URL diretto del PDF dell'istanza |
| ~~🧩 **Bug di copia**~~ | ~~1~~ | ~~`mxmap.it` salvato compresso e illeggibile (gzip/brotli non decodificato)~~ | **Risolto il 23/09**: i byte erano integri, bastava decomprimerli in locale (nessun nuovo download). La pagina è leggibile ma non ti nomina → spostata in «solo organizzazione» |
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
