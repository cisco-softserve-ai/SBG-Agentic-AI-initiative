#!/usr/bin/env python3
"""Minimal Jira Cloud REST client for framework users without jira-cli."""

from __future__ import annotations

import argparse
import base64
import json
import os
import platform
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


DEFAULT_BASE_URL = "https://cisco-sbg.atlassian.net"
DEFAULT_KEYCHAIN_SERVICE = "jira-api-token"


def keychain_token(account: str, service: str) -> str | None:
    if platform.system() != "Darwin":
        return None
    try:
        completed = subprocess.run(
            ["security", "find-generic-password", "-s", service, "-a", account, "-w"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=10,
            check=False,
        )
    except Exception:
        return None
    if completed.returncode == 0:
        return completed.stdout.strip()
    return None


def credentials() -> tuple[str, str, str]:
    base_url = os.environ.get("JIRA_BASE_URL", DEFAULT_BASE_URL).rstrip("/")
    account = os.environ.get("ATLASSIAN_ACCOUNT") or os.environ.get("JIRA_EMAIL")
    token = os.environ.get("JIRA_TOKEN")

    if account and not token:
        service = os.environ.get("JIRA_KEYCHAIN_SERVICE", DEFAULT_KEYCHAIN_SERVICE)
        token = keychain_token(account, service)

    if not account or not token:
        raise SystemExit(
            "Missing Jira credentials. Set ATLASSIAN_ACCOUNT and JIRA_TOKEN, "
            "or on macOS store a token in Keychain service "
            f"'{DEFAULT_KEYCHAIN_SERVICE}' for ATLASSIAN_ACCOUNT."
        )

    return base_url, account, token


def request_json(method: str, path: str, payload: dict[str, Any] | None = None) -> Any:
    base_url, account, token = credentials()
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    auth = base64.b64encode(f"{account}:{token}".encode("utf-8")).decode("ascii")
    req = urllib.request.Request(
        f"{base_url}{path}",
        data=body,
        method=method,
        headers={
            "Authorization": f"Basic {auth}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Jira REST error {exc.code}: {detail}") from exc


def whoami(_: argparse.Namespace) -> int:
    data = request_json("GET", "/rest/api/3/myself")
    safe = {
        "accountId": data.get("accountId"),
        "displayName": data.get("displayName"),
        "emailAddress": data.get("emailAddress"),
        "active": data.get("active"),
        "timeZone": data.get("timeZone"),
    }
    print(json.dumps(safe, indent=2, sort_keys=True))
    return 0


def search(args: argparse.Namespace) -> int:
    fields = [field.strip() for field in args.fields.split(",") if field.strip()]
    max_results = min(args.limit, 100)
    next_page_token = None
    issues: list[dict[str, Any]] = []

    while len(issues) < args.limit:
        payload = {
            "jql": args.jql,
            "fields": fields,
            "maxResults": min(max_results, args.limit - len(issues)),
        }
        if next_page_token:
            payload["nextPageToken"] = next_page_token
        data = request_json("POST", "/rest/api/3/search/jql", payload)
        batch = data.get("issues", [])
        if not batch:
            break
        issues.extend(batch)
        next_page_token = data.get("nextPageToken")
        if data.get("isLast", True) or not next_page_token:
            break

    if args.output:
        Path(args.output).write_text(json.dumps(issues, indent=2), encoding="utf-8")
    else:
        print(json.dumps(issues, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    who = sub.add_parser("whoami")
    who.set_defaults(func=whoami)

    find = sub.add_parser("search")
    find.add_argument("--jql", required=True)
    find.add_argument("--fields", default="key,summary,status,issuetype,assignee,created,updated,resolutiondate")
    find.add_argument("--limit", type=int, default=100)
    find.add_argument("--output")
    find.set_defaults(func=search)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
