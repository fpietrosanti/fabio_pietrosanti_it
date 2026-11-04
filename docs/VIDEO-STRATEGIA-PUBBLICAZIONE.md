# Strategia di pubblicazione video — YouTube e Bilibili

Analisi completa sui 173 file video dell'archivio (= **119 registrazioni distinte per URL di
fonte**, 156 ore). Dati di base: `data/video_inventory.json`, `data/video_risk.json`,
`data/video_liveness.json`; tabella per registrazione: `docs/VIDEO-PUBBLICAZIONE.md`.

## Executive summary

I due vincoli non sono gli stessi sulle due piattaforme, e vanno nella direzione opposta.

| | vincolo che morde | vincolo che non morde |
|---|---|---|
| **YouTube** | diritti (Content ID) | censura: nessuna |
| **Bilibili** | censura (revisione umana 审核) | diritti: nessun Content ID |

Da qui discende tutto:

- Su **YouTube** possiamo caricare poco (17 registrazioni, 18,7 ore: le nostre e quelle a
  licenza libera) ma **qualunque** contenuto, incluso whistleblowing e sorveglianza.
- Su **Bilibili** potremmo tecnicamente caricare molto di più (55 registrazioni in più, 82 ore,
  perché non c'è Content ID) ma **solo** la parte non politicamente sensibile.
- L'intersezione «nostro **e** pubblicabile in Cina» è **12 registrazioni**.
- Le **88 registrazioni di terzi** non vanno ricaricate su YouTube: vanno **incorporate** nella
  pagina. Il player YouTube embed è la soluzione legalmente pulita e non costa nulla.
- **113 fonti su 118 sono vive.** Non c'è un'emergenza di conservazione.

## 1. YouTube

### 1a. Da caricare sul canale — 17 registrazioni, 18,7 ore

Sono le uniche su cui abbiamo un titolo per pubblicare. Due con licenza CC **verificata nei
metadati del file**, quindici da eventi del mondo libero dove la licenza libera è
**probabile ma da confermare evento per evento prima del caricamento**.

| Anno | Durata | Titolo | Diritti | Cina |
|---|---|---|---|---|
| 2009 | 56m | Voice security and privacy (e-privacy VIII) | IA / libera | medio |
| 2011 | 77m | GlobaLeaks Live Launch (endsummercamp) | libera da confermare | 🔴 critico |
| 2013 | 47m | Digital Whistleblowing with GlobaLeaks (OHM2013) | libera da confermare | 🔴 critico |
| 2016 | 5m | Robots txt abuses by government agencies (33C3) | **CC BY-SA 4.0 verificata** | alto |
| 2017 | 49m | Regulating Law Enforcement use of Trojans (SHA2017) | **CC verificata** | alto |
| 2018 | 25m | Public money, public code, the Italian way (FOSDEM) | CC BY FOSDEM | basso |
| 2018 | 28m | Big Brother Awards Italia 2018 (e-privacy) | libera da confermare | medio |
| 2021 | 59m | The first AGPL compliance case (FOSDEM 2021) | CC BY FOSDEM | basso |
| 2022 | 100m | Linux Day Bari — Privacy e sicurezza del dato | libera da confermare | medio |
| 2022 | 82m | Linux Day Bari — Tavola rotonda | libera da confermare | basso |
| 2022 | 188m | e-privacy XXX — «Sospendiamo la privacy» | libera da confermare | alto |
| 2025 | 48m | La vera storia di Cassandra Crossing | da confermare con M. Flora | medio |

(più i doppioni di FOSDEM 2018 e 2021 presenti in più copie: una sola versione va caricata.)

**Rischio Content ID su questo gruppo: basso.** Materiale originale, nessuna traccia audio
commerciale rilevata. L'unico punto d'attenzione sono eventuali musiche di sigla nei montaggi
degli eventi: si risolvono tagliando i primi secondi.

### 1b. Da incorporare, non caricare — 88 registrazioni di terzi

Radio Radicale (13+2), Ciao Internet / Matteo Flora (21), International Journalism Festival
(11), e decine di canali singoli. Questo materiale **è già pubblico sul canale di chi l'ha
registrato**. Ricaricarlo sul nostro canale significherebbe duplicare il canale altrui con il
loro materiale, competendo con il loro originale: è una rivendicazione Content ID che arriva, e
arriva a ragione.

La cosa giusta da fare è **incorporare il player nella pagina**. Il video parte dentro
fabio.pietrosanti.it, le visualizzazioni restano al titolare, nessuna autorizzazione serve —
l'embed è esattamente l'uso che YouTube concede a chi pubblica. Risultato per te identico:
«tutto online, ben linkato e navigabile dalla pagina».

### 1c. Da lasciare come link — 9 registrazioni di emittenti

Rai 1 (Tg1, Tv7, Speciale Tg1, Codice ×3), Sky TG24, Euronews, La Stampa. **Content ID: alto.**
Le emittenti hanno le loro impronte caricate: la rivendicazione è automatica e immediata.
Restano come link alla pagina dell'emittente, come adesso.

## 2. Mave.io / Jet-Stream — cosa risolvono davvero

Il fatto tecnico è corretto: sono hosting video europei (olandesi), senza Content ID, e
Jet-Stream fa della sovranità digitale un argomento di vendita — il che è coerente con quello
che racconti.

Ma **non risolvono un problema di diritti.** Spostare un servizio del Tg1 su un server
olandese elimina il rilevamento, non il diritto d'autore della Rai: se la Rai se ne accorge, la
richiesta di rimozione arriva lo stesso, e questa volta arriva a te e non a una piattaforma che
fa da cuscinetto. Dato che la tua posizione pubblica è sulla legalità e la trasparenza, è
esattamente il tipo di esposizione che non conviene.

**Dove invece servono:** come player sulla homepage per i **tuoi 17 video liberi**, se vuoi
l'archivio ospitato in Europa invece che su Google. Costo contenuto, coerente con il messaggio,
e nessuna questione di diritti perché il materiale è tuo. Questo sì, e lo consiglio come
secondo player accanto all'embed YouTube.

## 3. Bilibili

### 3a. Il punto dei diritti: niente Content ID

È corretto, e cambia i numeri. Senza rilevamento automatico, le registrazioni di terzi
tecnicamente **passerebbero**: sono **55 registrazioni in più, 82 ore**, quelle di terzi o di
emittenti con rischio Cina basso o medio.

Tre precisazioni prima di considerarlo fatto:

1. **Bilibili ha una regola esplicita per il ricaricato** (搬运 / 转载): il video va dichiarato
   come ripubblicazione con la fonte. È una strada legittima e molto usata — ma è una
   dichiarazione, non un permesso: il titolare può sempre chiedere la rimozione.
2. **Il materiale italiano di terzi non ha pubblico cinese.** Caricare 82 ore di convegni in
   italiano su Bilibili non produce visualizzazioni: produce un canale pieno di video a zero
   views, che è il peggior biglietto da visita possibile.
3. **La revisione umana è il vero filtro**, e non guarda i diritti: guarda il contenuto. Un
   video rifiutato non è neutro — resta nello storico dell'account.

Quindi: sì, tecnicamente si può. Ma la leva non vale la pena **salvo** per materiale che un
pubblico cinese guarderebbe davvero.

### 3b. Rischio censura — tutte le 119 registrazioni

| Livello | N. | Cosa contiene |
|---|---|---|
| 🔴 critico | 25 | whistleblowing, GlobaLeaks, anonimato, Tor, libertà di stampa, dissidenti |
| 🟠 alto | 27 | sorveglianza, trojan di Stato, diritti umani, giornalismo d'inchiesta, trasparenza |
| 🟡 medio | 34 | privacy, crittografia, GDPR, sovranità digitale, software libero |
| 🟢 basso | 33 | longevità, biohacking, tecnologia generale, logistica |

I 25 critici sono **da escludere senza discussione**: GlobaLeaks Live Launch, Digital
Whistleblowing, le conferenze sul whistleblowing anonimo, Tor e privacy. Non è una questione di
probabilità di rifiuto — è materiale che in quella giurisdizione definisce chi lo carica.

### 3c. Da caricare — 12 candidati

I nostri o liberi con rischio Cina basso o medio:

- Public money, public code (FOSDEM 2018) — 25m — **basso**
- AGPL compliance case (FOSDEM 2021) — 59m — **basso**
- Linux Day Bari, tavola rotonda — 82m — **basso**
- Linux Day Bari, privacy e sicurezza del dato — 100m — medio
- Voice security and privacy (e-privacy 2009) — 56m — medio
- Big Brother Awards Italia 2018 — 28m — medio
- e-privacy XXX seconda giornata — 188m — medio
- Cassandra Crossing con Matteo Flora — 48m — medio

In pratica: **il software libero e la sovranità digitale passano, la sorveglianza no.**

### 3d. La scoperta che vale più dell'analisi

**Su Bilibili ci sei già.** L'archivio contiene due video 2026 del canale **时光派官方**
(TimePie) che ti riprendono al Settimo Forum Internazionale sulla Longevità, presentato come
«Biohacker from Italy». Sono passati la revisione, sono online, nessun problema.

Questo conferma empiricamente la divisione: **in Cina passa il biohacking, non passa la
sorveglianza.** E dà una strada già aperta: non serve costruire una presenza da zero, c'è un
canale cinese consolidato che ti ha già pubblicato e che ha il pubblico giusto.

**La strada più sensata non è caricare 12 conferenze italiane sul software libero.** È partire
dal materiale longevità/biohacking — rischio basso, pubblico reale, precedente già passato — e
valutare il resto dopo, a canale avviato.

### 3e. Due questioni aperte

**Accesso.** Non ho trovato documentazione ufficiale aggiornata sui requisiti per creator
stranieri. Fonti terze di agosto 2026 dicono che la verifica d'identità per stranieri è stata
tolta; guide più vecchie parlano di passaporto obbligatorio. Va verificato nella pagina 实名认证
dell'app — non si può stabilire dall'esterno.

**Esposizione personale.** La verifica con nome reale lega il tuo nome a quello che carichi, in
quella giurisdizione, e a Shenzhen ci vai. Finché il canale è biohacking non c'è nulla di
delicato. Se ci metti privacy e sovranità digitale — i 12 candidati sono quasi tutti lì — è una
scelta che va fatta consapevolmente. **È tua, non tecnica.**

## 4. Sottotitoli

Pipeline già disponibile e a costo zero: Whisper per la trascrizione, Claude CLI sul server per
la traduzione (abbonamento, nessuna API), ffmpeg per i sottotitoli. Circa 25 ore di CPU per
tutte le 156 ore, molto meno per il sottoinsieme pubblicabile: **18,7 ore ≈ 3 ore di
elaborazione**, che è niente.

Sottotitoli sì, inglese e cinese. **Doppiaggio con voce sintetica cinese no**: su materiale di
conferenza dove parli tu, una voce clonata riduce la credibilità invece di aumentarla, e per
12 video non vale la complessità.

## 5. Navigabilità dalla homepage

Obiettivo: il video parte **dentro** la pagina, non in una finestra altrove.

1. Embed YouTube in loco per tutto ciò che è su YouTube — nostro o di terzi, l'embed è
   consentito in entrambi i casi.
2. Player europeo (Jet-Stream o Mave.io) per i 17 liberi, come copia sovrana dell'archivio.
3. Link diretto per le emittenti e per Radio Radicale, che non consentono embed.
4. Una pagina indice «Video» filtrabile per anno, tema e lingua.

Con questo l'archivio è navigabile al 100% senza ricaricare una sola registrazione di terzi.

## 6. Cosa resta da decidere

- Confermare la licenza evento per evento sui **15 «libera da confermare»** prima di caricare.
- Verificare i requisiti Bilibili per stranieri nell'app.
- Decidere se il canale Bilibili è **solo longevità** (consigliato) o anche sovranità digitale.
- Scegliere il player europeo: Jet-Stream è più coerente col messaggio, Mave.io più semplice.
