# REDIS Jira Routine Task Identification & AI ROI Analysis

Generated: 2026-06-19

Prompt version: v6.1.1

## TABLE 1 — EXECUTIVE SUMMARY

| Field | Value |
|---|---|
| Projects | REDIS / ResourceDiscovery |
| Excluded Projects | None |
| Period | Assumed last 26 weeks through 2026-06-19 |
| Total Issues | 587 total → REDIS: 587 |
| Routine Issues | 306 total → REDIS: 306 |
| Routine Ratio | 52.1% |
| Workload Distribution | REDIS: 100% |
| Data Mode | Standard: summary/type/status/dates/epic available; worklogs and transition history not available |
| Top Cluster #1 | IaC/deployment/environment enablement |
| Top Cluster #2 | E2E/test validation and test tooling |
| Top Cluster #3 | Splunk/monitoring/detector operations |
| Confidence | Medium: strong summary/epic patterns; limited by missing worklogs and status history |

## TABLE 2 — DATA QUALITY PER PROJECT

| Data Element | Overall Status | REDIS | Impact |
|---|---|---|---|
| Summary | Available | Available | Supports keyword/text clustering |
| Issue Type | Available | Available | Supports structural grouping |
| Labels | Ignored | Ignored | Labels were exported but not used for classification |
| Status History | Not available | Not available | Cycle time/rework cannot be reliably calculated |
| Dates | Partial | Created/updated/resolved available | Lead time available for 265 resolved issues |
| Worklogs | Not available | Not available | Hours saved not calculated |
| Comments | Partial | Not in CLI export | Lowers confidence for some clusters |
| Assignee Expansion | Partial | Single-project REDIS analysis | Cross-project expansion not completed because stable assignee account IDs were not available in CLI export |

## TABLE 3 — PROJECT-ISOLATED CLUSTERS

| ID | Cluster Name | Project | SDLC Phase | Count | Routine Subset | Routine Score | Risk | Classification | Confidence |
|---|---|---|---|---:|---:|---:|---|---|---|
| C1 | Security/GHAS/Dependabot remediation | REDIS | Security / compliance | 51 | 36 | 13 | High | Routine with mandatory HITL | Medium |
| C2 | E2E/test validation and test tooling | REDIS | Test / validation | 88 | 70 | 15 | Medium | Strong Routine Candidate | Medium |
| C3 | IaC/deployment/environment enablement | REDIS | Deploy / operations | 168 | 95 | 13 | High | Routine with mandatory HITL | Medium |
| C4 | Splunk/monitoring/detector operations | REDIS | Operate / monitor | 64 | 48 | 14 | Medium | Strong Routine Candidate | Medium |
| C5 | Data ingestion/recommendation pipeline | REDIS | Build / data pipeline | 79 | 45 | 12 | Medium | Possible Routine Candidate | Medium |
| C6 | Operational cleanup/tech debt/tooling | REDIS | Maintain | 9 | 7 | 11 | Medium | Possible Routine Candidate | Low |
| C7 | API/UI/product feature implementation | REDIS | Build | 14 | 5 | 8 | Medium | Weak Routine Signal | Low |
| C8 | Non-routine or insufficient evidence | REDIS | Mixed | 114 | 0 | 5 | Medium | High-value / complex or not routine | Low |

## TABLE 4 — CLUSTER EVIDENCE

| ID | Pattern Description | Evidence | Missing Data | AI Opportunity | Validation Required |
|---|---|---|---|---|---|
| C1 | Repeated security review, cert, signer, vulnerability work | 51 matching issues; 22 resolved | Worklogs, full comments | Draft remediation plans, evidence summaries | Security review mandatory |
| C2 | Repeated E2E, validation, test monitor, dry-run work | 88 matching issues; 41 resolved | Status transitions | Test checklist drafts, validation summaries | Engineer review |
| C3 | Repeated IaC, deployment, environment, AWS region work | 168 matching issues; 66 resolved | Transition history | Deployment checklist preparation | Tech Lead mandatory HITL |
| C4 | Repeated Splunk detector, alert, monitoring, dashboard work | 64 matching issues; 25 resolved | Reopen history | Alert classification, runbook drafts | Engineer review |
| C5 | Repeated ingestion, mapping, SharedDB, recommendation pipeline work | 79 matching issues; 36 resolved | Comments/worklogs | Pipeline validation summaries | Tech Lead validation |
| C6 | Cleanup/refactor/tooling improvements | 9 matching issues; 6 resolved | Low volume | Refactor plan drafts | Engineer review |
| C7 | Product/API/UI feature work | 14 matching issues; 9 resolved | Low pattern strength | Acceptance criteria drafts | PM/Tech Lead validation |
| C8 | Mixed one-off work | 114 issues | Pattern evidence | Not recommended | Manual triage |

## TABLE 5A — AGGREGATED METRICS

| Metric | Value | Availability | Notes |
|---|---:|---|---|
| Total issues | 587 | Available | REDIS only |
| Routine issues | 306 | Estimated from routine-classified clusters | Validated: subset <= count |
| Routine ratio | 52.1% | Available | 306 / 587 |
| Median Cycle Time | Not available | Missing status transitions | Do not infer from lead time |
| Median Lead Time | 28.0 days | Available for resolved issues | Created → resolved; 265 issues |
| Worklog Hours | Not available | Missing worklogs | Hours saved not calculated |
| Rework Rate | Not available | Missing status history | Reopen/return-to-active not available |

## TABLE 5B — METRICS BY PROJECT

| Project | Data Mode | Total Issues | Routine Issues | Routine % | Median Cycle Time | Median Lead Time | Worklog Coverage | Status History Coverage | Rework Rate | Confidence |
|---|---|---:|---:|---:|---|---|---|---|---|---|
| REDIS | Standard | 587 | 306 | 52.1% | Not available | 28.0 days | Not available | Not available | Not available | Medium |

## TABLE 6 — AI SAVINGS SCENARIOS

| ID | Cluster | Project | Volume | Baseline Per Unit | Conservative | Moderate | Optimistic | Savings Type | Assumption Used | Impact Type | Confidence |
|---|---|---|---:|---|---|---|---|---|---|---|---|
| C1 | Security/GHAS remediation | REDIS | 36 | 23.6d lead time | 5% | 10% | 20% | Cycle-time reduction opportunity | No worklogs | Directional | Medium |
| C2 | E2E/test validation | REDIS | 70 | 28.0d lead time | 5% | 10% | 20% | Cycle-time reduction opportunity | No worklogs | Directional | Medium |
| C3 | IaC/deployment | REDIS | 95 | 26.0d lead time | 5% | 10% | 20% | Cycle-time reduction opportunity | No worklogs | Directional | Medium |
| C4 | Splunk/monitoring | REDIS | 48 | 64.3d lead time | 5% | 10% | 20% | Cycle-time reduction opportunity | No worklogs | Directional | Medium |
| C5 | Data pipeline | REDIS | 45 | 37.8d lead time | 5% | 10% | 20% | Cycle-time reduction opportunity | No worklogs | Directional | Medium |

## TABLE 7 — AI USE CASES + KPI

| ID | Use Case | Cluster | Project | AI Type | Expected Benefit | KPI | Formula | Baseline Period | Post-AI Period | Comparability Check | Method | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| U1 | Test validation assistant | C2 | REDIS | Checklist + summary | Faster validation prep | Lead time reduction | Median lead time before - after | Last 26 weeks | Pilot period | Partially comparable | Compare same cluster | Medium |
| U2 | Deployment checklist assistant | C3 | REDIS | Draft/checklist | Fewer manual prep steps | Rework reduction | Reopened/returned-active rate before - after | Last 26 weeks | Pilot period | Not comparable yet | Add status history tracking | Low |
| U3 | Monitoring/runbook assistant | C4 | REDIS | Classification + draft | Faster detector/runbook updates | Throughput | Completed routine issues per sprint after - before | Last 26 weeks | Pilot period | Partially comparable | Same JQL cluster | Medium |
| U4 | Security evidence assistant | C1 | REDIS | Evidence extraction | Faster review packages | Lead time reduction | Median lead time before - after | Last 26 weeks | Pilot period | Partially comparable | Security-reviewed sample | Medium |

## TABLE 8 — NOT AUTOMATED TASKS

| Cluster | Project | Reason | AI Allowed | Control |
|---|---|---|---|---|
| Security/GHAS remediation | REDIS | Security/compliance decisions are high risk | Yes, AI-assisted only | Security review mandatory |
| IaC/deployment | REDIS | Production/environment changes are high risk | Yes, with mandatory HITL | Tech Lead approval |
| Non-routine or insufficient evidence | REDIS | Weak or mixed routine signal | No | Manual triage |
| API/UI/product feature implementation | REDIS | Requires product judgment | Yes, AI-assisted only | PM/Tech Lead validation |

## TABLE 9 — IMPROVEMENTS

| Improvement | Purpose | Priority |
|---|---|---|
| Track worklogs only for pilot clusters | Enable real hours-saved calculation | High |
| Export changelog/status history for REDIS | Enable cycle time and rework rate | High |
| Add optional AI-assisted field for pilot tickets | Measure before/after impact | Medium |
| Standardize done-status interpretation | Improve lead-time consistency | Medium |
| Improve operational ticket resolution notes | Better evidence for clustering | Medium |

## TABLE 10 — FINAL RECOMMENDATIONS

| Area | Recommendation | Priority |
|---|---|---|
| Top AI Pilot Cluster | E2E/test validation and test tooling | High |
| Baseline Metric | Median lead time, not hours saved | High |
| AI Tracking Setup | Add pilot marker + compare same JQL cluster before/after | High |
| Validation Owner Role | Tech Lead for deployment/security; engineer review for test/monitoring | High |
| Risks to Monitor | Over-automation of security and deployment decisions | High |
| Next Evaluation | Re-run after 4-6 weeks of tagged pilot data | Medium |

## Notes

- Source query: `project = REDIS AND (created >= -26w OR updated >= -26w OR resolutiondate >= -26w) ORDER BY updated DESC`
- Dataset exported through configured `jira-cli`.
- Worklogs were not available from the exported search fields, so hours saved were not calculated.
- Cycle time was not calculated because status transition history was not available.
- Lead time was calculated only for issues with both created and resolved timestamps.
- Labels were exported but ignored for routine classification, per prompt rules.
- The interactive Jira config echoed the token during setup; rotating the Atlassian token after this work is prudent.

End of report
