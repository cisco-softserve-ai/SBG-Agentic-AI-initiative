---
name: jira-routine-analysis
description: Run this repository's SBG Agentic AI Jira routine-work framework for people-first team or goal-direction analysis. Use when the user asks to analyze Jira work by engineer list, contributors, team work, Jira project fallback, routine task candidates, AI offload opportunities, Jira ROI, historical run comparison, or progress over time. Default input is a list of engineer first/last names; the skill must clarify and confirm scope before querying Jira. Supports optional timeframe, project filters, excluded project keys, and current Cisco fiscal quarter defaults.
---

# Jira Routine Analysis

## First Run

Before analysis, run the setup verifier from the repository root:

```bash
python3 skills/jira-routine-analysis/scripts/doctor.py
```

If it reports failed Jira auth, help the user configure either `jira-cli` or the bundled REST client before continuing. Do not collect Jira data until read-only Jira access is verified and the user has confirmed the planned analysis inputs.

## Repository Contract

The framework repository should contain:

- `Master prompt.md`
- `framework/configs/default.yaml`
- `framework/docs/framework-design.md`
- `framework/runs/`
- `skills/jira-routine-analysis/`

If the current directory is not the repository root, search upward for `Master prompt.md` and `framework/configs/default.yaml`. If not found, ask for the repo path.

## Interaction Gate

Before querying Jira, creating datasets, or writing reports, show the planned input parameters and ask the user to confirm or correct them.

Always include:

- Engineer list, with resolved Jira identities where known
- Contribution scope
- Jira source
- Timeframe
- Included and excluded projects or filters
- Team / goal-direction label
- Output location and artifacts
- Data fields planned, including whether comments, changelogs, and worklogs will be attempted

If important input is missing, ask concise questions before any Jira pull. Important missing inputs include:

- No engineer list and no explicit request to derive engineers from a project/team
- Ambiguous engineer identity
- Unclear timeframe when the default current Cisco fiscal quarter may materially change the result
- Unclear source project/team when asked to derive people
- Requested comparison without a baseline run or period

Do not stop for minor defaults. State the default and ask for confirmation in the same pre-run checkpoint.

## Default Inputs

Default to people-first analysis.

Accept:

- Engineer names as `Name Surname`
- Multiple engineer names in text, bullets, CSV, or pasted roster form
- Optional goal-direction or team label
- Optional timeframe:
  - explicit `YYYY-MM-DD` to `YYYY-MM-DD`
  - Cisco fiscal quarter such as `FY2026 Q4`
  - default: current Cisco fiscal quarter
- Optional included project keys as filters
- Optional excluded project keys
- Optional project/team source to derive the engineer list

If an engineer cannot be identified unambiguously in Jira, ask the user to clarify before running analysis for that person. Do not guess between people with similar names.

Use Cisco fiscal quarters:

- Q1: August, September, October
- Q2: November, December, January
- Q3: February, March, April
- Q4: May, June, July

Use `scripts/cisco_fiscal_period.py` to calculate the default period or normalize fiscal-quarter requests.

## Jira Scope

Use only `https://cisco-sbg.atlassian.net`.

Resolve Jira access in this order:

1. `JIRA_CLI` environment variable
2. `jira-cli` on `PATH`
3. `~/.agents/skills/jira-issues/scripts/jira-cli`
4. `~/.codex/skills/jira-issues/scripts/jira-cli`
5. bundled REST client: `skills/jira-routine-analysis/scripts/jira_rest.py`

For the bundled REST client, use:

```bash
export ATLASSIAN_ACCOUNT="you@example.com"
export JIRA_TOKEN="<atlassian-api-token>"
```

On macOS, the REST client can also read `JIRA_TOKEN` from Keychain service `jira-api-token` for `ATLASSIAN_ACCOUNT`.

Use read-only Jira commands unless the user explicitly asks for writes.

## People Resolution

When the user provides engineer names:

1. Resolve each `Name Surname` to a Jira user identity where possible.
2. Present the resolved list back to the user before analysis.
3. Ask for clarification for ambiguous, missing, inactive, or duplicate matches.
4. Exclude unresolved people unless the user corrects or confirms a safe interpretation.

When the user provides a Jira project or team instead of engineers:

1. Treat it as a request to derive a proposed engineer list.
2. Pull candidate contributors from that source for the selected period using Jira contribution signals.
3. Show the proposed people list to the user.
4. Wait for the user to confirm, add, or remove people before running the routine analysis.

Project-only analysis remains a fallback only when the user explicitly confirms they want project scope rather than people scope.

## Contribution Definition

Default contributor scope includes any meaningful Jira contribution by the confirmed engineers in the selected period, not only assignment.

Include issues when a confirmed engineer appears as any of:

- Assignee
- Worklog author
- Comment author
- Reporter
- Status transition author or changelog actor
- Other available Jira activity author that indicates contribution

When some contribution signals are unavailable from the CLI/API path, collect the available signals and document missing ones as data-quality gaps. Do not silently reduce the definition to assignee-only.

If included project filters are supplied, apply them after resolving contributor activity. If excluded projects are supplied, remove them before metrics, clustering, links, and recommendations.

## Team Resolution

When the user provides a team name and asks to derive people, resolve Jira projects and ownership context from the Confluence page:

`https://cisco-sbg.atlassian.net/wiki/spaces/PROD/pages/1294373378/Umbrella+SSE+Eng+Team+Information`

Include only project links on `cisco-sbg.atlassian.net`. Record other Jira instances as out of scope. Use the team/project context only to propose the engineer list or optional project filters; still require user confirmation of the people list before the analysis run.

## Analysis Rules

Read `Master prompt.md` before producing the report. Treat it as the source of truth for:

- clustering rules
- routine scoring
- risk classification
- savings guardrails
- output tables
- validation rules

Generate one team or goal-direction rollup first, with project-isolated clusters inside it. Do not mix issues from multiple projects in one cluster.

Do not evaluate, rank, or compare individual engineers. People are used only to define the workload scope.

## Data Collection

For confirmed engineers, build Jira queries around contribution signals for the selected period.

Assignee baseline JQL:

```jql
assignee in (<ENGINEERS>)
AND (created >= "<START>" OR updated >= "<START>" OR resolutiondate >= "<START>")
AND (created <= "<END>" OR updated <= "<END>" OR resolutiondate <= "<END>")
ORDER BY updated DESC
```

Also attempt available Jira API/CLI paths for worklog author, comment author, reporter, and changelog actor contribution. If a signal cannot be queried directly, document the limitation and avoid claiming full contribution coverage.

When deriving engineers from a project before confirmation, use a discovery JQL such as:

```jql
project in (<PROJECTS>)
AND (created >= "<START>" OR updated >= "<START>" OR resolutiondate >= "<START>")
AND (created <= "<END>" OR updated <= "<END>" OR resolutiondate <= "<END>")
ORDER BY updated DESC
```

Then extract candidate people from available assignee, reporter, comment, worklog, and changelog fields. Present that list to the user for verification before the analysis run.

Export enough fields for reproducible analysis:

```text
key, project, issuetype, summary, status, priority, assignee, reporter,
created, updated, resolutiondate, epicLink, labels
```

If richer metrics are needed and available, also collect changelog, comments, and worklogs. If unavailable, report the data gap; do not invent cycle time, rework, contribution coverage, or hours saved.

When `jira-cli` is unavailable, collect with:

```bash
python3 skills/jira-routine-analysis/scripts/jira_rest.py search \
  --jql '<JQL>' \
  --fields 'key,project,issuetype,summary,status,priority,assignee,created,updated,resolutiondate,labels' \
  --limit 1000 \
  --output <issues.json>
```

## Storage

Store generated artifacts under:

```text
framework/runs/FY<YEAR>/Q<QUARTER>/<run-id>/<team-or-goal-slug>/
```

Recommended files:

- `run_config.yaml`
- `team_context.json`
- `people.json`
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
