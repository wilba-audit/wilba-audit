#!/usr/bin/env node
/**
 * collect_social.mjs — WILBA public social-data collector
 * ------------------------------------------------------
 * Pulls the maximum PUBLIC data available for a person/brand's social accounts,
 * so an audit can be built on real numbers instead of guesses. It gathers what
 * the platforms expose without login: profile stats, bios, and recent post
 * metadata (titles/captions, dates, and public view/like counts where shown).
 *
 * WHAT IT NEEDS
 *   - Node 18+ (uses native fetch). Node 22.21+: prefix with NODE_USE_ENV_PROXY=1
 *     if you're behind a proxy so fetch honours HTTPS_PROXY.
 *   - Playwright for the login-walled sites (Instagram/TikTok/LinkedIn):
 *       npm i playwright        (browser is auto-found; see CHROMIUM below)
 *     YouTube works WITHOUT a browser (public RSS), so you get real data even
 *     with no Playwright installed.
 *   - **Open outbound network.** It must be able to reach instagram.com,
 *     youtube.com, tiktok.com, linkedin.com. It will NOT run inside a sandbox
 *     whose egress policy blocks those hosts (e.g. a locked-down CI/agent env) —
 *     run it on a normal machine or an environment with open networking.
 *
 * USAGE
 *   node collect_social.mjs config.json
 * where config.json is:
 *   {
 *     "slug": "schoeman",
 *     "outDir": "outputs/schoeman",
 *     "accounts": {
 *       "instagram": "drginaschoeman",
 *       "youtube":   "https://www.youtube.com/@drginaschoeman",   // handle, /channel/ID, or channelId
 *       "tiktok":    "drginaschoeman",
 *       "linkedin":  "https://www.linkedin.com/in/dr-gina-schoeman-022a07b/",
 *       "x":         "ginaschoeman"
 *     }
 *   }
 * Writes: <outDir>/collected-data.json  and  <outDir>/collected-data.md
 * Anything blocked/unavailable is recorded honestly, never invented.
 */

import { writeFileSync, mkdirSync, readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';

const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36';
// Common locations for a pre-installed Chromium; else Playwright's own download.
const CHROMIUM_CANDIDATES = [
  process.env.CHROMIUM_PATH,
  '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  '/opt/pw-browsers/chromium/chrome-linux/chrome',
];

function log(...a){ console.error('[collect]', ...a); }

// ---------- YouTube (no browser needed: public RSS + oEmbed) ----------
async function collectYouTube(input){
  const res = { platform:'youtube', input, ok:false, notes:[] };
  try {
    let channelId = null;
    if (/^UC[\w-]{20,}$/.test(input)) channelId = input;
    else if (/\/channel\/(UC[\w-]{20,})/.test(input)) channelId = input.match(/\/channel\/(UC[\w-]{20,})/)[1];
    if (!channelId) {
      // resolve a handle/custom URL to a channelId by reading the page HTML
      const url = input.startsWith('http') ? input
        : `https://www.youtube.com/${input.startsWith('@')?input:'@'+input}`;
      const html = await (await fetch(url, { headers:{'user-agent':UA} })).text();
      const m = html.match(/"channelId":"(UC[\w-]{20,})"/) || html.match(/channel\/(UC[\w-]{20,})/);
      if (m) channelId = m[1];
      const subs = html.match(/"subscriberCountText".*?"simpleText":"([^"]+)"/);
      if (subs) res.subscribers = subs[1];
    }
    if (!channelId){ res.notes.push('could not resolve channelId'); return res; }
    res.channelId = channelId;
    const rss = await (await fetch(`https://www.youtube.com/feeds/videos.xml?channel_id=${channelId}`, { headers:{'user-agent':UA} })).text();
    const entries = [...rss.matchAll(/<entry>([\s\S]*?)<\/entry>/g)].map(e=>e[1]);
    res.recent = entries.map(e => ({
      title:  (e.match(/<title>([\s\S]*?)<\/title>/)||[])[1] || null,
      published: (e.match(/<published>([\s\S]*?)<\/published>/)||[])[1] || null,
      views:  (e.match(/views="(\d+)"/)||[])[1] || null,
      likes:  (e.match(/<media:starRating[^>]*count="(\d+)"/)||[])[1] || null,
      url:    (e.match(/<link rel="alternate" href="([^"]+)"/)||[])[1] || null,
    }));
    res.channelTitle = (rss.match(/<title>([\s\S]*?)<\/title>/)||[])[1] || null;
    res.videoCountInFeed = res.recent.length;
    res.ok = true;
  } catch(e){ res.error = String(e).slice(0,300); }
  return res;
}

// ---------- Browser-based platforms (Instagram / TikTok / LinkedIn / X) ----------
async function withBrowser(fn){
  let chromium;
  try { ({ chromium } = await import('playwright')); }
  catch { return { skipped:'playwright not installed — run: npm i playwright' }; }
  const { existsSync } = await import('node:fs');
  const exe = CHROMIUM_CANDIDATES.find(p => p && existsSync(p));
  const launchOpts = { headless:true };
  if (exe) launchOpts.executablePath = exe;
  if (process.env.HTTPS_PROXY) launchOpts.proxy = { server: process.env.HTTPS_PROXY };
  const browser = await chromium.launch(launchOpts);
  const ctx = await browser.newContext({ userAgent:UA, locale:'en-GB', viewport:{width:1280,height:900}, ignoreHTTPSErrors:true });
  try { return await fn(ctx); }
  finally { await browser.close(); }
}

async function grabMeta(ctx, url){
  const page = await ctx.newPage();
  const out = { url };
  try {
    const resp = await page.goto(url, { waitUntil:'domcontentloaded', timeout:35000 });
    out.status = resp ? resp.status() : null;
    await page.waitForTimeout(2500);
    out.title = await page.title();
    for (const [k,sel] of [['ogTitle','meta[property="og:title"]'],['ogDesc','meta[property="og:description"]'],['metaDesc','meta[name="description"]']]){
      out[k] = await page.locator(sel).first().getAttribute('content').catch(()=>null);
    }
    out.embeddedJson = await page.evaluate(() => {
      // capture the first large state blob many SPAs inline (IG/TikTok)
      const s = [...document.querySelectorAll('script')].map(x=>x.textContent||'')
        .find(t => /"edge_followed_by"|"follower_count"|SIGI_STATE|"stats":\{/.test(t));
      return s ? s.slice(0, 20000) : null;
    });
  } catch(e){ out.error = String(e).slice(0,220); }
  finally { await page.close(); }
  return out;
}

function parseIgCounts(meta){
  // IG og:description e.g. "12K Followers, 340 Following, 210 Posts - See Instagram photos..."
  const d = meta.ogDesc || meta.metaDesc || '';
  const m = d.match(/([\d.,KMkm]+)\s+Followers,\s+([\d.,KMkm]+)\s+Following,\s+([\d.,KMkm]+)\s+Posts/i);
  if (m) return { followers:m[1], following:m[2], posts:m[3] };
  const j = meta.embeddedJson || '';
  const f = j.match(/"edge_followed_by":\{"count":(\d+)\}/);
  return f ? { followers:f[1] } : null;
}

// ---------- Main ----------
const cfgPath = process.argv[2];
if (!cfgPath){ log('usage: node collect_social.mjs config.json'); process.exit(1); }
const cfg = JSON.parse(readFileSync(cfgPath,'utf8'));
const acc = cfg.accounts || {};
const data = { slug: cfg.slug, collectedAt:new Date().toISOString(), results:{} };

if (acc.youtube) { log('YouTube (RSS)…'); data.results.youtube = await collectYouTube(acc.youtube); }

const needsBrowser = ['instagram','tiktok','linkedin','x'].filter(p=>acc[p]);
if (needsBrowser.length){
  log('Browser pass for:', needsBrowser.join(', '));
  const browserData = await withBrowser(async ctx => {
    const r = {};
    if (acc.instagram){ const meta = await grabMeta(ctx, `https://www.instagram.com/${acc.instagram.replace(/^@/,'')}/`); r.instagram = { ...meta, parsed: parseIgCounts(meta) }; }
    if (acc.tiktok){ r.tiktok = await grabMeta(ctx, `https://www.tiktok.com/@${acc.tiktok.replace(/^@/,'')}`); }
    if (acc.linkedin){ r.linkedin = { note:'public view only — headline/name; engagement needs login', ...(await grabMeta(ctx, acc.linkedin)) }; }
    if (acc.x){ r.x = await grabMeta(ctx, `https://x.com/${acc.x.replace(/^@/,'')}`); }
    return r;
  });
  if (browserData.skipped) data.browserSkipped = browserData.skipped;
  else Object.assign(data.results, browserData);
}

// ---------- Write outputs ----------
const outDir = cfg.outDir || `outputs/${cfg.slug||'client'}`;
mkdirSync(outDir, { recursive:true });
writeFileSync(join(outDir,'collected-data.json'), JSON.stringify(data,null,2));

// human-readable markdown
let md = `# Collected public data — ${cfg.slug}\n\n_Collected ${data.collectedAt}. Public data only; blanks mean the platform hid it without login._\n`;
if (data.browserSkipped) md += `\n> ⚠️ Browser sites skipped: ${data.browserSkipped}\n`;
for (const [p,r] of Object.entries(data.results)){
  md += `\n## ${p}\n`;
  if (r.error) md += `- ⚠️ error: ${r.error}\n`;
  if (r.status && r.status>=400) md += `- ⚠️ HTTP ${r.status} (likely blocked/login-walled)\n`;
  if (p==='youtube' && r.ok){
    md += `- Channel: ${r.channelTitle||'?'} (${r.channelId})\n- Subscribers: ${r.subscribers||'[hidden]'}\n- Recent videos (${r.videoCountInFeed}):\n`;
    for (const v of (r.recent||[])) md += `  - **${v.views||'?'} views** · ${v.title} · ${(v.published||'').slice(0,10)}\n`;
  } else {
    if (r.parsed) md += `- Followers: ${r.parsed.followers||'?'} · Following: ${r.parsed.following||'?'} · Posts: ${r.parsed.posts||'?'}\n`;
    if (r.ogTitle) md += `- Title: ${r.ogTitle}\n`;
    if (r.ogDesc||r.metaDesc) md += `- Bio/desc: ${(r.ogDesc||r.metaDesc).slice(0,300)}\n`;
    if (r.note) md += `- Note: ${r.note}\n`;
  }
}
md += `\n---\n_Next: hand collected-data.md to the \`social-media-audit\` skill to produce the grounded audit._\n`;
writeFileSync(join(outDir,'collected-data.md'), md);

log('done →', join(outDir,'collected-data.md'));
console.log(md);
