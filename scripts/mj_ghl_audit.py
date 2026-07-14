"""Monkey Joe's — accurate read-only GHL account audit (runs in GitHub Actions).

The dev session's network blocks GHL, so `mj-audit.yml` runs this server-side and
commits results back.

Accuracy approach: discover every tag name from the location's tag list, then get
GHL's own authoritative COUNT for each tag (the search `total`, which is exact even
when the account has thousands of contacts). This avoids under-counting from
client-side pagination.

Writes:
  outputs/monkey-joes/reporting/ghl-audit.json   (authoritative tag counts + groups)
  outputs/monkey-joes/reporting/ghl-audit.md     (human-readable summary)
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
THROTTLE = 0.25

LOCS = [
    ("POL", "GHL_API_KEY_POL", "GHL_LOCATION_ID_POL"),
    ("WP", "GHL_API_KEY_WP", "GHL_LOCATION_ID_WP"),
]

# weekend BANANAS / 4th-of-July cohort tags (in case they aren't in the tag list yet)
KNOWN_EXTRA = [
    "weekend-stars-email-pol-2026-06-30", "weekend-stars-sms-pol-2026-07-02",
    "weekend-stars-email-wp-2026-06-30", "weekend-stars-sms-wp-2026-07-02",
]


def load_env() -> None:
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if "=" in line and not line.strip().startswith("#"):
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def _headers(api_key: str) -> dict:
    return {"Authorization": f"Bearer {api_key}", "Version": GHL_VERSION,
            "Content-Type": "application/json", "Accept": "application/json",
            "User-Agent": "wilba-mj/1.0"}


def _req(method: str, url: str, api_key: str, payload: dict | None = None) -> tuple[int, dict]:
    time.sleep(THROTTLE)
    data = json.dumps(payload).encode() if payload is not None else None
    req = request.Request(url, data=data, method=method, headers=_headers(api_key))
    try:
        with request.urlopen(req, timeout=40) as r:
            return r.status, json.loads(r.read() or b"{}")
    except error.HTTPError as e:
        return e.code, {"_error": e.read().decode("utf-8", "replace")[:300]}
    except Exception as e:  # noqa: BLE001
        return 0, {"_error": str(e)[:200]}


def list_tag_names(api_key: str, location_id: str) -> list[str]:
    status, data = _req("GET", f"{GHL_BASE}/locations/{location_id}/tags", api_key)
    names = []
    if status in (200, 201):
        for t in (data.get("tags") or []):
            n = t.get("name")
            if n:
                names.append(n)
    return names


def count_tag(api_key: str, location_id: str, tag: str) -> int:
    """GHL's authoritative count of contacts carrying this tag."""
    status, data = _req("POST", f"{GHL_BASE}/contacts/search", api_key,
                        {"locationId": location_id, "pageLimit": 1,
                         "filters": [{"field": "tags", "operator": "contains", "value": tag}]})
    return int(data.get("total", 0)) if status in (200, 201) else -1


def total_contacts(api_key: str, location_id: str) -> int:
    status, data = _req("POST", f"{GHL_BASE}/contacts/search", api_key,
                        {"locationId": location_id, "pageLimit": 1})
    return int(data.get("total", 0)) if status in (200, 201) else -1


def custom_fields(api_key: str, location_id: str) -> list[dict]:
    status, data = _req("GET", f"{GHL_BASE}/locations/{location_id}/customFields", api_key)
    return (data.get("customFields") or data.get("customField") or []) if status in (200, 201) else []


def child_bday_field(fields: list[dict]) -> dict | None:
    for f in fields:
        if "birth" in (f.get("name") or "").lower():
            return {"id": f.get("id"), "name": f.get("name"), "dataType": f.get("dataType")}
    return None


def audit_location(loc: str, api_key: str, location_id: str) -> dict:
    lc = loc.lower()
    res: dict = {"location_id": location_id}
    tc = total_contacts(api_key, location_id)
    if tc < 0:
        res["connection"] = "FAILED"; return res
    res["connection"] = "ok"
    res["total_contacts"] = tc

    names = sorted(set(list_tag_names(api_key, location_id)) | set(KNOWN_EXTRA))
    counts = {n: count_tag(api_key, location_id, n) for n in names}
    counts = {n: c for n, c in counts.items() if c > 0}  # drop empties
    res["tag_counts"] = dict(sorted(counts.items(), key=lambda kv: -kv[1]))

    def grp(*subs):
        return {t: c for t, c in counts.items() if any(s in t.lower() for s in subs)}

    # Redemptions: dedupe the two naming conventions (x-redeemed AND redeemed-x are the same event)
    redemption = grp("redeem")
    by_code = {}
    for code in ("bogo", "half", "welcome", "fjp", "bday25"):
        vals = [c for t, c in redemption.items() if code in t.lower()]
        if vals:
            by_code[code] = max(vals)  # the pair should match; max guards against one being stale
    res["redemptions_by_code"] = by_code
    res["redemptions_total"] = sum(by_code.values())
    res["redemption_tags_raw"] = redemption

    res["campaign_sends"] = grp("weekend-stars", "bananas", "nudge", "blast")
    res["offer_leads"] = grp("-lead", "offer-", "voucher-delivered", "promo-issued")
    res["birthday"] = grp("bday", "birthday")
    res["voice_inbound"] = grp("voice-agent", "inbound-call", "topic-party", "birthday-inquiry")

    res["metrics"] = {
        "voucher_delivered": counts.get("voucher-delivered", 0),
        "unsubscribed": counts.get("unsubscribed", 0),
    }
    fields = custom_fields(api_key, location_id)
    res["custom_fields_count"] = len(fields)
    res["child_birthday_field"] = child_bday_field(fields)
    return res


def render_md(rep: dict) -> str:
    L = ["# Monkey Joe's — GHL Account Audit (authoritative tag counts)", "",
         f"_Generated {rep['generated_at']} (live, server-side via GitHub Actions)_", ""]
    for loc, d in rep["locations"].items():
        L.append(f"## {loc}")
        if d.get("connection") != "ok":
            L += [f"- Connection: **{d.get('connection')}**", ""]; continue
        L += [
            f"- Connection: **ok** · {d['total_contacts']} total contacts in the account",
            f"- Opted-in (`voucher-delivered`): **{d['metrics']['voucher_delivered']}** · unsubscribed: {d['metrics']['unsubscribed']}",
            f"- **Redemptions by code:** {d['redemptions_by_code'] or 'none'}  →  **total {d['redemptions_total']}**",
            f"- **BANANAS / nudge campaign sends:** {d['campaign_sends'] or 'none'}",
            f"- Birthday: {d['birthday'] or 'none'}",
            f"- Voice/inbound: {d['voice_inbound'] or 'none'}",
        ]
        cb = d.get("child_birthday_field")
        L.append(f"- Child-birthday field: `{cb['id']}` ({cb['name']}, {cb['dataType']})" if cb else "- Child-birthday field: not found")
        L.append("\n<details><summary>All tag counts</summary>\n")
        for t, c in d["tag_counts"].items():
            L.append(f"  - `{t}`: {c}")
        L.append("\n</details>\n")
    return "\n".join(L)


def main() -> int:
    load_env()
    rep = {"generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(), "locations": {}}
    for loc, ke, ie in LOCS:
        key, lid = os.environ.get(ke), os.environ.get(ie)
        if not (key and lid):
            rep["locations"][loc] = {"connection": f"skipped — {ke}/{ie} not set"}; continue
        print(f"→ auditing {loc}...")
        rep["locations"][loc] = audit_location(loc, key, lid)
        print(f"   {loc}: {rep['locations'][loc].get('connection')}")
    (OUT_DIR / "ghl-audit.json").write_text(json.dumps(rep, indent=2))
    (OUT_DIR / "ghl-audit.md").write_text(render_md(rep))
    print(f"✓ wrote {OUT_DIR/'ghl-audit.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
