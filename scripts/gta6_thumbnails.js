const { chromium } = require('playwright');
const OUT = '/home/user/wilba-audit/outputs/gta6-codes/thumbnails/';
const scene = (w,h,hue) => `
<svg class="scene" viewBox="0 0 ${w} ${h}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
<defs>
 <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#120724"/><stop offset=".45" stop-color="${hue[0]}"/><stop offset=".75" stop-color="${hue[1]}"/><stop offset="1" stop-color="#1a0b2e"/></linearGradient>
 <linearGradient id="sun" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE14D"/><stop offset="1" stop-color="#FF2E88"/></linearGradient>
 <pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M60 0H0V60" fill="none" stroke="#00E5D4" stroke-opacity=".35" stroke-width="2"/></pattern>
</defs>
<rect width="${w}" height="${h}" fill="url(#sky)"/>
<g transform="translate(${w*0.72} ${h*0.62})">
 <circle r="${Math.min(w,h)*0.26}" fill="url(#sun)"/>
 ${[0,1,2,3,4].map(i=>`<rect x="-${w}" y="${Math.min(w,h)*(0.04+i*0.045)}" width="${2*w}" height="${6+i*3}" fill="#1a0b2e"/>`).join('')}
</g>
<g fill="#0b0618">
 ${Array.from({length:22},(_,i)=>{const bw=w/22, bh=h*(0.08+((i*37)%11)/60);return `<rect x="${i*bw}" y="${h*0.7-bh}" width="${bw-4}" height="${bh}"/>`}).join('')}
 <rect y="${h*0.7}" width="${w}" height="${h*0.3}" />
</g>
<g transform="translate(0 ${h*0.7})"><rect width="${w}" height="${h*0.3}" fill="url(#grid)" transform="skewX(0)"/></g>
${palm(w*0.06,h*0.72,h*0.42)}${palm(w*0.16,h*0.74,h*0.32)}
</svg>`;
function palm(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s/400})" fill="#07030f">
<path d="M-6 0 C0 -150 10 -280 30 -390 L42 -388 C26 -270 18 -150 14 0Z"/>
${[[-160,-330],[-120,-440],[40,-470],[170,-400],[190,-300],[-60,-470]].map(([a,b])=>`<path d="M36 -392 Q${(a+36)/2} ${b-40} ${a} ${b} Q${(a+36)/2} ${b-10} 36 -380Z"/>`).join('')}</g>`}
const logo = (size=1)=>`<div class="logo" style="font-size:${28*size}px"><span class="g">GTA</span><span class="d">&lt;DECODED/&gt;</span></div>`;
const css = `
*{margin:0;box-sizing:border-box}body{width:var(--w);height:var(--h);overflow:hidden;font-family:'Inter Display','Inter',sans-serif;background:#0b0618}
.scene{position:absolute;inset:0;width:100%;height:100%}
.scan{position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(0,0,0,.18) 0 2px,transparent 2px 5px);mix-blend-mode:multiply}
.shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(8,3,18,.92) 0%,rgba(8,3,18,.55) 48%,rgba(8,3,18,0) 75%)}
.logo{position:absolute;display:flex;gap:.35em;align-items:baseline;font-weight:900;letter-spacing:.02em}
.logo .g{color:#fff;font-family:'Inter Display';font-weight:900}.logo .d{color:#00E5D4;font-family:'JetBrains Mono';font-weight:800}
.chip{display:inline-flex;align-items:center;gap:.4em;font-family:'JetBrains Mono';font-weight:800;padding:.35em .7em;border-radius:.35em;letter-spacing:.04em}
.h{font-family:'Inter Display';font-weight:900;text-transform:uppercase;line-height:.92;color:#fff;letter-spacing:-.01em;text-shadow:0 .06em 0 rgba(0,0,0,.55),0 0 .5em rgba(255,46,136,.35)}
.h em{font-style:normal;background:linear-gradient(180deg,#FFE14D,#FF8A00);-webkit-background-clip:text;color:transparent;text-shadow:none;filter:drop-shadow(0 .06em 0 rgba(0,0,0,.55))}
.sub{font-family:'Inter';font-weight:700;color:#e9e3ff}
.foot{position:absolute;font-family:'JetBrains Mono';font-weight:600;color:rgba(255,255,255,.7)}
.slot{position:absolute;border:3px dashed rgba(0,229,212,.7);border-radius:18px;color:rgba(255,255,255,.85);font-family:'JetBrains Mono';font-weight:700;display:flex;align-items:center;justify-content:center;text-align:center;background:rgba(10,4,24,.35);backdrop-filter:blur(2px)}
`;
const chipC={GUIDE:['#FF8A00','#1a0b2e','▶'],DECODED:['#00E5D4','#081016','?'],'SCAM ALERT':['#FF2E88','#fff','⚠'],'BEGINNER GUIDE':['#FFE14D','#1a0b2e','★'],TESTED:['#00E5D4','#081016','✓']};
const chip=(t,s)=>{const [b,c,i]=chipC[t];return `<span class="chip" style="background:${b};color:${c};font-size:${s}px">${i} ${t}</span>`};
const items=[
 {f:'01-claim-free-gta-plus',chip:'GUIDE',h:'Claim your<br><em>free GTA+</em>',sub:'Pre-order bonus · step by step',hue:['#5b1e8c','#ff5a3c'],slot:'YOUR SCREENSHOT:<br>GTA+ claim screen'},
 {f:'02-do-cheats-exist',chip:'DECODED',h:'GTA 6 cheats:<br><em>real or fake?</em>',sub:'Every viral code, tested on PS5',hue:['#3a1a8a','#ff2e88'],slot:'YOUR CLIP:<br>entering the code'},
 {f:'03-fake-money-codes',chip:'SCAM ALERT',h:'Fake GTA 6<br><em>money codes</em>',sub:"Don't fall for these 5 traps",hue:['#6d0f4a','#ff2e2e'],slot:'YOUR SCREENSHOT:<br>scam site (blurred)'},
 {f:'04-first-10-things',chip:'BEGINNER GUIDE',h:'Do these<br><em>10 things</em><br>first',sub:'GTA 6 beginner guide',hue:['#103a6b','#ff8a00'],slot:'YOUR GAMEPLAY<br>frame here'},
];
const yt=(it)=>`<style>:root{--w:1280px;--h:720px}${css}</style>${scene(1280,720,it.hue)}<div class="scan"></div><div class="shade"></div>
${logo(1.15).replace('class="logo"','class="logo" style="left:56px;top:44px;font-size:32px"')}
<div style="position:absolute;left:56px;top:150px">${chip(it.chip,30)}</div>
<div class="h" style="position:absolute;left:56px;top:220px;font-size:104px;max-width:760px">${it.h}</div>
<div class="sub" style="position:absolute;left:58px;bottom:56px;font-size:30px">${it.sub}</div>
<div class="slot" style="right:48px;top:60px;width:340px;height:420px;font-size:22px;transform:rotate(3deg)">${it.slot}</div>
<div class="foot" style="right:52px;bottom:24px;font-size:15px">Fan-made · not affiliated with Rockstar Games</div>`;
const reel=(it)=>`<style>:root{--w:1080px;--h:1920px}${css}.shade{background:linear-gradient(180deg,rgba(8,3,18,.2) 0%,rgba(8,3,18,.85) 55%,rgba(8,3,18,.95) 100%)}</style>${scene(1080,1920,it.hue)}<div class="scan"></div><div class="shade"></div>
<div class="slot" style="left:140px;top:300px;width:800px;height:620px;font-size:34px">${it.slot}</div>
<div style="position:absolute;left:90px;right:70px;bottom:230px;display:flex;flex-direction:column;align-items:flex-start;gap:34px">${chip(it.chip,40)}<div class="h" style="font-size:132px">${it.h}</div><div class="sub" style="font-size:42px">${it.sub}</div></div>
${logo().replace('class="logo"','class="logo" style="left:90px;top:200px;font-size:44px"')}
<div class="foot" style="left:90px;bottom:120px;font-size:24px">Full guide → link in bio · Fan-made, not affiliated with Rockstar</div>`;
const carousel=()=>`<style>:root{--w:1080px;--h:1350px}${css}.shade{background:linear-gradient(180deg,rgba(8,3,18,.35),rgba(8,3,18,.92) 70%)}</style>${scene(1080,1350,['#2a1470','#ff2e88'])}<div class="scan"></div><div class="shade"></div>
${logo().replace('class="logo"','class="logo" style="left:80px;top:80px;font-size:40px"')}
<div style="position:absolute;left:80px;top:560px">${chip('GUIDE',38)}</div>
<div class="h" style="position:absolute;left:76px;top:650px;font-size:150px">7 GTA 6<br><em>tips</em> you<br>missed</div>
<div class="sub" style="position:absolute;left:80px;bottom:110px;font-size:38px">Swipe → · save this for later</div>
<div class="foot" style="left:80px;bottom:52px;font-size:22px">Fan-made · not affiliated with Rockstar Games</div>`;
(async()=>{const b=await chromium.launch();
 const shot=async(html,w,h,name)=>{const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:1});await p.setContent(html);await p.waitForTimeout(150);await p.screenshot({path:OUT+name});await p.close();};
 for(const it of items){await shot(yt(it),1280,720,`yt-web-${it.f}.png`);}
 for(const it of [items[1],items[0]]){await shot(reel(it),1080,1920,`ig-reel-cover-${it.f}.png`);}
 await shot(carousel(),1080,1350,'ig-carousel-cover-7-tips.png');
 // contact sheet for review
 const imgs=require('fs').readdirSync(OUT).filter(f=>f.endsWith('.png')&&!f.startsWith('00'));
 const sheet=`<body style="margin:0;background:#111;padding:30px;font-family:Inter;color:#fff;width:2000px"><h1 style="margin:0 0 20px">GTA Decoded · sample thumbnails</h1><div style="display:flex;flex-wrap:wrap;gap:24px;align-items:flex-start">${imgs.map(f=>`<figure style="margin:0"><img src="file://${OUT+f}" style="height:${f.startsWith('yt')?'270px':'480px'};border-radius:10px"><figcaption style="font-size:14px;opacity:.7">${f}</figcaption></figure>`).join('')}</div></body>`;
 const p=await b.newPage({viewport:{width:2060,height:800},deviceScaleFactor:1});await p.goto('file:///dev/null').catch(()=>{});await p.setContent(sheet);await p.waitForTimeout(400);await p.screenshot({path:OUT+'00-contact-sheet.png',fullPage:true});
 await b.close();console.log(imgs.join('\n'));})();
