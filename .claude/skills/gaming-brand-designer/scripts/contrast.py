"""WCAG contrast check. Usage: python3 contrast.py '#FF2E88' '#0B0710' ['#fg' '#bg' ...]"""
import sys
def lum(h):
    h = h.lstrip('#'); r, g, b = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)
def ratio(a, b):
    la, lb = lum(a), lum(b); return (max(la, lb) + .05) / (min(la, lb) + .05)
args = sys.argv[1:]
for fg, bg in zip(args[::2], args[1::2]):
    r = ratio(fg, bg); print(f'{fg} on {bg}: {r:.2f}  ' + ('PASS text' if r >= 4.5 else 'PASS large/icons only' if r >= 3 else 'FAIL'))
