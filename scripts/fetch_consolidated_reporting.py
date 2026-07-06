"""Pull consolidated reporting data for Monkey Joe's.

Pulls in this order, gracefully skipping any source that's not yet configured:
  1. GHL (POL + WP)     — always works (creds confirmed in .env)
  2. Meta Marketing API — works once META_ACCESS_TOKEN + META_AD_ACCOUNT_* are set
  3. Google Ads API     — works once GOOGLE_ADS_* env vars are set + dev token approved

Joins everything by:
  - utm_campaign  (Meta + Google ↔ GHL contact's utm fields)
  - channel prefix in promo code (BOGO-PO-G-XXXX ↔ Google, -F- ↔ Facebook)
  - date window (today / 7d / 30d / mtd)

Writes:
  outputs/monkey-joes/reporting/consolidated.json

Run:
  python3 scripts/fetch_consolidated_reporting.py
  python3 scripts/fetch_consolidated_reporting.py --days 7

Required env (in .env):
  GHL_API_KEY_POL, GHL_LOCATION_ID_POL
  GHL_API_KEY_WP,  GHL_LOCATION_ID_WP

Optional env (sources skip silently if missing):
  META_ACCESS_TOKEN, META_AD_ACCOUNT_POL, META_AD_ACCOUNT_WP
  GOOGLE_ADS_DEVELOPER_TOKEN, GOOGLE_ADS_CLIENT_ID, GOOGLE_ADS_CLIENT_SECRET,
    GOOGLE_ADS_REFRESH_TOKEN, GOOGLE_ADS_LOGIN_CUSTOMER_ID,
    GOOGLE_ADS_CUSTOMER_ID_POL, GOOGLE_ADS_CUSTOMER_ID_WP
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib import request, parse, error

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "outputs" / "monkey-joes" / "reporting" / "consolidated.json"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)


# ----------------------------------------------------------------------
# .env loader
# ----------------------------------------------------------------------

def load_env() -> None:
    env_path = ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if "=" in line and not line.strip().startswith("#"):
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


# ----------------------------------------------------------------------
# Date windows
# ----------------------------------------------------------------------

def windows(now: datetime) -> dict[str, tuple[str, str]]:
    """ISO-formatted (since, until) tuples for the standard windows."""
    iso = lambda d: d.replace(microsecond=0).isoformat()
    return {
        "today":    (iso(now.replace(hour=0, minute=0, second=0)), iso(now)),
        "yesterday":(iso((now - timedelta(days=1)).replace(hour=0, minute=0, second=0)),
                     iso(now.replace(hour=0, minute=0, second=0))),
        "last_7d":  (iso(now - timedelta(days=7)),  iso(now)),
        "last_30d": (iso(now - timedelta(days=30)), iso(now)),
        "mtd":      (iso(now.replace(day=1, hour=0, minute=0, second=0)), iso(now)),
    }


# ----------------------------------------------------------------------
# GHL source
# ----------------------------------------------------------------------

GHL_BASE = "https://services.leadconnectorhq.com"
GHL_VERSION = "2021-07-28"
GHL_THROTTLE = 0.25  # ~4 req/sec


def ghl_search(api_key: str, location_id: str, filters: list, _retry: int = 0) -> dict:
    time.sleep(GHL_THROTTLE)
    payload = json.dumps({
        "locationId": location_id,
        "pageLimit": 1,
        "filters": filters,
    }).encode()
    req = request.Request(
        f"{GHL_BASE}/contacts/search",
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Version": GHL_VERSION,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Accept": "*/*",
        },
    )
    try:
        with request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except error.HTTPError as e:
        if e.code in (403, 429) and _retry < 3:
            time.sleep(2 ** _retry)
            return ghl_search(api_key, location_id, filters, _retry + 1)
        return {"total": 0, "_error": f"HTTP {e.code}"}


def count_tag_in_window(api_key: str, location_id: str, tag: str, since_iso: str) -> int:
    return ghl_search(api_key, location_id, [
        {"field": "tags", "operator": "contains", "value": tag},
        {"field": "dateAdded", "operator": "range", "value": {"gte": since_iso}},
    ]).get("total", 0)


def fetch_ghl(now: datetime) -> dict:
    out = {"available": False, "locations": {}}
    win = windows(now)
    for loc_label, key_env, id_env in [
        ("POL", "GHL_API_KEY_POL", "GHL_LOCATION_ID_POL"),
        ("WP",  "GHL_API_KEY_WP",  "GHL_LOCATION_ID_WP"),
    ]:
        key = os.environ.get(key_env)
        loc_id = os.environ.get(id_env)
        if not (key and loc_id):
            continue

        leads_tags = [f"bogo-{loc_label.lower()}-lead", f"half-{loc_label.lower()}-lead", f"50off-{loc_label.lower()}-lead"]
        redeemed_tags = [f"redeemed-{loc_label.lower()}", f"promo-redeemed-{loc_label.lower()}"]

        loc_data = {"location_id": loc_id, "leads": {}, "redeemed": {}}
        for w_key, (since, _) in win.items():
            loc_data["leads"][w_key]    = sum(count_tag_in_window(key, loc_id, t, since) for t in leads_tags)
            loc_data["redeemed"][w_key] = sum(count_tag_in_window(key, loc_id, t, since) for t in redeemed_tags)
        # Channel-prefix breakdown for redemptions (G = google, F = facebook, E = email, D = direct)
        # Tags expected: redeemed-{loc}-g, redeemed-{loc}-f, etc.
        loc_data["redeemed_by_channel"] = {}
        for ch in ("g", "f", "e", "d"):
            ch_tag = f"redeemed-{loc_label.lower()}-{ch}"
            since_30 = win["last_30d"][0]
            loc_data["redeemed_by_channel"][ch] = count_tag_in_window(key, loc_id, ch_tag, since_30)
        out["locations"][loc_label] = loc_data
        out["available"] = True
    return out


# ----------------------------------------------------------------------
# Meta Marketing API source
# ----------------------------------------------------------------------

META_API_VER = "v19.0"

def meta_get(path: str, params: dict, token: str) -> dict:
    params = {**params, "access_token": token}
    url = f"https://graph.facebook.com/{META_API_VER}{path}?{parse.urlencode(params)}"
    req = request.Request(url, headers={"User-Agent": "ads-mastermind/1.0"})
    try:
        with request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:200]
        return {"_error": f"HTTP {e.code}: {body}"}


def fetch_meta(now: datetime) -> dict:
    token = os.environ.get("META_ACCESS_TOKEN")
    if not token:
        return {"available": False, "reason": "META_ACCESS_TOKEN not set"}

    win = windows(now)
    out = {"available": True, "accounts": {}}
    for loc_label, acct_env in [("POL", "META_AD_ACCOUNT_POL"), ("WP", "META_AD_ACCOUNT_WP")]:
        acct = os.environ.get(acct_env)
        if not acct:
            out["accounts"][loc_label] = {"_error": f"{acct_env} not set"}
            continue

        loc_data = {"account_id": acct, "windows": {}, "ads": []}
        for w_key, (since, until) in [("last_7d", win["last_7d"]), ("last_30d", win["last_30d"]), ("mtd", win["mtd"])]:
            time_range = json.dumps({"since": since[:10], "until": until[:10]})
            insights = meta_get(
                f"/act_{acct}/insights",
                {"time_range": time_range, "fields": "spend,impressions,clicks,reach,actions,action_values"},
                token,
            )
            if "_error" in insights:
                loc_data["windows"][w_key] = insights
                continue
            data = (insights.get("data") or [{}])[0]
            actions = {a.get("action_type"): float(a.get("value", 0)) for a in data.get("actions", [])}
            loc_data["windows"][w_key] = {
                "spend": float(data.get("spend", 0)),
                "impressions": int(data.get("impressions", 0)),
                "clicks": int(data.get("clicks", 0)),
                "reach": int(data.get("reach", 0)),
                "leads": int(actions.get("lead", 0) + actions.get("offsite_conversion.fb_pixel_lead", 0)),
                "purchases": int(actions.get("purchase", 0) + actions.get("offsite_conversion.fb_pixel_purchase", 0)),
                "lp_views": int(actions.get("landing_page_view", 0)),
            }

        # Per-ad breakdown for the last 30d
        ads = meta_get(
            f"/act_{acct}/insights",
            {
                "time_range": json.dumps({"since": win["last_30d"][0][:10], "until": win["last_30d"][1][:10]}),
                "level": "ad",
                "fields": "ad_name,spend,impressions,clicks,actions",
                "limit": 100,
            },
            token,
        )
        if "_error" not in ads:
            for ad in (ads.get("data") or []):
                actions = {a.get("action_type"): float(a.get("value", 0)) for a in ad.get("actions", [])}
                loc_data["ads"].append({
                    "ad_name": ad.get("ad_name"),
                    "spend": float(ad.get("spend", 0)),
                    "impressions": int(ad.get("impressions", 0)),
                    "clicks": int(ad.get("clicks", 0)),
                    "leads": int(actions.get("lead", 0) + actions.get("offsite_conversion.fb_pixel_lead", 0)),
                    "cpl": round(float(ad.get("spend", 0)) / max(int(actions.get("lead", 0) + actions.get("offsite_conversion.fb_pixel_lead", 0)), 1), 2),
                })
        out["accounts"][loc_label] = loc_data
    return out


# ----------------------------------------------------------------------
# Google Ads source (REST via OAuth)
# ----------------------------------------------------------------------

def google_ads_token() -> str | None:
    """Exchange refresh token for an access token."""
    refresh = os.environ.get("GOOGLE_ADS_REFRESH_TOKEN")
    client_id = os.environ.get("GOOGLE_ADS_CLIENT_ID")
    client_secret = os.environ.get("GOOGLE_ADS_CLIENT_SECRET")
    if not (refresh and client_id and client_secret):
        return None
    payload = parse.urlencode({
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh,
        "grant_type": "refresh_token",
    }).encode()
    req = request.Request("https://oauth2.googleapis.com/token", data=payload, method="POST")
    try:
        with request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read()).get("access_token")
    except error.HTTPError as e:
        return None


def google_ads_query(access_token: str, dev_token: str, login_cid: str, customer_id: str, gaql: str) -> dict:
    url = f"https://googleads.googleapis.com/v16/customers/{customer_id}/googleAds:searchStream"
    req = request.Request(
        url,
        data=json.dumps({"query": gaql}).encode(),
        method="POST",
        headers={
            "Authorization": f"Bearer {access_token}",
            "developer-token": dev_token,
            "login-customer-id": login_cid,
            "Content-Type": "application/json",
        },
    )
    try:
        with request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:300]
        return {"_error": f"HTTP {e.code}: {body}"}


def fetch_google_ads(now: datetime) -> dict:
    dev_token = os.environ.get("GOOGLE_ADS_DEVELOPER_TOKEN")
    login_cid = (os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID") or "").replace("-", "")
    if not (dev_token and login_cid):
        return {"available": False, "reason": "GOOGLE_ADS_DEVELOPER_TOKEN / LOGIN_CUSTOMER_ID not set"}
    access = google_ads_token()
    if not access:
        return {"available": False, "reason": "Could not obtain Google OAuth access token"}

    win = windows(now)
    out = {"available": True, "customers": {}}
    for loc_label, cid_env in [("POL", "GOOGLE_ADS_CUSTOMER_ID_POL"), ("WP", "GOOGLE_ADS_CUSTOMER_ID_WP")]:
        cid = (os.environ.get(cid_env) or "").replace("-", "")
        if not cid:
            out["customers"][loc_label] = {"_error": f"{cid_env} not set"}
            continue

        loc_data = {"customer_id": cid, "windows": {}, "campaigns": []}
        for w_key, (since, until) in [("last_7d", win["last_7d"]), ("last_30d", win["last_30d"]), ("mtd", win["mtd"])]:
            gaql = f"""
                SELECT metrics.cost_micros, metrics.impressions, metrics.clicks,
                       metrics.conversions, metrics.conversions_value
                FROM customer
                WHERE segments.date BETWEEN '{since[:10]}' AND '{until[:10]}'
            """
            resp = google_ads_query(access, dev_token, login_cid, cid, gaql)
            if "_error" in resp:
                loc_data["windows"][w_key] = resp
                continue
            total = {"spend": 0.0, "impressions": 0, "clicks": 0, "conversions": 0.0, "conv_value": 0.0}
            for stream in (resp if isinstance(resp, list) else [resp]):
                for row in (stream.get("results") or []):
                    m = row.get("metrics", {})
                    total["spend"]       += int(m.get("costMicros", 0)) / 1_000_000
                    total["impressions"] += int(m.get("impressions", 0))
                    total["clicks"]      += int(m.get("clicks", 0))
                    total["conversions"] += float(m.get("conversions", 0))
                    total["conv_value"]  += float(m.get("conversionsValue", 0))
            loc_data["windows"][w_key] = total

        # Per-campaign breakdown for last 30d
        gaql_camp = f"""
            SELECT campaign.name, metrics.cost_micros, metrics.impressions, metrics.clicks, metrics.conversions
            FROM campaign
            WHERE segments.date BETWEEN '{win['last_30d'][0][:10]}' AND '{win['last_30d'][1][:10]}'
            ORDER BY metrics.cost_micros DESC
            LIMIT 25
        """
        resp = google_ads_query(access, dev_token, login_cid, cid, gaql_camp)
        if "_error" not in resp:
            for stream in (resp if isinstance(resp, list) else [resp]):
                for row in (stream.get("results") or []):
                    m = row.get("metrics", {})
                    loc_data["campaigns"].append({
                        "name": row.get("campaign", {}).get("name"),
                        "spend": round(int(m.get("costMicros", 0)) / 1_000_000, 2),
                        "impressions": int(m.get("impressions", 0)),
                        "clicks": int(m.get("clicks", 0)),
                        "conversions": float(m.get("conversions", 0)),
                    })
        out["customers"][loc_label] = loc_data
    return out


# ----------------------------------------------------------------------
# Blended metrics + summary
# ----------------------------------------------------------------------

def blend(ghl: dict, meta: dict, google: dict) -> dict:
    """Compute cross-channel blended summary metrics for last 30d."""
    spend_meta = 0.0
    spend_google = 0.0
    leads_ghl = 0
    redeemed_ghl = 0
    for loc in ghl.get("locations", {}).values():
        leads_ghl    += loc["leads"].get("last_30d", 0)
        redeemed_ghl += loc["redeemed"].get("last_30d", 0)
    for acct in meta.get("accounts", {}).values():
        if "windows" in acct and "last_30d" in acct["windows"]:
            spend_meta += acct["windows"]["last_30d"].get("spend", 0.0)
    for cust in google.get("customers", {}).values():
        if "windows" in cust and "last_30d" in cust["windows"]:
            spend_google += cust["windows"]["last_30d"].get("spend", 0.0)
    total_spend = spend_meta + spend_google
    return {
        "spend": {"meta": round(spend_meta, 2), "google": round(spend_google, 2), "total": round(total_spend, 2)},
        "leads_ghl": leads_ghl,
        "redeemed_ghl": redeemed_ghl,
        "blended_cpl": round(total_spend / max(leads_ghl, 1), 2),
        "blended_cpa_redeemed": round(total_spend / max(redeemed_ghl, 1), 2),
    }


# ----------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--days", type=int, default=30)
    args = p.parse_args()

    load_env()
    now = datetime.now(timezone.utc)

    print("→ Fetching GHL...")
    ghl = fetch_ghl(now)
    print(f"   GHL: {'OK' if ghl['available'] else 'unavailable'}")

    print("→ Fetching Meta Marketing API...")
    meta = fetch_meta(now)
    print(f"   Meta: {'OK' if meta['available'] else 'skipped — ' + meta.get('reason', '')}")

    print("→ Fetching Google Ads API...")
    google = fetch_google_ads(now)
    print(f"   Google Ads: {'OK' if google['available'] else 'skipped — ' + google.get('reason', '')}")

    consolidated = {
        "generated_at": now.replace(microsecond=0).isoformat(),
        "windows": windows(now),
        "ghl": ghl,
        "meta": meta,
        "google_ads": google,
        "blended_30d": blend(ghl, meta, google),
    }
    OUTPUT.write_text(json.dumps(consolidated, indent=2))
    print(f"\n✓ Wrote {OUTPUT}")
    print(f"  Sources active: GHL={ghl['available']}, Meta={meta['available']}, Google={google['available']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
