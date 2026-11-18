# GTA 6 Codes Venture: Phased Roadmap

Effort figures are rough estimates of **human** hours, assuming Claude drafts the work. "Dev" means your developer.

## Phase 0: Foundations and launch-week capture (Days 0–3, starting 18 Nov 2026)
| # | Task | Deliverable | Depends on | Effort | Done when |
|---|---|---|---|---|---|
| 0.1 | Decide the brand name (no GTA or Rockstar marks) and check domain and handle availability | Name and domain registered; handles reserved on YouTube, TikTok, IG and X | — | 1–2 h Jess | Domain owned; the same handle secured on 3+ platforms |
| 0.2 | Secure testing capability | Console, game copy and capture method working (PS5 or Xbox built-in capture is enough) | Game purchase | 1 h plus the purchase | A 30-second test clip captured and transferred to Drive |
| 0.3 | Create accounts | Google account for the brand; Search Console and GA4 (pending domain); Beehiiv/Kit; Cloudflare; private GitHub repo | 0.1 | 1.5 h Jess, or dev | Logins stored in a password manager, not in chat or the repo |
| 0.4 | Start the ledger | `code-ledger.csv` with launch claims logged as Unverified (agent), and offers rows F4 | — | Agent plus 20 min review | Every row has a source and `date_first_seen` |
| 0.5 | Launch-day test session | Test the top claimed cheats on camera and record the game version | 0.2, 0.4 | 2–3 h Tester | Each tested claim has a verdict and an evidence clip |
| 0.6 | Email Take-Two about monetisation | Polite question to copyright@take2games.com; keep the reply | — | 15 min | Sent; the reply is logged in `/outputs/gta6-codes/legal-log.md` |

## Phase 1: MVP live (Week 1)
| # | Task | Deliverable | Depends on | Effort | Done when |
|---|---|---|---|---|---|
| 1.1 | Scaffold the Astro site and ledger rendering | Repo, site deployed on Cloudflare Pages with a preview URL per PR | 0.3 | Dev 6–10 h (Claude Code can do most of it) | Ledger CSV renders as an accessible table with status badges |
| 1.2 | Write the MVP pages (§3.2 of the plan) | ~12 pages, including disclaimer, editorial policy, corrections | 1.1, 0.4 | Agent drafts, then Jess reviews 2–3 h | Every factual line ties to a ledger row or a cited source |
| 1.3 | Technical SEO basics | Sitemap, robots, schema, OG, GSC and Bing submitted | 1.1 | Dev 2 h | GSC shows the sitemap processed |
| 1.4 | EP1 long-form and 5–7 verdict Shorts | Published videos linked to ledger rows | 0.5 | Host and editor 8–12 h | Passed `gta6-publish-gate`; Jess approved |
| 1.5 | Email signup ("Ledger alerts") | Form on hub and cheats page, welcome email | 0.3 | 1 h | Test signup received |

## Phase 2: Production rhythm (Weeks 2–4)
| # | Task | Deliverable | Depends on | Effort / week | Done when |
|---|---|---|---|---|---|
| 2.1 | Weekly episode cycle (§4.2) | 1 long-form and 3–5 clips per week | Phase 1 | 6–10 h human | 3 consecutive weeks shipped on schedule |
| 2.2 | Guides cluster | Trophies, how-to-enter and scams pages built from real tests | Tests done | 2 h review | Pages indexed in GSC |
| 2.3 | Automations A2 (validation and deploy) and A3 (staleness) | GitHub Actions running | 1.1 | Dev 4–6 h | A bad row blocks a merge; stale rows raise an issue |
| 2.4 | Corrections flow A7 | Form to issue to Slack | 1.1 | Dev 2 h | Test correction processed end to end |
| 2.5 | Install the skills team | Six skills used for every task | — | Done in draft; tuning 2 h | Each skill used at least twice and tweaked from feedback |

## Phase 3: Automate and monetise (Months 2–3)
| # | Task | Deliverable | Depends on | Effort | Done when |
|---|---|---|---|---|---|
| 3.1 | A4 video-to-clips package | Drive drop produces `package.md` | 2.1 | Dev 6–8 h | 2 episodes packaged automatically |
| 3.2 | A6 weekly scorecard | Monday email | GSC, GA4 and YouTube API access | Dev 4–6 h | 4 consecutive scorecards |
| 3.3 | A1 claims inbox | Daily PR of proposed Unverified rows | 2.3 | Dev 4 h | 1 week of runs with fewer than 20% junk claims |
| 3.4 | Affiliate setup | Disclosure page, 3–5 relevant links | Traffic exists | 2 h | Links live, disclosure visible |
| 3.5 | Monetisation readiness | Ad network or YPP application, if eligible and the Take-Two answer allows it | 0.6 | 2 h | Decision logged |

## Phase 4: Scale (Months 3–6)
- **A5 draft scheduling.** Human still flips to public.
- **PC launch wave.** Pre-built pages, test plan and a PC capture setup, once a date is announced [VERIFY].
- **Second host or tester** (contractor) using the SOPs. Measure hours per episode.
- **Expand scope** beyond GTA 6 only if the KPIs justify it. The brand name already allows it.
- **Package the system as a WILBA case study** with `/share`.
