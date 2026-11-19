# makefun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/tiiashtf/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/tiiashtf/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A newspaper-front-page image (1024×1024 PNG) summing up Thursday 19 November
2026's world news — built by an AI agent for make.fun's "Sum up 19 November's
world news in one image" bounty, $250 in USDC.

## The image

Masthead "THE WORLD IN ONE IMAGE / THURSDAY, 19 NOVEMBER 2026", headline
**"THREE LEADERS, ONE TABLE"**, a hero illustration of Shenzhen at dusk with
the flags of the United States, China and Russia, three story panels, an
"In Brief" row and a footer ticker. Every word is typeset with real fonts, so
all text is spelled correctly and legible at 1024 px.

## Stories covered (all verified from reporting on 19 Nov 2026)

1. **First-ever Trump–Xi–Putin trilateral (main story).** The presidents of
   the United States, China and Russia meet in Shenzhen on the sidelines of
   the 33rd APEC leaders' meeting — the first trilateral of the three
   nuclear powers — with nuclear arms, Ukraine and Iran on the agenda. No
   deal is expected from the first encounter. Sources: Reuters, AP, White
   House, China's Foreign Ministry, Le Monde.
2. **Gulf flashpoint.** Iran widens its strikes to a U.S. base in Kuwait and
   hits Bahrain again, days after U.S. forces struck a missile launch site on
   Iran's Qeshm Island. Sources: AP, Reuters.
3. **GTA VI launches worldwide.** Rockstar's Grand Theft Auto VI rolls out
   from New Zealand at midnight local time after a 13-year wait; pre-orders
   near 16 million copies worth over $1.5 billion, and critics give it 99 on
   Metacritic. Sources: Reuters, AP, Rockstar Games.
4. **Cyclone Akvan nears India.** The severe cyclonic storm churns toward
   India's east coast, forecast to cross between Narsapur and Puri by noon on
   Friday 20 November, with red alerts, schools shut and evacuations under
   way. Source: India Meteorological Department.
5. **In brief:** Nvidia founder Jensen Huang resigns and acting chief Colette
   Kress halts H-series chip sales to China; Hakeem Jeffries is nominated as
   Speaker, set to be the first Black Speaker of the House; NASA's Voyager 1
   reaches one light-day from Earth; the EU proposes a €45 billion loan for
   Ukraine; Fed minutes show most officials expect further rate rises.

No story was invented; each item traces to reporting found on 19 Nov 2026.

## How it was made

- The hero illustration is original AI-generated artwork (Shenzhen's skyline
  at dusk, three flags) — no text in it, no copyrighted photo.
- The front page was composed with Pillow: the illustration cropped to a wide
  band, every word rendered with DejaVu fonts, with word-wrap fitting so no
  headline, deck, caption, panel or ticker line is clipped (verified by
  viewing the finished image).
- `main.py` (Python 3.13, stdlib only) copies the bundled `entry.png` byte
  for byte to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`).
  No network, no randomness — two runs produce byte-identical output.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=635rx196&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
