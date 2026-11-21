[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/c/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/lathixbt/news-image-20261120-entry-acct4/rank.svg)](https://make.fun/c/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/lathixbt/news-image-20261120-entry-acct4/reward.svg)](https://make.fun/c/news-image-20261120)

# The World in One Day — Friday 20 November 2026

A square 1:1 editorial news infographic poster: **33 stories, 7 regions, every one
dated Friday 20 November 2026**. "MAP DESK" edition — a pine-green field-desk
layout with the world map in the bottom-left corner, three illustrated hero
scenes on top, and the remaining stories filling the grid and the list to the
right of the map.

## What's on the poster

- **Header** — masthead, subtitle, and a 6-number stat strip (3 bridges hit in
  Kyiv · 300,000+ moved to shelters · −6.2% Taiwan · 100,000 youth visas a year
  · 2.3% Japan CPI · 118 runs by Glenn Phillips), plus region chips
  (Europe 8 · Asia 8 · Middle East 3 · Africa 5 · Americas 3 · Oceania 3 ·
  Global 3).
- **Heroes (3)** — Kyiv: Russian missiles hit three bridges (at least eight
  killed); Cyclone Akvan comes ashore near Gopalpur; the AI sell-off sinks
  Asia's markets (Taiwan −6.2%, worst week since 1991).
- **Grid (12)** — UK–EU reset deal, COP31's last scheduled day, the missile in
  Poland, Iraq, Italy's strike, Japan's inflation, Korea's impeachment move,
  Kenya's first oil well, Phillips 118, UK cyber, Lviv, Moscow/Estonia.
- **List (18)** — Berlin, Beijing, SoftBank −14.48%, Kospi −7.9% for the week,
  Ganjam's 209 mm, the ship fired on off Yemen, Abuja, Malawi, AfDB, Nasdaq
  futures, Nicholls 175*, ASX, the EU's "unacceptable" draft, ATP's $350m plan,
  Angola's De Beers stake, Trump's 90-minute press conference, Saudi's
  interception, Doerkson sworn in as BC premier.
- **Map** — "WHERE IT HAPPENED": a world map with 12 numbered pins, each
  positioned from its story's real coordinates (Kyiv 50.4°N 30.5°E, Gopalpur
  19.3°N 84.9°E, Taipei 25.0°N 121.5°E, and nine more verified the same way),
  with a numbered legend mapping every pin to its story.
- **DATE CHECK** — the four Thursday 19 November stories left out (World Court
  ruling on Myanmar, the Shenzhen three-leader declaration, Tonga's drought
  emergency, the migrant boat lost off Senegal) and the two things that had not
  yet happened (BepiColombo's Mercury orbit entry; any final COP31 text).

Every story happened, or was first reported, on Friday 20 November 2026.
Sources are named beside each story. All drawings are original vector art.

## Build

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py   # writes entry.png (1024×1024)
```

`main.py` uses only the Python standard library plus Pillow, reads no files
besides its own source and the system DejaVu fonts, and is fully deterministic:
re-running it reproduces `entry.png` byte-for-byte (same SHA-256).

## License

MIT — see [LICENSE](LICENSE).
