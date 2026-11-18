"""GTA Decoded logo v2: emblem badge + bold logotype + lockup (pink/purple/black)."""
import math, os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
OUT = sys.argv[1] if len(sys.argv) > 1 else 'outputs/gta6-codes/brand/logos'
os.makedirs(OUT, exist_ok=True)
INTER = TTFont('/usr/share/fonts/opentype/inter/InterDisplay-Black.otf')
ANTON = TTFont('outputs/gta6-codes/brand/fonts/Anton-Regular.ttf')
MONO = TTFont('/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-ExtraBold.ttf')
K = dict(black='#0B0710', white='#F7F1FA', pink='#FF2E88', pinkL='#FF8FC6', mag='#C42BD6', purple='#7B2FF2', deep='#2A0E4A')

def glyphs(font, text, size, x=0.0, y=0.0, track=0.0):
    gs = font.getGlyphSet(); cmap = font.getBestCmap(); s = size / font['head'].unitsPerEm
    pen = SVGPathPen(gs); cx = 0.0
    for ch in text:
        g = cmap[ord(ch)]; gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x + cx, y))); cx += gs[g].width * s + track
    return pen.getCommands(), cx - track

def adv(font, ch, size):
    return font.getGlyphSet()[font.getBestCmap()[ord(ch)]].width * size / font['head'].unitsPerEm

def ring_text(phrases, R, cx, cy, size, fill, dot):
    chars = sum(len(p) for p in phrases)
    natural = sum(adv(MONO, c, size) for p in phrases for c in p)
    C = 2 * math.pi * R
    gap = (C - natural) / len(phrases)
    out = []; theta = 0.0  # radians, clockwise from top
    for p in phrases:
        for c in p:
            a = adv(MONO, c, size); mid = theta + (a / 2) / R
            if c != ' ':
                d, _ = glyphs(MONO, c, size, -a / 2, 0)
                out.append(f'<path transform="rotate({math.degrees(mid):.2f} {cx} {cy}) translate({cx} {cy - R})" d="{d}" fill="{fill}"/>')
            theta += a / R
        dm = theta + (gap / 2) / R
        out.append(f'<rect transform="rotate({math.degrees(dm):.2f} {cx} {cy}) translate({cx} {cy - R - size*0.36}) rotate(45)" x="-7" y="-7" width="14" height="14" fill="{dot}"/>')
        theta += gap / R
    return ''.join(out)

def palm(x, y, h, lean, flip=1):
    # trunk: tapered curve; fronds: drooping leaves
    tx, ty = x + lean, y - h
    trunk = f'<path d="M{x-14} {y} Q{x+lean*0.2-10} {y-h*0.5} {tx-6} {ty} L{tx+6} {ty} Q{x+lean*0.2+12} {y-h*0.5} {x+14} {y} Z"/>'
    leaves = []
    for ang, ln, droop in [(-172, 175, 95), (-150, 185, 60), (-122, 150, 22), (-58, 150, 22), (-30, 185, 60), (-8, 175, 95), (-95, 110, 0)]:
        a = math.radians(ang); ex = tx + math.cos(a) * ln * flip; ey = ty + math.sin(a) * ln * 0.5 + droop
        mx = tx + (ex - tx) * 0.5; my = ty + (ey - ty) * 0.5 - 52
        nx = tx + (ex - tx) * 0.55; ny = ty + (ey - ty) * 0.55 - 20
        leaves.append(f'<path d="M{tx} {ty} Q{mx:.1f} {my:.1f} {ex:.1f} {ey:.1f} Q{nx:.1f} {ny:.1f} {tx} {ty+8} Z"/>')
    return f'<g fill="{K["black"]}">{trunk}{"".join(leaves)}<circle cx="{tx}" cy="{ty+6}" r="12"/></g>'

def emblem(uid='e', ring=True):
    cx = cy = 500; H = 610  # horizon
    bld = []; xs = 268
    import random; rnd = random.Random(6)
    while xs < 735:
        w = rnd.choice([26, 34, 42, 30]); h = rnd.choice([30, 52, 70, 44, 88, 60])
        if 455 < xs < 545: h = rnd.choice([120, 104])
        bld.append(f'<rect x="{xs}" y="{H-h}" width="{w}" height="{h+2}"/>')
        if h > 100: bld.append(f'<rect x="{xs + w/2 - 2}" y="{H-h-26}" width="4" height="28"/>')
        xs += w + 3
    grid = []
    for k in range(1, 9):
        y = H + 6 * k * k
        grid.append(f'<line x1="100" y1="{y}" x2="900" y2="{y}"/>')
    for i in range(-10, 11):
        grid.append(f'<line x1="{cx + i*22}" y1="{H}" x2="{cx + i*150}" y2="1000"/>')
    stripes = ''.join(f'<rect x="250" y="{y}" width="500" height="{hh}" fill="black"/>' for y, hh in [(500, 7), (528, 10), (560, 13), (594, 16)])
    RING_T = f'''<circle cx="{cx}" cy="{cy}" r="496" fill="{K['black']}"/>
<circle cx="{cx}" cy="{cy}" r="474" fill="none" stroke="{K['pink']}" stroke-width="8"/>
<circle cx="{cx}" cy="{cy}" r="382" fill="none" stroke="{K['pink']}" stroke-width="8"/>
{ring_text(['GTA DECODED', 'GUIDES', 'VERIFIED CODES', 'TUTORIALS'], 408, cx, cy, 54, K['white'], K['pink'])}
'''
    chev = lambda d: f'<path d="{d}" fill="none" stroke="{K["white"]}" stroke-width="34" stroke-linecap="square" stroke-linejoin="miter"/>'
    return f'''<defs>
<radialGradient id="{uid}glow" cx="50%" cy="58%" r="55%"><stop offset="0" stop-color="{K['pink']}" stop-opacity=".55"/><stop offset="1" stop-color="{K['pink']}" stop-opacity="0"/></radialGradient>
<linearGradient id="{uid}sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{K['black']}"/><stop offset=".35" stop-color="{K['deep']}"/><stop offset=".62" stop-color="{K['purple']}"/><stop offset=".78" stop-color="{K['mag']}"/></linearGradient>
<linearGradient id="{uid}sun" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{K['pinkL']}"/><stop offset=".55" stop-color="{K['pink']}"/><stop offset="1" stop-color="{K['mag']}"/></linearGradient>
<clipPath id="{uid}disc"><circle cx="{cx}" cy="{cy}" r="372"/></clipPath>
<mask id="{uid}cuts"><rect width="1000" height="1000" fill="white"/>{stripes}</mask>
</defs>
{RING_T if ring else f'<circle cx="{cx}" cy="{cy}" r="390" fill="{K["black"]}"/><circle cx="{cx}" cy="{cy}" r="382" fill="none" stroke="{K["pink"]}" stroke-width="10"/>'}
<g clip-path="url(#{uid}disc)">
<rect width="1000" height="{H}" fill="url(#{uid}sky)"/>
<circle cx="{cx}" cy="{H-40}" r="330" fill="url(#{uid}glow)"/>
<circle cx="{cx}" cy="{H-6}" r="230" fill="url(#{uid}sun)" mask="url(#{uid}cuts)"/>
<g fill="{K['black']}">{''.join(bld)}</g>
<rect y="{H}" width="1000" height="400" fill="{K['black']}"/>
<g stroke="{K['pink']}" stroke-width="3" stroke-opacity=".85">{''.join(grid)}</g>
<line x1="100" y1="{H}" x2="900" y2="{H}" stroke="{K['pinkL']}" stroke-width="4"/>
{palm(236, 790, 360, 34)}{palm(784, 770, 270, -26, -1)}
</g>
{chev('M218 420 L168 500 L218 580')}{chev('M782 420 L832 500 L782 580')}'''

def svgdoc(w, h, body, title, extra=''):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}"{extra}><title>{title}</title>{body}</svg>\n'

def anton_logo(stacked, ink, pink):
    size = 300
    if stacked:
        d1, w1 = glyphs(ANTON, 'GTA', size, 0, size * 0.86, track=4)
        d2, w2 = glyphs(ANTON, 'DECODED', size * 0.62, 0, size * 0.86 + size * 0.62 * 0.95, track=2)
        dot = size * 0.62 * 0.16
        W = max(w1, w2 + dot * 1.5) ; H = size * 0.86 + size * 0.62 * 0.95 + 8
        dotx = w2 + dot * 0.45; doty = size * 0.86 + size * 0.62 * 0.95 - dot
        body = f'<path d="{d1}" fill="{ink}"/><path d="{d2}" fill="{pink}"/><rect x="{dotx:.1f}" y="{doty:.1f}" width="{dot:.1f}" height="{dot:.1f}" fill="{pink}"/>'
        return body, W, H
    d1, w1 = glyphs(ANTON, 'GTA', size, 0, size * 0.86, track=4)
    d2, w2 = glyphs(ANTON, 'DECODED', size, w1 + size * 0.14, size * 0.86, track=4)
    dot = size * 0.16; x2 = w1 + size * 0.14 + w2
    body = f'<path d="{d1}" fill="{ink}"/><path d="{d2}" fill="{pink}"/><rect x="{x2 + dot*0.45:.1f}" y="{size*0.86 - dot:.1f}" width="{dot:.1f}" height="{dot:.1f}" fill="{pink}"/>'
    return body, x2 + dot * 1.5, size * 0.86 + 6

files = {'gta-decoded-emblem.svg': svgdoc(1000, 1000, emblem(), 'GTA Decoded emblem')}
for theme, ink, pink in [('dark', K['white'], K['pink']), ('light', K['black'], '#C8106A')]:
    for kind, st in [('stacked', True), ('line', False)]:
        b, w, h = anton_logo(st, ink, pink)
        files[f'gta-decoded-logotype-{kind}-{theme}.svg'] = svgdoc(int(w + 8), int(h + 8), f'<g transform="translate(4 4)">{b}</g>', f'GTA Decoded logotype, {kind}, for {theme} backgrounds')
    b, w, h = anton_logo(True, ink, pink)
    sc = 520 / h
    files[f'gta-decoded-lockup-{theme}.svg'] = svgdoc(int(600 + w * sc + 20), 560, f'<g transform="translate(0 0) scale(.56)">{emblem("x"+theme)}</g><g transform="translate(600 20) scale({sc:.4f})">{b}</g>', f'GTA Decoded lockup for {theme} backgrounds')
for n, v in files.items(): open(os.path.join(OUT, n), 'w').write(v)
print('\n'.join(files))

# ---- v4: GTA-style poster badge (outlined, gradient, shadow, over the scene) ----
def poster_letters(uid, text, size, x, y, fill, outline=K['black'], ow=22, shadow=K['purple'], sh=(14, 14), track=6):
    d, w = glyphs(ANTON, text, size, x, y, track=track)
    return (f'<path d="{d}" transform="translate({sh[0]} {sh[1]})" fill="{shadow}" stroke="{outline}" stroke-width="{ow}" stroke-linejoin="round" paint-order="stroke"/>'
            f'<path d="{d}" fill="{fill}" stroke="{outline}" stroke-width="{ow}" stroke-linejoin="round" paint-order="stroke"/>'), w

def badge_v4(uid='b'):
    defs = f'''<defs><linearGradient id="{uid}g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE0F0"/><stop offset=".3" stop-color="{K['pinkL']}"/><stop offset=".62" stop-color="{K['pink']}"/><stop offset="1" stop-color="{K['mag']}"/></linearGradient></defs>'''
    scene = f'<g transform="translate(60 -40) scale(.88)">{emblem(uid+"e", ring=False)}</g>'
    gta, gw = poster_letters(uid, 'GTA', 400, 0, 0, f'url(#{uid}g)')
    gx = (1000 - gw) / 2
    dec_d, dw = glyphs(ANTON, 'DECODED.', 150, 0, 0, track=4)
    tw = dw + 90
    tape = (f'<g transform="translate({(1000 - tw)/2:.0f} 860) rotate(-4 {tw/2:.0f} 80)">'
            f'<rect x="14" y="14" width="{tw:.0f}" height="170" fill="{K["black"]}"/>'
            f'<rect width="{tw:.0f}" height="170" fill="{K["pink"]}" stroke="{K["black"]}" stroke-width="10"/>'
            f'<path d="{dec_d}" transform="translate(45 150)" fill="{K["white"]}" stroke="{K["black"]}" stroke-width="12" stroke-linejoin="round" paint-order="stroke"/></g>')
    return defs + scene + f'<g transform="translate({gx+25:.0f} 820) skewX(-8)">{gta}</g>' + tape

open(os.path.join(OUT, 'gta-decoded-badge.svg'), 'w').write(svgdoc(1000, 1080, badge_v4(), 'GTA Decoded badge logo'))
# horizontal poster wordmark
g2, gw2 = poster_letters('h', 'GTA', 300, 30, 300, 'url(#hg)')
d2, dw2 = glyphs(ANTON, 'DECODED.', 300, 0, 0, track=4)
hdefs = f'<defs><linearGradient id="hg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE0F0"/><stop offset=".3" stop-color="{K["pinkL"]}"/><stop offset=".62" stop-color="{K["pink"]}"/><stop offset="1" stop-color="{K["mag"]}"/></linearGradient></defs>'
dec = (f'<path d="{d2}" transform="translate({30+gw2+60:.0f} 300) translate(14 14)" fill="{K["purple"]}" stroke="{K["black"]}" stroke-width="22" stroke-linejoin="round" paint-order="stroke"/>'
       f'<path d="{d2}" transform="translate({30+gw2+60:.0f} 300)" fill="{K["white"]}" stroke="{K["black"]}" stroke-width="22" stroke-linejoin="round" paint-order="stroke"/>')
open(os.path.join(OUT, 'gta-decoded-wordmark-poster.svg'), 'w').write(svgdoc(int(30+gw2+60+dw2+60), 360, hdefs + f'<g transform="skewX(-8) translate(40 0)">{g2}{dec}</g>', 'GTA Decoded poster wordmark'))
print('v4 done')
