"""The Decoder: GTA Decoded's faceless hoodie mascot. The visor shows the verdict.
Writes outputs/gta6-codes/brand/decoder/decoder-{mood}.svg (transparent) and decoder-scene-{mood}.svg."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gta6_logo_concepts import glyphs, width, svg, MONO, K
OUT = 'outputs/gta6-codes/brand/decoder'; os.makedirs(OUT, exist_ok=True)
MOODS = {'default': ('#FF2E88', 'arrows'), 'confirmed': ('#4BE3B0', 'check'), 'busted': ('#FF2E88', 'cross'), 'unverified': ('#FFC547', 'q')}
HOOD = 'M500 120 C 715 120 815 290 815 470 C 815 610 760 705 690 760 L 310 760 C 240 705 185 610 185 470 C 185 290 285 120 500 120 Z'
VOID = 'M500 240 C 640 240 695 360 695 475 C 695 590 630 675 500 675 C 370 675 305 590 305 475 C 305 360 360 240 500 240 Z'
BODY = 'M60 1000 C 70 830 210 745 350 725 L 650 725 C 790 745 930 830 940 1000 Z'
def visor_glyph(kind, col):
    cx, cy = 500, 478
    if kind == 'arrows':
        d, w = glyphs(MONO, '↑→↓←', 62, 0, 0, track=6)
        return f'<path d="{d}" transform="translate({cx - w/2:.0f} {cy + 22})" fill="{col}"/>'
    if kind == 'check':
        return f'<path d="M{cx-58} {cy} L{cx-18} {cy+36} L{cx+62} {cy-38}" fill="none" stroke="{col}" stroke-width="24" stroke-linecap="square"/>'
    if kind == 'cross':
        return f'<path d="M{cx-42} {cy-40} L{cx+42} {cy+40} M{cx+42} {cy-40} L{cx-42} {cy+40}" stroke="{col}" stroke-width="24" stroke-linecap="square"/>'
    d, w = glyphs(MONO, '?', 120, 0, 0)
    return f'<path d="{d}" transform="translate({cx - w/2:.0f} {cy + 44})" fill="{col}"/>'
def decoder(mood, uid):
    col, kind = MOODS[mood]
    defs = f'''<linearGradient id="hood{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4A1C8C"/><stop offset="1" stop-color="#22093E"/></linearGradient>
<linearGradient id="body{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3A1470"/><stop offset="1" stop-color="#1A0833"/></linearGradient>
<filter id="glow{uid}" x="-40%" y="-80%" width="180%" height="260%"><feGaussianBlur stdDeviation="14" result="b"/><feFlood flood-color="{col}" flood-opacity=".9"/><feComposite in2="b" operator="in" result="g"/><feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<radialGradient id="faceglow{uid}" cx="50%" cy="55%" r="50%"><stop offset="0" stop-color="{col}" stop-opacity=".22"/><stop offset="1" stop-color="{col}" stop-opacity="0"/></radialGradient>'''
    o = K['black']
    body = f'''<g transform="translate(22 22)" fill="{K['purple']}"><path d="{BODY}"/><path d="{HOOD}"/></g>
<path d="{BODY}" fill="url(#body{uid})" stroke="{o}" stroke-width="16" stroke-linejoin="round"/>
<path d="M150 1000 C 160 870 250 800 350 780" fill="none" stroke="#FF2E88" stroke-width="10" stroke-linecap="round" opacity=".85"/>
<path d="{HOOD}" fill="url(#hood{uid})" stroke="{o}" stroke-width="16" stroke-linejoin="round"/>
<path d="M232 600 C 205 520 205 360 300 250 C 345 200 410 165 480 155" fill="none" stroke="#FF2E88" stroke-width="12" stroke-linecap="round" opacity=".9"/>
<path d="{VOID}" fill="#05030A" stroke="{o}" stroke-width="12"/>
<path d="{VOID}" fill="url(#faceglow{uid})"/>
<rect x="335" y="418" width="330" height="120" rx="60" fill="#120A22" stroke="{col}" stroke-width="8" filter="url(#glow{uid})"/>
{visor_glyph(kind, col)}
<path d="M445 740 C 440 790 432 840 428 880" fill="none" stroke="{K['white']}" stroke-width="12" stroke-linecap="round"/>
<path d="M555 740 C 560 790 568 840 572 880" fill="none" stroke="{K['white']}" stroke-width="12" stroke-linecap="round"/>
<rect x="414" y="874" width="28" height="44" rx="6" fill="#FF2E88" stroke="{o}" stroke-width="6"/>
<rect x="558" y="874" width="28" height="44" rx="6" fill="#FF2E88" stroke="{o}" stroke-width="6"/>
<rect x="680" y="840" width="74" height="74" rx="14" fill="#FF2E88" stroke="{o}" stroke-width="8"/>
<path transform="translate(717 877)" d="M0 -22 L20 2 H8 V22 H-8 V2 H-20 Z" fill="{o}"/>'''
    return defs, body
def scene(uid):
    import random; r = random.Random(3); b = []; x = 0
    while x < 1000:
        w = r.choice([40, 60, 80, 50]); h = r.choice([120, 200, 260, 160, 320, 90])
        b.append(f'<rect x="{x}" y="{700-h}" width="{w-6}" height="{h}"/>'); x += w
    grid = ''.join(f'<line x1="0" y1="{700+k*k*6}" x2="1000" y2="{700+k*k*6}"/>' for k in range(1, 12)) + ''.join(f'<line x1="{500+i*40}" y1="700" x2="{500+i*170}" y2="1250"/>' for i in range(-14, 15))
    return f'''<defs><linearGradient id="sky{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0B0710"/><stop offset=".55" stop-color="#3A1470"/><stop offset=".72" stop-color="#C42BD6"/><stop offset=".74" stop-color="#0B0710"/></linearGradient></defs>
<rect width="1000" height="1250" fill="url(#sky{uid})"/><circle cx="500" cy="640" r="230" fill="#FF2E88" opacity=".9"/>
<g fill="#0B0710">{"".join(b)}</g><rect y="700" width="1000" height="550" fill="#0B0710"/><g stroke="#FF2E88" stroke-width="3" opacity=".55">{grid}</g>'''
files = {}
for m in MOODS:
    d, b = decoder(m, m)
    files[f'decoder-{m}.svg'] = svg(1000, 1000, b, f'The Decoder ({m})', d)
    files[f'decoder-scene-{m}.svg'] = svg(1000, 1250, scene(m) + f'<defs>{d}</defs><g transform="translate(0 250)">{b}</g>', f'The Decoder in the city ({m})')
for n, v in files.items(): open(os.path.join(OUT, n), 'w').write(v)
print('\n'.join(files))
