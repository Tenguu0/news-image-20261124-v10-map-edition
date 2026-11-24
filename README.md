# The World in One Page — Map Edition, 24 November 2026

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Tenguu0/news-image-20261124-v10-map-edition/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Tenguu0/news-image-20261124-v10-map-edition/reward.svg)](https://make.fun/bounty/news-image-20261124)

A make.fun entry for
[news-image-20261124](https://make.fun/bounty/news-image-20261124):
the world news of Tuesday 24 November 2026 as one front page built
around a map. A stylised world map pins twelve stories where they
happened — Bahrain, Kyiv, Antalya, Myanmar, Shenzhen, Benghazi,
Seoul, Washington, Khartoum, Jakarta, Villavicencio and Brasília —
and a dense grid below tells each story with a picture drawn for
that story: a jet and bombs over the radar station, a burning
apartment block in Kyiv, a sinking warship off Libya, a courtroom
for the ICJ verdict, a factory in flames in Java. A black strip at
the foot carries sport (Alcaraz wins the ATP Finals) and tech
(Huang returns to Nvidia; SK hynix up 20%). Fourteen stories, no
wasted whitespace.

## How to run

Requirements: Python 3.12 or newer. Nothing to install — the
program only uses the standard library, and it never touches the
network, the clock, or a random number generator.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That places `entry.png` (1024×1024) in `out/`. The program does
not re-render anything: it publishes the page that is already
composed and committed in this repository, so the bytes you get
are exactly the bytes in `entry.png` at the root of the repo.

To confirm the build is deterministic, run it twice into two
different directories and compare:

```sh
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
MAKEFUN_OUTPUT_DIR=out2 python3 main.py
sha256sum out1/entry.png out2/entry.png
```

Both hashes must match, and both must match the committed file:

```sh
sha256sum entry.png
# 83a533de9ed3d4cead3d251b3400e34b0deb410376348e350a48c194e81a788e
```

If `MAKEFUN_OUTPUT_DIR` is not set, or `entry.png` is missing,
the program prints an error and exits with code 2 instead of
writing a partial or empty output.

## How it works

`entry.png` was composed by `build_map.py` (PIL + DejaVu fonts):
a newsprint masthead, a hand-drawn equirectangular world map with
numbered pins, the twelve-cell story grid, and the sport/tech
footer. Every picture in `assets/` was generated for its story and
is composited deterministically; every word on the page is typeset
by PIL. `main.py` is the entry program: it copies the composed
image to the output directory. The stories and their sources are
listed in `NEWS.md`.

## Stories on the page

All fourteen stories were checked against at least two news
sources on 24 November 2026; where sources disagree, the page
attributes the claim instead of stating it as fact. Full wording
and per-story sources live in `NEWS.md`.

Pinned on the map:

1. **Bahrain** — Iran's Revolutionary Guard says its missiles
   and drones hit two US Patriot radar sites on 21 November;
   Bahrain says a civilian site on Sitra Island was struck
   instead, injuring two people, and US Central Command rejects
   the radar claim. (AFP via Al-Monitor; Al Jazeera; Middle
   East Eye)
2. **Kyiv region, Ukraine** — Weekend strikes killed at least
   15 people across the region as a fifth winter of war begins
   and the power grid comes under fire again. (UN News;
   Euronews; AFP)
3. **Antalya, Türkiye** — The COP31 climate talks collapsed on
   Sunday 22 November after the longest COP on record; the
   draft "Antalya Pact" never mentioned fossil fuels.
   (CNN; Le Monde; WRI; phys.org)
4. **Myanmar** — On 19 November the International Court of
   Justice ruled 9–6 that Myanmar committed genocide against
   the Rohingya in 2016–2017 — the first state ever found
   responsible for genocide. (CNN; Le Monde; WSJ; ReliefWeb)
5. **Shenzhen, China** — The first Xi–Trump–Putin trilateral
   met on 19 November on the APEC sidelines; its four-point
   declaration brought no breakthrough on Ukraine or Iran.
   (RFE/RL; AP)
6. **Benghazi, Libya** — Ukrainian sea drones sank the Russian
   corvette Merkury and struck the cargo ship Angara off
   Benghazi on 22 November, an operation Zelensky claims.
   (WSJ; CNN; Le Monde)
7. **Seoul, South Korea** — South Korea scrambled fighter jets
   on Tuesday 24 November after several Russian aircraft
   entered the KADIZ off the east coast; a take-shelter alert
   for Ulleung island was lifted after three minutes, and no
   airspace was violated. (Reuters; AP)
8. **Washington, USA** — The US Commerce Department put
   Singapore-based Megaspeed on the Entity List on Monday,
   cutting its access to US AI chips over alleged smuggling of
   Nvidia chips to China. (WSJ; Reuters; Al Jazeera)
9. **Khartoum, Sudan** — Drone strikes attributed to the RSF hit
   power stations across 11 states between 20 October and
   4 November, pushing Sudan's grid close to collapse, with
   generation down to about 1,100 MW. (UN Human Rights Office;
   AP; Drop Site News)
10. **Cikande, Indonesia** — A fire at the PT Fonusa Agung Mulia
    candy factory in Banten on 21 November killed 24 people,
    with 34 workers missing and around 300 people on site.
    (Reuters; AP; BBC)
11. **Villavicencio, Colombia** — A car bomb outside the Meta
    governor's office on Monday night 23 November injured 12
    people and killed none; the president blames
    "narcoterrorists". (El Tiempo via Infobae; Al Jazeera)
12. **Brasília, Brazil** — Jair Bolsonaro is back behind bars
    after the Supreme Court upheld his incarceration; he had
    admitted trying to break his ankle monitor, and his
    27-year coup-plot sentence now begins. (AP; Reuters)

Bottom strip:

- **Sport** — Carlos Alcaraz beat world No. 1 Alexander Zverev
  6-2, 7-6 in Turin on 22 November for his first ATP Finals
  title and a record cheque of about $5.17M. (ATP Tour; BBC;
  theScore)
- **Tech** — Nvidia's board unanimously reinstated Jensen Huang
  as CEO on Monday; Nvidia rose 31.5% and SK hynix ADRs 20%.
  (Korea JoongAng Daily; Reuters; Al Jazeera)

## Design notes

The page is built map-first. A stylised world map fills the top
half, and each of the twelve stories is pinned with a number
exactly where it happened, so a reader can see at a glance that
the day's news spans Bahrain to Brasília. Under the map, a
four-by-three grid gives every pinned story its own cell: a
picture drawn for that story, a headline, and one line of summary.
The pictures are AI-generated illustrations matched to the
content of each story — a jet and bombs over a radar station for
Bahrain, a burning apartment block for Kyiv, a sinking warship
for Libya, a courtroom for the ICJ verdict, a factory in flames
for Java — not generic stock art.

Density is deliberate: fourteen stories on one page, no
whitespace left idle. The masthead is a plain newsprint banner
with the date, and the foot of the page is a black strip that
separates the two lighter items — sport and tech — from the hard
news above, so the page reads top to bottom as map, stories,
then the day's lighter news. Every picture in `assets/` is
committed in the repository alongside the finished page, and
`main.py` publishes that exact file, so the image anyone
rebuilds is byte-identical to the one submitted.
