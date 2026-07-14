"""Monkey Joe's — comprehensive read-only GHL account audit (runs in GitHub Actions).

The dev session's network blocks GHL, so `mj-audit.yml` runs this server-side and
commits results back. This version pulls EVERY contact and tallies EVERY tag, so
we can see the real picture: audience, redemptions by code, campaign sends (incl.
the weekend BANANAS / 4th-of-July blast), birthday funnel, and custom fields.

Writes:
  outputs/monkey-joes/reporting/ghl-audit.json   (full tag histogram + metrics)
  outputs/monkey-joes/reporting/ghl-audit.md     (human-readable summary)

Required env (secrets in Actions, or .env locally):
  GHL_API_KEY_POL, GHL_LOCATION_ID_POL
  GHL_API_KEY_WP,  GHL_LOCATION_ID_WP
"""
from __future__ import annotations

import json
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib import error, request

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
        "User-Agent": "wilba-mj/1.0",
    }


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


def fetch_all_contacts(api_key: str, location_id: str) -> list[dict]:
    """Pull every contact (paginated) so we can tally all tags client-side."""
    out, page = [], 1
    while True:
        status, data = _req("POST", f"{GHL_BASE}/contacts/search", api_key,
                            {"locationId": location_id, "pageLimit": 100, "page": page})
        if status not in (200, 201):
            break
        batch = data.get("contacts", [])
        if not batch:
            break
        out.extend(batch)
        total = data.get("total")
        if len(batch) < 100 or (total and len(out) >= total):
            break
        page += 1
        if page > 60:  # safety
            break
    return out


def custom_fields(api_key: str, location_id: str) -> list[dict]:
    status, data = _req("GET", f"{GHL_BASE}/locations/{location_id}/customFields", api_key)
    if status not in (200, 201):
        return []
    return data.get("customFields", data.get("customField", [])) or []


def find_child_birthday_field(fields: list[dict]) -> dict | None:
    for f in fields:
        if "birth" in (f.get("name") or "").lower():
            return {"id": f.get("id"), "name": f.get("name"), "dataType": f.get("dataType")}
    return None


def audit_location(loc: str, api_key: str, location_id: str) -> dict:
    lc = loc.lower()
    res: dict = {"location_id": location_id, "connection": "unknown"}
    contacts = fetch_all_contacts(api_key, location_id)
    if not contacts:
        # distinguish auth failure from a truly empty account
        st, _ = _req("POST", f"{GHL_BASE}/contacts/search", api_key,
                     {"locationId": location_id, "pageLimit": 1})
        res["connection"] = "ok (empty)" if st in (200, 201) else f"FAILED ({st})"
        return res
    res["connection"] = "ok"
    res["total_contacts"] = len(contacts)

    # Full tag histogram
    hist = Counter()
    with_email = with_phone = 0
    for c in contacts:
        for t in (c.get("tags") or []):
            hist[t] += 1
        if c.get("email"):
            with_email += 1
        if c.get("phone"):
            with_phone += 1
    res["with_email"] = with_email
    res["with_phone"] = with_phone
    res["all_tags"] = dict(hist.most_common())

    # Grouped views
    def match(*subs):
        return {t: n for t, n in hist.items() if any(s in t.lower() for s in subs)}

    res["redemption_tags"] = match("redeem", "redeemed", "used", "promo-redeemed")
    res["campaign_tags"] = match("weekend-stars", "bananas", "stars", "blast", "4th", "july")
    res["offer_lead_tags"] = match("bogo", "50off", "half", "welcome", "voucher-delivered", "fjp", "fj-")
    res["birthday_tags"] = match("bday", "birthday")

    # Headline metrics
    res["metrics"] = {
        "voucher_delivered": hist.get("voucher-delivered", 0),
        "unsubscribed": hist.get("unsubscribed", 0),
        "redemptions_total": sum(res["redemption_tags"].values()),
        "birthday_leads": hist.get(f"birthday-{lc}-lead", 0),
        "birthday_booked": hist.get(f"birthday-{lc}-booked", 0),
    }

    fields = custom_fields(api_key, location_id)
    res["custom_fields_count"] = len(fields)
    res["child_birthday_field"] = find_child_birthday_field(fields)
    return res


def render_md(report: dict) -> str:
    L = ["# Monkey Joe's — GHL Account Audit (comprehensive)", "",
         f"_Generated {report['generated_at']} (live, server-side via GitHub Actions)_", ""]
    for loc, d in report["locations"].items():
        L.append(f"## {loc}")
        if d.get("connection") != "ok":
            L.append(f"- Connection: **{d.get('connection')}**"); L.append(""); continue
        m = d["metrics"]
        L += [
            f"- Connection: **ok** · {d['total_contacts']} contacts ({d['with_email']} email · {d['with_phone']} phone)",
            f"- Opted-in (`voucher-delivered`): **{m['voucher_delivered']}** · unsubscribed: {m['unsubscribed']}",
            f"- **Redemptions tracked: {m['redemptions_total']}**  → {d['redemption_tags'] or 'none found'}",
            f"- Birthday: {m['birthday_leads']} leads · {m['birthday_booked']} booked",
        ]
        cb = d.get("child_birthday_field")
        L.append(f"- Child-birthday field: `{cb['id']}` ({cb['name']}, {cb['dataType']})" if cb
                 else "- Child-birthday field: not found")
        L.append(f"- **Campaign sends (incl. BANANAS/4th-of-July):** {d['campaign_tags'] or 'none found'}")
        L.append(f"- Offer/lead tags: {d['offer_lead_tags'] or 'none'}")
        L.append("")
        L.append("<details><summary>All tags</summary>\n")
        for t, n in d["all_tags"].items():
            L.append(f"  - `{t}`: {n}")
        L.append("\n</details>\n")
    return "\n".join(L)


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
        print(f"   {loc}: {report['locations'][loc].get('connection')}")
    (OUT_DIR / "ghl-audit.json").write_text(json.dumps(report, indent=2))
    (OUT_DIR / "ghl-audit.md").write_text(render_md(report))
    print(f"\n✓ wrote {OUT_DIR/'ghl-audit.json'} and ghl-audit.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
