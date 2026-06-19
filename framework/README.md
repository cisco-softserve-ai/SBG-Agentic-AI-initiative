# Jira Routine AI Opportunity Framework

This framework turns the master Jira routine-analysis prompt into repeatable,
team-based runs with local historical tracking.

## Scope

- Primary unit: team.
- Jira scope: `cisco-sbg.atlassian.net` only.
- Team metadata source: Confluence page `Umbrella/SSE Eng Team Information`.
- Analysis policy source: `Master prompt.md`.
- Default period: current Cisco fiscal quarter.
- Output mode: local Markdown and JSON files.
- Publishing: none unless explicitly requested.

## Cisco Fiscal Quarter Calendar

Cisco fiscal year starts in August.

| Fiscal Quarter | Months |
|---|---|
| Q1 | August, September, October |
| Q2 | November, December, January |
| Q3 | February, March, April |
| Q4 | May, June, July |

On 2026-06-19, the default period is Cisco FY2026 Q4:
2026-05-01 through 2026-07-31.

## Planned Workflow

1. Extract or refresh the team catalog from Confluence.
2. Select one or more teams.
3. Resolve each team to one or more Jira project keys.
4. Run the master prompt analysis for each team/project set.
5. Store a team rollup report with project-isolated clusters, plus machine-readable metrics.
6. Compare current run with previous runs in the same quarter or prior quarters.

## Directory Layout

```text
framework/
  configs/       Run defaults and named run configs
  data/          Team catalog and non-sensitive normalized metadata
  prompts/       Versioned prompt snapshots
  runs/          Local generated run outputs, git ignored
  comparisons/   Local generated diff outputs, git ignored
  scripts/       Future automation scripts
  docs/          Framework design notes
```

## Artifact Model

Each run should produce:

```text
framework/runs/FY2026/Q4/<run-id>/<team-slug>/
  run_config.yaml
  team_context.json
  issues.json
  metrics.json
  clusters.json
  report.md
```

Each comparison should produce:

```text
framework/comparisons/FY2026/Q4/<comparison-id>/
  comparison_config.yaml
  diff.json
  summary.md
```
