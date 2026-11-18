"""GTA Decoded final logo suite: C (input keys) + A (verdict stamps). Writes to outputs/gta6-codes/brand/final."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gta6_logo_concepts import glyphs, centered, width, svg, ANTON, MONO, K, stamp_rect, INK
OUT = 'outputs/gta6-codes/brand/final'; os.makedirs(OUT, exist_ok=True)
GRAD = '''<linearGradient id="sun{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFB3D9"/><stop offset=".35" stop-color="#FF2E88"/><stop offset="1" stop-color="#C42BD6"/></linearGradient>
<filter id="glow{u}" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="{b}" result="b"/><feFlood flood-color="#FF2E88" flood-opacity=".85"/><feComposite in2="b" operator="in" result="g"/><feMerge><feMergeNode in="g"/><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'''

def key(x, y, s, d, fill, stroke, arrow, glow=None):
    r = s * 0.18; a = {'up': 0, 'right': 90, 'down': 180, 'left': 270}[d]
    f = f' filter="url(#glow{glow})"' if glow else ''
    return (f'<g transform="translate({x} {y})"><rect x="{-s/2+s*0.08}" y="{-s/2+s*0.11}" width="{s}" height="{s}" rx="{r}" fill="{K["purple"]}"/>'
            f'<rect x="{-s/2}" y="{-s/2}" width="{s}" height="{s}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{s*0.075}"{f}/>'
            f'<path transform="rotate({a})" d="M0 {-s*0.27} L{s*0.25} {s*0.02} H{s*0.095} V{s*0.27} H{-s*0.095} V{s*0.02} H{-s*0.25} Z" fill="{arrow}"/></g>')
def keys(cx, cy, s, u, line=K['white']):
    o = (s + s * 0.16) * 0.72
    return (key(cx + o, cy, s, 'right', K['black'], line, line) + key(cx, cy + o, s, 'down', K['black'], line, line) +
            key(cx - o, cy, s, 'left', K['black'], line, line) + key(cx, cy - o, s, 'up', K['pink'], K['black'], K['black'], glow=u))
def words(u, x, base, size, gta_fill):
    g, gw = glyphs(ANTON, 'GTA', size, 0, 0, track=size * 0.02)
    d, dw = glyphs(ANTON, 'DECODED', size, 0, 0, track=size * 0.02)
    sw = size * 0.075; sh = size * 0.05
    lay = lambda path, fill, dx: (f'<g transform="translate({dx} 0)"><path d="{path}" transform="translate({sh} {sh})" fill="{K["purple"]}" stroke="{K["black"]}" stroke-width="{sw}" stroke-linejoin="round" paint-order="stroke"/>'
                                  f'<path d="{path}" fill="{fill}" stroke="{K["black"]}" stroke-width="{sw}" stroke-linejoin="round" paint-order="stroke"/></g>')
    gap = size * 0.16
    return f'<g transform="translate({x} {base}) skewX(-9)">{lay(g, gta_fill, 0)}{lay(d, f"url(#sun{u})", gw + gap)}</g>', gw + gap + dw + sh + sw
def tagline(x, y, size, color):
    return f'<path d="{glyphs(MONO, "↑ → ↓ ←  NO-BS GTA 6 CODES & GUIDES", size, x, y, track=size*0.06)[0]}" fill="{color}"/>'

files = {}
for theme, gta, tag in [('dark', K['white'], K['violet']), ('light', K['white'], K['purple'])]:
    u = 'h' + theme
    w, ww = words(u, 470, 300, 250, gta)
    files[f'gtad-logo-horizontal-{theme}.svg'] = svg(int(470 + ww + 70), 470, keys(210, 225, 118, u) + w + tagline(484, 410, 34, tag), f'GTA Decoded logo for {theme} backgrounds', GRAD.format(u=u, b=10))
    u = 's' + theme
    w, ww = words(u, 0, 0, 230, gta)
    W = int(ww + 80)
    files[f'gtad-logo-stacked-{theme}.svg'] = svg(W, 720, keys(W / 2, 200, 120, u) + f'<g transform="translate(40 600)">{w}</g>' + f'<g transform="translate({(W - width(MONO, "NO-BS GTA 6 CODES & GUIDES", 30, 1.8)) / 2:.0f} 690)"><path d="{glyphs(MONO, "NO-BS GTA 6 CODES & GUIDES", 30, 0, 0, track=1.8)[0]}" fill="{tag}"/></g>', f'GTA Decoded stacked logo for {theme} backgrounds', GRAD.format(u=u, b=10))
    u = 'w' + theme
    w, ww = words(u, 30, 280, 250, gta)
    files[f'gtad-wordmark-{theme}.svg'] = svg(int(30 + ww + 60), 330, w, f'GTA Decoded wordmark for {theme} backgrounds', GRAD.format(u=u, b=10))
av = ('<rect width="1000" height="1000" fill="#0B0710"/><circle cx="500" cy="500" r="470" fill="url(#avbg)"/>' + keys(500, 512, 262, 'av'))
files['gtad-avatar.svg'] = svg(1000, 1000, av, 'GTA Decoded profile picture', GRAD.format(u='av', b=18) + '<radialGradient id="avbg" cx="50%" cy="45%" r="55%"><stop offset="0" stop-color="#3A1470"/><stop offset="1" stop-color="#0B0710"/></radialGradient>')
for name, col_d, col_l, rot in [('confirmed', K['mint'], '#0A6E4C', 4), ('unverified', '#FFC547', '#7A4F00', -3), ('busted', K['pink'], '#B80E62', -8), ('expired', '#9A8FA8', '#625770', 3)]:
    for theme, col in [('dark', col_d), ('paper', col_l)]:
        W, H, b, d = stamp_rect(f'st{name}{theme}', col, 'GTA DECODED VERDICT', name.upper(), 'TESTED ON CAMERA', rot=rot)
        files[f'stamp-{name}-{theme}.svg'] = svg(W, H, b, f'{name.title()} verdict stamp', d)
for theme, col in [('dark', K['mint']), ('paper', '#0A6E4C')]:
    W, H, b, d = stamp_rect(f'stoff{theme}', col, 'GTA DECODED VERDICT', 'CONFIRMED', 'OFFICIAL SOURCE', rot=4)
    files[f'stamp-confirmed-official-{theme}.svg'] = svg(W, H, b, 'Confirmed (official source) verdict stamp', d)
for n, v in files.items(): open(os.path.join(OUT, n), 'w').write(v)
print('\n'.join(files))
