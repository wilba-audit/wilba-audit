# Clinic outreach sequence (GHL)

Four emails over seven days, then stop. Anyone who replies leaves the sequence at once.
The offer is the aged-leads revenue share: 10% of what it books, nothing upfront.

Each contact carries four custom fields, filled per clinic in `ghl-import.csv`:

| Field | GHL merge tag | What it holds |
|---|---|---|
| Cold subject | `{{contact.cold_subject}}` | A subject written for that clinic |
| Cold opener | `{{contact.cold_opener}}` | Two short paragraphs built from a verified fact about that clinic |
| CRM phrase | `{{contact.crm_phrase}}` | The booking system we saw them using, e.g. "Zenoti" |
| Timezone line | `{{contact.tz_line}}` | The "Worth 15 minutes?" line, worded for their country |

Email 1 is the personal one. Follow-ups are short and reuse the same subject with "Re:"
so they read as one conversation.

Every email is plain text: no images, no links in the body, no tracking pixel. That is
the single biggest thing that keeps cold mail out of spam.

---

## Email 1 · Day 0

**Subject:** `{{contact.cold_subject}}`

```
{{contact.cold_opener}}

I work with a build partner on a system that connects to {{contact.crm_phrase}}, finds the enquiries and past patients that went quiet, and follows them up over SMS and calls until they book or tell you to stop. Nothing migrates, and your team approves anything before it goes to a patient.

We take 10% of what it books, nothing upfront.

{{contact.tz_line}}

Jess

Jess Morrell
WILBA, wilba.ai

If this isn't relevant, reply "no" and I won't email again.
```

---

## Email 2 · Day 2

**Subject:** `Re: {{contact.cold_subject}}`

```
Bringing this back to the top of your inbox.

The short version: we only get paid out of bookings the system makes for you, 10% of each one. If it books nothing, it costs you nothing.

Worth 15 minutes?

Jess
```

---

## Email 3 · Day 4

**Subject:** `Re: {{contact.cold_subject}}`

```
One more thought, then I'll leave it with you.

Most clinics have a long tail of people who enquired, had a consult, or came in once and never came back. It isn't anyone's job to chase them, so nobody does. That list is what we work, and it's already paid for.

Happy to show you in 15 minutes what it would look like on {{contact.crm_phrase}}.

Jess
```

---

## Email 4 · Day 7 (close-out)

**Subject:** `Re: {{contact.cold_subject}}`

```
I'll stop here so I'm not cluttering your inbox.

If waking up old enquiries is ever worth a look, the offer stands: 10% of what it books, nothing upfront. Just reply to this email.

All the best,
Jess
```

Nobody gets a fifth email. After day 7 with no reply, the opportunity moves to
**No response** and can be revisited in three months.

---

## Footer (needed for US and UK sends)

The US (CAN-SPAM) requires a real postal address and a working opt-out in every
commercial email. UK and Australian rules also expect a clear way to opt out. In the
workflow's email settings, turn on GHL's unsubscribe footer and add WILBA's business
address to it.
