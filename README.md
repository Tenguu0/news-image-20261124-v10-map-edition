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

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

It writes `out/entry.png` (1024×1024 PNG). Python 3.12+, standard
library only — no network, no randomness, no clock, so every run
writes the same bytes.

## How it works

`entry.png` was composed by `build_map.py` (PIL + DejaVu fonts):
a newsprint masthead, a hand-drawn equirectangular world map with
numbered pins, the twelve-cell story grid, and the sport/tech
footer. Every picture in `assets/` was generated for its story and
is composited deterministically; every word on the page is typeset
by PIL. `main.py` is the entry program: it copies the composed
image to the output directory. The stories and their sources are
listed in `NEWS.md`.
