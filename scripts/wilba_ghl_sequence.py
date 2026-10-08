"""Build WILBA's 10-email clinic outreach sequence for GoHighLevel.

Writes, under outputs/pipeline/ghl/:
  email-sequence.md        the 10 emails in plain text, with GHL merge tags
  templates/email-NN.html  branded HTML for each email, to paste into GHL's code editor
  email-1-preview.md       email 1 as each of the 100 clinics will receive it

Run again after changing the copy below: python3 scripts/wilba_ghl_sequence.py
"""
from __future__ import annotations

import csv
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "outputs" / "pipeline" / "ghl"
CALENDAR = "https://calendly.com/hello-wilba"
INK, BLUE, GREY = "#1a1a1a", "#87abdd", "#5a5a5a"

# (day, subject, body, button label or None). Body is plain text with GHL merge tags.
# Paragraphs are separated by blank lines. "{cal}" marks where the calendar link goes.
EMAILS = [
    (0, "{{contact.cold_subject}}", """{{contact.cold_opener}}

Here's what I'd like to do. We plug into {{contact.crm_phrase}}, find those people, and follow them up by text and phone until they book or say stop. Nothing changes for your team.

You pay 10% of the bookings it brings in. Nothing upfront. And if you don't love what we build, you get every cent back.

{{contact.tz_line}} Grab any time that suits here: {cal}""", "Book a 15-minute chat"),

    (2, "Re: {{contact.cold_subject}}", """Did you get a chance to see my note?

The short version: there's money sitting in {{contact.crm_phrase}} from people who enquired and never booked. We go and get it, and you only pay out of what comes back.

If it's easier, pick a time here: {cal}""", None),

    (4, "Worst case", """Here's the worst that can happen if you say yes:

We build it, it books nobody, and you've paid nothing.

Here's the best:

Patients who'd drifted away come back in, and you keep 90% of every booking.

And if you don't like what we've built, you get a full refund. No awkward conversation.

Fifteen minutes is all it takes to see which one you'd get: {cal}""", "Pick a time"),

    (7, "{{contact.company_name}}", """Are you open to waking up your old leads?""", None),

    (10, "The maths on old enquiries", """Quick back-of-envelope.

Say {{contact.crm_phrase}} holds 500 people who enquired and never booked. If 1 in 20 comes back for a {{contact.currency}}400 treatment, that's {{contact.currency}}10,000 in bookings you've already paid to attract.

Our share is {{contact.currency}}1,000. Yours is {{contact.currency}}9,000. And you didn't spend another cent on ads.

Happy to run the real numbers with you: {cal}""", "Run my numbers"),

    (14, "Why we only take 10%", """Most agencies charge a setup fee, a monthly retainer, and hope it works.

We'd rather get paid when you do. That's why it's 10% of the bookings we bring in, nothing upfront, and a full refund if you don't love what we build.

If we don't deliver, we don't eat. It keeps us honest.

{cal}""", "Book a 15-minute chat"),

    (18, "What your team actually does", """The question I get most: "What does my team have to do?"

Almost nothing. The system works inside {{contact.crm_phrase}}, your team approves anything before it goes to a patient, and there's one "AI off" switch if they ever want to pause it.

No new software to learn. No migration.

Worth a look? {cal}""", None),

    (23, "Quick question", """What happens at {{contact.company_name}} to an enquiry that doesn't book?

Just curious. Most clinics tell me "nothing, really", and that's the gap we fill.

Jess""", None),

    (30, "Should I close your file?", """I haven't heard back, so I'm guessing old enquiries aren't a priority right now. Totally fine.

Should I close your file, or would you like me to keep you on the list?

Either way, just reply with a quick "close" or "keep".""", None),

    (40, "Last one from me", """I'll leave it here so I'm not cluttering your inbox.

If waking up old enquiries is ever worth a look, the offer stands: 10% of what it books, nothing upfront, full refund if you don't love it.

My calendar is always open: {cal}""", "Book a 15-minute chat"),
]

SIGN_TEXT = f"Jess\n\nJess Morrell\nWILBA, wilba.ai\nBook a call: {CALENDAR}"
OPT_OUT = 'If this isn\'t for you, reply "no" and I won\'t email again.'


def plain(body: str) -> str:
    text = body.replace("{cal}", CALENDAR)
    if not text.rstrip().endswith("Jess"):
        text += "\n\n" + SIGN_TEXT
    else:
        text = text.rstrip()[: -len("Jess")] + SIGN_TEXT
    return text + "\n\n" + OPT_OUT


def html_email(body: str, button: str | None) -> str:
    paras = []
    for p in body.split("\n\n"):
        p = p.strip()
        if p == "Jess":
            continue
        safe = html.escape(p, quote=False).replace("\n", "<br>")
        link = f'<a href="{CALENDAR}" style="color:{INK};font-weight:600">{CALENDAR.replace("https://", "")}</a>'
        if button and safe.strip() == "{cal}":
            continue  # the button replaces a bare link paragraph
        if button:
            safe = safe.replace(": {cal}", ".")  # the button carries the link
        safe = safe.replace("{cal}", link)
        paras.append(f'<p style="margin:0 0 16px">{safe}</p>')
    btn = ""
    if button:
        btn = (f'<table cellpadding="0" cellspacing="0" border="0" style="margin:4px 0 22px"><tr>'
               f'<td style="background:{INK};border-radius:6px">'
               f'<a href="{CALENDAR}" style="display:inline-block;padding:11px 20px;color:#ffffff;'
               f'font-size:14px;font-weight:600;text-decoration:none">{html.escape(button)} &rarr;</a>'
               f'</td></tr></table>')
    sig = (f'<p style="margin:0 0 18px">Jess</p>'
           f'<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;max-width:420px">'
           f'<tr><td colspan="2" style="height:3px;background:{INK};background:linear-gradient(90deg,{INK} 0%,{BLUE} 100%);font-size:0;line-height:0">&nbsp;</td></tr>'
           f'<tr><td style="padding:12px 18px 0 0;vertical-align:top">'
           f'<p style="margin:0;font-size:15px;font-weight:700;color:{INK}">Jess Morrell</p>'
           f'<p style="margin:2px 0 6px;font-size:10px;letter-spacing:1px;text-transform:uppercase;font-weight:600;color:{BLUE}">Founder &amp; AI Automation Strategist</p>'
           f'<p style="margin:0;font-size:12px;color:{GREY}"><a href="https://www.wilba.ai/" style="color:{INK};font-weight:600;text-decoration:none">wilba.ai</a> &middot; <a href="{CALENDAR}" style="color:{GREY}">Book a call</a> &middot; Victoria, Australia</p></td>'
           f'<td style="padding:12px 0 0 18px;vertical-align:middle;border-left:1px solid #ebebeb">'
           f'<p style="margin:0;font-size:20px;font-weight:800;letter-spacing:-1px;color:{INK}">wilba<span style="color:{BLUE}">.ai</span></p></td></tr></table>')
    foot = f'<p style="margin:22px 0 0;font-size:11px;color:#9a9a9a">{html.escape(OPT_OUT)}</p>'
    return ('<div style="font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.55;'
            f'color:{INK};max-width:560px">' + "".join(paras) + btn + sig + foot + "</div>\n")


def main() -> None:
    md = ["# Clinic outreach sequence (GHL): 10 emails",
          "",
          "Dean Jackson / Joe Polish style: short, plain, one easy question per email, and the",
          "risk reversal up front. Ten emails over 40 days. Anyone who replies or books a call",
          "drops out straight away.",
          "",
          "**The offer:** you pay 10% of the bookings we bring in, nothing upfront, and if you",
          "don't love what we build you get every cent back.",
          "",
          "> **Check the guarantee with Griffin before go-live.** Nobody pays upfront, so \"full",
          "> refund\" means refunding the 10% they've paid us. If he won't agree, swap it for:",
          "> \"If you don't love it, we switch it off and you owe nothing more.\"",
          "",
          f"**Calendar link:** {CALENDAR} (the one already live on the audit funnel). If you'd",
          "rather book into a GHL calendar, swap the link and bookings will move the card to",
          "Call booked on their own.",
          "",
          "**Branded versions:** `templates/email-01.html` to `email-10.html`. In GHL, open the",
          "email step, choose the code editor, and paste the file in. The branding is the WILBA",
          "wordmark, colours and signature, all in text. There are no images, so it still lands",
          "in the inbox like a personal email.",
          "",
          "| # | Day | Subject | Job |",
          "|---|---|---|---|"]
    jobs = ["Personal opener + offer", "Nudge", "Worst case / best case", "Nine-word email",
            "The maths", "Why revenue share", "What the team does", "Curiosity question",
            "Close the file?", "Last one, door open"]
    for i, (day, subj, _, _) in enumerate(EMAILS, 1):
        md.append(f"| {i} | {day} | `{subj}` | {jobs[i-1]} |")
    md.append("")
    for i, (day, subj, body, button) in enumerate(EMAILS, 1):
        md += ["---", "", f"## Email {i} · Day {day} · {jobs[i-1]}", "",
               f"**Subject:** `{subj}`", "", "```", plain(body), "```", ""]
        (OUT / "templates" / f"email-{i:02d}.html").write_text(html_email(body, button), encoding="utf-8")
    md += ["---", "", "## Footer (needed for US and UK sends)", "",
           "In the US, CAN-SPAM requires a real postal address and a working opt-out in every",
           "commercial email. In the workflow's email settings, turn on GHL's unsubscribe",
           "footer and add WILBA's business address to it.", ""]
    (OUT / "email-sequence.md").write_text("\n".join(md), encoding="utf-8")

    rows = list(csv.DictReader((OUT / "ghl-import.csv").open(encoding="utf-8")))
    prev = ["# Email 1 for all 100 prospects", "",
            "What each clinic receives first, in send order (grade A first). The branded version",
            "adds the WILBA signature and a \"Book a 15-minute chat\" button.", ""]
    day0 = EMAILS[0][2]
    for n, r in enumerate(rows, 1):
        body = day0
        for k in ("cold_opener", "crm_phrase", "tz_line", "currency"):
            body = body.replace("{{contact.%s}}" % k, r.get(k, ""))
        prev += ["---", "", f"## {n}. {r['company_name']} ({r['country']}, grade {r['icp_grade']}) · {r['email']}",
                 "", f"**Subject:** {r['cold_subject']}", "", body.replace("{cal}", CALENDAR), "", "Jess", ""]
    (OUT / "email-1-preview.md").write_text("\n".join(prev), encoding="utf-8")
    print(f"wrote {len(EMAILS)} emails, {len(rows)} previews")


if __name__ == "__main__":
    main()
