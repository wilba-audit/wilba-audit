// Render an HTML or SVG file to PNG with Playwright.
// Usage: node render.js in.html|in.svg out.png [width=1600] [height=900] [scale=1]
// Full-page screenshot for HTML; SVG is shown at the given width/height.
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const [inp, out, w = 1600, h = 900, sc = 1] = process.argv.slice(2);
  if (!inp || !out) { console.error('usage: node render.js in out.png [w] [h] [scale]'); process.exit(1); }
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: +sc });
  const abs = path.resolve(inp);
  if (abs.endsWith('.svg')) {
    const data = 'data:image/svg+xml;base64,' + fs.readFileSync(abs).toString('base64');
    await p.setContent(`<body style="margin:0"><img src="${data}" style="width:${w}px;height:${h}px;display:block;object-fit:contain"></body>`);
  } else { await p.goto('file://' + abs); }
  await p.waitForTimeout(400);
  await p.screenshot({ path: out, fullPage: !abs.endsWith('.svg') });
  await b.close(); console.log('wrote', out);
})();
