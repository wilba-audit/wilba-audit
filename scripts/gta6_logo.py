"""GTA Decoded logo generator: writes SVG logo variants with real letter outlines."""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import os, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'outputs/gta6-codes/brand/logos'
os.makedirs(OUT, exist_ok=True)
INTER = '/usr/share/fonts/opentype/inter/InterDisplay-Black.otf'
MONO = '/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-ExtraBold.ttf'
# Palette: pink, purple, black (sunset over the city at night)
C = dict(night='#0B0710', ink_dark='#F7F1FA', ink_light='#0B0710',
         b1='#FF6FB5', b2='#FF2E88', b3='#C42BD6', b4='#7B2FF2',
         pink='#FF2E88', pink_light='#C8106A', chev_dark='#F7F1FA', chev_light='#0B0710')

def text_path(font_file, text, size, x, y, tracking=0.0):
    f = TTFont(font_file); gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f['head'].unitsPerEm
    s = size / upm; pen = SVGPathPen(gs); cx = 0.0
    for ch in text:
        g = cmap[ord(ch)]
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x + cx, y)))
        cx += gs[g].width * s + tracking * size
    return pen.getCommands(), cx - tracking * size

def mark(colors, ox=0, oy=0, scale=1.0, mono=None, chev=None):
    """Sun with retro slices between teal code chevrons, drawn on a 512 grid."""
    g, o, p, q = (mono,)*4 if mono else (colors['b1'], colors['b2'], colors['b3'], colors['b4'])
    t = mono or chev or colors['chev_dark']
    cid = f"sun{ox}{oy}{int(scale*100)}{'m' if mono else ''}"
    return f'''<g transform="translate({ox} {oy}) scale({scale})">
<clipPath id="{cid}"><circle cx="256" cy="256" r="132"/></clipPath>
<g clip-path="url(#{cid})">
<rect x="100" y="120" width="312" height="114" fill="{g}"/>
<rect x="100" y="246" width="312" height="50" fill="{o}"/>
<rect x="100" y="310" width="312" height="34" fill="{p}"/>
<rect x="100" y="362" width="312" height="30" fill="{q}"/>
</g>
<path d="M132 168 L70 256 L132 344" fill="none" stroke="{t}" stroke-width="36" stroke-linecap="square" stroke-linejoin="miter"/>
<path d="M380 168 L442 256 L380 344" fill="none" stroke="{t}" stroke-width="36" stroke-linecap="square" stroke-linejoin="miter"/>
</g>'''

def svg(w, h, body, title, y0=0):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {y0} {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n'

def wordmark(gta_fill, dec_fill, cursor_fill, x, base, size):
    d1, w1 = text_path(INTER, 'GTA', size, x, base, tracking=-0.01)
    x2 = x + w1 + size * 0.22
    d2, w2 = text_path(MONO, 'DECODED', size * 0.86, x2, base)
    cur_x = x2 + w2 + size * 0.06
    body = (f'<path d="{d1}" fill="{gta_fill}"/><path d="{d2}" fill="{dec_fill}"/>'
            f'<rect x="{cur_x:.1f}" y="{base - size*0.10:.1f}" width="{size*0.42:.1f}" height="{size*0.12:.1f}" fill="{cursor_fill}"/>')
    return body, cur_x + size * 0.42 - x

files = {}
files['gta-decoded-mark.svg'] = svg(512, 512, mark(C, chev=C['b4']), 'GTA Decoded mark')
files['gta-decoded-mark-mono.svg'] = svg(512, 512, mark(C, mono='currentColor').replace('<svg', '<svg'), 'GTA Decoded mark, one colour')
files['gta-decoded-avatar.svg'] = svg(512, 512, f'<rect width="512" height="512" rx="112" fill="{C["night"]}"/>' + mark(C, 46, 46, 0.82), 'GTA Decoded profile picture')
for theme, gta, dec, chev in [('dark', C['ink_dark'], C['pink'], C['chev_dark']), ('light', C['ink_light'], C['pink_light'], C['chev_light'])]:
    size = 120
    wm, ww = wordmark(gta, dec, dec, 196, 150, size)
    W = int(196 + ww + 24)
    files[f'gta-decoded-wordmark-{theme}.svg'] = svg(W, 120, mark(C, 0, 6, 0.36, chev=chev) + wm, f'GTA Decoded logo for {theme} backgrounds', y0=40)
    # stacked
    wm2, ww2 = wordmark(gta, dec, dec, 0, 0, 96)
    W2 = int(ww2) + 48
    files[f'gta-decoded-stacked-{theme}.svg'] = svg(W2, 300, mark(C, (W2-320)/2, -62, 0.625, chev=chev) + f'<g transform="translate(24 285)">{wm2}</g>', f'GTA Decoded stacked logo for {theme} backgrounds')
for n, s in files.items():
    open(os.path.join(OUT, n), 'w').write(s)
print('\n'.join(files))
