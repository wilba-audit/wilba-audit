# Clinic Pipeline

`clinic-pipeline.csv` — 80 private clinics (38 UK / 42 AU) in hormone, menopause,
longevity, functional medicine and doctor-led aesthetics. Built 24 Aug 2026.

## How it was built

Sourced by search, then **every clinic verified against its own website** via
domain-scoped search. Direct page fetching is blocked by this session's network
egress policy, so anything the site did not publish in a search-indexed page is
recorded as blank, never guessed. `email_source` says where each address came from.

- 42 of 80 publish a contact email — those are ready to contact today.
- 38 do not (enquiry form or phone only). That absence is itself a qualifying
  signal and is written into `opening_angle`.

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

**Not yet done:** finding emails for the 38 clinics that don't publish one.
Most list a named doctor, so the address is usually findable — that's the next
research pass, or a paid enrichment tool once volume justifies it.
