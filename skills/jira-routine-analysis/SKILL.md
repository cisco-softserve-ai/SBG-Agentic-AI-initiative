---
name: jira-routine-analysis
description: Run this repository's Jira routine-work and AI opportunity framework for team- or project-based analysis. Use when the user asks to analyze Jira project(s), team Jira work, routine task candidates, AI offload opportunities, Jira ROI, historical run comparison, or progress over time. Supports Jira project keys and optional timeframe input; default timeframe is the current Cisco fiscal quarter. On first use, verify repository setup, Jira CLI availability/authentication, and output folders before collecting data.
---

# Jira Routine Analysis

## First Run

Before analysis, run the setup verifier from the repository root:

```bash
python3 skills/jira-routine-analysis/scripts/doctor.py
```

If it reports a missing Jira CLI or failed auth, help the user fix that before continuing. Do not collect Jira data until read-only Jira access is verified.

## Inputs

Accept:

- Jira project key or keys, for example `REDIS` or `REDIS,CNHE`
- Team name, when the user wants team-based analysis
- Optional timeframe:
  - explicit `YYYY-MM-DD` to `YYYY-MM-DD`
  - Cisco fiscal quarter such as `FY2026 Q4`
  - default: current Cisco fiscal quarter
- Optional excluded project keys

Use Cisco fiscal quarters:

- Q1: August, September, October
- Q2: November, December, January
- Q3: February, March, April
- Q4: May, June, July

Use `scripts/cisco_fiscal_period.py` to calculate the default period or normalize fiscal-quarter requests.

## Repository Contract

The framework repository should contain:

- `Master prompt.md`
- `framework/configs/default.yaml`
- `framework/docs/framework-design.md`
- `framework/runs/`
- `skills/jira-routine-analysis/`

If the current directory is not the repository root, search upward for `Master prompt.md` and `framework/configs/default.yaml`. If not found, ask for the repo path.

## Jira Scope

Use only `https://cisco-sbg.atlassian.net`.

Resolve Jira CLI in this order:

1. `JIRA_CLI` environment variable
2. `jira-cli` on `PATH`
3. `~/.agents/skills/jira-issues/scripts/jira-cli`
4. `~/.codex/skills/jira-issues/scripts/jira-cli`

Use read-only Jira commands unless the user explicitly asks for writes.

## Team Resolution

When the user provides a team name, resolve Jira projects from the Confluence page:

`https://cisco-sbg.atlassian.net/wiki/spaces/PROD/pages/1294373378/Umbrella+SSE+Eng+Team+Information`

Include only project links on `cisco-sbg.atlassian.net`. Record other Jira instances as out of scope.

When the user provides project keys directly, run project-based analysis and label the team as provided by the user or `Unspecified`.

## Analysis Rules

Read `Master prompt.md` before producing the report. Treat it as the source of truth for:

- clustering rules
- routine scoring
- risk classification
- savings guardrails
- output tables
- validation rules

Generate one team rollup first, with project-isolated clusters inside it. Do not mix issues from multiple projects in one cluster.

## Data Collection

Build JQL with the selected period:

```jql
project in (<PROJECTS>)
AND (created >= "<START>" OR updated >= "<START>" OR resolutiondate >= "<START>")
AND (created <= "<END>" OR updated <= "<END>" OR resolutiondate <= "<END>")
ORDER BY updated DESC
```

Export enough fields for reproducible analysis:

```text
key, project, issuetype, summary, status, priority, assignee,
created, updated, resolutiondate, epicLink, labels
```

If richer metrics are needed and available, also collect changelog, comments, and worklogs. If unavailable, report the data gap; do not invent cycle time, rework, or hours saved.

## Storage

Store generated artifacts under:

```text
framework/runs/FY<YEAR>/Q<QUARTER>/<run-id>/<team-slug>/
```

Recommended files:

- `run_config.yaml`
- `team_context.json`
- `issues.json`
- `metrics.json`
- `clusters.json`
- `team-report.md`

Raw snapshots are local artifacts and must remain git-ignored.

## Comparison

When asked to compare runs, compare evidence only:

- total issues
- routine issues
- routine ratio
- cluster count and volume
- new/removed clusters
- AI candidate changes
- risk/control changes
- data-quality changes
- lead-time/cycle-time/worklog availability changes
- recommendation changes

If a metric is missing or scopes differ, mark it `Not comparable` and explain why.

