"""GTA Decoded logo concepts v5: A Stamp, B Glitch, C Input. Writes SVGs."""
import math, os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
OUT = sys.argv[1] if len(sys.argv) > 1 else 'outputs/gta6-codes/brand/concepts'
os.makedirs(OUT, exist_ok=True)
ANTON = TTFont('outputs/gta6-codes/brand/fonts/Anton-Regular.ttf')
MONO = TTFont('/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-ExtraBold.ttf')
INTER = TTFont('/usr/share/fonts/opentype/inter/InterDisplay-Black.otf')
K = dict(black='#0B0710', white='#F7F1FA', pink='#FF2E88', pinkL='#FF8FC6', mag='#C42BD6', purple='#7B2FF2', violet='#A97BFF', mint='#4BE3B0', paper='#EDE9E4')

def glyphs(font, text, size, x=0.0, y=0.0, track=0.0):
    gs = font.getGlyphSet(); cmap = font.getBestCmap(); s = size / font['head'].unitsPerEm
    pen = SVGPathPen(gs); cx = 0.0
    for ch in text:
        g = cmap[ord(ch)]; gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x + cx, y))); cx += gs[g].width * s + track
    return pen.getCommands(), cx - track
def width(font, text, size, track=0.0): return glyphs(font, text, size, 0, 0, track)[1]
def centered(font, text, size, cx, y, track=0.0):
    w = width(font, text, size, track); return glyphs(font, text, size, cx - w / 2, y, track)[0]
def svg(w, h, body, title, defs=''):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}"><title>{title}</title><defs>{defs}</defs>{body}</svg>\n'

INK = '''<filter id="ink{u}" x="-5%" y="-5%" width="110%" height="110%">
<feTurbulence type="fractalNoise" baseFrequency="{f}" numOctaves="3" seed="{seed}" result="n"/>
<feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -4.2 3.05" result="m"/>
<feComposite in="SourceGraphic" in2="m" operator="in" result="t"/>
<feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="4" result="w"/>
<feDisplacementMap in="t" in2="w" scale="5" xChannelSelector="R" yChannelSelector="G"/></filter>'''

# ---------- A: THE STAMP ----------
def stamp_rect(u, color, top, main, bottom, rot=-5):
    W, H = 980, 440
    msize = min(200, 200 * (W - 170) / width(ANTON, main, 200, 6))
    d_main = centered(ANTON, main, msize, W/2, 205 + msize * 0.47, track=6)
    d_top = centered(MONO, top, 34, W/2, 84, track=6)
    d_bot = centered(MONO, bottom, 34, W/2, 392, track=4)
    body = f'''<g transform="rotate({rot} {W/2} {H/2})" filter="url(#ink{u})" fill="{color}">
<path fill-rule="evenodd" d="M24 24 H{W-24} V{H-24} H24 Z M40 40 V{H-40} H{W-40} V40 Z"/>
<path fill-rule="evenodd" d="M56 56 H{W-56} V{H-56} H56 Z M64 64 V{H-64} H{W-64} V64 Z"/>
<rect x="64" y="104" width="{W-128}" height="6"/><rect x="64" y="{H-112}" width="{W-128}" height="6"/>
<path d="{d_top}"/><path d="{d_main}"/><path d="{d_bot}"/></g>'''
    return W, H, body, INK.format(u=u, f=0.85, seed=11)

def stamp_round(u, color, center='GTA', sub='DECODED', ring='TESTED ON CAMERA', ring2='NO-BS GTA 6'):
    W = H = 1000; cx = cy = 500
    parts = [f'<path fill-rule="evenodd" d="M{cx} {cy-470} a470 470 0 1 0 0.1 0 Z M{cx} {cy-446} a446 446 0 1 1 -0.1 0 Z"/>',
             f'<path fill-rule="evenodd" d="M{cx} {cy-330} a330 330 0 1 0 0.1 0 Z M{cx} {cy-316} a316 316 0 1 1 -0.1 0 Z"/>']
    def arc_text(text, R, size, top=True):
        out = []; total = sum(width(MONO, c, size) for c in text) + 8 * (len(text) - 1)
        ang = -total / R / 2
        for c in text:
            a = width(MONO, c, size); mid = ang + (a / 2) / R
            if c != ' ':
                if top:
                    d, _ = glyphs(MONO, c, size, -a/2, 0)
                    out.append(f'<path transform="rotate({math.degrees(mid):.2f} {cx} {cy}) translate({cx} {cy-R})" d="{d}"/>')
                else:
                    d, _ = glyphs(MONO, c, size, -a/2, size*0.72)
                    out.append(f'<path transform="rotate({-math.degrees(mid):.2f} {cx} {cy}) translate({cx} {cy+R-size*0.72})" d="{d}"/>')
            ang += (a + 8) / R
        return ''.join(out)
    parts.append(arc_text(ring, 368, 62, True)); parts.append(arc_text(ring2, 368, 62, False))
    for sx in (-1, 1):
        parts.append(f'<path transform="translate({cx + sx*392} {cy}) rotate(45)" d="M-16 -16 H16 V16 H-16 Z"/>')
    parts.append(f'<path d="{centered(ANTON, center, 330, cx, cy + 80, track=8)}"/>')
    parts.append(f'<rect x="{cx-250}" y="{cy+110}" width="500" height="92"/>')
    sub_d = centered(ANTON, sub, 74, cx, cy + 186, track=10)
    body = f'<g filter="url(#ink{u})" fill="{color}">{"".join(parts)}</g><path d="{sub_d}" fill="{K["black"]}" filter="url(#ink{u})"/>'
    return W, H, body, INK.format(u=u, f=0.8, seed=5)

# ---------- B: THE GLITCH ----------
def glitch_word(u, line1='GTA', line2='DECODED', base=K['white'], accent=K['pink']):
    W, H = 1100, 560
    d1 = centered(ANTON, line1, 300, W/2, 280, track=10)
    d2 = centered(ANTON, line2, 190, W/2, 470, track=8)
    slices = [(168, 9, 26), (418, 7, -20)]
    clip = ''.join(f'<clipPath id="s{u}{i}"><rect x="0" y="{y}" width="{W}" height="{h}"/></clipPath>' for i, (y, h, dx) in enumerate(slices))
    main = f'<path d="{d1}" fill="{base}"/><path d="{d2}" fill="{accent}"/>'
    body = (f'<g opacity=".9"><path d="{d1}" transform="translate(-6 0)" fill="{K["purple"]}"/><path d="{d2}" transform="translate(-6 0)" fill="{K["purple"]}"/></g>'
            f'<g opacity=".9"><path d="{d1}" transform="translate(6 0)" fill="{K["pink"]}"/><path d="{d2}" transform="translate(6 0)" fill="{K["violet"]}"/></g>'
            + main +
            ''.join(f'<g clip-path="url(#s{u}{i})" transform="translate({dx} 0)"><rect x="0" y="{y}" width="{W}" height="{h}" fill="{K["black"]}"/>{main}</g>' for i, (y, h, dx) in enumerate(slices)) +
            f'<path d="{glyphs(MONO, "> DECODING... 100%", 30, 120, 520)[0]}" fill="{K["violet"]}"/>'
            f'<rect x="470" y="496" width="22" height="30" fill="{K["pink"]}"/>'
            f'<g fill="{K["black"]}" opacity=".18">' + ''.join(f'<rect x="0" y="{y}" width="{W}" height="2"/>' for y in range(40, 480, 12)) + '</g>')
    return W, H, body, clip

def glitch_avatar(u):
    W = H = 1000
    d = centered(ANTON, 'GD', 560, 500, 720, track=20)
    slices = [(380, 16, 34), (600, 12, -28)]
    clip = ''.join(f'<clipPath id="a{u}{i}"><rect x="0" y="{y}" width="{W}" height="{h}"/></clipPath>' for i, (y, h, dx) in enumerate(slices))
    main = f'<path d="{d}" fill="{K["white"]}"/>'
    body = (f'<rect width="1000" height="1000" fill="{K["black"]}"/>'
            f'<rect x="60" y="60" width="880" height="880" fill="none" stroke="{K["pink"]}" stroke-width="18"/>'
            f'<path d="{d}" transform="translate(-16 0)" fill="{K["purple"]}"/><path d="{d}" transform="translate(16 0)" fill="{K["pink"]}"/>{main}'
            + ''.join(f'<g clip-path="url(#a{u}{i})" transform="translate({dx} 0)"><rect y="{y}" width="{W}" height="{h}" fill="{K["black"]}"/>{main}</g>' for i, (y, h, dx) in enumerate(slices)) +
            f'<rect x="700" y="760" width="110" height="34" fill="{K["pink"]}"/>'
            f'<g fill="{K["black"]}" opacity=".2">' + ''.join(f'<rect y="{y}" width="1000" height="3"/>' for y in range(0, 1000, 16)) + '</g>')
    return W, H, body, clip

# ---------- C: THE INPUT ----------
def key(x, y, s, d, fill, stroke, arrow):
    r = s * 0.18
    a = {'up': 0, 'right': 90, 'down': 180, 'left': 270}[d]
    return (f'<g transform="translate({x} {y})"><rect x="{-s/2+10}" y="{-s/2+14}" width="{s}" height="{s}" rx="{r}" fill="{K["purple"]}"/>'
            f'<rect x="{-s/2}" y="{-s/2}" width="{s}" height="{s}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{s*0.07}"/>'
            f'<path transform="rotate({a})" d="M0 {-s*0.26} L{s*0.24} {s*0.02} H{s*0.09} V{s*0.26} H{-s*0.09} V{s*0.02} H{-s*0.24} Z" fill="{arrow}"/></g>')
def input_icon(cx, cy, s, gap):
    o = s + gap
    return (key(cx, cy - o * 0.72, s, 'up', K['pink'], K['black'], K['black']) +
            key(cx + o * 0.72, cy, s, 'right', K['black'], K['white'], K['white']) +
            key(cx, cy + o * 0.72, s, 'down', K['black'], K['white'], K['white']) +
            key(cx - o * 0.72, cy, s, 'left', K['black'], K['white'], K['white']))
def input_word(u, ink=K['white'], dark=True):
    W, H = 0, 480
    icon = input_icon(220, 230, 120, 20)
    gta, gw = glyphs(ANTON, 'GTA', 250, 0, 0, track=6)
    dec, dw = glyphs(ANTON, 'DECODED', 250, 0, 0, track=6)
    st = K['black']
    words = (f'<g transform="translate(470 290) skewX(-9)">'
             f'<path d="{gta}" transform="translate(12 12)" fill="{K["purple"]}" stroke="{st}" stroke-width="18" stroke-linejoin="round" paint-order="stroke"/>'
             f'<path d="{gta}" fill="{ink}" stroke="{st}" stroke-width="18" stroke-linejoin="round" paint-order="stroke"/>'
             f'<g transform="translate({gw+44} 0)"><path d="{dec}" transform="translate(12 12)" fill="{K["purple"]}" stroke="{st}" stroke-width="18" stroke-linejoin="round" paint-order="stroke"/>'
             f'<path d="{dec}" fill="{K["pink"]}" stroke="{st}" stroke-width="18" stroke-linejoin="round" paint-order="stroke"/></g></g>')
    combo = glyphs(MONO, '↑ → ↓ ← ↑ → ↓ ←  NO-BS GTA 6 CODES', 34, 480, 400, track=2)[0]
    body = icon + words + f'<path d="{combo}" fill="{K["violet"] if dark else K["purple"]}"/>'
    W = int(470 + gw + 44 + dw + 60)
    return W, H, body, ''
def input_avatar(u):
    return 1000, 1000, f'<rect width="1000" height="1000" fill="{K["black"]}"/>' + input_icon(500, 500, 230, 40), ''

def build_concepts():
    files = {}
    W, H, b, d = stamp_rect('a1', K['pink'], 'TESTED ON CAMERA', 'GTA DECODED', 'NO-BS GTA 6 GUIDES & CODES'); files['A-stamp-wordmark.svg'] = svg(W, H, b, 'GTA Decoded stamp', d)
    W, H, b, d = stamp_round('a2', K['pink']); files['A-stamp-round.svg'] = svg(W, H, b, 'GTA Decoded round stamp', d)
    W, H, b, d = stamp_rect('a3', K['pink'], 'GTA DECODED VERDICT', 'BUSTED', 'TESTED ON PS5 · 19 NOV 2026', rot=-8); files['A-verdict-busted.svg'] = svg(W, H, b, 'Busted stamp', d)
    W, H, b, d = stamp_rect('a4', K['mint'], 'GTA DECODED VERDICT', 'CONFIRMED', 'TESTED ON PS5 · 19 NOV 2026', rot=4); files['A-verdict-confirmed.svg'] = svg(W, H, b, 'Confirmed stamp', d)
    W, H, b, d = glitch_word('b1'); files['B-glitch-wordmark.svg'] = svg(W, H, b, 'GTA Decoded glitch wordmark', d)
    W, H, b, d = glitch_avatar('b2'); files['B-glitch-avatar.svg'] = svg(W, H, b, 'GTA Decoded glitch avatar', d)
    W, H, b, d = input_word('c1'); files['C-input-wordmark.svg'] = svg(W, H, b, 'GTA Decoded input wordmark', d)
    W, H, b, d = input_word('c3', ink=K['white'], dark=False); files['C-input-wordmark-light.svg'] = svg(W, H, b, 'GTA Decoded input wordmark light', d)
    W, H, b, d = input_avatar('c2'); files['C-input-avatar.svg'] = svg(W, H, b, 'GTA Decoded input avatar', d)
    W, H, b, d = stamp_rect('a5', '#B80E62', 'GTA DECODED VERDICT', 'BUSTED', 'TESTED ON PS5 · 19 NOV 2026', rot=-8); files['A-verdict-busted-paper.svg'] = svg(W, H, b, 'Busted stamp', d)
    W, H, b, d = stamp_rect('a6', '#0A6E4C', 'GTA DECODED VERDICT', 'CONFIRMED', 'TESTED ON PS5 · 19 NOV 2026', rot=4); files['A-verdict-confirmed-paper.svg'] = svg(W, H, b, 'Confirmed stamp', d)
    W, H, b, d = stamp_rect('a7', '#B80E62', 'TESTED ON CAMERA', 'GTA DECODED', 'NO-BS GTA 6 GUIDES & CODES'); files['A-stamp-wordmark-paper.svg'] = svg(W, H, b, 'GTA Decoded stamp', d)
    for n, s in files.items(): open(os.path.join(OUT, n), 'w').write(s)
    print('\n'.join(files))

if __name__ == '__main__':
    build_concepts()
