#!/usr/bin/env python3
"""First-run verifier for the Jira routine analysis skill."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path


ROOT_MARKERS = ("Master prompt.md", "framework/configs/default.yaml")
JIRA_URL = "https://cisco-sbg.atlassian.net"


def find_repo_root(start: Path) -> Path | None:
    current = start.resolve()
    for candidate in (current, *current.parents):
        if all((candidate / marker).exists() for marker in ROOT_MARKERS):
            return candidate
    return None


def find_jira_cli() -> str | None:
    env_path = os.environ.get("JIRA_CLI")
    if env_path and Path(env_path).exists():
        return env_path

    path_cli = shutil.which("jira-cli")
    if path_cli:
        return path_cli

    home = Path.home()
    candidates = [
        home / ".agents/skills/jira-issues/scripts/jira-cli",
        home / ".codex/skills/jira-issues/scripts/jira-cli",
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return None


def run(command: list[str], cwd: Path) -> tuple[int, str]:
    try:
        completed = subprocess.run(
            command,
            cwd=str(cwd),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=30,
            check=False,
        )
        return completed.returncode, completed.stdout.strip()
    except Exception as exc:  # pragma: no cover - defensive CLI diagnostics
        return 1, str(exc)


def check_gitignore(root: Path) -> bool:
    gitignore = root / ".gitignore"
    if not gitignore.exists():
        return False
    text = gitignore.read_text(encoding="utf-8")
    return "framework/runs/" in text and "framework/comparisons/" in text


def fiscal_period(root: Path) -> dict[str, object]:
    script = root / "skills/jira-routine-analysis/scripts/cisco_fiscal_period.py"
    code, output = run([sys.executable, str(script), "--date", date.today().isoformat()], root)
    if code != 0:
        raise RuntimeError(output)
    return json.loads(output)


def main() -> int:
    root = find_repo_root(Path.cwd())
    checks: list[tuple[str, bool, str]] = []

    if root is None:
        print("FAIL: repository root not found. Run from the SBG Agentic AI repo.")
        return 1

    checks.append(("repo_root", True, str(root)))
    checks.append(("master_prompt", (root / "Master prompt.md").exists(), "Master prompt.md"))
    checks.append(("framework_config", (root / "framework/configs/default.yaml").exists(), "framework/configs/default.yaml"))
    checks.append(("gitignore_generated_artifacts", check_gitignore(root), ".gitignore covers runs/comparisons"))

    for path in (
        root / "framework/runs",
        root / "framework/comparisons",
        root / "framework/data",
    ):
        path.mkdir(parents=True, exist_ok=True)
        checks.append((f"directory:{path.relative_to(root)}", path.exists(), str(path.relative_to(root))))

    try:
        period = fiscal_period(root)
        checks.append(("cisco_fiscal_period", True, f"{period['label']} {period['start']}..{period['end']}"))
    except Exception as exc:
        checks.append(("cisco_fiscal_period", False, str(exc)))

    jira_cli = find_jira_cli()
    checks.append(("jira_cli_found", jira_cli is not None, jira_cli or "Set JIRA_CLI or install jira-cli"))

    if jira_cli:
        code, output = run([jira_cli, "whoami"], root)
        auth_ok = code == 0 and "Authenticated as" in output
        checks.append(("jira_auth", auth_ok, "whoami ok" if auth_ok else output[:500]))

    print("Jira Routine Analysis setup check")
    print(f"Jira scope: {JIRA_URL}")
    failed = False
    for name, ok, detail in checks:
        status = "OK" if ok else "FAIL"
        print(f"{status}: {name} - {detail}")
        failed = failed or not ok

    if failed:
        print("\nNext steps:")
        print("- Install or configure jira-cli if missing.")
        print("- Run jira-cli config for cisco-sbg.atlassian.net if auth fails.")
        print("- Re-run this doctor before analysis.")
        return 1

    print("\nReady for Jira routine analysis.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

