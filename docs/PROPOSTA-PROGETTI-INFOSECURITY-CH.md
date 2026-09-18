# infosecurity.ch — post che sono progetti di ricerca o scoperte

Analisi del dump del blog (77 post, 2007–2011 + 2017) nel repo `infosecurity-ch`, 2026-09-18. Proposta da
discutere con Fabio: cosa elevare a **progetto/ricerca** (sezione sul sito + eventuale voce LinkedIn Projects),
cosa tenere come **post** del blog, e come raggruppare.

## A. Candidati forti (ricerca/scoperta con esito verificabile)

### A1. Il caso SecurStar / PhoneCrypt — la falsa «ricerca indipendente» sulla cifratura voce (2010)
- Post: 2010-01-30 «About the SecurStar GmbH Phonecrypt voice encryption analysis…» (4.171 parole),
  2010-02-01 «SecurStar GmbH Phonecrypt answers…», «Dishonest security…», «Evidence that infosecurityguard.com/notrax
  is SecurStar GmbH Phonecrypt – A fake independent research on voice crypto», 2010-05-25 «Exploit code against
  SecurStar DriveCrypt published».
- Scoperta: il sito «indipendente» infosecurityguard.com che aveva «bocciato» 12 prodotti su 15 era riconducibile
  al produttore SecurStar. Prove tecniche pubblicate (analisi dei domini, dei server, dei testi).
- Esito: ripreso da The Register (2010-02-01) e CSO Online/Techworld; già elencato nel vecchio sito come ricerca.
- **Proposta:** progetto «Debunking di una falsa ricerca indipendente (SecurStar, 2010)».

### A2. Tor exit node a basso rischio legale: dall'esperimento (2011) alle modifiche a Tor (2017)
- Post: 2011-01-24 «My TOR exit node experience trying to filter out noisy traffic» (exit node
  `privacyresearch.infosecurity.ch` + Tor2web su `tor.infosecurity.ch`), 2017-06-10 «Low Liability – Reduced Abuses
  Tor Exit Nodes».
- Esito: ticket aperti al Tor Project; **OutboundExitAddress implementato** in Tor (da verificare versione/ticket);
  altre proposte (exit policy per ASN, …). Collegato a Tor2web e all'honeypot sugli hidden service del 2014.
- **Proposta:** progetto «Tor exit node a bassa responsabilità (2011–2017)», con i ticket Tor come fonti.

### A3. Analisi della sicurezza e della scelta delle curve ellittiche (2010)
- Post: 2010-09-26 «Not every elliptic curve is the same: trough on ECC security» (2.208 parole), presentato come
  «My own ECC curve security and selection analysis»: prodotti proprietari che usano curve e lunghezze arbitrarie.
- **Proposta:** ricerca (paper/nota tecnica) nella sezione Ricerca.

### A4. Onestà del mercato della cifratura voce: «snake oil» e concorsi di marketing (2009–2010)
- Post: 2009-11-25 «Gold-Lock Security Encryption Contest: be careful!», 2010-07-19 «Snake-oil security claims on
  crypto security product», 2010-04-20 «Encryption is not scrambling», 2010-10-21 «Eight Epic Failure of Regulating
  Cryptography».
- **Proposta:** unire ad A1 in un unico progetto «Trasparenza e snake oil nella cifratura voce (2009–2010)».

## B. Già progetti (da collegare come fonti)
- **PrivateGSM / PrivateWave**: 2010-10-19 PrivateGSM con ZRTP/SRTP-SDES; 2010-10-25 howto Asterisk 1.8 + PrivateGSM +
  snom; 2011-01-12 **ZORG** (implementazione ZRTP C++/Java open source); 2011-04-11 «RFC 6189: ZRTP is finally a
  standard!»; 2010-09-01 «Voice security protocol review» (slide).
- **Talk**: 2009-07-06 «Voice Security and Privacy slides» (Security Summit 2009); 2010-06-02 WHYMCA; 2010-08-26
  «Voice communication security workshop» (Università di Trento); 2010-08-15 CFP 27C3.

## C. Analisi/commenti con valore storico (post, non progetti)
- 2010-06-07 **«The (old) Crypto AG case and some thinking about it»**: nel 2010 ricostruiva il caso Crypto AG; nel
  2020 lo scandalo è riesploso (Washington Post/ZDF «Rubikon») e Valigia Blu lo ha intervistato: **collegare** i due.
- 2010-07-23 «GSM cracking in penetration test methodologies (OSSTMM)?»: proposta di includere il cracking GSM A5/1
  (Kraken) nelle metodologie di penetration test.
- 2010-07-07 «Blackberry Security and Encryption: Devil or Angel?» (1.704 parole); 2010-06-01 «iPhone PIN: useless
  encryption»; 2009-07-27 «Chinese espionage: the worst and more silent threat…» (1.169 parole);
  2009-07-21 «Switzerland start realtime internet interception»; 2009-07-21 «UAE government placing backdoors into
  Blackberry devices»; 2010-09-25 ESSOR (SDR europeo); 2011-01-23 TETRA hacking (OsmocomTETRA);
  2011-02-23 GSM cracking a Friburgo.

## D. Da verificare con Fabio
1. A1 + A4 insieme o separati?
2. A2: confermi che OutboundExitAddress è stato implementato grazie al tuo ticket? (cerco il ticket e la versione di Tor)
3. A3: c'era un documento/paper oltre al post?
4. C'erano altri blog/post (es. su PrivateWave blog, VOIPSA blog) da trattare allo stesso modo?

## Decisioni di Fabio (2026-09-18)
- Proposta approvata. SecurStar e snake oil = **due progetti distinti**. ECC = solo il post.
- OutboundExitAddress: Fabio non ricordava; **verificato**: ticket Tor #17975 aperto da «naif» il 2016-01-02, chiuso il
  2017-01-27 e implementato in **Tor 0.3.0** come `OutboundBindAddressExit` / `OutboundBindAddressOR` (ReleaseNotes:
  «Closes ticket 17975», codice di Michael Sonntag).
- Registrati in `data/projects.json`. Crypto AG 2010 da collegare a Valigia Blu 2020 nella pagina del sito.
