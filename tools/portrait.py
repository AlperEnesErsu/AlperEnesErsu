# -*- coding: utf-8 -*-
"""Turn the portrait photo into a dot-matrix tone map for the hero banner.

A passport-style photo (flat lighting, white backdrop) does not survive a
character ramp -- the face collapses into the lightest glyphs and only the
silhouette reads. A halftone dot grid carries the same information far better
at the same cell count, and is still plain SVG (one <circle> per dot).

Writes dots.json: {"cols", "rows", "grid"} where grid[r][c] is 0 (background)
to 1 (darkest ink).
"""
import json, os, sys
from PIL import Image, ImageFilter

SRC = sys.argv[1] if len(sys.argv) > 1 else "portrait.jpg"
COLS = 48
CROP = (0.18, 0.19, 0.86, 0.68)   # head + shoulders, as fractions of the frame
BG = 243                          # >= this is the white studio backdrop
LOCAL = 1.0                       # local-contrast strength (unsharp on a big radius)
GAMMA = 1.0
FLOOR = 0.06                      # dots fainter than this are dropped

im = Image.open(SRC).convert("L")
w, h = im.size
im = im.crop((int(CROP[0] * w), int(CROP[1] * h), int(CROP[2] * w), int(CROP[3] * h)))
ROWS = max(1, round(COLS * im.height / im.width))

im = im.filter(ImageFilter.UnsharpMask(radius=max(2, im.width // COLS), percent=120, threshold=1))

# local contrast: without it the evenly lit face has almost no tonal range
blur = im.filter(ImageFilter.GaussianBlur(radius=im.width / 8.0))
pi, pb = im.load(), blur.load()
boosted = im.copy()
po = boosted.load()
for y in range(im.height):
    for x in range(im.width):
        po[x, y] = max(0, min(255, int(pi[x, y] + LOCAL * (pi[x, y] - pb[x, y]))))

small = boosted.resize((COLS, ROWS), Image.LANCZOS)
px = list(small.getdata())

subject = sorted(v for v in px if v < BG) or sorted(px)
lo = subject[int(len(subject) * 0.02)]
hi = subject[int(len(subject) * 0.97)]
span = max(1, hi - lo)

grid = []
for r in range(ROWS):
    row = []
    for c in range(COLS):
        v = px[r * COLS + c]
        if v >= BG:
            row.append(0.0)
            continue
        t = max(0.0, min(1.0, 1.0 - (v - lo) / span))   # clamp before gamma
        t = t ** GAMMA
        row.append(round(t, 2) if t > FLOOR else 0.0)
    grid.append(row)

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "dots.json"), "w", encoding="utf-8") as f:
    json.dump({"cols": COLS, "rows": ROWS, "grid": grid}, f)

print("%dx%d, %d dots" % (COLS, ROWS, sum(1 for r in grid for t in r if t)))
