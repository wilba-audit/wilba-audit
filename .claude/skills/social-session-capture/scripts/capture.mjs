#!/usr/bin/env node
/**
 * capture.mjs — WILBA human-in-the-loop authenticated capture
 * -----------------------------------------------------------
 * "Logs in via Playwright" the RESPONSIBLE way: the ACCOUNT OWNER logs in
 * themselves in a visible browser (they type the password, they do 2FA), the
 * session is saved locally, and we then capture THEIR OWN pages (analytics,
 * recent activity) for review.
 *
 *   • No passwords are stored or typed by the bot — the human logs in.
 *   • Headed (visible) browser by default — a person is in control.
 *   • Runs on the owner's machine; the session file stays local (gitignored).
 *   • Only visits URLs YOU pass (the owner's own pages), at a gentle pace.
 *
 * ⚠️ USE ONLY on accounts you own or have explicit permission to access.
 *    Automated *scraping* of these platforms can still breach their terms and
 *    put an account at risk — keep it light, keep a human present, and prefer
 *    the owner's native "export/download your data" where possible.
 *
 * ⚠️ Will NOT run inside the Claude web sandbox (egress to social hosts is
 *    blocked). Run it on a normal computer.
 *
 * STEP 1 — save a login session (opens a window; you log in; press Enter):
 *   node capture.mjs login linkedin
 *   node capture.mjs login instagram
 *
 * STEP 2 — capture your own pages listed in a config:
 *   node capture.mjs capture config.json
 * where config.json =
 *   {
 *     "slug": "schoeman",
 *     "platform": "linkedin",
 *     "outDir": "outputs/schoeman/captures",
 *     "consent": "I own or have explicit permission to access these accounts",
 *     "pages": [
 *       { "name": "recent-activity", "url": "https://www.linkedin.com/in/…/recent-activity/all/" },
 *       { "name": "analytics",       "url": "https://www.linkedin.com/…/analytics/" }
 *     ]
 *   }
 * Saves full-page screenshots + extracted visible text per page.
 */

import { chromium } from 'playwright';
import { mkdirSync, existsSync, writeFileSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import readline from 'node:readline';

const CHROMIUM_CANDIDATES = [
  process.env.CHROMIUM_PATH,
  '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  '/opt/pw-browsers/chromium/chrome-linux/chrome',
];
const exe = CHROMIUM_CANDIDATES.find(p => p && existsSync(p));
const AUTH_DIR = '.auth';
const LOGIN_URLS = {
  linkedin:  'https://www.linkedin.com/login',
  instagram: 'https://www.instagram.com/accounts/login/',
  facebook:  'https://www.facebook.com/login/',
  tiktok:    'https://www.tiktok.com/login',
};

function launchOpts(headed){
  const o = { headless: !headed };
  if (exe) o.executablePath = exe;
  if (process.env.HTTPS_PROXY) o.proxy = { server: process.env.HTTPS_PROXY };
  return o;
}
const ask = q => new Promise(res => {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  rl.question(q, a => { rl.close(); res(a); });
});

async function doLogin(platform){
  const url = LOGIN_URLS[platform];
  if (!url) { console.error('unknown platform:', platform, '— known:', Object.keys(LOGIN_URLS).join(', ')); process.exit(1); }
  mkdirSync(AUTH_DIR, { recursive: true });
  console.log(`\nOpening a VISIBLE browser at ${platform} login.`);
  console.log('→ Log in yourself (password + any 2FA). The bot will NOT touch your credentials.');
  const browser = await chromium.launch(launchOpts(true));
  const ctx = await browser.newContext({ locale: 'en-GB', viewport: { width: 1280, height: 900 } });
  const page = await ctx.newPage();
  await page.goto(url, { waitUntil: 'domcontentloaded' }).catch(()=>{});
  await ask('\nWhen you are fully logged in, come back here and press ENTER to save the session… ');
  const out = join(AUTH_DIR, `${platform}.json`);
  await ctx.storageState({ path: out });
  await browser.close();
  console.log(`✓ Session saved to ${out} (local only — keep it private; it is gitignored).`);
}

async function doCapture(cfgPath){
  const cfg = JSON.parse(readFileSync(cfgPath, 'utf8'));
  if (!/permission|own/i.test(cfg.consent || '')) {
    console.error('✗ Refusing: set "consent" in the config confirming you own or have explicit permission for these accounts.');
    process.exit(1);
  }
  const auth = join(AUTH_DIR, `${cfg.platform}.json`);
  if (!existsSync(auth)) { console.error(`✗ No saved session for ${cfg.platform}. Run:  node capture.mjs login ${cfg.platform}`); process.exit(1); }
  const outDir = cfg.outDir || `outputs/${cfg.slug||'client'}/captures`;
  mkdirSync(outDir, { recursive: true });

  // Headed by default so a human can watch; set HEADLESS=1 to override on your own machine.
  const browser = await chromium.launch(launchOpts(!process.env.HEADLESS));
  const ctx = await browser.newContext({ storageState: auth, locale: 'en-GB', viewport: { width: 1280, height: 1000 } });
  const index = [];
  for (const p of (cfg.pages || [])) {
    const page = await ctx.newPage();
    try {
      console.log('▶ capturing', p.name, '—', p.url);
      await page.goto(p.url, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await page.waitForTimeout(3500);
      // gentle scroll to load a few posts, human-paced
      for (let i = 0; i < 5; i++) { await page.mouse.wheel(0, 1400); await page.waitForTimeout(1500 + i*300); }
      const shot = join(outDir, `${p.name}.png`);
      await page.screenshot({ path: shot, fullPage: true });
      const text = (await page.evaluate(() => document.body.innerText || '')).replace(/\n{3,}/g, '\n\n').slice(0, 12000);
      writeFileSync(join(outDir, `${p.name}.txt`), text);
      index.push({ name: p.name, screenshot: shot, textChars: text.length });
    } catch (e) { console.error('  ⚠️', p.name, String(e).slice(0,140)); index.push({ name: p.name, error: String(e).slice(0,140) }); }
    await page.waitForTimeout(2500); // pacing between pages
    await page.close();
  }
  await browser.close();
  writeFileSync(join(outDir, 'captures-index.json'), JSON.stringify(index, null, 2));
  console.log(`\n✓ Captured ${index.length} page(s) → ${outDir}`);
  console.log('  Give the .png + .txt files to the social-media-audit skill for the grounded review.');
}

const [cmd, arg] = process.argv.slice(2);
if (cmd === 'login' && arg) await doLogin(arg);
else if (cmd === 'capture' && arg) await doCapture(arg);
else { console.error('usage:\n  node capture.mjs login <linkedin|instagram|facebook|tiktok>\n  node capture.mjs capture config.json'); process.exit(1); }
