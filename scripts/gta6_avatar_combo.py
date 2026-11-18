"""GTA Decoded Instagram avatar: stacked 'GTA / DECODED.' with the arrow keys right of GTA, fitted to a circle."""
import math, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gta6_logo_concepts import glyphs, width, svg, ANTON, K
from gta6_brand_final import keys, GRAD
OUT = 'outputs/gta6-codes/brand/final'
cap = ANTON['OS/2'].sCapHeight / ANTON['head'].unitsPerEm   # cap height as fraction of size
C, R = 500, 500           # canvas centre, circle radius
SAFE = 452                # keep every corner inside this radius
def build(block_w):
    s2 = block_w / width(ANTON, 'DECODED.', 100, 2) * 100          # DECODED. fills the block width
    s1 = s2 * 1.62                                                  # GTA is bigger, as in the reference
    gw = width(ANTON, 'GTA', s1, s1 * 0.02)
    h1, h2, gap = s1 * cap, s2 * cap, s2 * 0.16
    H = h1 + gap + h2
    return s1, s2, gw, h1, h2, gap, H
# find the largest block that fits the circle
bw = 760
while True:
    s1, s2, gw, h1, h2, gap, H = build(bw)
    if math.hypot(bw / 2, H / 2) <= SAFE: break
    bw -= 4
x0, y0 = C - bw / 2, C - H / 2
gta, _ = glyphs(ANTON, 'GTA', s1, x0, y0 + h1, track=s1 * 0.02)
dec, _ = glyphs(ANTON, 'DECODED.', s2, x0, y0 + H, track=2)
# keys fill the space right of GTA (cluster extent ~2.67 x key size, plus shadow)
area_x0 = x0 + gw + s1 * 0.07; area_w = x0 + bw - area_x0; area_h = h1
ks = min(area_w, area_h) / 2.78
kcx = area_x0 + area_w / 2 - ks * 0.04; kcy = y0 + h1 / 2 - ks * 0.04
body = (f'<rect width="1000" height="1000" fill="{K["black"]}"/>'
        f'<circle cx="{kcx:.0f}" cy="{kcy:.0f}" r="{ks*2.2:.0f}" fill="url(#halo)"/>'
        f'<path d="{gta}" fill="{K["white"]}"/><path d="{dec}" fill="{K["pink"]}"/>' + keys(kcx, kcy, ks, 'cmb'))
defs = GRAD.format(u='cmb', b=max(4, ks * 0.09)) + '<radialGradient id="halo"><stop offset="0" stop-color="#3A1470" stop-opacity=".9"/><stop offset="1" stop-color="#0B0710" stop-opacity="0"/></radialGradient>'
open(os.path.join(OUT, 'gtad-avatar-combo.svg'), 'w').write(svg(1000, 1000, body, 'GTA Decoded profile picture', defs))
print(f'block {bw}px, GTA {s1:.0f}px, DECODED {s2:.0f}px, key {ks:.0f}px')
