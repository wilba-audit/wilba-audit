# Clinic Pipeline

`clinic-pipeline.csv` — 80 private clinics (38 UK / 42 AU) in hormone, menopause,
longevity, functional medicine and doctor-led aesthetics. Built 24 Aug 2026.

## How it was built

Sourced by search, then **every clinic verified against its own website** via
domain-scoped search. Direct page fetching is blocked by this session's network
egress policy, so anything the site did not publish in a search-indexed page is
recorded as blank, never guessed. `email_source` says where each address came from.

- **62 of 80 are reachable by email** (was 42 — see the 20 Sep pass below).
- 17 publish no reachable address (form, phone, ticket portal, or an address that
  only renders in a browser). That absence is itself a qualifying signal and is
  written into `opening_angle`.
- 1 is disqualified: The Longevity Doctor now redirects to a different company.

## Columns

| Column | Meaning |
|---|---|
| `priority` | A = named owner + published email + high fee + clear weakness · B = partial · C = too large, too cheap, or a chain |
| `opening_angle` | A specific, verified fact about how that clinic handles enquiries. Use it as the first line. Not a guess — each one came off their own site. |
| `fit_flag` | Where the clinic likely breaks the 2–15 staff profile |
| `status` | New → Draft ready → Emailed → Follow-up 1 → Follow-up 2 → Replied → Call booked → Proposal sent → Won / Lost / Disqualified |
| `next_action` / `next_action_date` | What happens next and when |

## Working it

Ten drafts are in Gmail waiting for approval (see `first-10-outreach.md`).
Daily rhythm: Claude drafts 10, Jess approves and sends, Claude tracks replies
and follow-ups at day 3, 7 and 14, and updates `status` here.

## The 20 Sep 2026 pass

The session that built this list could not fetch web pages, so anything not visible
in a search-index snippet was left blank. A later session could reach the sites, so
all 38 blanks were re-checked against the clinics' own contact pages:

- **24 now have a real published address**, read off the page. None constructed.
- **4 publish an address that is Cloudflare-obfuscated** — present on the page and
  readable in a browser, but not machine-readable (17, 20, 59, 79).
- **9 genuinely publish no email**: form and/or phone only.
- **1 (Esteem Clinic, 52)** blocks automated access and needs a manual look.

The 19 A-priority addresses that already existed were re-verified at the same time.
**Nine of their opening angles were wrong** and four clinics lost their address
entirely — the original pass inferred from search snippets rather than live pages,
so some entries were never right. Treat any row whose `email_source` does not say
"verified 20 Sep 2026" as unconfirmed.

**Not yet done:** the B and C priority addresses from the original 42 have not been
re-verified and carry the same risk.
