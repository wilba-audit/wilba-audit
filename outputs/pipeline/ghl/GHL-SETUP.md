# Clinic outreach in GoHighLevel: setup guide

What this builds: a pipeline board for 100 clinic prospects, every prospect loaded as a
contact with a personal first email, and one workflow that sends four emails over seven
days, moves each card along the board, and stops the moment someone replies.

**Nothing sends until the workflow is published.** Build it, test it on your own email
address, and only then switch it on.

Files in this folder:

- `ghl-import.csv` — the 100 prospects, ready for GHL's contact import
- `email-sequence.md` — the four emails, word for word (Dean Jackson style, with the refund guarantee)
- `email-1-preview.md` — the first email exactly as each of the 100 clinics will get it
- `scripts/wilba_ghl_load.py` + the "WILBA GHL load" GitHub Action — loads the same 100
  through the API instead of the CSV, once a token is in place

---

## What's left for you (about 20 minutes)

1. Make a separate WILBA sub-account in GHL (step 1).
2. Create the **Clinic outreach** pipeline with the 11 stages (step 2).
3. Then **either** upload `ghl-import.csv` yourself (steps 3 and 4), **or** send Claude a
   Private Integration token and your Location ID and Claude loads all 100 for you.
4. Build the two workflows (step 5) and test on your own email (step 6).
5. Confirm the refund guarantee with Griffin, and choose how to send (see the end of this guide).
6. Tell Claude "go". Nothing sends before that.

---

## 1. Use a separate sub-account

Create (or use) a sub-account just for WILBA's own sales, not one shared with any
client. If cold email ever gets an account flagged, it should only be this one.

## 2. Create the pipeline

Opportunities → Pipelines → Create new pipeline. Name: **Clinic outreach**.

| # | Stage | Moved by |
|---|---|---|
| 1 | New prospect | Import |
| 2 | Email 1 sent | Workflow |
| 3 | Follow-up 1 sent | Workflow |
| 4 | Follow-up 2 sent | Workflow |
| 5 | Final email sent | Workflow |
| 6 | Replied | Workflow (on reply) |
| 7 | Call booked | You |
| 8 | Proposal sent | You |
| 9 | Won | You |
| 10 | No response | Workflow (day 7, no reply) |
| 11 | Not interested | You |

## 3. Create the custom fields

Settings → Custom Fields → Add field (Contact):

| Name | Type |
|---|---|
| Cold subject | Single line |
| Cold opener | Multi line |
| CRM phrase | Single line |
| Timezone line | Single line |
| Pipeline ID | Single line |
| ICP grade | Single line |

GHL turns these into the merge tags `{{contact.cold_subject}}`, `{{contact.cold_opener}}`
and so on. Check the tag GHL shows for each field matches; if it differs, use GHL's.

## 4. Import the 100 prospects

Contacts → Import → upload `ghl-import.csv`.

- Map each column to the field of the same name (the four cold fields to the custom
  fields above).
- Tick **Create opportunities**, pipeline **Clinic outreach**, stage **New prospect**.
- Tags: the file already gives every contact `clinic-outreach` plus a grade tag
  (`grade-a`, `grade-b`, `grade-c`) and a country tag.

## 5. Build the workflow

Automation → Workflows → Create → Start from scratch. Name: **Clinic outreach sequence**.

**Settings (the cog):**
- **Stop on response: ON.** This is what stops follow-ups when someone replies.
- Allow re-entry: OFF.
- Time window: Mon to Fri, 8am to 4pm in the contact's timezone.

**Trigger:** Contact Tag added → `outreach-go`.
You start a batch by adding `outreach-go` to that day's contacts, so you control volume.

**Steps:**

1. **Drip mode**: batch size 10, every 1 day. (Raise to 15, then 20, once the first
   week shows no bounce or spam problems.)
2. **Send email**: Email 1 from `email-sequence.md`. From name "Jess Morrell".
3. **Update opportunity**: stage → Email 1 sent.
4. **Wait** 2 days.
5. **Send email**: Email 2. **Update opportunity** → Follow-up 1 sent.
6. **Wait** 2 days.
7. **Send email**: Email 3. **Update opportunity** → Follow-up 2 sent.
8. **Wait** 3 days.
9. **Send email**: Email 4. **Update opportunity** → Final email sent.
10. **Wait** 3 days, then **Update opportunity** → No response, and add tag
    `outreach-no-response`.

**Second, small workflow: "Clinic outreach replied".** Trigger: Customer replied
(channel: email), filter tag is `clinic-outreach`. Actions: update opportunity → Replied,
add tag `outreach-replied`, and send yourself an internal notification.

## 6. Test before going live

Create one contact with your own email, fill the four cold fields, add `outreach-go`,
and check that the email arrives in the inbox (not spam), reads correctly, and that the
card moves on the board. Reply to it and check the follow-ups stop.

## 7. Go live

Only after the sending setup below is in place and the test passes. Add `outreach-go`
to the first 10 grade-A contacts.

---

## Sending: the risk, plainly

GHL's own email service (LeadConnector) is shared by every GHL user, and its rules ban
sending to people who didn't opt in. These 100 addresses are public business inboxes,
which is legal to email in the UK, US and Australia with an opt-out, but it still counts
as cold email to GHL. If bounces or spam complaints pile up, GHL can suspend email on the
account, and if you send from `wilba.ai`, Gmail and Outlook start treating your real
business domain as a spammer too.

**Safest setup inside GHL (recommended):**

1. Buy a second domain that looks like yours (for example `getwilba.com`) and set up one
   Google Workspace mailbox on it, `jess@` that domain. About USD 10 a month for the
   domain and mailbox.
2. Add SPF, DKIM and DMARC records for it. Let it warm up for two weeks before sending
   (a warm-up tool, or just normal back-and-forth email).
3. In the WILBA sub-account, connect that mailbox as the email service (Settings → Email
   Services → SMTP or Google). Mail then goes out through Google, not GHL's shared
   servers, and replies land in that mailbox and in GHL's conversations.
4. Keep `wilba.ai` out of cold sends entirely. Replies that turn into real conversations
   can move to `jess@wilba.ai`.
5. 10 a day, rising to 20 over two weeks. Plain text, opt-out line, postal address.

**Faster but riskier:** send from GHL's built-in email straight away. It works, but it's
the setup most likely to get the account flagged.

**Safest overall (the earlier recommendation):** send through Instantly on two spare
domains and keep GHL as the board only. Most deliverable, but it splits the work across
two tools.
