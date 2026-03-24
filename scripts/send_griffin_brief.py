#!/usr/bin/env python3
"""
WILBA — Baha Baha Villas Developer Brief
Generates a branded PDF summary and emails it to Griffin.
"""

import os
import base64
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, Image
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName, FileType, Disposition
)

# ── Brand colours ──────────────────────────────────────────────────────────────
NAVY      = colors.HexColor('#2C3E6B')
OCEAN     = colors.HexColor('#4A90D9')
SAND      = colors.HexColor('#F5F0E8')
SLATE     = colors.HexColor('#7B8FA1')
CHARCOAL  = colors.HexColor('#2D2D2D')
WHITE     = colors.white
LIGHT_BG  = colors.HexColor('#F0F4FA')

OUTPUT_PATH = "outputs/baha-baha/baha-baha-griffin-brief.pdf"
LOGO_PATH   = "reference/brand/wilba.ai (1).png"

# ── Styles ─────────────────────────────────────────────────────────────────────
def make_styles():
    return {
        'cover_title': ParagraphStyle(
            'cover_title', fontName='Helvetica-Bold', fontSize=26,
            textColor=WHITE, leading=32, alignment=TA_LEFT
        ),
        'cover_sub': ParagraphStyle(
            'cover_sub', fontName='Helvetica', fontSize=13,
            textColor=colors.HexColor('#BFD0E8'), leading=18, alignment=TA_LEFT
        ),
        'cover_meta': ParagraphStyle(
            'cover_meta', fontName='Helvetica', fontSize=10,
            textColor=colors.HexColor('#8AAAC8'), leading=14, alignment=TA_LEFT
        ),
        'section_heading': ParagraphStyle(
            'section_heading', fontName='Helvetica-Bold', fontSize=13,
            textColor=NAVY, leading=18, spaceBefore=14, spaceAfter=6
        ),
        'sub_heading': ParagraphStyle(
            'sub_heading', fontName='Helvetica-Bold', fontSize=10,
            textColor=OCEAN, leading=14, spaceBefore=8, spaceAfter=3
        ),
        'body': ParagraphStyle(
            'body', fontName='Helvetica', fontSize=9.5,
            textColor=CHARCOAL, leading=14, spaceAfter=4
        ),
        'body_small': ParagraphStyle(
            'body_small', fontName='Helvetica', fontSize=8.5,
            textColor=SLATE, leading=12, spaceAfter=3
        ),
        'bullet': ParagraphStyle(
            'bullet', fontName='Helvetica', fontSize=9.5,
            textColor=CHARCOAL, leading=14, leftIndent=12,
            bulletIndent=0, spaceAfter=3
        ),
        'table_header': ParagraphStyle(
            'table_header', fontName='Helvetica-Bold', fontSize=8.5,
            textColor=WHITE, leading=12
        ),
        'table_cell': ParagraphStyle(
            'table_cell', fontName='Helvetica', fontSize=8.5,
            textColor=CHARCOAL, leading=12
        ),
        'tag': ParagraphStyle(
            'tag', fontName='Helvetica-Bold', fontSize=8,
            textColor=WHITE, leading=10
        ),
        'footer': ParagraphStyle(
            'footer', fontName='Helvetica', fontSize=8,
            textColor=SLATE, leading=11, alignment=TA_CENTER
        ),
        'alert_red': ParagraphStyle(
            'alert_red', fontName='Helvetica-Bold', fontSize=9,
            textColor=colors.HexColor('#C0392B'), leading=13
        ),
        'alert_orange': ParagraphStyle(
            'alert_orange', fontName='Helvetica-Bold', fontSize=9,
            textColor=colors.HexColor('#E67E22'), leading=13
        ),
    }


def build_pdf(output_path):
    S = make_styles()
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=18*mm, rightMargin=18*mm,
        topMargin=15*mm, bottomMargin=15*mm
    )
    W = A4[0] - 36*mm  # usable width

    story = []

    # ── COVER BAND ──────────────────────────────────────────────────────────────
    # Navy band with logo + title
    cover_data = [[
        Paragraph('BAHA BAHA VILLAS<br/><font size="16">Developer Brief</font>', S['cover_title']),
        ''
    ]]
    cover_table = Table(cover_data, colWidths=[W * 0.7, W * 0.3])
    cover_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), NAVY),
        ('TOPPADDING',    (0, 0), (-1, -1), 16),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 16),
        ('LEFTPADDING',   (0, 0), (-1, -1), 16),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 12),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(cover_table)

    # Sub-band: meta info
    today = date.today().strftime("%d %B %Y")
    meta_data = [[
        Paragraph(f'Prepared by Jess Morrell · WILBA · wilba.ai', S['cover_meta']),
        Paragraph(f'To: Griffin (Developer) · {today}', S['cover_meta']),
        Paragraph('USD $1,800 setup + $300/month', S['cover_meta']),
    ]]
    meta_table = Table(meta_data, colWidths=[W*0.4, W*0.35, W*0.25])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), OCEAN),
        ('TOPPADDING',    (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING',   (0, 0), (-1, -1), 16),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10*mm))

    # ── WHAT THIS IS ────────────────────────────────────────────────────────────
    story.append(Paragraph('What This Is', S['section_heading']))
    story.append(HRFlowable(width=W, thickness=1.5, color=NAVY, spaceAfter=6))
    story.append(Paragraph(
        'WILBA\'s first hospitality client. Sean owns a surf/accommodation property in West Sumbawa, '
        'Indonesia called Baha Baha Villas. We scoped two AI automations on the discovery call (23 Mar 2026).',
        S['body']
    ))
    story.append(Spacer(1, 4*mm))

    phases_data = [
        [Paragraph('Phase 1', S['table_header']), Paragraph('Daily Ops Brief', S['table_header']), Paragraph('2 weeks', S['table_header'])],
        [Paragraph('', S['table_cell']),
         Paragraph('Every morning at 6am WITA — pulls all bookings, emails the team: check-ins, check-outs, transfers, in-house guests, upcoming arrivals. Zero manual admin.', S['table_cell']),
         Paragraph('USD $800 setup\nUSD $150/mo', S['table_cell'])],
        [Paragraph('Phase 2', S['table_header']), Paragraph('AI Email Receptionist', S['table_header']), Paragraph('2 weeks', S['table_header'])],
        [Paragraph('', S['table_cell']),
         Paragraph('Monitors Gmail inbox every 15 min. Detects guest language, classifies intent, drafts reply in their language. Owner reviews before sending (auto-send for FAQs).', S['table_cell']),
         Paragraph('USD $1,000 setup\nUSD $150/mo', S['table_cell'])],
    ]
    phases_table = Table(phases_data, colWidths=[W*0.12, W*0.65, W*0.23])
    phases_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), NAVY),
        ('BACKGROUND', (1, 0), (2, 0), NAVY),
        ('BACKGROUND', (0, 2), (0, 2), OCEAN),
        ('BACKGROUND', (1, 2), (2, 2), OCEAN),
        ('BACKGROUND', (0, 1), (-1, 1), LIGHT_BG),
        ('BACKGROUND', (0, 3), (-1, 3), LIGHT_BG),
        ('TOPPADDING',    (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING',   (0, 0), (-1, -1), 8),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#D0D8E8')),
    ]))
    story.append(phases_table)
    story.append(Spacer(1, 6*mm))

    # ── TECH STACK ──────────────────────────────────────────────────────────────
    story.append(Paragraph('Tech Stack', S['section_heading']))
    story.append(HRFlowable(width=W, thickness=1.5, color=NAVY, spaceAfter=6))

    stack_data = [
        [Paragraph('Layer', S['table_header']), Paragraph('Tool', S['table_header']), Paragraph('Notes', S['table_header'])],
        ['Hosting', 'Render.com', 'Same as WILBA audit pipeline — cron jobs'],
        ['PMS', 'Booking Layer', 'REST API — needs key from Sean'],
        ['Channel Manager', 'ChanX', 'Connects BL to OTAs — we don\'t touch directly'],
        ['Surf vendor', 'World Safaris', 'Manual Google Sheet (MVP); email parser Phase 2'],
        ['AI', 'Claude API', 'Haiku for daily brief; Sonnet for email responder'],
        ['Email delivery', 'SendGrid', 'Already in WILBA stack'],
        ['Guest inbox', 'Gmail', 'OAuth 2.0 — one-time setup with Sean'],
        ['Language', 'Python 3.11', 'Consistent with audit pipeline'],
        ['Timezone', 'WITA (UTC+8)', 'Same as Bali'],
    ]
    stack_table = Table(
        [[Paragraph(str(c), S['table_header'] if r == 0 else S['table_cell'])
          for c in row] for r, row in enumerate(stack_data)],
        colWidths=[W*0.22, W*0.22, W*0.56]
    )
    stack_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('TOPPADDING',    (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING',   (0, 0), (-1, -1), 8),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#D0D8E8')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(stack_table)
    story.append(Spacer(1, 6*mm))

    # ── WHAT'S BUILT ────────────────────────────────────────────────────────────
    story.append(Paragraph('What\'s Already Built', S['section_heading']))
    story.append(HRFlowable(width=W, thickness=1.5, color=NAVY, spaceAfter=6))

    built_data = [
        [Paragraph('File', S['table_header']), Paragraph('Status', S['table_header']), Paragraph('Notes', S['table_header'])],
        ['scripts/baha_baha_daily_brief.py',    '✅ Built', 'Needs Booking Layer API key to test'],
        ['scripts/baha_baha_email_responder.py','✅ Built', 'Needs Gmail OAuth to test'],
        ['scripts/requirements-baha-baha.txt',  '✅ Done',  'All Python deps'],
        ['outputs/baha-baha/system-design.md',  '✅ Done',  'Full architecture, API endpoints, email format'],
        ['outputs/baha-baha/booking-data-model.md','✅ Done','Room/package schema — names are placeholders'],
        ['outputs/baha-baha/discovery-notes.md','✅ Done',  'Tech stack, open questions'],
        ['outputs/baha-baha/proposal.md',       '✅ Done',  'Sent to Sean — scope, pricing, timeline'],
    ]
    built_table = Table(
        [[Paragraph(str(c), S['table_header'] if r == 0 else S['table_cell'])
          for c in row] for r, row in enumerate(built_data)],
        colWidths=[W*0.42, W*0.13, W*0.45]
    )
    built_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('TOPPADDING',    (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING',   (0, 0), (-1, -1), 8),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#D0D8E8')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(built_table)
    story.append(Spacer(1, 6*mm))

    # ── WAITING ON SEAN ─────────────────────────────────────────────────────────
    story.append(Paragraph('Waiting On Sean (Blockers)', S['section_heading']))
    story.append(HRFlowable(width=W, thickness=1.5, color=NAVY, spaceAfter=6))

    blockers = [
        ('🔴', 'Booking Layer API key', 'Sean: account settings → API → Generate key', 'Core data source — nothing runs without this'),
        ('🔴', 'Booking Layer access', 'Add jessmorrell@gmail + Griffin as Manager/Dev', 'Was due 25 Mar — confirm done'),
        ('🔴', 'Gmail OAuth setup', '5-min call with Sean to authorise the bookings inbox', 'Email responder can\'t run without this'),
        ('🟡', 'World Safaris sample email', 'Sean to forward one booking confirmation', 'Needed to design the email parser (Phase 2)'),
        ('🟡', 'Exact room/villa names', 'As they appear in Booking Layer (Baja room, studio + others)', 'Placeholders in data model now'),
        ('🟡', 'Exact package names', 'Accommodation only, surf, meals, combos — as in BL', 'Same — need real names'),
        ('🟡', 'Daily brief recipients', 'Who gets the morning email (names + addresses)', 'Sean + team — confirm list'),
        ('🟡', 'Brief send time (WITA)', 'What time should it land in their inbox?', 'Default: 6:00am WITA'),
    ]
    blocker_data = [
        [Paragraph('', S['table_header']),
         Paragraph('Item', S['table_header']),
         Paragraph('Action', S['table_header']),
         Paragraph('Why', S['table_header'])]
    ]
    for pri, item, action, why in blockers:
        blocker_data.append([
            Paragraph(pri, S['body']),
            Paragraph(item, S['body']),
            Paragraph(action, S['body_small']),
            Paragraph(why, S['body_small']),
        ])
    blocker_table = Table(blocker_data, colWidths=[W*0.05, W*0.22, W*0.38, W*0.35])
    blocker_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('TOPPADDING',    (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#D0D8E8')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(blocker_table)
    story.append(Spacer(1, 6*mm))

    # ── KEY INTEL FROM DISCOVERY CALL ───────────────────────────────────────────
    story.append(Paragraph('Key Intel from Discovery Call (Fireflies, 23 Mar)', S['section_heading']))
    story.append(HRFlowable(width=W, thickness=1.5, color=NAVY, spaceAfter=6))

    intel_items = [
        ('Team', 'Sean (owner/decisions) · Mashi (Booking Layer + ops) · Danny (transport/flights)'),
        ('Rooms confirmed', 'Baja room, Studio (+ others TBC) — studio + 2-bed need to link as a group unit; BL can\'t do this yet. Mashi is working on it.'),
        ('Agencies', 'One Wave (12.5% commission) · World Safaris (20%) · via ChanX channel manager'),
        ('Primary guest channel', 'WhatsApp — more important than email. Phase 1 chatbot should prioritise WA over email.'),
        ('Scope note', 'Sean described Phase 1 as: chatbot on website + WhatsApp + Instagram. Our proposal has daily brief as Phase 1. Needs alignment — Jess is following up with Sean.'),
        ('BL user access', 'Jess needs to be re-added as Manager (jessmorrell@gmail.com). Developer also needs adding. Sean\'s deadline was 25 Mar.'),
        ('Accounting', 'Journal.co.id + Moka POS are disconnected. Out of scope for Phase 1 — do not build anything that assumes accounting integration.'),
        ('Google Drive', 'Content is disorganised. Blocks any future content automation. Not our problem for Phase 1.'),
    ]
    for label, detail in intel_items:
        row_data = [[
            Paragraph(label, S['sub_heading']),
            Paragraph(detail, S['body']),
        ]]
        row_table = Table(row_data, colWidths=[W*0.22, W*0.78])
        row_table.setStyle(TableStyle([
            ('TOPPADDING',    (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING',   (0, 0), (-1, -1), 0),
            ('RIGHTPADDING',  (0, 0), (-1, -1), 0),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor('#D0D8E8')),
        ]))
        story.append(row_table)

    story.append(Spacer(1, 6*mm))

    # ── RENDER DEPLOYMENT ────────────────────────────────────────────────────────
    story.append(Paragraph('Render Deployment', S['section_heading']))
    story.append(HRFlowable(width=W, thickness=1.5, color=NAVY, spaceAfter=6))

    deploy_data = [
        [Paragraph('Service', S['table_header']), Paragraph('Type', S['table_header']),
         Paragraph('Schedule (UTC)', S['table_header']), Paragraph('Script', S['table_header'])],
        ['baha-daily-brief',    'Cron Job', '0 22 * * *  (= 6am WITA)', 'scripts/baha_baha_daily_brief.py'],
        ['baha-email-responder','Cron Job', '*/15 * * * *',               'scripts/baha_baha_email_responder.py'],
    ]
    deploy_table = Table(
        [[Paragraph(str(c), S['table_header'] if r == 0 else S['table_cell'])
          for c in row] for r, row in enumerate(deploy_data)],
        colWidths=[W*0.22, W*0.12, W*0.28, W*0.38]
    )
    deploy_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('TOPPADDING',    (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING',   (0, 0), (-1, -1), 8),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#D0D8E8')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(deploy_table)
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph('Environment Variables (add to Render):', S['sub_heading']))
    env_vars = [
        'ANTHROPIC_API_KEY       — already set (shared with audit pipeline)',
        'SENDGRID_API_KEY        — already set (shared with audit pipeline)',
        'BOOKING_LAYER_API_KEY   — from Sean\'s Booking Layer account',
        'GMAIL_CREDENTIALS_JSON  — OAuth credentials for bookings Gmail',
        'GMAIL_TOKEN_JSON        — OAuth refresh token',
        'BRIEF_RECIPIENTS        — comma-separated email list for daily brief',
        'BRIEF_SEND_TIME         — e.g. "06:00" WITA',
    ]
    for v in env_vars:
        story.append(Paragraph(f'• {v}', S['bullet']))
    story.append(Spacer(1, 6*mm))

    # ── QUESTIONS FOR GRIFFIN ───────────────────────────────────────────────────
    story.append(Paragraph('Questions for You', S['section_heading']))
    story.append(HRFlowable(width=W, thickness=1.5, color=NAVY, spaceAfter=6))

    questions = [
        ('Booking Layer API', 'Once Sean sends the key, can you hit /reservations and confirm field names match what\'s in the script? Docs suggest standard REST but worth validating against a live endpoint.'),
        ('World Surfaris MVP', 'Proposing a manual Google Sheet for Phase 1. Does the script handle this already, or do you want a different fallback?'),
        ('Gmail OAuth on Render', 'Audit pipeline uses env vars for credentials. Same approach here? Or prefer a secret file?'),
        ('Phase 1 scope', 'Sean mentioned chatbot (WA/IG/website) as Phase 1 in the call, but our proposal has daily brief as Phase 1. I\'m aligning with Sean — let me know if this changes your architecture significantly.'),
    ]
    for q, detail in questions:
        story.append(Paragraph(f'<b>{q}</b>', S['body']))
        story.append(Paragraph(detail, S['body_small']))
        story.append(Spacer(1, 2*mm))

    story.append(Spacer(1, 6*mm))

    # ── BIGGER PICTURE ──────────────────────────────────────────────────────────
    bigger_data = [[Paragraph(
        '<b>Bigger Picture:</b> Once live, this becomes WILBA\'s Hospitality AI Receptionist template — '
        'resold to surf resorts, retreat centres, and boutique properties globally. '
        'Baha Baha is the pilot. Let\'s make it bulletproof.',
        ParagraphStyle('bigger', fontName='Helvetica', fontSize=9.5, textColor=WHITE, leading=14)
    )]]
    bigger_table = Table(bigger_data, colWidths=[W])
    bigger_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), NAVY),
        ('TOPPADDING',    (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING',   (0, 0), (-1, -1), 14),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 14),
        ('ROUNDEDCORNERS', [4]),
    ]))
    story.append(bigger_table)
    story.append(Spacer(1, 4*mm))

    # ── FOOTER ──────────────────────────────────────────────────────────────────
    story.append(HRFlowable(width=W, thickness=0.5, color=SLATE, spaceAfter=4))
    story.append(Paragraph(
        'WILBA · wilba.ai · Jess Morrell · Jess@wilba.ai',
        S['footer']
    ))

    doc.build(story)
    print(f"✅ PDF created: {output_path}")
    return output_path


def send_email(pdf_path):
    api_key = os.environ.get('SENDGRID_API_KEY')
    if not api_key:
        raise ValueError("SENDGRID_API_KEY not set in environment")

    with open(pdf_path, 'rb') as f:
        pdf_data = base64.b64encode(f.read()).decode()

    from_email = os.environ.get('FROM_EMAIL', 'hello@wilba.ai')
    message = Mail(
        from_email=from_email,
        to_emails='jess@wilba.ai',
        subject='Baha Baha Villas — Developer Brief',
        html_content="""
<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; color: #2D2D2D;">
  <div style="background: #2C3E6B; padding: 24px 28px; border-radius: 6px 6px 0 0;">
    <h1 style="color: white; margin: 0; font-size: 22px; font-weight: bold;">Baha Baha Villas</h1>
    <p style="color: #BFD0E8; margin: 6px 0 0; font-size: 14px;">Developer Brief — AI Receptionist & Daily Ops Brief</p>
  </div>
  <div style="background: #4A90D9; padding: 8px 28px;">
    <p style="color: white; margin: 0; font-size: 12px;">USD $1,800 setup + $300/month retainer · WILBA's first hospitality client</p>
  </div>
  <div style="padding: 24px 28px; background: #F5F0E8;">
    <p>Hey Griffin,</p>
    <p>Full brief attached as a PDF — everything you need to pick this up.</p>
    <p><strong>The short version:</strong></p>
    <ul style="line-height: 1.8;">
      <li>Surf resort in West Sumbawa, Indonesia — owner is Sean</li>
      <li><strong>Phase 1:</strong> Daily 6am ops brief email (Booking Layer → Claude → SendGrid)</li>
      <li><strong>Phase 2:</strong> Multi-language email responder (Gmail → Claude → Gmail Drafts)</li>
      <li>Scripts are already built in the repo — just need Sean's API key and Gmail OAuth to test</li>
      <li>Deploy to Render — same setup as the audit pipeline</li>
    </ul>
    <p><strong>What we're waiting on from Sean:</strong></p>
    <ol style="line-height: 1.8;">
      <li>Booking Layer API key (he was adding you as a user too — should be done)</li>
      <li>Gmail OAuth setup (5-min call)</li>
      <li>World Safaris sample booking email</li>
      <li>Exact room and package names from Booking Layer</li>
    </ol>
    <p>Key question: Sean described Phase 1 as a chatbot on WhatsApp/Instagram/website in the call,
    but the proposal has daily brief as Phase 1. I'm aligning with him — let me know if that changes
    your architecture significantly before I confirm.</p>
    <p>Full details, Render env vars, API endpoints, and questions for you are all in the PDF.</p>
    <p style="margin-top: 24px;">Talk soon,<br><strong>Jess</strong></p>
  </div>
  <div style="background: #2C3E6B; padding: 12px 28px; border-radius: 0 0 6px 6px; text-align: center;">
    <p style="color: #8AAAC8; margin: 0; font-size: 11px;">WILBA · wilba.ai · Jess@wilba.ai</p>
  </div>
</div>
"""
    )

    attachment = Attachment()
    attachment.file_content = FileContent(pdf_data)
    attachment.file_type = FileType('application/pdf')
    attachment.file_name = FileName('Baha-Baha-Villas-Developer-Brief.pdf')
    attachment.disposition = Disposition('attachment')
    message.attachment = attachment

    sg = SendGridAPIClient(api_key)
    response = sg.send(message)
    print(f"✅ Email sent — status {response.status_code}")
    return response.status_code


if __name__ == '__main__':
    # Load .env if present
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    os.environ.setdefault(k.strip(), v.strip())

    pdf_path = build_pdf(OUTPUT_PATH)
    status = send_email(pdf_path)

    if status in (200, 202):
        print("🏄 Done — PDF built and email sent to griffin@wilba.ai")
    else:
        print(f"⚠️  Email may not have sent correctly — status: {status}")
