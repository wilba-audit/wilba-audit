"""Monkey Joe's — Meta/Facebook Ads management (write access).

Gives the mj-growth-operator live control of both MJ ad accounts via the Meta
Marketing API — list, pause, enable, and adjust budgets. Reporting lives in
`fetch_consolidated_reporting.py`; this file is the *write* layer.

Requires in .env:
  META_ACCESS_TOKEN         (ads_read + ads_management)
  META_AD_ACCOUNT_POL       (numeric ad account id, no act_ prefix)
  META_AD_ACCOUNT_WP

Usage:
  # Verify the token can see both accounts
  python3 scripts/mj_meta_manage.py verify

  # List campaigns with status + daily budget + last-7d spend
  python3 scripts/mj_meta_manage.py list --loc POL
  python3 scripts/mj_meta_manage.py list --loc WP

  # Pause / enable a campaign (dry-run unless --execute)
  python3 scripts/mj_meta_manage.py pause  --loc POL --campaign 1234567890 --execute
  python3 scripts/mj_meta_manage.py enable --loc POL --campaign 1234567890 --execute

  # Set an ad set's daily budget (USD). Guardrail: refuses > --max (default 60)
  python3 scripts/mj_meta_manage.py budget --loc WP --adset 987654321 --daily 25 --execute

All mutations are no-ops without --execute, and print exactly what they would do.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from urllib import request, parse, error

from dotenv import load_dotenv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(ROOT, ".env"))

API_VER = "v21.0"
TOKEN = os.getenv("META_ACCESS_TOKEN")
ACCOUNTS = {
    "POL": os.getenv("META_AD_ACCOUNT_POL"),
    "WP": os.getenv("META_AD_ACCOUNT_WP"),
}
# Safety: never push a daily budget above this (USD) without an explicit override.
DEFAULT_MAX_DAILY = 60.0


def _need_token() -> None:
    if not TOKEN:
        sys.exit("ERROR: META_ACCESS_TOKEN not set in .env — paste it in and retry.")


def _acct(loc: str) -> str:
    acct = ACCOUNTS.get(loc)
    if not acct:
        sys.exit(f"ERROR: META_AD_ACCOUNT_{loc} not set in .env.")
    return acct if acct.startswith("act_") else f"act_{acct}"


def api(method: str, path: str, params: dict | None = None) -> dict:
    params = {**(params or {}), "access_token": TOKEN}
    url = f"https://graph.facebook.com/{API_VER}{path}"
    data = None
    if method == "GET":
        url += "?" + parse.urlencode(params)
    else:
        data = parse.urlencode(params).encode()
    req = request.Request(url, data=data, method=method,
                          headers={"User-Agent": "mj-meta-manage/1.0"})
    try:
        with request.urlopen(req, timeout=40) as r:
            return json.loads(r.read().decode())
    except error.HTTPError as e:
        return {"_error": e.code, "body": e.read().decode()[:500]}


def cmd_verify(_args) -> int:
    _need_token()
    ok = True
    for loc, acct in ACCOUNTS.items():
        if not acct:
            print(f"  {loc}: ✗ META_AD_ACCOUNT_{loc} not set"); ok = False; continue
        res = api("GET", f"/{_acct(loc)}", {"fields": "name,account_status,currency,amount_spent"})
        if "_error" in res:
            print(f"  {loc}: ✗ {res['_error']} {res['body']}"); ok = False
        else:
            print(f"  {loc}: ✓ {res.get('name')} · status {res.get('account_status')} · {res.get('currency')}")
    print("\nVerified — Meta write access is live." if ok else "\nSome accounts failed — check token scopes (ads_management) + account IDs.")
    return 0 if ok else 1


def cmd_list(args) -> int:
    _need_token()
    res = api("GET", f"/{_acct(args.loc)}/campaigns",
              {"fields": "name,status,effective_status,daily_budget,objective,"
                         "insights.date_preset(last_7d){spend,clicks,cpc,actions}",
               "limit": 100})
    if "_error" in res:
        print(f"✗ {res['_error']} {res['body']}"); return 1
    print(f"\n{args.loc} campaigns:")
    for c in res.get("data", []):
        db = c.get("daily_budget")
        db = f"${int(db)/100:.0f}/day" if db else "adset-budget"
        spend = ""
        ins = (c.get("insights", {}) or {}).get("data")
        if ins:
            spend = f" · 7d spend ${float(ins[0].get('spend',0)):.2f}"
        print(f"  [{c['id']}] {c.get('effective_status'):16} {db:14} {c.get('name')}{spend}")
    return 0


def _set_status(loc: str, campaign_id: str, status: str, execute: bool) -> int:
    _need_token()
    verb = "PAUSE" if status == "PAUSED" else "ENABLE"
    print(f"{verb} campaign {campaign_id} ({loc})")
    if not execute:
        print("  (dry-run) add --execute to apply."); return 0
    res = api("POST", f"/{campaign_id}", {"status": status})
    if "_error" in res:
        print(f"  ✗ {res['_error']} {res['body']}"); return 1
    print(f"  ✓ {verb.lower()}d."); return 0


def cmd_pause(args) -> int:
    return _set_status(args.loc, args.campaign, "PAUSED", args.execute)


def cmd_enable(args) -> int:
    return _set_status(args.loc, args.campaign, "ACTIVE", args.execute)


def cmd_budget(args) -> int:
    _need_token()
    if args.daily > args.max:
        sys.exit(f"REFUSED: ${args.daily}/day exceeds guardrail ${args.max}/day. "
                 f"Raise --max explicitly and confirm with Jess (spend cap).")
    cents = int(round(args.daily * 100))
    print(f"SET daily budget of adset {args.adset} ({args.loc}) → ${args.daily:.2f}/day")
    if not args.execute:
        print("  (dry-run) add --execute to apply."); return 0
    res = api("POST", f"/{args.adset}", {"daily_budget": cents})
    if "_error" in res:
        print(f"  ✗ {res['_error']} {res['body']}"); return 1
    print("  ✓ budget updated."); return 0


def main() -> int:
    p = argparse.ArgumentParser(description="MJ Meta Ads management")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("verify").set_defaults(func=cmd_verify)

    lp = sub.add_parser("list"); lp.add_argument("--loc", required=True, choices=["POL", "WP"])
    lp.set_defaults(func=cmd_list)

    for name, fn in (("pause", cmd_pause), ("enable", cmd_enable)):
        sp = sub.add_parser(name)
        sp.add_argument("--loc", required=True, choices=["POL", "WP"])
        sp.add_argument("--campaign", required=True)
        sp.add_argument("--execute", action="store_true")
        sp.set_defaults(func=fn)

    bp = sub.add_parser("budget")
    bp.add_argument("--loc", required=True, choices=["POL", "WP"])
    bp.add_argument("--adset", required=True)
    bp.add_argument("--daily", type=float, required=True)
    bp.add_argument("--max", type=float, default=DEFAULT_MAX_DAILY)
    bp.add_argument("--execute", action="store_true")
    bp.set_defaults(func=cmd_budget)

    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
