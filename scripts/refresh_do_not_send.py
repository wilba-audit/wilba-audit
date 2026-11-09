#!/usr/bin/env python3
"""Regenerate outputs/pipeline/DO-NOT-SEND.txt from the pipeline CSV.

WHY THIS IS A STANDALONE SCRIPT RATHER THAN A STEP INSIDE append_prospects.py.
It was first written as a step in the appender, on 9 Nov 2026, and that was the wrong
hook for two reasons found immediately:

  1. The appender returns early when it is given no rows, so any run that appended
     nothing would silently skip the refresh.
  2. More importantly, a grade change is not an append. On 9 Nov ten rows changed grade
     by a direct edit to the CSV - nine recoveries, one disqualification - and not one of
     them went through the appender. Those are exactly the changes a do-not-send list has
     to track: a row leaving C for B is a row that becomes sendable, and a row becoming
     DISQ is one that must stop.

So the refresh has to be runnable on its own, after ANY change to the CSV, and the
appender calls it as well. Run it with no arguments:  python3 scripts/refresh_do_not_send.py

The file it writes is the sourcing side's authoritative answer to "which rows must not go
out", so the drafting side can RE-DERIVE its skip list from a committed source every run
instead of appending to one and trusting it. That matters because the drafting channel's
own skip list was silently truncated by two edits on 4-5 Nov, releasing every hold with
nobody noticing. Nothing was sent, because the send trigger was off.

A grade is a qualification verdict, NOT a send clearance: a row can be A or B and still be
unsendable for a reason the grade does not carry. Those live in the row's notes and in the
sourcing log, not here.
"""
import collections, csv, io, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIPELINE = os.path.join(REPO, 'outputs/pipeline/clinic-pipeline.csv')
TARGET = os.path.join(REPO, 'outputs/pipeline/DO-NOT-SEND.txt')
SENDABLE = ('A', 'B')


def refresh(quiet=False):
    with io.open(PIPELINE, encoding='utf-8') as fh:
        rows = list(csv.DictReader(fh))
    non = [r for r in rows
           if (r.get('icp_fit') or '').strip().upper() not in SENDABLE]
    ids = sorted((r['id'] for r in non), key=int)
    grades = dict(collections.Counter(
        (r.get('icp_fit') or '?').strip().upper() for r in non))

    # Keep the explanatory header, replace only the id list, so the rationale cannot be
    # lost by a regeneration. If the header has gone, the file is rebuilt without it and
    # the caller is told, rather than quietly writing a bare list nobody can interpret.
    head = []
    if os.path.exists(TARGET):
        with io.open(TARGET, encoding='utf-8') as fh:
            head = [ln for ln in fh if ln.startswith('#') or not ln.strip()]
    if not head:
        print('WARNING: %s had no comment header; writing ids only. '
              'Restore the rationale from git history.' % os.path.basename(TARGET))

    with io.open(TARGET, 'w', encoding='utf-8') as fh:
        fh.writelines(head)
        fh.writelines(i + '\n' for i in ids)

    if not quiet:
        print('DO-NOT-SEND.txt: %d non-sendable of %d rows %s'
              % (len(ids), len(rows), grades))
    return ids


if __name__ == '__main__':
    refresh()
    sys.exit(0)
