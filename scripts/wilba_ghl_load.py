"""Load WILBA's clinic prospects into Jess's own GHL sub-account.

Reads outputs/pipeline/ghl/ghl-import.csv and, for each row, upserts a contact (with the
cold-email custom fields and tags) and an opportunity in the "Clinic outreach" pipeline
at the "New prospect" stage.

It never sends anything and never adds the `outreach-go` tag, so no workflow fires.

The pipeline itself must already exist (GHL's API cannot create pipelines). Custom fields
are created if missing.

Dry run by default. Pass --live to write.

Env: WILBA_GHL_TOKEN (Private Integration token), WILBA_GHL_LOCATION_ID.
Run from GitHub Actions ("WILBA GHL load"); the dev session's network can't reach GHL.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from pathlib import Path
from urllib import error, request

GHL_BASE = "https://services.leadconnectorhq.com"
GHL_VERSION = "2021-07-28"
ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "outputs" / "pipeline" / "ghl" / "ghl-import.csv"
REPORT_PATH = ROOT / "outputs" / "pipeline" / "ghl" / "load-report.md"

PIPELINE_NAME = "Clinic outreach"
FIRST_STAGE = "New prospect"
CUSTOM_FIELDS = {  # csv column -> (GHL field name, dataType)
    "cold_subject": ("Cold subject", "TEXT"),
    "cold_opener": ("Cold opener", "LARGE_TEXT"),
    "crm_phrase": ("CRM phrase", "TEXT"),
    "tz_line": ("Timezone line", "TEXT"),
    "currency": ("Currency", "TEXT"),
    "pipeline_id": ("Pipeline ID", "TEXT"),
    "icp_grade": ("ICP grade", "TEXT"),
}


def _req(method: str, path: str, token: str, payload: dict | None = None) -> tuple[int, dict]:
    data = json.dumps(payload).encode() if payload is not None else None
    req = request.Request(f"{GHL_BASE}{path}", data=data, method=method, headers={
        "Authorization": f"Bearer {token}", "Version": GHL_VERSION,
        "Content-Type": "application/json", "Accept": "application/json",
        "User-Agent": "wilba-outreach/1.0"})
    try:
        with request.urlopen(req, timeout=30) as resp:
            return resp.status, json.loads(resp.read() or b"{}")
    except error.HTTPError as e:
        body = e.read().decode(errors="replace")
        try:
            return e.code, json.loads(body)
        except ValueError:
            return e.code, {"raw": body[:300]}


def find_pipeline(token: str, loc: str) -> tuple[str, str] | None:
    status, data = _req("GET", f"/opportunities/pipelines?locationId={loc}", token)
    if status != 200:
        sys.exit(f"Could not list pipelines ({status}): {data}")
    for p in data.get("pipelines", []):
        if p.get("name", "").strip().lower() == PIPELINE_NAME.lower():
            for s in p.get("stages", []):
                if s.get("name", "").strip().lower() == FIRST_STAGE.lower():
                    return p["id"], s["id"]
            sys.exit(f'Pipeline "{PIPELINE_NAME}" has no "{FIRST_STAGE}" stage.')
    return None


def ensure_fields(token: str, loc: str, live: bool) -> dict[str, str]:
    status, data = _req("GET", f"/locations/{loc}/customFields?model=contact", token)
    if status != 200:
        sys.exit(f"Could not list custom fields ({status}): {data}")
    existing = {f["name"].strip().lower(): f["id"] for f in data.get("customFields", [])}
    ids = {}
    for col, (name, dtype) in CUSTOM_FIELDS.items():
        if name.lower() in existing:
            ids[col] = existing[name.lower()]
        elif live:
            s, d = _req("POST", f"/locations/{loc}/customFields", token,
                        {"name": name, "dataType": dtype, "model": "contact"})
            if s not in (200, 201):
                sys.exit(f"Could not create field {name} ({s}): {d}")
            ids[col] = (d.get("customField") or d)["id"]
            print(f"created custom field {name}")
        else:
            ids[col] = f"(would create {name})"
    return ids


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="write to GHL (default: dry run)")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    token, loc = os.environ.get("WILBA_GHL_TOKEN"), os.environ.get("WILBA_GHL_LOCATION_ID")
    if not token or not loc:
        sys.exit("WILBA_GHL_TOKEN and WILBA_GHL_LOCATION_ID must be set.")

    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    if args.limit:
        rows = rows[: args.limit]

    pipe = find_pipeline(token, loc)
    pipeline_id, stage_id = pipe or (None, None)
    if not pipe:
        print(f'No pipeline named "{PIPELINE_NAME}" yet: loading contacts only. '
              "Re-run after creating it to add the opportunity cards.")
    field_ids = ensure_fields(token, loc, args.live)

    done, failed = 0, []
    for r in rows:
        contact = {
            "locationId": loc, "email": r["email"], "companyName": r["company_name"],
            "name": r["company_name"], "website": r["website"], "country": r["country"],
            "source": "WILBA clinic outreach",
            "tags": [t.strip() for t in r["tags"].split(",") if t.strip()],
            "customFields": [{"id": field_ids[c], "field_value": r[c]} for c in CUSTOM_FIELDS],
        }
        if r.get("phone"):
            contact["phone"] = r["phone"]
        if not args.live:
            done += 1
            continue
        s, d = _req("POST", "/contacts/upsert", token, contact)
        if s not in (200, 201):
            failed.append((r["company_name"], f"contact {s}: {d}"))
            continue
        cid = d["contact"]["id"]
        if not pipeline_id:
            done += 1
            time.sleep(0.25)
            continue
        s, d = _req("GET", f"/opportunities/search?location_id={loc}&contact_id={cid}"
                    f"&pipeline_id={pipeline_id}", token)
        if s == 200 and d.get("opportunities"):
            done += 1
            continue
        s, d = _req("POST", "/opportunities/", token, {
            "locationId": loc, "pipelineId": pipeline_id, "pipelineStageId": stage_id,
            "name": r["company_name"], "status": "open", "contactId": cid})
        if s not in (200, 201):
            failed.append((r["company_name"], f"opportunity {s}: {d}"))
        else:
            done += 1
        time.sleep(0.25)  # stay well under GHL's burst limit

    mode = "LIVE" if args.live else "DRY RUN"
    lines = [f"# GHL load report ({mode}, {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())})",
             "", f"- Pipeline: {'found' if pipe else 'NOT FOUND (contacts only, no cards)'}",
             f"- Custom fields: {', '.join(f'{c}={v}' for c, v in field_ids.items())}",
             f"- Rows: {len(rows)}", f"- Loaded: {done}", f"- Failed: {len(failed)}", ""]
    lines += [f"- {name}: {why}" for name, why in failed]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
