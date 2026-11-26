#!/usr/bin/env python3
"""Generate outputs/pipeline/COVERAGE.md: every market sweep ever recorded, in one place.

WHY THIS EXISTS. For five consecutive nights a sourcing run briefed suburbs that a prior
sweep had already worked, and for four of those nights the response was to write a better
grep pattern. That does not work, because the thing being grepped is prose: each worker
labels its own coverage however it likes. Six label shapes exist in near-misses.md as of
26 Nov 2026 -- "Markets swept:", "Market:", "Towns briefed.", "Towns worked:",
"Swept <date>." and "Assigned:" -- and the night a fix back-filled aliases for the two
shapes then in view, a worker lost most of its budget to a sweep recorded under a third.

A fix that enumerates the instances in view cannot find an instance nobody knows about.
So this script does not grep for labels it knows. It finds every coverage-shaped line AND
reports every heading it could not classify, so a seventh label shape announces itself in
the output instead of hiding until someone pays for it.

Run it before briefing a sourcing run:

    python3 scripts/coverage_index.py            # writes outputs/pipeline/COVERAGE.md
    python3 scripts/coverage_index.py --check    # print the unclassified lines and exit

THE INDEX IS AN ORIENTATION TOOL AND NOT A CLEARANCE. It tells you where to read. The
only check that tells you the truth is grepping each candidate's NAME, its DOMAIN, and
its name with whitespace collapsed, and reading every hit in context -- because a sweep
can work a suburb without naming it, and can name a suburb without working it.
"""
import argparse
import os
import re
import sys

SRC = 'outputs/pipeline/near-misses.md'
OUT = 'outputs/pipeline/COVERAGE.md'

# Every label shape that has ever declared coverage in this file. Add to it rather than
# replacing: an old shape stays in the file forever once written.
LABELS = (
    re.compile(r'^\*{0,2}Markets? swept[:.]\*{0,2}\s*(.*)', re.I),
    re.compile(r'^\*{0,2}Market[:.]\*{0,2}\s*(.*)', re.I),
    re.compile(r'^\*{0,2}Towns? (?:briefed|worked|swept)[:.]\*{0,2}\s*(.*)', re.I),
    re.compile(r'^\*{0,2}Swept\s+(\d{4}-\d{2}-\d{2})[:.]\*{0,2}\s*(.*)', re.I),
    re.compile(r'^\*{0,2}Assigned[:.]\*{0,2}\s*(.*)', re.I),
    re.compile(r'^\*{0,2}Suburbs?(?: swept| briefed| worked)?[:.]\*{0,2}\s*(.*)', re.I),
)

# Lines that look like they might declare coverage but match no label above. Printed so a
# new shape is visible. Deliberately over-inclusive: a false alarm costs one read, a miss
# costs a worker's budget.
# It must LOOK like a label, not merely contain a coverage word: either bolded, or a short
# phrase closed by a colon. Without that this matched 137 lines, almost all of them wrapped
# prose containing the word "sweep" - and an alarm that cries 137 times is not read.
SUSPECT = re.compile(
    r'^(?:\*\*[^*]{3,40}(?:swept|sweep|briefed|worked|covered|coverage|ground|metros?'
    r'|markets?|territor|suburbs?|towns?|cities)[^*]{0,20}\*\*'
    r'|[A-Z][\w\- ]{0,30}(?:swept|sweep|briefed|worked|covered|coverage|ground|metros?'
    r'|markets?|territor|suburbs?|towns?|cities)[\w\- ]{0,20}:)', re.I)

# A SOURCE is coverable ground too, and this was learned the expensive way: a precinct directory
# re-opened on 26 Nov returned 5 of 5 leaves already in the pipeline, and a Fresha suburb slug
# re-indexed on 25 Nov returned 0 of 12 new. Nine fetches, 10% of a run's budget, for nothing -
# and both were avoidable from the coverage record, which until now only recorded PLACES.
SOURCE_URL = re.compile(
    r'(?:https?://)?(?:www\.)?('
    r'fresha\.com/lp/[a-z]{2}/[bt]t/[a-z0-9-]+/in/[a-z]{2}-[a-z0-9-]+(?:/[a-z0-9-]+)?'
    r'|[a-z0-9][a-z0-9-]{3,40}\.(?:com\.au|org\.au|co\.nz|co\.uk|ie|ca|com|org)'
    r'/(?:directory|trader|traders|our-members|members|category|trader-category|businesses|'
    r'business-directory|shop|stores)[a-z0-9/_-]*'
    r')', re.I)

DATE = re.compile(r'\b(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+20\d\d'
                  r'|\d{4}-\d{2}-\d{2})', re.I)
HEADING = re.compile(r'^#{1,3}\s+(.*)')


def read_blocks(path):
    """Yield (line_no, heading_in_force, label_text, places) for every coverage line."""
    heading = ''
    hdr_line = 0
    with open(path, encoding='utf-8') as fh:
        lines = fh.read().splitlines()
    found, suspects, sources = [], [], {}
    for i, line in enumerate(lines, 1):
        h = HEADING.match(line)
        if h:
            # Several sections are fenced by "# =====" divider lines. Taking one as the heading
            # in force prints a row of equals signs where the market name should be, so skip
            # anything with no letters in it and keep the real heading.
            text = h.group(1).strip()
            if re.search(r'[A-Za-z]', text):
                heading, hdr_line = text, i
            continue
        hit = None
        for pat in LABELS:
            m = pat.match(line)
            if m:
                hit = ' '.join(g for g in m.groups() if g)
                break
        if hit is not None:
            # a label's places usually wrap over the next few lines
            tail = []
            for nxt in lines[i:i + 5]:
                if not nxt.strip() or HEADING.match(nxt) or nxt.startswith('**'):
                    break
                tail.append(nxt.strip())
            found.append((i, heading, hdr_line, ' '.join([hit] + tail)))
        elif SUSPECT.match(line):
            suspects.append((i, heading, line.strip()[:160]))
        for sm in SOURCE_URL.finditer(line):
            sources.setdefault(sm.group(1).rstrip('.,;)').lower(), []).append((i, heading))
    return found, suspects, sources


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true',
                    help='print unclassified coverage-shaped lines and exit')
    args = ap.parse_args()

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src = os.path.join(root, SRC)
    if not os.path.exists(src):
        sys.exit('not found: %s' % src)
    found, suspects, sources = read_blocks(src)

    # A suspect line that IS one of the found lines is not a suspect.
    found_lines = {ln for ln, _, _, _ in found}
    suspects = [s for s in suspects if s[0] not in found_lines]

    if args.check:
        print('%d coverage lines classified, %d lines unclassified' % (len(found), len(suspects)))
        for ln, head, text in suspects:
            print('  %6d  [%s]  %s' % (ln, head[:40], text))
        return

    out = [
        '# Coverage index — every market sweep on record',
        '',
        '**Generated by `scripts/coverage_index.py`. Do not edit by hand; it is overwritten.**',
        'Regenerate it before briefing a sourcing run.',
        '',
        'This exists because the coverage check failed five nights running, each time because a',
        'sweep had labelled its ground with a phrase the night\'s grep did not know. Six label',
        'shapes are in use. Enumerating the labels in view never found the one out of view, so this',
        'is derived from the file every run instead of maintained by hand.',
        '',
        '**THIS IS AN ORIENTATION TOOL, NOT A CLEARANCE.** It tells you where to read. The check',
        'that tells you the truth is grepping each candidate clinic\'s NAME, its DOMAIN, and its',
        'name with whitespace collapsed, and reading every hit in context — a sweep can work a',
        'suburb without naming it, and name a suburb without working it.',
        '',
        '| near-misses.md line | date | section | ground declared |',
        '| --- | --- | --- | --- |',
    ]
    for ln, head, hdr_line, text in found:
        d = DATE.search(head) or DATE.search(text)
        text = ' '.join(text.split())
        if len(text) > 300:
            text = text[:297] + '…'
        out.append('| %d | %s | %s | %s |'
                   % (ln, d.group(1) if d else '—',
                      (head[:70] or '(no heading)').replace('|', '\\|'),
                      text.replace('|', '\\|')))
    out += ['', '**%d coverage lines.**' % len(found), '']
    out += [
        '## Sources already worked — a SOURCE is coverable ground too',
        '',
        'A precinct directory re-opened on 26 Nov returned 5 of 5 leaves already in the pipeline,',
        'and a Fresha suburb slug re-indexed on 25 Nov returned 0 of 12 new names. Nine fetches,',
        'a tenth of that run\'s budget, for nothing — and both were avoidable from the record,',
        'which until then tracked only places. **Both species are ONE-SHOT with themselves.**',
        'Check this table before fetching an index, a slug or a trader directory.',
        '',
        '| times seen | source | first recorded under |',
        '| --- | --- | --- |',
    ]
    for src_url, seen in sorted(sources.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        line0, head0 = seen[0]
        out.append('| %d | `%s` | line %d, %s |'
                   % (len(seen), src_url, line0,
                      (head0[:60] or '(no heading)').replace('|', '\\|')))
    out += ['', '**%d distinct sources.**' % len(sources), '']
    if suspects:
        out += [
            '## Coverage-shaped lines this script could NOT classify',
            '',
            'Each one may be a seventh label shape. Read them; if one declares ground, add its',
            'shape to `LABELS` in the script rather than back-filling an alias by hand.',
            '',
        ]
        for ln, head, text in suspects:
            out.append('- **line %d** (%s) — `%s`' % (ln, head[:50], text.replace('`', "'")))
        out.append('')
    else:
        out += ['No unclassified coverage-shaped lines.', '']

    dest = os.path.join(root, OUT)
    with open(dest, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out))
    print('%s: %d coverage lines, %d sources, %d unclassified'
          % (OUT, len(found), len(sources), len(suspects)))


if __name__ == '__main__':
    main()
