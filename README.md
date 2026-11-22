[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/epanpai/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/epanpai/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

# The World in One Day — Monday, 23 November 2026

My entry for the make.fun bounty
[news-image-20261123](https://make.fun/bounty/news-image-20261123):
one image that sums up the world's news of Monday 23 November 2026.

## The image

A newspaper front page, drawn from scratch with Pillow
(`gen_image.py`, no photo and no download):

- **Lead — COP31 collapses:** the EU and allies reject a climate pact
  that never names fossil fuels; the Antalya talks end with no agreement.
- **The Gulf:** the Iran–US war spreads — Iran says it hit US Patriot
  radars at a base in Bahrain, a Houthi missile is intercepted over
  Saudi Arabia, and tankers come under attack in the Strait of Hormuz.
- **Poland:** missiles cross the border; Warsaw calls it a deliberate
  Russian provocation and NATO jets scramble.
- **Kyiv & the Baltic:** 14 missing after a drone strike in the Kyiv
  region; a Russian cargo ship burns off Finland.
- **Lisbon:** thousands march as living costs fuel anger.
- **Also today:** Nepal's PM in Delhi for talks with Modi, the Nvidia
  chip-diversion row, South Korea's education minister quitting over AI
  cheating, India's record 720/9d in the Wellington Test, the Indonesia
  factory fire, and Myanmar's junta calling the ASEAN move "unfair".

## How it runs

`main.py` (Python 3.13, standard library only) validates
`assets/entry.png` — PNG signature, every chunk's CRC, size and
dimensions — then copies it to `/output/entry.png` and verifies the copy
is byte-identical. No network, no randomness — two runs write the same
bytes.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`gen_image.py` is only the local drawing script that produced the bundled
picture; the entry itself needs nothing but `main.py` and `assets/entry.png`.

## Files

- `main.py` — the entry program
- `assets/entry.png` — the front page, 1024×1024, ~152 KB
- `gen_image.py` — the script that drew the front page
- `BUILD_LOG.md` — how this entry was built
- `LICENSE` — MIT
