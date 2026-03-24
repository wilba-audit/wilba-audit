from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.platypus import KeepTogether

OUTPUT_PATH = "/Users/jessmorrell/Documents/AAA/aios-starter-kit/outputs/invoices/WILBA-INV-001-MonkeyJoes.pdf"

# Brand colours
DARK = colors.HexColor("#1A1A2E")
ACCENT = colors.HexColor("#E63946")
MID = colors.HexColor("#4A4A6A")
LIGHT_BG = colors.HexColor("#F8F8FC")
WHITE = colors.white

doc = SimpleDocTemplate(
    OUTPUT_PATH,
    pagesize=A4,
    leftMargin=20*mm,
    rightMargin=20*mm,
    topMargin=16*mm,
    bottomMargin=16*mm,
)

styles = getSampleStyleSheet()

# Custom styles
def s(name, **kwargs):
    return ParagraphStyle(name, **kwargs)

style_h1 = s("h1", fontName="Helvetica-Bold", fontSize=28, textColor=DARK, leading=34)
style_tag = s("tag", fontName="Helvetica", fontSize=10, textColor=ACCENT, leading=14)
style_label = s("label", fontName="Helvetica-Bold", fontSize=8, textColor=MID, leading=12, spaceAfter=2)
style_value = s("value", fontName="Helvetica", fontSize=10, textColor=DARK, leading=14)
style_value_bold = s("valuebold", fontName="Helvetica-Bold", fontSize=10, textColor=DARK, leading=14)
style_small = s("small", fontName="Helvetica", fontSize=8, textColor=MID, leading=11)
style_note = s("note", fontName="Helvetica-Oblique", fontSize=9, textColor=MID, leading=13)
style_total_label = s("totlbl", fontName="Helvetica-Bold", fontSize=11, textColor=WHITE, leading=16)
style_total_val = s("totval", fontName="Helvetica-Bold", fontSize=14, textColor=WHITE, leading=18)
style_section_head = s("sechead", fontName="Helvetica-Bold", fontSize=9, textColor=ACCENT, leading=12, spaceAfter=4)

story = []

# ── HEADER ────────────────────────────────────────────────────────────────────
header_data = [
    [
        Paragraph("INVOICE", style_h1),
        Table(
            [
                [Paragraph("INVOICE NO.", style_label), Paragraph("INV-2026-001", style_value_bold)],
                [Paragraph("DATE", style_label),        Paragraph("17 March 2026", style_value)],
                [Paragraph("PROJECT", style_label),     Paragraph("Monkey Joe's — Stage 1", style_value)],
                [Paragraph("STATUS", style_label),      Paragraph("Due on Receipt", style_value_bold)],
            ],
            colWidths=[28*mm, 45*mm],
            style=TableStyle([
                ("VALIGN", (0,0), (-1,-1), "TOP"),
                ("TOPPADDING", (0,0), (-1,-1), 2),
                ("BOTTOMPADDING", (0,0), (-1,-1), 2),
                ("LEFTPADDING", (0,0), (-1,-1), 0),
                ("RIGHTPADDING", (0,0), (-1,-1), 0),
            ])
        )
    ]
]
header_table = Table(header_data, colWidths=[90*mm, None])
header_table.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 0),
]))
story.append(header_table)
story.append(Spacer(1, 6*mm))
story.append(HRFlowable(width="100%", thickness=1.5, color=ACCENT))
story.append(Spacer(1, 6*mm))

# ── FROM / TO ─────────────────────────────────────────────────────────────────
from_block = [
    [Paragraph("FROM", style_section_head)],
    [Paragraph("Jessica Morrell", style_value_bold)],
    [Paragraph("WILBA / wilba.ai", style_value)],
    [Paragraph("Jan Juc, Surf Coast VIC, Australia", style_value)],
    [Paragraph("jjessmorrell@gmail.com", style_note)],
    [Paragraph("ABN: 79 635 508 306", style_small)],
]

to_block = [
    [Paragraph("BILL TO", style_section_head)],
    [Paragraph("William Milner", style_value_bold)],
    [Paragraph("Founder, Lanyu", style_value)],
    [Paragraph("william@lanyu.ai", style_value)],
    [Paragraph("Re: Monkey Joe's Pilot Campaign", style_note)],
]

from_table = Table(from_block, colWidths=[80*mm])
from_table.setStyle(TableStyle([
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ("TOPPADDING", (0,0), (-1,-1), 1),
    ("BOTTOMPADDING", (0,0), (-1,-1), 1),
]))

to_table = Table(to_block, colWidths=[80*mm])
to_table.setStyle(TableStyle([
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ("TOPPADDING", (0,0), (-1,-1), 1),
    ("BOTTOMPADDING", (0,0), (-1,-1), 1),
]))

parties = Table([[from_table, to_table]], colWidths=[90*mm, 80*mm])
parties.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 0),
]))
story.append(parties)
story.append(Spacer(1, 8*mm))

# ── SERVICES TABLE ────────────────────────────────────────────────────────────
story.append(Paragraph("SERVICES", style_section_head))
story.append(Spacer(1, 2*mm))

col_widths = [90*mm, 35*mm, 25*mm, 20*mm]
service_header = ["DESCRIPTION", "DETAIL", "QTY", "AMOUNT (USD)"]

services = [
    [
        Paragraph("<b>Campaign Research &amp; Market Analysis</b>", styles["Normal"]),
        Paragraph("Audience research, competitor review, local market analysis for Pointe Orlando &amp; Winter Park locations", style_small),
        "1",
        "$300"
    ],
    [
        Paragraph("<b>Marketing Audit</b>", styles["Normal"]),
        Paragraph("Audit of existing assets: email list (20K contacts), Facebook presence (30K followers), GBP listings, current ad activity", style_small),
        "1",
        "$250"
    ],
    [
        Paragraph("<b>Campaign Strategy Development</b>", styles["Normal"]),
        Paragraph("Full strategy document covering Google Ads, email reactivation, lead retargeting, offer structure &amp; landing page brief", style_small),
        "1",
        "$400"
    ],
    [
        Paragraph("<b>Google Ads Setup &amp; Structure</b>", styles["Normal"]),
        Paragraph("Account setup, keyword research, ad copy, campaign architecture for 2 locations ($1,500/month ad spend)", style_small),
        "1",
        "$300"
    ],
    [
        Paragraph("<b>GBP Optimisation &amp; Facebook Pixel Setup</b>", styles["Normal"]),
        Paragraph("Google Business Profile photo revamp &amp; copy update, Facebook Pixel installation &amp; verification", style_small),
        "1",
        "$250"
    ],
]

table_data = [
    [Paragraph(h, s(f"h_{i}", fontName="Helvetica-Bold", fontSize=8, textColor=WHITE)) for i, h in enumerate(service_header)]
] + services + [
    ["", "", Paragraph("<b>SUBTOTAL</b>", styles["Normal"]), Paragraph("<b>$1,500</b>", styles["Normal"])],
    ["", "", Paragraph("<b>TOTAL DUE</b>", s("td", fontName="Helvetica-Bold", fontSize=10, textColor=DARK)), Paragraph("<b>$1,500 USD</b>", s("tv", fontName="Helvetica-Bold", fontSize=10, textColor=DARK))],
]

svc_table = Table(table_data, colWidths=col_widths, repeatRows=1)
svc_table.setStyle(TableStyle([
    # Header row
    ("BACKGROUND", (0,0), (-1,0), DARK),
    ("TEXTCOLOR", (0,0), (-1,0), WHITE),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 8),
    ("TOPPADDING", (0,0), (-1,0), 6),
    ("BOTTOMPADDING", (0,0), (-1,0), 6),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    # Alternating rows
    ("BACKGROUND", (0,1), (-1,1), LIGHT_BG),
    ("BACKGROUND", (0,2), (-1,2), WHITE),
    ("BACKGROUND", (0,3), (-1,3), LIGHT_BG),
    ("BACKGROUND", (0,4), (-1,4), WHITE),
    ("BACKGROUND", (0,5), (-1,5), LIGHT_BG),
    # Body
    ("FONTNAME", (0,1), (-1,-3), "Helvetica"),
    ("FONTSIZE", (0,1), (-1,-3), 9),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("TOPPADDING", (0,1), (-1,-3), 5),
    ("BOTTOMPADDING", (0,1), (-1,-3), 5),
    # Subtotal/total rows
    ("TOPPADDING", (0,-2), (-1,-1), 5),
    ("BOTTOMPADDING", (0,-2), (-1,-1), 5),
    ("LINEABOVE", (0,-2), (-1,-2), 1, MID),
    ("LINEABOVE", (0,-1), (-1,-1), 1.5, DARK),
    # Grid
    ("GRID", (0,0), (-1,-3), 0.25, colors.HexColor("#DDDDEE")),
    ("LINEBEFORE", (0,0), (0,-1), 0, WHITE),
]))
story.append(svc_table)
story.append(Spacer(1, 8*mm))

# ── PAYMENT SCHEDULE ──────────────────────────────────────────────────────────
story.append(Paragraph("PAYMENT SCHEDULE", style_section_head))
story.append(Spacer(1, 2*mm))

pay_data = [
    [
        Paragraph("<b>PAYMENT</b>", s("ph", fontName="Helvetica-Bold", fontSize=8, textColor=WHITE)),
        Paragraph("<b>DUE DATE</b>", s("ph2", fontName="Helvetica-Bold", fontSize=8, textColor=WHITE)),
        Paragraph("<b>AMOUNT</b>", s("ph3", fontName="Helvetica-Bold", fontSize=8, textColor=WHITE)),
        Paragraph("<b>DESCRIPTION</b>", s("ph4", fontName="Helvetica-Bold", fontSize=8, textColor=WHITE)),
    ],
    [
        Paragraph("Payment 1 of 2", styles["Normal"]),
        Paragraph("<b>Upon Receipt</b>", styles["Normal"]),
        Paragraph("<b>$750 USD</b>", styles["Normal"]),
        Paragraph("50% deposit — due immediately to commence work", style_small),
    ],
    [
        Paragraph("Payment 2 of 2", styles["Normal"]),
        Paragraph("31 March 2026", styles["Normal"]),
        Paragraph("$750 USD", styles["Normal"]),
        Paragraph("Balance — due 14 days from invoice date", style_small),
    ],
]

pay_table = Table(pay_data, colWidths=[30*mm, 35*mm, 30*mm, None])
pay_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), ACCENT),
    ("TEXTCOLOR", (0,0), (-1,0), WHITE),
    ("BACKGROUND", (0,1), (-1,1), LIGHT_BG),
    ("BACKGROUND", (0,2), (-1,2), WHITE),
    ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE", (0,1), (-1,-1), 9),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#DDDDEE")),
]))
story.append(pay_table)
story.append(Spacer(1, 8*mm))

# ── PAYMENT DETAILS ───────────────────────────────────────────────────────────
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#CCCCDD")))
story.append(Spacer(1, 4*mm))

pay_info = [
    [
        Paragraph("PAYMENT DETAILS", style_section_head),
        Paragraph("NOTES", style_section_head),
    ],
    [
        Table([
            [Paragraph("Bank:", style_label), Paragraph("Westpac", style_value)],
            [Paragraph("Account Name:", style_label), Paragraph("Jessica Morrell", style_value)],
            [Paragraph("BSB:", style_label), Paragraph("033 364", style_value)],
            [Paragraph("Account No.:", style_label), Paragraph("952070", style_value)],
            [Paragraph("Reference:", style_label), Paragraph("INV-2026-001", style_value_bold)],
            [Paragraph("", style_label), Paragraph("", style_value)],
            [Paragraph("Wise Tag:", style_label), Paragraph("@leadinglegalptyltd", style_value_bold)],
            [Paragraph("Wise Link:", style_label), Paragraph("<link href='https://wise.com/pay/business/leadinglegalptyltd' color='#E63946'>Pay via Wise</link>", style_value)],
        ], colWidths=[28*mm, 55*mm], style=TableStyle([
            ("LEFTPADDING", (0,0), (-1,-1), 0),
            ("RIGHTPADDING", (0,0), (-1,-1), 0),
            ("TOPPADDING", (0,0), (-1,-1), 2),
            ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ])),
        Paragraph(
            "Payment in USD preferred. Please include invoice number as reference. "
            "Late payments may incur a 5% fee after 7 days past due date. "
            "Work commences upon receipt of first payment.",
            style_note
        )
    ]
]

pay_info_table = Table(pay_info, colWidths=[90*mm, None])
pay_info_table.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ("TOPPADDING", (0,0), (-1,-1), 2),
    ("BOTTOMPADDING", (0,0), (-1,-1), 2),
]))
story.append(pay_info_table)
story.append(Spacer(1, 6*mm))

# ── FOOTER ─────────────────────────────────────────────────────────────────────
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#CCCCDD")))
story.append(Spacer(1, 3*mm))
story.append(Paragraph(
    "Thank you for the opportunity — excited to get this campaign fired up. | WILBA / wilba.ai | jjessmorrell@gmail.com",
    s("footer", fontName="Helvetica-Oblique", fontSize=8, textColor=MID, alignment=TA_CENTER)
))

doc.build(story)
print(f"Invoice generated: {OUTPUT_PATH}")
