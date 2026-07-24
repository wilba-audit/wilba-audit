#!/usr/bin/env node
/**
 * parse_exports.mjs — WILBA owner-export parser
 * ---------------------------------------------
 * Ingests the analytics files an ACCOUNT OWNER can legitimately export from each
 * platform (no scraping, no login) and turns them into a structured summary the
 * `social-media-audit` skill can consume. This is the compliant, works-anywhere
 * path: the client exports her own data; we parse it.
 *
 * Currently handles well:
 *   - LinkedIn "Profile Growth and Discovery" CSVs
 *       (Date, Views, Reach, Reposts, Followers)  and  (Date, Page Followers)
 *   - Generic tabular CSVs (best-effort numeric summary)
 * Best-effort / extensible:
 *   - Meta "Download Your Information" JSON (Instagram/Facebook) — points you to
 *     the relevant files; full parsing is added per client as formats vary.
 *
 * USAGE
 *   node parse_exports.mjs <dir-or-file> [<dir-or-file> ...] [--out summary.md]
 * Prints a Markdown summary and (with --out) writes it to a file.
 * Never invents a value; blanks stay blank and are reported honestly.
 */

import { readFileSync, readdirSync, statSync, writeFileSync } from 'node:fs';
import { join, basename, extname } from 'node:path';

const args = process.argv.slice(2);
let outFile = null;
const inputs = [];
for (let i = 0; i < args.length; i++) {
  if (args[i] === '--out') { outFile = args[++i]; continue; }
  inputs.push(args[i]);
}
if (!inputs.length) { console.error('usage: node parse_exports.mjs <dir-or-file> [--out summary.md]'); process.exit(1); }

// expand dirs → files
const files = [];
for (const p of inputs) {
  const st = statSync(p);
  if (st.isDirectory()) for (const f of readdirSync(p)) files.push(join(p, f));
  else files.push(p);
}

const num = x => { x = String(x ?? '').trim().replace(/[",]/g, ''); return /^\d+(\.\d+)?$/.test(x) ? Number(x) : null; };

// minimal CSV parser (handles quoted fields with commas)
function parseCSV(text){
  const rows = [];
  for (const line of text.split(/\r?\n/)) {
    if (line === '') continue;
    const cells = []; let cur = '', q = false;
    for (const ch of line) {
      if (ch === '"') q = !q;
      else if (ch === ',' && !q) { cells.push(cur); cur = ''; }
      else cur += ch;
    }
    cells.push(cur);
    rows.push(cells.map(c => c.replace(/^﻿/, '').trim()));
  }
  return rows;
}

function summariseLinkedInProfile(name, rows){
  const data = rows.slice(1).filter(r => r.some(c => c !== ''));
  const views = data.map(r => num(r[1])).filter(v => v !== null);
  const reach = data.map(r => num(r[2])).filter(v => v !== null);
  const reps  = data.map(r => num(r[3])).filter(v => v !== null);
  const fol   = data.map(r => num(r[4])).filter(v => v !== null);
  const first = fol[fol.length - 1], last = fol[0];
  const vTot = views.reduce((a,b)=>a+b,0);
  const postDays = views.filter(v => v > (vTot/Math.max(views.length,1))).length; // rough: above-avg days ≈ post days
  return {
    kind: 'linkedin-profile', name,
    followers: last, followerChange: (last!=null&&first!=null)?last-first:null,
    daysWithData: views.length,
    viewsTotal: vTot, viewsAvg: views.length?Math.round(vTot/views.length):null,
    viewsMin: views.length?Math.min(...views):null, viewsMax: views.length?Math.max(...views):null,
    volatility: (views.length&&Math.min(...views)>0)?Math.round(Math.max(...views)/Math.min(...views)):null,
    repostsTotal: reps.reduce((a,b)=>a+b,0),
    reachVals: reach,
    approxPostDays: postDays,
  };
}

function summarise(file){
  const ext = extname(file).toLowerCase();
  const name = basename(file);
  try {
    if (ext === '.csv') {
      const rows = parseCSV(readFileSync(file, 'utf8'));
      const hdr = (rows[0] || []).map(h => h.toLowerCase());
      if (hdr.includes('followers') && hdr.includes('reposts')) return summariseLinkedInProfile(name, rows);
      if (hdr.some(h => h.includes('page followers'))) {
        const data = rows.slice(1).map(r => num(r[1])).filter(v => v !== null);
        return { kind:'linkedin-page', name, pageFollowers:data[0]??null, change:(data.length>1)?data[0]-data[data.length-1]:null, series:data };
      }
      // generic csv
      const colN = rows[0]?.length || 0;
      return { kind:'generic-csv', name, columns:rows[0], rows:rows.length-1 };
    }
    if (ext === '.json') {
      const j = JSON.parse(readFileSync(file,'utf8'));
      return { kind:'json', name, topKeys:Object.keys(j).slice(0,12), note:'Meta DYI/IG insights — structure varies; parse per client.' };
    }
    return { kind:'unknown', name, note:'unrecognised export type' };
  } catch(e){ return { kind:'error', name, error:String(e).slice(0,160) }; }
}

const results = files.map(summarise);

// dedupe identical linkedin-profile summaries (same followers+views), flag as duplicate export
const seen = new Map();
for (const r of results) {
  if (r.kind === 'linkedin-profile') {
    const key = `${r.followers}|${r.viewsTotal}`;
    if (seen.has(key)) r.duplicateOf = seen.get(key); else seen.set(key, r.name);
  }
}

// ---- Markdown report ----
let md = `# Ingested analytics summary\n\n_Parsed ${files.length} file(s). Owner exports only — no scraped or invented data._\n`;
const profiles = results.filter(r => r.kind === 'linkedin-profile' && !r.duplicateOf);
const dups = results.filter(r => r.duplicateOf);
const pages = results.filter(r => r.kind === 'linkedin-page');

if (profiles.length) {
  md += `\n## LinkedIn profiles\n\n| File | Followers | Δ/week | Avg views/day | View swing | Reposts | Post-days≈ |\n|---|--:|--:|--:|--:|--:|--:|\n`;
  for (const p of profiles)
    md += `| ${p.name} | ${p.followers ?? '?'} | ${p.followerChange!=null?(p.followerChange>=0?'+':'')+p.followerChange:'?'} | ${p.viewsAvg ?? '?'} | ${p.viewsMin ?? '?'}→${p.viewsMax ?? '?'}${p.volatility?` (${p.volatility}×)`:''} | ${p.repostsTotal} | ${p.approxPostDays} |\n`;
  if (profiles.length > 1)
    md += `\n> ⚠️ **${profiles.length} distinct LinkedIn profiles detected** (different follower counts) — likely a fragmented presence. Confirm which is primary.\n`;
}
if (dups.length) md += `\n_(Ignored ${dups.length} duplicate export(s): ${dups.map(d=>d.name).join(', ')}.)_\n`;
if (pages.length) { md += `\n## LinkedIn company page(s)\n`; for (const p of pages) md += `- **${p.name}**: ${p.pageFollowers ?? '?'} followers (${p.change!=null?(p.change>=0?'+':'')+p.change:'?'} over range)${p.pageFollowers!=null&&p.pageFollowers<50?' — essentially dormant':''}\n`; }

const others = results.filter(r => !['linkedin-profile','linkedin-page'].includes(r.kind) && !r.duplicateOf);
if (others.length){ md += `\n## Other files\n`; for (const o of others) md += `- **${o.name}** (${o.kind})${o.note?` — ${o.note}`:''}${o.error?` — ⚠️ ${o.error}`:''}\n`; }

md += `\n---\n_Next: feed this summary to \`social-media-audit\` for the grounded audit. For post-STYLE review, add screenshots and use the manual-review-protocol._\n`;

console.log(md);
if (outFile) { writeFileSync(outFile, md); console.error('[ingest] wrote', outFile); }
