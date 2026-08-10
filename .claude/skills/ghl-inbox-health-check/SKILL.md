---
name: ghl-inbox-health-check
description: >-
  Use when auditing or troubleshooting a GoHighLevel shared inbox (the
  Conversations tab: WhatsApp, SMS, email) for a client build, or running a
  routine health check before or after go-live. Covers the whole inbound and
  outbound pipeline: WhatsApp Business / Coexistence connection, messaging
  wallet and billing, Meta Business verification, inbound webhooks, the 24-hour
  customer-service window and approved templates, user access and
  notifications, and double-messaging. Produces a plain-English health report,
  a prioritised fix list, and a ready-to-send message for the developer. Built
  for non-technical operators. Trigger on: "inbox not working", "messages not
  coming through", "can't reply", "WhatsApp not connected", "conversations not
  loading", "double messaging", "shared inbox audit", "is the inbox working",
  "GHL health check".
---

# GHL Inbox Health Check

You are running a **calm, methodical health check on a GoHighLevel shared inbox** for a non-technical operator (Jess). Your job is to find out exactly where the WhatsApp-to-GHL pipeline is broken, tell her in plain English, fix what she can fix herself, and hand the rest to the developer with the precise detail he needs. No jargon dumps. One step at a time.

## Pin the context first

- **This is operational, not clinical.** The GHL inbox handles patient conversations; the clinical record stays in Semble. Never suggest moving clinical content into GHL.
- **Who owns what:** the developer (Griffin) builds and owns the GHL/WhatsApp configuration; Jess owns the workstream and runs this check. Some fixes are Jess's (wallet, users, moving the team to GHL-only); some are Griffin's (webhooks, reconnection, templates).
- **The Schoeman inbox specifics:** WhatsApp runs on **Coexistence** (the phone WhatsApp app and the Cloud API together). The clinic number is **+44 7426 494321**. PAs on the inbox are **Zoey, Louise, Isabell**, office hours Mon–Fri 9–5. (Lisa's departure is confidential — do not surface it in anything team-facing.)
- **Access limit:** a cloud dev session usually cannot reach GHL directly (network block, no connector, no stored credentials). So run this as a **guided diagnostic** — you tell Jess exactly what to click and read back — unless GHL API credentials are available, in which case use the automated layer at the end.

## Step 0 — Pin the symptom before touching anything

Ask, and get a clear answer, before diagnosing. This alone usually halves the possible causes:
1. **Inbound, outbound, or both?** Are new messages not *arriving* in Conversations, or can the team not *send/reply*, or both?
2. **When did it start,** and did anything change around then (a migration, a workflow switched on, a billing lapse, a phone reset)?
3. **Who is affected** — everyone, or one PA?
4. **Any error message** on screen? Read it out.

Record the answers. They point straight at the section below.

## The pipeline — what a working inbox needs (check in this order)

Each link must be healthy. Walk them top to bottom; stop and fix at the first failure, then continue.

**1. WhatsApp connection.**
GHL → Settings → Integrations / Phone Numbers / WhatsApp. Is the clinic number shown as **Connected** (green), not "disconnected" or "pending"? On Coexistence, confirm the phone app is still linked and the Cloud API connection is live.

**2. Messaging wallet / billing.**
GHL → Settings → Company Billing / Wallet. Is the **balance above zero**, and is **auto-recharge on**? WhatsApp/LC messaging is prepaid — an empty wallet stops sending completely, which reads as "the inbox died." This is the single most common cause; check it early.

**3. Meta Business verification & WABA health.**
Meta Business Manager → Security Center. Is the business **verified** and the WhatsApp number in **good standing** (not restricted, quality not flagged red)? A lapsed verification or a quality drop blocks business-initiated messaging.

**4. Inbound test (live).**
From a personal phone, send a WhatsApp to **+44 7426 494321**. Within ~1 minute it should appear in GHL → Conversations. If it does not arrive, the inbound webhook or the connection (steps 1/3) is the problem.

**5. Outbound test (live).**
Reply to that test message from inside GHL. Within the 24-hour window a free-form reply should deliver (ticks). **Outside 24 hours** of the patient's last message, GHL blocks free-form and requires a **Meta-approved template** — if that's what's happening, it's not "broken," it's the window. Confirm at least one approved template exists.

**6. User access & notifications.**
Each PA should be logged into the correct sub-account, able to see Conversations, and receiving notifications. Confirm no one is locked out, removed, or on the wrong location. Remove any test users.

**7. Double-messaging / Coexistence.**
If patients get answered twice, the team is likely replying in **both** the phone WhatsApp app and GHL (Coexistence mirrors both). The fix is operational: move the team to **GHL-only** for replies. Get a screenshot to confirm before changing anything.

## Triage table

| Symptom | Most likely cause | Where to check | Who fixes |
| --- | --- | --- | --- |
| Nothing sends; looks totally dead | Wallet empty | Billing / Wallet balance | Jess / clinic (top up) |
| Business-initiated messages blocked | Meta verification lapsed / WABA restricted | Meta Business Manager → Security Center | Griffin + clinic docs |
| Number shows disconnected / pending | WhatsApp / Coexistence connection dropped | Settings → WhatsApp | Griffin (reconnect) |
| Inbound messages not arriving | Webhook down or connection broken | Inbound live test (Step 4) | Griffin |
| Can't send after a gap, but recent chats work | 24-hour window; needs approved template | Try replying to a >24h old chat | Griffin (templates) |
| One PA can't see the inbox | User access / wrong location | Settings → Team / My Staff | Jess / Griffin |
| Patients answered twice | Coexistence mirroring (app + GHL) | Ask team where they reply | Jess (move to GHL-only) |

## Output — the health report

After the walk-through, give Jess a short report, not a transcript:
- **One-line verdict:** "Inbox healthy," or "Down — cause: [X]."
- **Pipeline results:** each of the 7 links marked healthy / failed, in plain English.
- **Fix list, prioritised:** what she can fix now (with the exact clicks), and what to hand Griffin.
- **Message to Griffin (drafted):** the symptom (inbound/outbound/both), when it started, which link failed, and the error text — so he can act without a back-and-forth. Keep it factual and short.

## Go-live readiness (use the same steps as a pre-launch check)

Before launch, all seven links should pass **and**: at least one approved template exists for out-of-window messages; every PA has done a successful send and receive; notifications are on; the wallet has auto-recharge; and the team knows to reply in GHL only. Report it as a simple checklist.

## Automated layer (optional, once credentials exist)

If GHL API access is provided (location ID + API key, stored as repo/GitHub secrets — never in chat), a health-check script can run server-side (mirroring the pattern already used for the Monkey Joe's `mj_ghl_audit` GitHub Action, because the dev network blocks GHL) and commit a report: connection status, recent inbound/outbound counts, wallet balance, and any restricted state. Build this only when the developer supplies access; until then, the guided diagnostic above is the tool.

## Guardrails

- Never invent a status you cannot see — if you can't reach GHL, say so and guide Jess to read it out.
- Change nothing live (users, templates, connection) without confirming with Jess first; some actions are Griffin's to make.
- Keep clinical content out of GHL; keep confidential team matters (e.g. staffing changes) out of anything team-facing.
