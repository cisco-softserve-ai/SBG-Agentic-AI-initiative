# Framework Design

## Purpose

Build a repeatable system for identifying routine Jira work, AI assistance
candidates, data-quality gaps, and progress over time.

The framework should help answer:

- Which teams have repeatable work suitable for AI assistance?
- Which clusters are strong pilot candidates?
- Which clusters require human-in-the-loop controls?
- Which Jira data gaps prevent confident ROI measurement?
- What changed between runs?
- Is a team's measurable AI opportunity improving over time?

## Source Of Truths

| Area | Source |
|---|---|
| Analysis rules | `Master prompt.md` |
| Team and project ownership | Confluence team information page |
| Jira issue data | `cisco-sbg.atlassian.net` |
| Historical results | Local `framework/runs/` folder |
| Diffs | Local `framework/comparisons/` folder |

## Team Catalog

The Confluence page should be parsed into a normalized team catalog.

Recommended fields:

| Field | Description |
|---|---|
| `team_name` | Human-readable team name |
| `team_slug` | Stable local identifier |
| `responsibilities` | Service/responsibility text from Confluence |
| `jira_projects` | Jira project keys on `cisco-sbg.atlassian.net` only |
| `ignored_jira_links` | Jira links outside the supported Jira cloud |
| `environments` | Environment coverage |
| `locations` | Team locations |
| `managers` | Managers/leaders from Confluence |
| `pm` | Product manager(s) |
| `security_champion` | Security champion(s), if listed |
| `pagerduty_links` | PagerDuty references |
| `scrum_or_kanban` | Team working model |
| `security_case_enabled` | Security case ticketing flag |
| `source_page_version` | Confluence version used |
| `source_last_modified` | Confluence last modified timestamp |

Confluence should be treated as the team/project ownership source unless a
project cannot be queried or an explicit override is configured.

## Run Hierarchy

Use a fiscal-quarter hierarchy with run IDs inside each quarter:

```text
framework/runs/FY2026/Q4/2026-06-19T120000Z/<team-slug>/
```

This supports both:

- Snapshot-to-snapshot comparisons inside a quarter.
- Quarter-to-quarter comparisons over time.

## Report Shape

The primary report artifact is a team rollup with project-isolated clusters.

This means:

- One report is generated per team per run.
- Team-level executive summary and recommendations appear first.
- Metrics include both team totals and per-project breakdowns.
- Clusters remain project-isolated; no cluster may mix issues from multiple
  Jira projects.
- If a team owns multiple supported Jira projects, each project keeps its own
  cluster set inside the team report.
- If a project is listed in Confluence but is outside `cisco-sbg.atlassian.net`,
  it is recorded as ignored/out-of-scope rather than included in analysis.

Recommended report artifact:

```text
framework/runs/FY2026/Q4/<run-id>/<team-slug>/team-report.md
```

Optional drill-down artifacts can be generated later:

```text
framework/runs/FY2026/Q4/<run-id>/<team-slug>/projects/<project-key>/report.md
```

## Comparison Strategy

Use a hierarchical comparison model:

| Comparison Type | Purpose |
|---|---|
| Same-quarter latest vs previous | Detect short-term movement and data changes |
| Current quarter vs previous quarter | Measure broader trend |
| Team vs team within same quarter | Identify relative opportunity areas without evaluating individuals |
| Cluster lineage over time | Track whether the same routine area is shrinking, growing, or changing risk |

All diffs must be evidence-based. If a metric is unavailable in one run, the
diff should report `Not comparable` rather than inventing a trend.

## Required Diff Fields

| Area | Diff Output |
|---|---|
| Scope | Team, project list, excluded projects, period, prompt version |
| Volume | Total issues delta, routine issues delta, routine ratio delta |
| Clusters | New, removed, renamed/matched, volume changes, routine score changes |
| AI opportunity | New/removed pilot candidates, priority changes |
| Risk | Risk classification changes and required control changes |
| Data quality | Worklog, status history, comments, dates, assignee coverage changes |
| Metrics | Lead time, cycle time, rework, worklog availability where comparable |
| Recommendations | Added, removed, changed recommendations |
| Confidence | Confidence changes and reasons |

## Open Design Decisions

1. Whether to parse Confluence team catalog automatically on every run or only
   refresh it on demand.
2. Whether to store raw issue descriptions/comments when richer Jira exports are
   enabled.
3. How to define cluster lineage when the master prompt evolves and cluster
   names change.
4. Whether optional project drill-down reports are needed in addition to the
   default team rollup.
