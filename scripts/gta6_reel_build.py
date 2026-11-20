"""Assemble GTA Decoded Reels: Artlist AI shot + Noto Sans captions + claim card with stamp slam + end card.
Usage: python3 scripts/gta6_reel_build.py <reel-id> <shot.mp4>   (silent 1080x1920 MP4 out)"""
import json, os, subprocess, sys, tempfile, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = f'{ROOT}/outputs/gta6-codes/brand'; OUT = f'{ROOT}/outputs/gta6-codes/reels'
REELS = {
 'reel-1-30fps': {'caps': [(0, 3.6, '13 YEARS…'), (3.6, 8, '…FOR *30 FPS?*')],
                  'eyebrow': 'WHAT STREAMERS SAY', 'lines': ['“Capped at 30 on PS5”', '“Even the Pro runs at 30”'], 'q': 'REAL OR *BUSTED?*',
                  'stamp': 'unverified', 'end': 'VERDICT *INCOMING.*'},
 'reel-2-score': {'caps': [(0, 3.6, 'IT SCORED *A 100.*'), (3.6, 8, '*“NOT A PERFECT GAME.”*')],
                  'eyebrow': 'BOTH CAN BE TRUE', 'lines': ['A 100 = best in its class', 'Not zero flaws'], 'q': 'PERFECT SCORES *ALL AROUND?*',
                  'stamp': 'unverified', 'end': 'READ THE REVIEW. *NOT THE NUMBER.*'},
 'reel-3-glitch': {'caps': [(0, 3.6, '15 MINUTES IN.'), (3.6, 8, '*FIRST GLITCH.*')],
                  'eyebrow': 'REPORTED ON STREAM', 'lines': ['Plane jump clips through objects', 'A weird marker on a blimp'], 'q': 'ONE-OFF OR *EVERY TIME?*',
                  'stamp': 'unverified', 'end': 'SEEN A BUG? *SEND IT.*'}}
def hl(s): 
    import re; return re.sub(r'\*([^*]+)\*', r'<em>\1</em>', s)
def b64(p, t):
    import base64; return f'data:{t};base64,' + base64.b64encode(open(p, 'rb').read()).decode()
CSS = """*{margin:0;box-sizing:border-box}body{width:1080px;height:1920px;overflow:hidden;font-family:'Noto Sans';background:transparent}
.cap{position:absolute;left:70px;right:110px;top:300px;font:900 118px/1.02 'Noto Sans';text-transform:uppercase;color:#F7F1FA;letter-spacing:-.01em;
paint-order:stroke;-webkit-text-stroke:14px #0B0710;text-shadow:8px 8px 0 #7B2FF2}.cap em,h1 em,.q em{font-style:normal;color:#FF2E88}
.card{position:absolute;inset:0;background:radial-gradient(900px 800px at 80% 10%,#2A0E4A,#0B0710 70%)}
.eb{position:absolute;left:80px;top:300px;font:800 40px 'JetBrains Mono';letter-spacing:.08em;color:#0B0710;background:#FF2E88;padding:14px 22px;transform:rotate(-2deg);box-shadow:7px 7px 0 #7B2FF2}
.lines{position:absolute;left:80px;right:90px;top:430px;display:flex;flex-direction:column;gap:26px;font:800 64px/1.15 'Noto Sans';color:#F7F1FA}
.q{position:absolute;left:80px;right:90px;top:820px;font:900 104px/1 'Noto Sans';color:#F7F1FA;text-transform:uppercase}
.stamp{position:absolute;width:820px;left:130px;top:1130px;transform-origin:50% 50%}
.dec{position:absolute;width:560px;right:-60px;bottom:-20px;opacity:.95}
h1{position:absolute;left:80px;right:80px;top:820px;font:900 120px/1 'Noto Sans';text-transform:uppercase;color:#F7F1FA}
.logo{position:absolute;left:80px;top:300px;width:900px}.handle{position:absolute;left:80px;top:1330px;font:800 52px 'JetBrains Mono';color:#F7F1FA;border:5px solid #F7F1FA;padding:20px 30px;box-shadow:9px 9px 0 #FF2E88}
.legal{position:absolute;left:80px;bottom:330px;font:600 30px 'JetBrains Mono';color:#B3A6C2}"""
def shots(pages):
    """pages: list of (html, png_path, transparent)"""
    js = 'const { chromium } = require("playwright");const fs=require("fs");(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});' + \
         'const jobs=JSON.parse(fs.readFileSync(process.argv[2],"utf8"));for(const [h,o,t] of jobs){await p.setContent(h);await p.waitForTimeout(120);await p.screenshot({path:o,omitBackground:t});}await b.close();})();'
    d = tempfile.mkdtemp(); jf = f'{d}/jobs.json'; open(jf, 'w').write(json.dumps(pages)); sf = f'{d}/s.js'; open(sf, 'w').write(js)
    subprocess.run(['node', sf, jf], check=True, cwd=ROOT)
def build(rid, shot):
    R = REELS[rid]; t = tempfile.mkdtemp()
    stamp = b64(f'{B}/final/stamp-{R["stamp"]}-dark.svg', 'image/svg+xml'); dec = b64(f'{B}/decoder/decoder-{R["stamp"]}.svg', 'image/svg+xml')
    logo = b64(f'{B}/final/gtad-logo-horizontal-dark.svg', 'image/svg+xml')
    head = f'<html><head><style>{CSS}</style></head><body>'
    pages = [(head + f'<div class="cap">{hl(c)}</div></body></html>', f'{t}/cap{i}.png', True) for i, (_, _, c) in enumerate(R['caps'])]
    card = head + f'<div class="card"></div><img class="dec" src="{dec}"><div class="eb">{R["eyebrow"]}</div><div class="lines">' + ''.join(f'<div>{l}</div>' for l in R['lines']) + f'</div><div class="q">{hl(R["q"])}</div>'
    scales = [None, 2.2, 1.8, 1.45, 1.2, 1.05, 0.96, 1.0]
    for i, s in enumerate(scales):
        st = '' if s is None else f'<img class="stamp" src="{stamp}" style="transform:rotate(-6deg) scale({s});opacity:{min(1, 0.4 + (2.2 - s))}">'
        pages.append((card + st + '</body></html>', f'{t}/card{i}.png', False))
    pages.append((head + f'<div class="card"></div><img class="logo" src="{logo}"><h1>{hl(R["end"])}</h1><div class="handle">FOLLOW @GTA.DE.CODED</div><div class="legal">Fan-made · not affiliated with Rockstar<br>AI-generated visuals</div></body></html>', f'{t}/end.png', False))
    shots(pages)
    # 1) shot segment: 8s, crop/scale to 1080x1920, captions timed
    seg1 = f'{t}/seg1.mp4'
    fc = '[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30,trim=0:8,setpts=PTS-STARTPTS[v0];'
    last = 'v0'
    for i, (a, b, _) in enumerate(R['caps']):
        fc += f'[{last}][{i+1}:v]overlay=0:0:enable=\'between(t,{a},{b})\'[v{i+1}];'; last = f'v{i+1}'
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-i', shot] + sum([['-i', f'{t}/cap{i}.png'] for i in range(len(R['caps']))], []) + \
          ['-filter_complex', fc.rstrip(';'), '-map', f'[{last}]', '-an', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', '30', seg1]
    subprocess.run(cmd, check=True)
    # 2) card segment (5s, stamp slams at 1.0s) + 3) end card (3s) via concat of stills
    lst = f'{t}/list.txt'; durs = [1.0] + [1/30] * 6 + [4.0 - 6/30]
    with open(lst, 'w') as f:
        for i, d in enumerate(durs): f.write(f"file '{t}/card{i if i < 7 else 7}.png'\nduration {d:.4f}\n")
        f.write(f"file '{t}/end.png'\nduration 3.0\nfile '{t}/end.png'\n")
    seg2 = f'{t}/seg2.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-vf', 'fps=30,format=yuv420p', '-c:v', 'libx264', seg2], check=True)
    out = f'{OUT}/{rid}.mp4'
    open(f'{t}/all.txt', 'w').write(f"file '{seg1}'\nfile '{seg2}'\n")
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', f'{t}/all.txt', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', '30', '-movflags', '+faststart', out], check=True)
    shutil.rmtree(t); print(out)
if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2])
