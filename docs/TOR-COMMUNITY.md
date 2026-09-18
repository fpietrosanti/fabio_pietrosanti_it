# Partecipazione alla Tor Community

Generato da `tools/tor_community.py` (archivi pubblici delle mailing list Tor + ticket GitLab/Trac aperti da «naif»).
I singoli post non entrano nell'elenco media: qui c'è il riepilogo della partecipazione.

- **Post in mailing list:** 366 (primo: (2011, 3), ultimo: (2019, 10))
- **Ticket aperti:** 28 (2012-05-28 → 2019-10-12)

## Proposta di presentazione (da approvare)
**Tor Project community contributor, 2011–2019** — 366 messaggi sulle mailing list (tor-talk 227, tor-dev 93,
tor-relays 31, tor-onions 7, tor-project 5, tor-reports 3), 28 feature request/bug report, di cui almeno due entrati in
Tor: **#13865** («-f -», torrc da standard input, Tor 0.2.6) e **#17975** (OutboundBindAddressExit/OR, Tor 0.3.0).
Temi: operazione di exit relay a bassa responsabilità, Tor2web, hidden service su larga scala (10.000 HS, chiavi via
control port), Tor come libreria/embedding in applicazioni (GlobaLeaks, APAF GSoC), usabilità di Tor Browser.
Periodo più intenso: 2011–2013 (Tor2web e GlobaLeaks). Livello di dettaglio sul sito: riepilogo + ticket linkati;
singoli post non elencati.

## Per anno

| Anno | tor-talk | tor-relays | tor-dev | tor-onions | tor-project | tor-reports | Ticket |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2011 | 55 | 14 | 7 |  |  |  |  |
| 2012 | 80 | 5 | 35 |  |  |  | 6 |
| 2013 | 31 | 1 | 23 |  |  | 3 | 2 |
| 2014 | 22 | 3 | 15 |  |  |  | 1 |
| 2015 | 13 |  | 10 |  |  |  | 6 |
| 2016 | 18 | 6 | 1 | 5 | 3 |  | 7 |
| 2017 | 6 | 1 | 1 | 1 | 1 |  | 3 |
| 2018 |  | 1 | 1 | 1 |  |  | 2 |
| 2019 | 2 |  |  |  | 1 |  | 1 |

## Ticket

- 2012-05-28 [tpo/core/tor#5976](https://gitlab.torproject.org/tpo/core/tor/-/work_items/5976) — Load Tor Hidden Service Key via Tor Control Protocol · milestone Tor: unspecified
- 2012-06-02 [tpo/core/tor#6031](https://gitlab.torproject.org/tpo/core/tor/-/work_items/6031) — Distinguish when a Tor HS is "not found" vs "not reachable" (exists / does not exists) · milestone Tor: 0.2.6.x-final
- 2012-07-01 [tpo/core/tor#6268](https://gitlab.torproject.org/tpo/core/tor/-/work_items/6268) — Implement user-defined SSL Ciphers and TLS version · milestone Tor: unspecified
- 2012-07-03 [tpo/core/tor#6289](https://gitlab.torproject.org/tpo/core/tor/-/work_items/6289) — Multiple Socks Server support in Tor Client · milestone Tor: unspecified
- 2012-07-03 [tpo/core/tor#6288](https://gitlab.torproject.org/tpo/core/tor/-/work_items/6288) — Aggressive reconnection attempt when using Tor Client with Socks · milestone Tor: unspecified
- 2012-07-30 [tpo/network-health/metrics/onionoo#6488](https://gitlab.torproject.org/tpo/network-health/metrics/onionoo/-/work_items/6488) — Integrate TorBEL's Exit node in Onionoo protocol
- 2013-08-12 [tpo/applications/tor-browser#9456](https://gitlab.torproject.org/tpo/applications/tor-browser/-/work_items/9456) — Reset file attribute information after usage
- 2013-09-06 [tpo/core/tor#9685](https://gitlab.torproject.org/tpo/core/tor/-/work_items/9685) — Improve Tor2web mode performance by having Tor2web client to be the RendezVous Point · milestone Tor: unspecified
- 2014-11-30 [tpo/core/tor#13865](https://gitlab.torproject.org/tpo/core/tor/-/work_items/13865) — Enable Tor to load Torrc from <stdin> removing the need to write it to filesystem · milestone Tor: 0.2.6.x-final
- 2015-02-14 [tpo/core/tor#14899](https://gitlab.torproject.org/tpo/core/tor/-/work_items/14899) — Enable Tor to work without using filesystem for cached files
- 2015-02-20 [tpo/network-health/metrics/onionoo#14974](https://gitlab.torproject.org/tpo/network-health/metrics/onionoo/-/work_items/14974) — Onionoo should output full tor-exit-address
- 2015-03-09 [tpo/core/tor#15199](https://gitlab.torproject.org/tpo/core/tor/-/work_items/15199) — Build, Release, Distribute a Tor2web enabled version of Tor · milestone Tor: unspecified
- 2015-03-13 [tpo/core/tor#15251](https://gitlab.torproject.org/tpo/core/tor/-/work_items/15251) — Make tor support starting with 10.000 Tor Hidden Service · milestone Tor: unspecified
- 2015-03-15 [tpo/core/tor#15271](https://gitlab.torproject.org/tpo/core/tor/-/work_items/15271) — Enable exposing a Tor HS without Location Anonymity (-3 hops) · milestone Tor: unspecified
- 2015-09-08 [tpo/core/tor#17019](https://gitlab.torproject.org/tpo/core/tor/-/work_items/17019) — Include Tor2web and Encrypted Services in default Tor build · milestone Tor: unspecified
- 2016-01-02 [tpo/core/tor#17975](https://gitlab.torproject.org/tpo/core/tor/-/work_items/17975) — Introduce OutboundExitAddress to enable exit-only traffic to go via a different IP address · milestone Tor: 0.3.0.x-final
- 2016-01-25 [tpo/core/tor#18142](https://gitlab.torproject.org/tpo/core/tor/-/work_items/18142) — Anti-Automated-Scanning: Support "marking" with iptables TCP connections differently "for each circuits"
- 2016-02-07 [tpo/applications/tor-browser#18269](https://gitlab.torproject.org/tpo/applications/tor-browser/-/work_items/18269) — Enable Tor Browser users to become "easy to be run" Tor Exit relay
- 2016-02-07 [tpo/core/tor#18268](https://gitlab.torproject.org/tpo/core/tor/-/work_items/18268) — Make Tor aware of the top-30 destinations of Tor Exit traffic · milestone Tor: unspecified
- 2016-02-07 [tpo/core/tor#18267](https://gitlab.torproject.org/tpo/core/tor/-/work_items/18267) — Enable Exit Policy by Autonomous System Numbers
- 2016-02-11 [tpo/core/tor#18300](https://gitlab.torproject.org/tpo/core/tor/-/work_items/18300) — Tor shall explicitly report of Nickname is wrong length or contain illegal character
- 2016-12-01 [tpo/network-health/metrics/relay-search#20846](https://gitlab.torproject.org/tpo/network-health/metrics/relay-search/-/work_items/20846) — Atlas report wrong geoip information (maybe outdated)
- 2017-07-04 [tpo/applications/tor-browser#22809](https://gitlab.torproject.org/tpo/applications/tor-browser/-/work_items/22809) — Tor Browser does not provide red security warning for downloading executable in HTTP
- 2017-08-22 [tpo/core/tor#23295](https://gitlab.torproject.org/tpo/core/tor/-/work_items/23295) — Detect AES-NI hw encryption also if no cpu flags for AES-NI is present · milestone Tor: unspecified
- 2017-10-30 [tpo/applications/tor-browser#24054](https://gitlab.torproject.org/tpo/applications/tor-browser/-/work_items/24054) — Prevent Tor Browser from being used as a Javascript Miner
- 2018-03-13 [tpo/tpa/team#40397](https://gitlab.torproject.org/tpo/tpa/team/-/work_items/40397) — Introduce TLS MITM Detection on Tor Project websites
- 2018-03-13 [tpo/web/tpo#133](https://gitlab.torproject.org/tpo/web/tpo/-/work_items/133) — Introduce TLS MITM Detection on Tor Project websites
- 2019-10-12 [tpo/core/tor#32048](https://gitlab.torproject.org/tpo/core/tor/-/work_items/32048) — Loading a high number of Onion V3 Descriptors trough Tor Control Port lead to sustained 100% CPU · milestone Tor: unspecified

## Discussioni principali (per numero di messaggi)

- tor-talk: How to make 100.000 bridge? (6)
- tor-talk: Automatic vulnerability scanning of Tor Network? (6)
- tor-talk: Making TOR exit-node IP address configurable (5)
- tor-relays: Network Scan through Tor Exit Node (Port 80) (5)
- tor-talk: Exit Traffic classification and discrimination (4)
- tor-talk: Does tor browser bundle can goes on Mac App Store? (4)
- tor-talk: [Bitcoin-development] Tor hidden service support (4)
- tor-talk: Tor as a sort of "library/dependancy" for third party software (4)
- tor-talk: Hijacking Advertising to give a Tor Exit node economic sustainability? (4)
- tor-relays: Sharing experience with Via Nano 1.6ghz with Padlock hw accel (4)
- tor-dev: Embedding tor in an application and using tor without opening a port (4)
- tor-talk: A possible way to make end-users to contribute to Tor exit traffic (3)
- tor-talk: Pissed off about Blacklists, and what to do? (3)
- tor-talk: tor2web - How can I get my hidden service indexed? (3)
- tor-talk: Unsigned Mac OS X binary for TorBrowser (3)
- tor-talk: Limiting number of outbound TCP connection from One Circuit (3)
- tor-talk: Data storage in cached-descriptors (3)
- tor-talk: Tor Browser Bundle: Usability Improvement Proposal (windows) (3)
- tor-relays: Filtering at Exit Node [was: Network Scan through Tor Exit Node (Port 80)] (3)
- tor-relays: first using bridge then become bridge (3)
- tor-dev: Making and distributing custom TBB with a new "home-page" (3)
- tor-dev: Using Tor as a library (3)
- tor-dev: [GSoC] APAF Report (3)
- tor-dev: Tor HS keys password protection against impersonation attacks? (3)
- tor-dev: TorHS related files re-organization ? (3)
- tor-dev: Tor for iOS via official channels (3)
- tor-dev: Windows Alternative of torsocks/tsocks ? (3)
- tor-talk: Is there a limit to how many .onion addresses I can generate/advertise/use for one hidden service? (2)
- tor-talk: On further minimizing harassment for Tor Exit Nodes (2)
- tor-talk: A multi-layer proof of work system to solve the Tor/CloudFlare problem? (2)
- tor-talk: "Tor Browsers" on SourceForge (2)
- tor-talk: Gmail is blocking sending email from smtp.gmail.com (2)
- tor-talk: Possible upcoming attempts to disable the Tor network (2)
- tor-talk: [IDEA] Google App Engine, Tor Hidden Service Viewer (2)
- tor-talk: Linux mailer "sendmail compatible" with socks support? (2)
- tor-talk: Fwd: SecureDrop, new whistleblower submission system (2)
- tor-talk: Tor Mail Gateway (2)
- tor-talk: Tor for upcoming FirefoxOS? (2)
- tor-talk: "Torifier" for Windows (2)
- tor-talk: TOR Fone - p2p secure and anonymous VoIP tool (2)
- tor-talk: Porn make the world more free: Tor Porn Bundle? (2)
- tor-talk: Tor on Raspberry Pi (2)
- tor-talk: howto: Raspberry Pi as transparent tor proxy (2)
- tor-talk: hidden services and stream isolation (file transfer over Tor HS speedup?) (2)
- tor-talk: Distribution of Linux static tor binary? (2)
- tor-talk: HTTPS to hidden service unecessary? (2)
- tor-talk: "*.onion" performance tru "onion.to" (2)
- tor-talk: Tor traffic statistics? (2)
- tor-talk: Bridge: Why not just stateless TCP socket proxy / forwarders? (2)
- tor-talk: TBB, iptables, and seperation of concerns (2)
- tor-talk: tor-exit running ntop (2)
- tor-talk: Implement JSONP interface for check.torproject.org (2)
- tor-talk: What happen if one create 2000 exit nodes for 6 hours? (2)
- tor-talk: Fwd: Tor Browser Bundle: PGP encryption built-in? (2)
- tor-talk: Ideas to securely implement PGP encryption/decryption (2)
- tor-talk: anonymous surveys via Tor? (2)
- tor-talk: built-in tor2web functionalities into TOR? (2)
- tor-relays: How to protect yourself from network scanning (2)
- tor-relays: Network Scan through Tor Exit Node (Port 80) - PORTSCAN (2)
- tor-dev: RFC: Ephemeral Hidden Services via the Control Port (2)
