// Render GTA Decoded Instagram stories (1080x1920) and feed slides (1080x1350) from content.json.
// Usage: node scripts/gta6_ig_render.js [id-filter]
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const ROOT = path.resolve(__dirname, '..'); const B = ROOT + '/outputs/gta6-codes/brand/';
const IG = ROOT + '/outputs/gta6-codes/instagram/';
const C = JSON.parse(fs.readFileSync(IG + 'content.json', 'utf8'));
const d64 = (f, t) => `data:${t};base64,` + fs.readFileSync(f).toString('base64');
const anton = d64(B + 'fonts/Anton-Regular.ttf', 'font/ttf');
const svg = f => d64(B + 'final/' + f, 'image/svg+xml');
const dec = m => d64(B + 'decoder/decoder-' + m + '.svg', 'image/svg+xml');
const T = { night: { bg: '#0B0710', ink: '#F7F1FA', muted: '#B3A6C2', pink: '#FF2E88', raised: '#17101F', line: '#2C2038', accent: '#A97BFF', word: 'gtad-wordmark-dark.svg', st: 'dark' },
            paper: { bg: '#EDE9E4', ink: '#0B0710', muted: '#594C66', pink: '#B80E62', raised: '#F7F4F0', line: '#D6CFC7', accent: '#5E1BC4', word: 'gtad-wordmark-light.svg', st: 'paper' } };
const fmt = s => s.replace(/\{last_checked\}/g, C.last_checked).split('|').join('<br>').replace(/\*([^*]+)\*/g, '<em>$1</em>').replace(/\*([^*]+)$/, '<em>$1</em>');
const head = s => { const lines = s.split('|'); let open = false; return lines.map(l => { let o = l; if (open) o = '<em>' + o; const n = (l.match(/\*/g) || []).length; if (n % 2) open = !open; o = o.replace(/\*([^*]*)\*/g, '<em>$1</em>').replace(/\*/g, open ? '<em>' : '</em>'); if (open) o += '</em>'; return o; }).join('<br>'); };
function page(f) {
  const t = T[f.theme], story = f.size === 'story', W = 1080, H = story ? 1920 : 1350;
  const pad = story ? 96 : 84, hs = story ? (f.layout === 'list' || f.layout === 'status' ? 190 : 220) : (f.layout === 'list' ? 140 : 160);
  const stampRow = ['confirmed', 'unverified', 'busted', 'expired'].map(s => `<img src="${svg(`stamp-${s}-${t.st}.svg`)}">`).join('');
  const items = (f.items || []).map((x, i) => `<li><b>${String(i + 1).padStart(2, '0')}</b><span>${x}</span></li>`).join('');
  const slot = f.slot ? `<div class="slot">${f.slot}</div>` : '';
  const stamp = f.stamp ? `<img class="stamp" src="${svg(`stamp-${f.stamp}-${t.st}.svg`)}">` : '';
  let mid = '';
  if (f.layout === 'list' || f.layout === 'status') mid = `<ol>${items}</ol>`;
  if (f.layout === 'stamps') mid = `<div class="stamps">${stampRow}</div><div class="legend">Confirmed · Unverified · Busted · Expired</div>`;
  if (f.layout === 'poll' || f.layout === 'reveal') mid = `<div class="media">${slot}${stamp}</div>`;
  return `<html><head><style>@font-face{font-family:Anton;src:url(${anton})}
*{box-sizing:border-box;margin:0}body{width:${W}px;height:${H}px;background:${t.bg};color:${t.ink};font-family:Inter,sans-serif;overflow:hidden;position:relative}
.glow{position:absolute;inset:0;background:${f.theme === 'night' ? 'radial-gradient(900px 700px at 85% 0%,#2A0E4A,transparent 70%)' : 'none'}}
.wrap{position:absolute;inset:${story ? 150 : 72}px ${pad}px ${story ? 230 : 72}px;display:flex;flex-direction:column;gap:${story ? 44 : 32}px}
.main{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:${(f.layout==='poll'||f.layout==='reveal'||f.decoder)?'flex-start':'center'};position:relative;z-index:1;gap:${story ? 52 : 36}px}.top{display:flex;justify-content:space-between;align-items:center}.top img{height:${story ? 64 : 54}px}
.ctr{font:800 26px 'JetBrains Mono',monospace;color:${t.muted};letter-spacing:.06em}
.eb{align-self:flex-start;font:800 ${story ? 36 : 30}px 'JetBrains Mono',monospace;letter-spacing:.08em;color:${t.bg};background:${t.pink};padding:12px 18px;transform:rotate(-2deg);box-shadow:6px 6px 0 ${f.theme === 'night' ? '#7B2FF2' : '#0B0710'}}
h1{font:${hs}px/.92 Anton,Impact,sans-serif;text-transform:uppercase;letter-spacing:.005em}h1 em{font-style:normal;color:${t.pink}}
.sub{font:600 ${story ? 52 : 42}px/1.3 Inter,sans-serif;color:${t.muted};max-width:900px}
ol{list-style:none;display:flex;flex-direction:column;gap:${story ? 30 : 22}px}li{display:flex;gap:26px;align-items:baseline;font:600 ${story ? 52 : 42}px/1.25 Inter,sans-serif}
li b{font:800 ${story ? 40 : 34}px 'JetBrains Mono',monospace;color:${t.pink};min-width:64px}
.stamps{display:grid;grid-template-columns:1fr 1fr;gap:${story ? 40 : 26}px 30px}.stamps img{width:100%}.legend{font:800 24px 'JetBrains Mono',monospace;color:${t.muted};letter-spacing:.06em}
.media{position:relative;flex:1;min-height:${story ? 420 : 240}px;max-height:${story ? 760 : 470}px}.slot{position:absolute;inset:0;border:4px dashed ${t.accent};border-radius:24px;background:${t.raised};display:flex;align-items:center;justify-content:center;text-align:center;padding:40px;font:800 30px/1.4 'JetBrains Mono',monospace;color:${t.muted};letter-spacing:.05em}
.stamp{position:absolute;width:62%;right:-6px;bottom:-14px}
.cta{align-self:flex-start;font:800 40px 'JetBrains Mono',monospace;letter-spacing:.06em;border:4px solid ${t.ink};padding:22px 28px;box-shadow:8px 8px 0 ${t.pink}}
.dec{position:absolute;right:${story ? -70 : -40}px;bottom:${story ? 0 : -10}px;width:${story ? 700 : 500}px;z-index:0}.top{position:relative;z-index:2}.foot{z-index:2;${f.decoder ? 'max-width:'+(story?440:420)+'px;' : ''}position:absolute;left:${pad}px;right:${pad}px;bottom:${story ? 130 : 34}px;font:600 24px 'JetBrains Mono',monospace;color:${t.muted};display:flex;justify-content:space-between}
</style></head><body><div class="glow"></div><div class="wrap">
<div class="top"><img src="${svg(t.word)}"><span class="ctr">${f.counter || ''}</span></div>
<div class="main"><div class="eb">${fmt(f.eyebrow)}</div><h1>${head(f.head)}</h1>
${f.sub && f.layout !== 'cta' ? `<p class="sub">${f.sub}</p>` : ''}${mid}
${f.layout === 'cta' ? `<p class="sub">${f.sub}</p><div class="cta">@GTADECODED</div>` : ''}
</div></div>${f.decoder ? `<img class="dec" src="${dec(f.decoder)}">` : ''}<script>const h=document.querySelector('h1');let fs=parseFloat(getComputedStyle(h).fontSize);while(h.scrollWidth>h.clientWidth&&fs>60){fs-=4;h.style.fontSize=fs+'px';}</script><div class="foot"><span>FAN-MADE · NOT AFFILIATED WITH ROCKSTAR</span><span>${story || f.decoder ? '' : '@GTADECODED'}</span></div></body></html>`;
}
(async () => {
  const filt = process.argv[2] || ''; const b = await chromium.launch();
  for (const f of C.frames.filter(x => x.id.includes(filt))) {
    const p = await b.newPage({ viewport: { width: 1080, height: f.size === 'story' ? 1920 : 1350 } });
    await p.setContent(page(f)); await p.waitForTimeout(250);
    await p.screenshot({ path: IG + (f.size === 'story' ? 'stories/' : 'feed/') + f.id + '.png' }); await p.close();
  }
  await b.close(); console.log('rendered');
})();
