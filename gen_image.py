#!/usr/bin/env python3
"""Draw the front page for Monday 23 November 2026 (PIL, build-time only).

The entry itself is main.py + assets/entry.png; this script only produced
the bundled picture. Layout: masthead, COP31 lead with a cracked-globe
drawing, Hormuz war column, three middle panels (Poland, Kyiv/ship fire,
Lisbon), and an "also today" ticker.
"""
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 232)
INK = (20, 20, 20)
RED = (178, 34, 28)
BLUE = (28, 68, 128)
TEAL = (18, 110, 110)
ORANGE = (214, 96, 20)
GREY = (90, 88, 80)
LIGHT = (232, 226, 210)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_DIR / name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)      # noqa: E731
SERIF = lambda s: font("DejaVuSerif.ttf", s)            # noqa: E731
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)        # noqa: E731
SANS = lambda s: font("DejaVuSans.ttf", s)               # noqa: E731


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt, width: int) -> list[str]:
    out, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            line = trial
        else:
            if line:
                out.append(line)
            line = word
    if line:
        out.append(line)
    return out


def para(draw, x, y, text, fnt, width, leading, color=INK):
    for ln in wrap(draw, text, fnt, width):
        draw.text((x, y), ln, font=fnt, fill=color)
        y += leading
    return y


def rule(draw, x0, y, x1, width=2, color=INK):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)


def kicker(draw, x, y, text, color=RED):
    draw.text((x, y), text, font=SANS_B(17), fill=color)
    return y + 24


def headline(draw, x, y, text, size, width, color=INK):
    fnt = SERIF_B(size)
    for ln in wrap(draw, text, fnt, width):
        draw.text((x, y), ln, font=fnt, fill=color)
        y += size + 6
    return y


def main() -> None:
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=4)

    # ---- Masthead -------------------------------------------------------
    d.text((512, 34), "THE WORLD IN ONE DAY", font=SERIF_B(58),
           fill=INK, anchor="ma")
    rule(d, 28, 108, 996, 3)
    d.text((512, 118), "MONDAY, 23 NOVEMBER 2026  •  THE DAY IN ONE PICTURE",
           font=SANS_B(20), fill=INK, anchor="ma")
    rule(d, 28, 152, 996, 2)

    # ---- Lead: COP31 (left, wide) --------------------------------------
    lx, lw = 28, 600
    y = kicker(d, lx, 168, "CLIMATE  •  ANTALYA, TÜRKIYE")
    y = headline(d, lx, y, "COP31 DEAL COLLAPSES", 52, lw)
    y = para(d, lx, y + 4,
             "EU and allies reject a climate pact that never names fossil "
             "fuels. Talks end in Antalya with no agreement.",
             SERIF(22), lw, 30)
    # Cracked globe art, left of the lead body
    cx, cy, r = lx + 130, 470, 105
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(66, 130, 180),
              outline=INK, width=3)
    # land blobs
    d.ellipse([cx - 78, cy - 62, cx - 8, cy + 2], fill=(74, 140, 74))
    d.ellipse([cx + 6, cy - 30, cx + 74, cy + 34], fill=(74, 140, 74))
    d.ellipse([cx - 40, cy + 40, cx + 30, cy + 86], fill=(96, 150, 80))
    # crack across the globe
    d.line([(cx - 88, cy - 58), (cx - 30, cy - 6), (cx - 58, cy + 40),
            (cx + 8, cy + 66), (cx + 52, cy + 96)], fill=RED, width=6)
    # NO DEAL stamp, overlapping the globe's lower right
    stamp = Image.new("RGBA", (330, 92), (0, 0, 0, 0))
    sd = ImageDraw.Draw(stamp)
    sd.rectangle([4, 4, 325, 87], outline=RED, width=5)
    sd.text((165, 46), "NO DEAL", font=SANS_B(52), fill=RED, anchor="mm")
    stamp = stamp.rotate(-12, expand=True, resample=Image.BICUBIC)
    img.paste(stamp, (lx + 150, 452), stamp)
    y = para(d, lx + 300, 392,
             "“A pact that cannot say\n"
             "the words ‘fossil fuels’\n"
             "is no pact at all.”",
             SERIF(20), 300, 27, color=GREY)
    y = para(d, lx, 606,
             "The draft text avoided any mention of the fuels that cause "
             "global warming. The European Union and other nations refused "
             "it on Sunday; the summit closed without a deal.",
             SANS(18), lw, 26)

    # ---- Hormuz war (right column) --------------------------------------
    rx, rw = 652, 344
    y = kicker(d, rx, 168, "WAR  •  THE GULF")
    y = headline(d, rx, y, "WAR SPREADS ACROSS THE GULF", 34, rw)
    # Sea + burning tanker art
    ax0, ay0, ax1, ay1 = rx, y + 6, rx + rw, y + 190
    d.rectangle([ax0, ay0, ax1, ay1], fill=(38, 84, 130), outline=INK, width=2)
    # strait shoreline
    d.polygon([(ax0, ay1), (ax0, ay1 - 46), (ax0 + 130, ay1 - 30),
               (ax0 + 220, ay1 - 52), (ax1, ay1 - 26), (ax1, ay1)],
              fill=(214, 196, 150))
    d.text((ax0 + 10, ay1 - 28), "STRAIT OF HORMUZ", font=SANS_B(15),
           fill=(60, 48, 30))
    # tanker hull
    d.rectangle([ax0 + 60, ay0 + 122, ax0 + 300, ay0 + 150], fill=(40, 40, 44))
    d.rectangle([ax0 + 210, ay0 + 96, ax0 + 252, ay0 + 122], fill=(40, 40, 44))
    d.rectangle([ax0 + 60, ay0 + 150, ax0 + 300, ay0 + 158], fill=RED)
    # flames + smoke
    for fx, fy, fr in [(120, 104, 24), (150, 90, 30), (185, 104, 22),
                       (225, 96, 26)]:
        d.ellipse([ax0 + fx - fr, ay0 + fy - fr, ax0 + fx + fr,
                   ay0 + fy + fr], fill=ORANGE)
        d.ellipse([ax0 + fx - fr // 2, ay0 + fy - fr // 2,
                   ax0 + fx + fr // 2, ay0 + fy + fr // 2], fill=(240, 200, 60))
    for sx, sy, sr in [(140, 46, 16), (175, 34, 20), (210, 48, 14)]:
        d.ellipse([ax0 + sx - sr, ay0 + sy - sr, ax0 + sx + sr,
                   ay0 + sy + sr], fill=(60, 60, 60))
    y = ay1 + 12
    y = para(d, rx, y,
             "Iran says its forces hit US Patriot radars at a base in "
             "Bahrain. A Houthi missile is intercepted over Saudi Arabia "
             "as tankers come under attack in the Strait.",
             SANS(18), rw, 26)
    y = para(d, rx, y + 8,
             "The Iran–US war now engulfs Saudi Arabia and Bahrain.",
             SERIF(19), rw, 27)

    rule(d, 28, 726, 996, 2)

    # ---- Three middle panels --------------------------------------------
    py, ph = 744, 132
    panels = [
        (28, 316, "POLAND",
         "Missiles cross the border",
         "Warsaw calls it a deliberate Russian provocation. NATO jets "
         "scramble."),
        (360, 316, "KYIV  •  THE BALTIC",
         "14 missing; ship ablaze",
         "A drone hits a building in the Kyiv region; a cargo ship burns "
         "off Finland."),
        (692, 304, "LISBON",
         "Thousands march on prices",
         "Crowds fill Lisbon's streets as living costs fuel anger."),
    ]
    for px, pw, kick, head, body in panels:
        d.rectangle([px, py, px + pw, py + ph], outline=INK, width=2)
        kicker(d, px + 12, py + 10, kick)
        hy = headline(d, px + 12, py + 36, head, 19, pw - 24)
        para(d, px + 12, hy + 4, body, SANS(14), pw - 24, 19)
    rule(d, 28, 892, 996, 2)

    # ---- Ticker: also today ----------------------------------------------
    y = kicker(d, 28, 906, "ALSO TODAY")
    items = [
        "Nepal PM in Delhi for talks with Modi",
        "Nvidia row: AI chips diverted to China",
        "South Korea education minister quits over AI cheating",
        "India 720/9d — record in Wellington Test",
        "Indonesia factory fire: 7 dead, 50 missing",
        "Myanmar junta calls ASEAN move “unfair”",
    ]
    col_w = 480
    for i, item in enumerate(items):
        ix = 28 + (i % 2) * col_w
        iy = y + (i // 2) * 26
        d.text((ix, iy), "▪  " + item, font=SANS(15), fill=INK)

    out = Path(__file__).resolve().parent / "assets" / "entry.png"
    img.save(out, optimize=True)
    print(f"saved {out} {out.stat().st_size} bytes")


if __name__ == "__main__":
    main()
