"""Monkey Joe's — read-only GHL account audit (runs server-side in GitHub Actions).

This is the "live access via GitHub Actions" path: this session's network policy
blocks GHL directly, but a GitHub Actions runner reaches it fine. The
`mj-audit.yml` workflow runs this and commits the results back to the repo so
they can be read from any session.

For each location (POL + WP) it reports, using only READ calls:
  - audience counts by key tag (voucher-delivered, unsubscribed, lead + redemption tags)
  - the custom-field list, and specifically the child-birthday field id
    (this is the value that belongs in the CHILD_BDAY_FIELD_ID secret)

Writes:
  outputs/monkey-joes/reporting/ghl-audit.json   (machine-readable)
  outputs/monkey-joes/reporting/ghl-audit.md     (human-readable summary)

Required env (secrets in Actions, or .env locally):
  GHL_API_KEY_POL, GHL_LOCATION_ID_POL
  GHL_API_KEY_WP,  GHL_LOCATION_ID_WP

Run:
  python3 scripts/mj_ghl_audit.py
"""
from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib import error, parse, request

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "outputs" / "monkey-joes" / "reporting"
OUT_DIR.mkdir(parents=True, exist_ok=True)

GHL_BASE = "https://services.leadconnectorhq.com"
GHL_VERSION = "2021-07-28"
THROTTLE = 0.3

LOCS = [
    ("POL", "GHL_API_KEY_POL", "GHL_LOCATION_ID_POL"),
    ("WP", "GHL_API_KEY_WP", "GHL_LOCATION_ID_WP"),
]

# Tags worth counting. Keep in sync with the campaign scheme.
COUNT_TAGS = [
    "voucher-delivered",
    "unsubscribed",
    "birthday-{loc}-lead",
    "birthday-{loc}-booked",
    "redeemed-{loc}",
    "promo-redeemed-{loc}",
]


def load_env() -> None:
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if "=" in line and not line.strip().startswith("#"):
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def _headers(api_key: str) -> dict:
    return {
        "Authorization": f"Bearer {api_key}",
        "Version": GHL_VERSION,
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "mj-ghl-audit/1.0",
    }


def _req(method: str, url: str, api_key: str, payload: dict | None = None) -> tuple[int, dict]:
    time.sleep(THROTTLE)
    data = json.dumps(payload).encode() if payload is not None else None
    req = request.Request(url, data=data, method=method, headers=_headers(api_key))
    try:
        with request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read() or b"{}")
    except error.HTTPError as e:
        return e.code, {"_error": e.read().decode("utf-8", "replace")[:300]}
    except Exception as e:  # noqa: BLE001
        return 0, {"_error": str(e)[:200]}


def count_tag(api_key: str, location_id: str, tag: str) -> int:
    status, data = _req(
        "POST", f"{GHL_BASE}/contacts/search", api_key,
        {"locationId": location_id, "pageLimit": 1,
         "filters": [{"field": "tags", "operator": "contains", "value": tag}]},
    )
    return int(data.get("total", 0)) if status in (200, 201) else -1


def custom_fields(api_key: str, location_id: str) -> list[dict]:
    status, data = _req("GET", f"{GHL_BASE}/locations/{location_id}/customFields", api_key)
    if status not in (200, 201):
        return []
    return data.get("customFields", data.get("customField", [])) or []


def find_child_birthday_field(fields: list[dict]) -> dict | None:
    for f in fields:
        name = (f.get("name") or "").lower()
        if "birth" in name and ("child" in name or "kid" in name or "dob" in name or "birth" in name):
            return {"id": f.get("id"), "name": f.get("name"), "dataType": f.get("dataType")}
    # fallback: any field mentioning birthday
    for f in fields:
        if "birth" in (f.get("name") or "").lower():
            return {"id": f.get("id"), "name": f.get("name"), "dataType": f.get("dataType")}
    return None


def audit_location(loc: str, api_key: str, location_id: str) -> dict:
    result: dict = {"location_id": location_id, "connection": "unknown", "tags": {}, "custom_fields": {}}
    # connection test
    status, _ = _req("POST", f"{GHL_BASE}/contacts/search", api_key,
                     {"locationId": location_id, "pageLimit": 1})
    result["connection"] = "ok" if status in (200, 201) else f"FAILED ({status})"
    if result["connection"] != "ok":
        return result
    for tmpl in COUNT_TAGS:
        tag = tmpl.format(loc=loc.lower())
        result["tags"][tag] = count_tag(api_key, location_id, tag)
    fields = custom_fields(api_key, location_id)
    result["custom_fields"]["count"] = len(fields)
    result["custom_fields"]["all"] = [{"id": f.get("id"), "name": f.get("name")} for f in fields]
    result["custom_fields"]["child_birthday"] = find_child_birthday_field(fields)
    return result


def render_md(report: dict) -> str:
    lines = ["# Monkey Joe's — GHL Account Audit", "",
             f"_Generated {report['generated_at']} (server-side via GitHub Actions)_", ""]
    for loc, data in report["locations"].items():
        lines.append(f"## {loc}")
        lines.append(f"- Connection: **{data['connection']}**")
        if data["connection"] == "ok":
            for tag, n in data["tags"].items():
                lines.append(f"- `{tag}`: {n if n >= 0 else 'error'}")
            cb = data["custom_fields"].get("child_birthday")
            if cb:
                lines.append(f"- **Child-birthday field:** `{cb['id']}` ({cb['name']}) "
                             f"→ set this as the `CHILD_BDAY_FIELD_ID` secret")
            else:
                lines.append("- **Child-birthday field:** not found — Radar can't anchor to the "
                             "child's birthday until this field exists + is populated")
            lines.append(f"- Custom fields total: {data['custom_fields'].get('count', 0)}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    load_env()
    report = {"generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
              "locations": {}}
    for loc, key_env, id_env in LOCS:
        key, lid = os.environ.get(key_env), os.environ.get(id_env)
        if not (key and lid):
            report["locations"][loc] = {"connection": f"skipped — {key_env}/{id_env} not set"}
            continue
        print(f"→ auditing {loc}...")
        report["locations"][loc] = audit_location(loc, key, lid)
        print(f"   {loc}: {report['locations'][loc]['connection']}")
    (OUT_DIR / "ghl-audit.json").write_text(json.dumps(report, indent=2))
    (OUT_DIR / "ghl-audit.md").write_text(render_md(report))
    print(f"\n✓ wrote {OUT_DIR/'ghl-audit.json'} and ghl-audit.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
