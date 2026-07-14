# /mj-ghl — Monkey Joe's GHL Account Health Check & Operations

> Monkey Joe's runs on GoHighLevel (GHL / LeadConnector). Two sub-accounts:
> **Pointe Orlando (POL)** and **Winter Park (WP)**. Everything is driven by contact tags.
> This command inspects and operates that account in plain English.

## When Jess runs this
She'll say `/mj-ghl` — usually meaning "tell me what's going on in the GHL account" or
"do X in GHL." Figure out which from her words. Default to the **health check** (Section A)
if she just runs it bare.

## Credentials
The live automations authenticate with GitHub Actions **secrets**:
`GHL_API_KEY_POL`, `GHL_LOCATION_ID_POL`, `GHL_API_KEY_WP`, `GHL_LOCATION_ID_WP`.
For a **local** run you need those same values in `.env` at repo root. If `.env` is missing
or the keys aren't set, DON'T guess — tell Jess: *"The GHL keys live in GitHub secrets. Paste
me both location API keys + location IDs and I'll run this live, or I can trigger the GitHub
Action instead."* Never print secret values back to her.

## The GHL API (for reference — the scripts already wrap this)
- Base: `https://services.leadconnectorhq.com`
- Header `Version: 2021-07-28` for contacts; `2021-04-15` for conversations/messages
- Auth: `Authorization: Bearer <location API key>`
- Search contacts: `POST /contacts/search` with `{locationId, pageLimit, page, filters:[{field,operator,value}]}`
- Custom fields: `GET /locations/{locationId}/customFields`
- Add tag: `POST /contacts/{id}/tags` `{tags:[...]}`
- Send message: `POST /conversations/messages` (Email or SMS)
- Reuse the proven helpers in `scripts/mj_weekend_bananas_blast.py`
  (`fetch_audience`, `send_message`, `apply_cohort_tag`).

## Key tags in use
- `voucher-delivered` — the broad opted-in audience (both locations)
- `unsubscribed` — always exclude
- Lead tags: `bogo-{loc}-lead`, `half-{loc}-lead`, `50off-{loc}-lead`, `birthday-{loc}-lead`
- Redemption tags: `redeemed-{loc}`, `promo-redeemed-{loc}`, channel split `redeemed-{loc}-g|f|e|d`
- Birthday sequence: `bday-start-YYYY-MM-DD`, `bday-sent-dN`, `bday-radar-{window}-{year}`, `birthday-{loc}-booked`

---

## Section A — Health Check (default)

Run this and report in a short, plain-English scorecard. Do it for **both** POL and WP.

1. **Connection test.** Confirm both API keys authenticate (a single `contacts/search` with
   `pageLimit:1`). If either fails, say which and stop for that location.
2. **Audience sizes.** Count contacts for: `voucher-delivered`, `unsubscribed`, each lead tag,
   each redemption tag. Present as a small table per location.
3. **Custom fields.** Pull `GET /locations/{id}/customFields`. Confirm the **child-birthday
   field exists** and report its **field ID** (this is the `CHILD_BDAY_FIELD_ID` the birthday
   radar needs). Flag if missing.
4. **Tag hygiene.** List tags actually in use. Flag inconsistencies — e.g. old `WACKY-*` /
   Aluvii-era codes vs the live `redeemed-*` / `bogo-*` scheme. Note anything that looks
   orphaned or misspelled.
5. **Deliverability sanity.** Confirm the sending identity (`hello@monkeyjoespo.com`) and
   whether WP should send from its own domain.
6. **Verdict.** Green/amber/red per location, with the 1–3 things most worth fixing.

## Section B — Operations (when she asks for an action)
- **Send a blast:** adapt `scripts/mj_weekend_bananas_blast.py`. ALWAYS dry-run first, show her
  the audience size + a preview, and get a "yes" before `--execute`.
- **Tag cleanup / re-tagging:** propose the change, show counts affected, confirm, then apply.
- **Add/verify a custom field:** create via API only after confirming with her.

## Guardrails
- Every send or bulk tag change is **dry-run first, confirm, then execute**. Never send to a
  live audience without explicit go-ahead.
- Respect `unsubscribed` — always excluded.
- Report numbers, not jargon. Jess is non-technical: "1,240 opted-in parents at Pointe Orlando,
  38 unsubscribed" — not raw JSON.

## After running
If you changed anything (tags, fields, sends), note it and consider whether
`outputs/monkey-joes/` docs or CLAUDE.md need updating.
