# <TEAM_OR_GOAL> Jira Routine Task Identification & AI ROI Analysis

Generated: <YYYY-MM-DD>

Prompt version: <PROMPT_VERSION>

Analysis scope: <PEOPLE_FIRST | PROJECT_FALLBACK>

Jira source: <https://cisco-sbg.atlassian.net>

## Input Parameters

| Field | Value |
|---|---|
| Team / Goal Direction | <TEAM_OR_GOAL_LABEL> |
| Confirmed Engineers | <NAME SURNAME; NAME SURNAME; ...> |
| Contribution Signals | <Assignee, Reporter, Comment Author, Worklog Author, Changelog Actor, ...> |
| Included Projects / Filters | <PROJECTS_OR_NONE> |
| Excluded Projects | <PROJECTS_OR_NONE> |
| Period | <FYYYYY QN or YYYY-MM-DD to YYYY-MM-DD> |
| Data Sources Attempted | <Jira CLI/API paths and exported fields> |
| Data Gaps | <Unavailable comments/worklogs/changelog/status history/etc.> |

## TABLE 1 — EXECUTIVE SUMMARY

| Field | Value |
|---|---|
| Projects | <PROJECT_LIST> |
| Excluded Projects | <PROJECT_LIST_OR_NONE> |
| Period | <PERIOD> |
| Total Issues | <TOTAL> total -> <PROJECT>: <COUNT>; ... |
| Routine Issues | <TOTAL> total -> <PROJECT>: <COUNT>; ... |
| Routine Ratio | <PERCENT> |
| Workload Distribution | <PROJECT>: <PERCENT>; ... |
| Data Mode | <Rich / Standard / Minimal + explanation> |
| Top Cluster #1 | <CLUSTER_NAME> |
| Top Cluster #2 | <CLUSTER_NAME> |
| Top Cluster #3 | <CLUSTER_NAME> |
| Confidence | <OVERALL_CONFIDENCE + reason> |

## TABLE 2 — DATA QUALITY PER PROJECT

| Data Element | Overall Status | <PROJECT_A> | <PROJECT_B> | Impact |
|---|---|---|---|---|
| Summary | <STATUS> | <STATUS> | <STATUS> | <IMPACT> |
| Issue Type | <STATUS> | <STATUS> | <STATUS> | <IMPACT> |
| Labels | Ignored | Ignored | Ignored | Labels are not used for clustering |
| Status History | <STATUS> | <STATUS> | <STATUS> | <IMPACT> |
| Dates | <STATUS> | <STATUS> | <STATUS> | <IMPACT> |
| Worklogs | <STATUS> | <STATUS> | <STATUS> | <IMPACT> |
| Comments | <STATUS> | <STATUS> | <STATUS> | <IMPACT> |
| Contribution Coverage | <STATUS> | <STATUS> | <STATUS> | <Which contribution signals were available> |

## TABLE 3 — PROJECT-ISOLATED CLUSTERS

| ID | Cluster Name | Project | SDLC Phase | Count | Routine Subset | Routine Score | Risk | Risk Details | Classification | Classification Details | Confidence |
|---|---|---|---|---:|---:|---:|---|---|---|---|---|
| C1 | <CLUSTER_NAME> | <PROJECT> | <PHASE> | <N> | <N> | <0-18> | <Low/Medium/High> | <DETAILS> | <CLASSIFICATION> | <EVIDENCE_OR_JQL> | <CONFIDENCE> |

## TABLE 4 — CLUSTER EVIDENCE

| ID | Pattern Description | Evidence | Missing Data | AI Opportunity | Validation Required |
|---|---|---|---|---|---|
| C1 | <PATTERN> | <SUMMARY/EVIDENCE> | <MISSING_FIELDS> | <AI_ASSISTANCE_MODE> | <VALIDATION_OWNER> |

## TABLE 5A — AGGREGATED METRICS

| Metric | Value | Availability | Notes |
|---|---:|---|---|
| Total issues | <N> | <Available/Partial/Missing> | <NOTES> |
| Routine issues | <N> | <Available/Inferred> | <NOTES> |
| Routine ratio | <PERCENT> | <Available/Inferred> | <NOTES> |
| Median Cycle Time (Routine Issues) | <VALUE_OR_NOT_AVAILABLE> | <STATUS> | <NOTES> |
| Median Lead Time (Routine Issues) | <VALUE_OR_NOT_AVAILABLE> | <STATUS> | <NOTES> |
| Worklog Hours (Routine Issues) | <VALUE_OR_NOT_AVAILABLE> | <STATUS> | <NOTES> |
| Rework Rate | <VALUE_OR_NOT_AVAILABLE> | <STATUS> | <NOTES> |

## TABLE 5B — METRICS BY PROJECT

| Project | Data Mode | Total Issues | Routine Issues | Routine % | Median Cycle Time | Median Lead Time | Worklog Coverage | Status History Coverage | Rework Rate | Measurement Confidence |
|---|---|---:|---:|---:|---|---|---|---|---|---|
| <PROJECT> | <MODE> | <N> | <N> | <PERCENT> | <VALUE> | <VALUE> | <COVERAGE> | <COVERAGE> | <VALUE> | <CONFIDENCE> |

## TABLE 6 — AI SAVINGS SCENARIOS

| ID | Cluster | Project | Volume | Baseline Per Unit | Conservative Saving | Moderate Saving | Optimistic Saving | Savings Type | Assumption Used | Impact Type | Confidence |
|---|---|---|---:|---|---|---|---|---|---|---|---|
| C1 | <CLUSTER> | <PROJECT> | <N> | <BASELINE_OR_NOT_AVAILABLE> | <VALUE> | <VALUE> | <VALUE> | <TYPE> | <ASSUMPTION> | <Confirmed/Proxy-based/Directional/Not estimable> | <CONFIDENCE> |

## TABLE 7 — AI USE CASES + KPI

| ID | Use Case | Cluster | Project | AI Type | Expected Benefit | KPI | KPI Formula | Baseline Period | Post-AI Period | Comparability Check | Measurement Method | Measurement Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| U1 | <USE_CASE> | <CLUSTER> | <PROJECT> | <AI_TYPE> | <BENEFIT> | <KPI> | <FORMULA> | <PERIOD> | <PERIOD> | <Comparable/Partially comparable/Not comparable> | <METHOD> | <CONFIDENCE> |

## TABLE 8 — NOT AUTOMATED TASKS

| Cluster | Project | Reason | AI Allowed | Control |
|---|---|---|---|---|
| <CLUSTER> | <PROJECT> | <REASON> | <No / Yes, AI-assisted only / Yes, with mandatory HITL> | <CONTROL> |

## TABLE 9 — IMPROVEMENTS

| Improvement | Purpose | Priority |
|---|---|---|
| <IMPROVEMENT> | <PURPOSE> | <High/Medium/Low> |

## TABLE 10 — FINAL RECOMMENDATIONS

| Area | Recommendation | Priority |
|---|---|---|
| Top AI Pilot Cluster | <RECOMMENDATION> | <High/Medium/Low> |
| Baseline Metric | <RECOMMENDATION> | <High/Medium/Low> |
| AI Tracking Setup | <RECOMMENDATION> | <High/Medium/Low> |
| Validation Owner Role | <RECOMMENDATION> | <High/Medium/Low> |
| Risks to Monitor | <RECOMMENDATION> | <High/Medium/Low> |
| Next Evaluation | <RECOMMENDATION> | <High/Medium/Low> |

## Report Rules

- Keep the report table-first and evidence-based.
- Preserve project isolation in every cluster.
- Do not rank, score, or compare individual engineers.
- Do not use labels as the primary routine classification signal.
- Do not calculate hours saved without worklogs or another reliable effort baseline.
- Mark unavailable cycle time, rework, worklogs, comments, or contribution signals as data-quality gaps.
- High-risk routine work may be AI-assisted only with mandatory human validation.
- End the rendered report with: `End of report`

End of report
