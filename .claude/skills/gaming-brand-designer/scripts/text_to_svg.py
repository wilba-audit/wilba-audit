"""Turn text into SVG path data using a TTF/OTF font (no font needed when rendering).

Library use:
    from text_to_svg import glyphs, centered, width
    d, w = glyphs('/path/Anton-Regular.ttf', 'GTA', size=300, x=0, y=280, track=6)
CLI:
    python3 text_to_svg.py FONT "TEXT" SIZE > out.svg   # quick standalone SVG
Requires: pip install fonttools
"""
import sys
from functools import lru_cache
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

@lru_cache(maxsize=16)
def _font(path):
    return TTFont(path)

def glyphs(font_path, text, size, x=0.0, y=0.0, track=0.0):
    """Return (path_d, advance_width). y is the baseline; track is extra px between letters."""
    f = _font(font_path); gs = f.getGlyphSet(); cmap = f.getBestCmap()
    s = size / f['head'].unitsPerEm; pen = SVGPathPen(gs); cx = 0.0
    for ch in text:
        name = cmap.get(ord(ch))
        if name is None:
            raise ValueError(f'{ch!r} is not in {font_path}; pick another font or character')
        gs[name].draw(TransformPen(pen, (s, 0, 0, -s, x + cx, y)))
        cx += gs[name].width * s + track
    return pen.getCommands(), cx - track

def width(font_path, text, size, track=0.0):
    return glyphs(font_path, text, size, 0, 0, track)[1]

def centered(font_path, text, size, cx, y, track=0.0):
    return glyphs(font_path, text, size, cx - width(font_path, text, size, track) / 2, y, track)[0]

def fit_size(font_path, text, max_width, start=300, track=0.0):
    """Largest size <= start at which text fits max_width."""
    return min(start, start * max_width / width(font_path, text, start, track))

if __name__ == '__main__':
    font, text, size = sys.argv[1], sys.argv[2], float(sys.argv[3])
    d, w = glyphs(font, text, size, 10, size * 0.9)
    print(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w+20:.0f} {size*1.15:.0f}"><path d="{d}"/></svg>')
