# Clinic outreach in GoHighLevel: setup guide

WILBA sub-account Location ID: `A3tY7p4YMaGWtkblpmUX`

What this builds: a pipeline board for 100 clinic prospects, every prospect loaded as a
contact with a personal first email, and one workflow that sends ten branded emails over
40 days, moves each card along the board, and stops the moment someone replies.

**Nothing sends until the workflow is published.** Build it, test it on your own email
address, and only then switch it on.

Files in this folder:

- `ghl-import.csv` — the 100 prospects, ready for GHL's contact import
- `email-sequence.md` — the ten emails, word for word (Dean Jackson style, with the refund guarantee)
- `templates/email-01.html` to `email-10.html` — the branded versions to paste into GHL
- `email-1-preview.md` — the first email exactly as each of the 100 clinics will get it
- `scripts/wilba_ghl_load.py` + the "WILBA GHL load" GitHub Action — loads the same 100
  through the API instead of the CSV, once a token is in place

---

## Status (8 Oct 2026)

**Done by Claude:** the 7 custom fields are created and all 100 clinics are loaded as contacts,
with their fields and tags, in sub-account `A3tY7p4YMaGWtkblpmUX`. Nothing has been sent.

**What's left for you:**

1. Create the **Clinic outreach** pipeline with the 11 stages (step 2). Then tell Claude,
   and Claude adds the 100 opportunity cards in New prospect. Skip step 4.
2. Build the two workflows (step 5) and test them on your own email address (step 6).
3. Confirm the refund guarantee with Griffin, and choose how to send (see the end of this guide).
4. Tell Claude "go". Nothing sends before that.

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
| 3 | Following up (emails 2 to 4) | Workflow |
| 4 | Long follow-up (emails 5 to 9) | Workflow |
| 5 | Final email sent | Workflow |
| 6 | Replied | Workflow (on reply) |
| 7 | Call booked | You, or automatic with a GHL calendar |
| 8 | Proposal sent | You |
| 9 | Won | You |
| 10 | No response | Workflow (after email 10) |
| 11 | Not interested | You |

## 3. Create the custom fields

Settings → Custom Fields → Add field (Contact):

| Name | Type |
|---|---|
| Cold subject | Single line |
| Cold opener | Multi line |
| CRM phrase | Single line |
| Timezone line | Single line |
| Currency | Single line |
| Pipeline ID | Single line |
| ICP grade | Single line |

GHL turns these into merge tags such as `{{contact.cold_subject}}`. Check that the tag GHL
shows for each field matches the one used in the emails, and if it doesn't, use GHL's.

## 4. Import the 100 prospects

Contacts → Import → upload `ghl-import.csv`.

- Map each column to the field with the same name.
- Tick **Create opportunities**, pick pipeline **Clinic outreach** and stage **New prospect**.
- Tags: the file already gives every contact `clinic-outreach`, a grade tag
  (`grade-a`, `grade-b`, `grade-c`) and a country tag.

## 5. Build the workflow

Automation → Workflows → Create → Start from scratch. Name: **Clinic outreach sequence**.

**Settings (the cog icon):**
- **Stop on response: ON.** This is what stops the follow-ups when someone replies.
- Allow re-entry: OFF.
- Time window: Mon to Fri, 8am to 4pm in the contact's timezone.

**Trigger:** Contact Tag added → `outreach-go`.
You start a batch by adding `outreach-go` to that day's contacts, so you control the volume.

**Steps.** For each email, add a **Send email** action, open the code editor, and paste in
`templates/email-NN.html`. Then set the subject from `email-sequence.md`, with the from name
"Jess Morrell".

| Step | Wait before it | Send | Then move the card to |
|---|---|---|---|
| 1 | Drip mode: 10 a day | Email 1 | Email 1 sent |
| 2 | 2 days | Email 2 | Following up |
| 3 | 2 days | Email 3 | |
| 4 | 3 days | Email 4 | |
| 5 | 3 days | Email 5 | Long follow-up |
| 6 | 4 days | Email 6 | |
| 7 | 4 days | Email 7 | |
| 8 | 5 days | Email 8 | |
| 9 | 7 days | Email 9 | |
| 10 | 10 days | Email 10 | Final email sent |
| End | 7 days | (none) | No response, plus the tag `outreach-no-response` |

Raise the Drip from 10 to 15 and then 20 once the first week shows no bounce or spam problems.

**Second, small workflow: "Clinic outreach replied".** Trigger: Customer replied
(channel: email), filtered to the tag `clinic-outreach`. Actions: move the card to Replied,
add the tag `outreach-replied`, and send yourself an internal notification.

**Optional third workflow: "Clinic outreach booked".** If you move from Calendly to a
GHL calendar, set the trigger to Appointment booked on that calendar. The actions are:
move the card to Call booked and remove the contact from the sequence workflow.

## 6. Test before going live

Create one contact with your own email, fill the five cold fields, add `outreach-go`,
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
