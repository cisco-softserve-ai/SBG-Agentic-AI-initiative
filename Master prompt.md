############################################################
PROMPT VERSION: v6.1.1
NAME: Jira Routine Task Identification & AI ROI Analysis
      (Multi-Project, Label-Free, Assignee-Based, Project-Isolated Clustering)
OWNER: AI Transformation Program
LAST UPDATED: 2026-06-17

CHANGELOG:
- v6.1.1 → Added project exclusion capability (strict pre-analysis filtering)
- v6.1 → Added contributor definition = Assignee only; validation rules; project-level data quality in metrics; conservative/moderate/optimistic savings; baseline comparability guardrail; risk-control guardrails
- v6.0 → Data quality by project + metrics by project + Routine Score definition clarified
- v5.0 → Multi-project full workload scope + project-isolated clustering
- v4.0 → ROI measurement + KPI formulas + Routine Subset + detailed classification
- v3.0 → Label-free clustering
############################################################

==================================================
1. INPUT PARAMETERS
==================================================

Use the following inputs:

- Primary Jira project(s): [PROJECT_KEY or multiple project keys]
- Excluded Jira project(s): [OPTIONAL LIST OF PROJECT KEYS]
- Analysis period: [START_DATE → END_DATE]
- Issue types to include: [Task, Bug, Story, Support, Sub-task, Improvement, Incident, etc.]
- Done statuses: [Done, Closed, Resolved, Released, Completed, etc.]

If any input parameter is missing:
- Use reasonable Jira defaults.
- Document the assumption in TABLE 2 — DATA QUALITY PER PROJECT.
- Do not stop the analysis.

==================================================
1A. PROJECT EXCLUSION RULE
==================================================

The analysis MUST support explicit exclusion of selected Jira projects.

1. Any project listed in "Excluded Jira project(s)" MUST NOT be included in:
   - dataset construction
   - clustering
   - metrics calculation
   - AI savings analysis
   - output tables
   - Jira links (Count / Routine Subset)

2. During Project Scope Expansion:
   - identify all Jira projects where contributors worked
   - REMOVE excluded projects BEFORE dataset construction

3. Issues from excluded projects:
   - MUST NOT be included in clusters, metrics, or outputs

4. If an assignee works in both included and excluded projects:
   - include only their work from included projects

5. Exclusion MUST be applied BEFORE:
   - clustering
   - metrics
   - savings calculations

OUTPUT REQUIREMENT:

TABLE 1 MUST include:

| Excluded Projects | <list or None> |

EXCLUSION SAFETY CHECK:

If excluded projects represent:
- more than 50% of workload OR
- key systems

Add warning:
"Exclusion may impact completeness of workload analysis"

VALIDATION:

Excluded projects must not appear in:
- TABLE 3
- TABLE 5A / 5B
- TABLE 6
- TABLE 7
- ANY Jira link

==================================================
2. CONTRIBUTOR DEFINITION
==================================================

Contributors are defined as Jira Assignees only.

When expanding scope from primary project(s) to secondary/shared projects:

1. Identify all unique assignees from the primary Jira project(s) within the selected analysis period.

2. Include issues from additional Jira projects only if:
   - the issue is assigned to one of those identified assignees, and
   - the issue was completed or active within the selected analysis period.

3. Do NOT include people based only on:
   - reporter field
   - comments
   - watchers
   - reviewers
   - linked PR reviewers
   - mentioned users
   - transition authors

Unless explicitly requested, only assignees define contributor scope.

Reason:
Using assignee-only scope avoids pulling unrelated stakeholders, reporters, reviewers, or commenters into the workload analysis.

==================================================
3. PROJECT SCOPE EXPANSION
==================================================

Step 1 — Identify primary assignees:
- From the primary Jira project(s), extract all unique assignees within the analysis period.

Step 2 — Expand project scope:
- Identify all Jira projects where these assignees are assigned to issues during the same analysis period.

Step 3 — Apply exclusion:
- Remove all excluded projects

Step 4 — Build full workload dataset:
Include:
- issues from non-excluded primary project(s)
- issues from non-excluded secondary/shared projects where identified assignees are assigned

Step 5 — Preserve project boundaries:
- Analyze full workload across projects.
- But clusters must remain strictly project-isolated.

6. Dataset filtering requirement:
All issues must satisfy:
- project NOT IN Excluded Jira project(s)

Result:
Full team workload across all relevant Jira systems, without mixing different project/system contexts.

==================================================
4. CORE RULES
==================================================

Follow these rules strictly:

1. Do NOT rely on Jira labels for classification.
2. Do NOT evaluate, rank, compare, or score individuals.
3. Do NOT stop the analysis because of missing data.
4. Missing data reduces confidence only; it does not block routine task identification.
5. ALWAYS include project-level breakdowns.
6. ALWAYS preserve project/system boundaries.
7. ALWAYS return all required tables.
8. Do NOT invent metrics.
9. Do NOT calculate hours saved without worklogs or another reliable effort baseline.
10. If using cycle time, call it cycle-time reduction opportunity, not hours saved.
11. High-risk routine work must require human-in-the-loop validation and must not be presented as safe for full automation.

==================================================
5. CLUSTERING RULE — PROJECT ISOLATION
==================================================

Clusters must be created separately per Jira project.

Each cluster:
- must belong to exactly one Jira project
- must contain issues from one project only
- must NOT mix issues from different Jira projects

Reason:
Different Jira projects may represent different systems, workflows, monitoring sources, business processes, and risk contexts.

Mixing issues from different projects may:
- hide root-cause differences
- produce incorrect automation assumptions
- reduce actionability
- create misleading AI opportunities

Therefore:
- analyze full workload across projects
- but cluster only within each project

==================================================
6. LABEL-INDEPENDENT ROUTINE IDENTIFICATION
==================================================

Do NOT use labels as a primary routine detection mechanism.

Labels may be:
- inconsistent
- missing
- project-specific
- manually applied with different meanings
- unsuitable for cross-project standardization

Routine work must be identified using universal Jira signals.

Use these signals:

1. Frequency:
   - Similar tasks repeat multiple times in the selected period.
   - Similar tasks repeat across sprints, releases, or operational cycles.

2. Text similarity:
   - Similar summaries.
   - Similar descriptions.
   - Similar comments.
   - Similar resolution notes.

3. Structural similarity:
   - Same issue type.
   - Similar parent/epic structure.
   - Similar subtask patterns.
   - Similar linked issue structure.

4. Workflow similarity:
   - Similar status transitions.
   - Similar lifecycle shape.
   - Similar handoffs.
   - Similar reopen/rework pattern.

5. Predictability:
   - Clear input.
   - Clear output.
   - Repeatable resolution path.
   - Low ambiguity.
   - Limited need for strategic judgment.

6. AI suitability:
   - AI can assist with drafting, summarizing, classifying, generating, checking, comparing, troubleshooting, or preparing output.

==================================================
7. FALSE SIMILARITY GUARDRAIL
==================================================

Do not classify issues as routine based on generic summaries alone.

If summaries are vague, such as:
- “Fix issue”
- “Investigate problem”
- “Update config”
- “Check failure”
- “Support request”

Then require at least one additional supporting signal:
- similar description
- similar comments
- similar workflow
- similar issue type
- similar resolution pattern
- repeated component/system context
- repeated status lifecycle
- repeated operational source

If no additional supporting signal exists:
- classify as Weak Routine Signal or Not Enough Evidence
- reduce confidence
- do not overstate routine classification

==================================================
8. ROUTINE SCORE
==================================================

Each cluster must receive a Routine Score.

Routine Score is a composite score from 0 to 18.

Score each of the following 9 criteria from 0 to 2:

1. Frequency
   - 0 = rare / one-off
   - 1 = occasional repetition
   - 2 = frequent repetition

2. Repetition
   - 0 = different each time
   - 1 = partially repeated
   - 2 = same or highly similar steps

3. Rule-based behavior
   - 0 = no rule pattern
   - 1 = partial rule logic
   - 2 = clear rule-based execution

4. Low ambiguity
   - 0 = high ambiguity
   - 1 = moderate ambiguity
   - 2 = low ambiguity

5. Standard input/output
   - 0 = inconsistent input/output
   - 1 = partially standardized
   - 2 = predictable input/output

6. Workflow consistency
   - 0 = inconsistent workflow
   - 1 = partially similar workflow
   - 2 = consistent lifecycle/status path

7. Time/effort relevance
   - 0 = low impact
   - 1 = moderate impact
   - 2 = meaningful effort or elapsed time

8. AI suitability
   - 0 = not suitable for AI
   - 1 = partially suitable
   - 2 = strong AI support potential

9. Reuse potential
   - 0 = not reusable
   - 1 = partially reusable
   - 2 = reusable prompt/template/workflow potential

Routine Score =
Frequency
+ Repetition
+ Rule-based behavior
+ Low ambiguity
+ Standard input/output
+ Workflow consistency
+ Time/effort relevance
+ AI suitability
+ Reuse potential

Classification mapping:
- 14–18 → Strong Routine Candidate
- 10–13 → Possible Routine Candidate
- 7–9 → Weak Routine Signal
- Less than 7 → High-Value / Complex or Not Routine
- High risk + repetitive → Routine with HITL

==================================================
9. RISK CLASSIFICATION
==================================================

Classify each cluster risk as Low, Medium, or High.

Low Risk:
- documentation draft
- status summary
- repeated formatting
- test data draft
- simple access troubleshooting
- low-impact operational analysis

Medium Risk:
- troubleshooting recommendation
- code/test generation
- CI/CD configuration draft
- build failure classification
- monitoring alert classification
- deployment checklist preparation

High Risk:
- production decision
- architecture decision
- compliance/security approval
- incident root-cause conclusion
- customer-sensitive communication
- risk acceptance
- budget/contract approval
- security hardening
- production deployment approval

==================================================
10. AUTOMATION SAFETY GUARDRAIL
==================================================

High-risk clusters must never be marked as full automation candidates.

High-risk routine clusters may only be marked as:
- AI-assisted preparation
- draft generation
- summarization
- checklist support
- evidence extraction
- recommendation with mandatory human validation

Required control must be explicitly stated:
- Tech Lead validation
- Security review
- Incident Manager approval
- PM/Delivery validation
- Customer approval
- Mandatory HITL

==================================================
11. DATA MODE
==================================================

Assign data mode overall and per project.

Rich:
- summary/description available
- status history available
- comments available
- worklogs or estimates available
- dates available
- enough data for stronger metric confidence

Standard:
- summary/description available
- issue type available
- dates available
- status history available or partially available
- worklogs missing or partial

Minimal:
- only summary, issue type, status, and dates available
- weak comments/status/worklog data

Data mode must be shown:
- in TABLE 1 for overall analysis
- in TABLE 5B per project

==================================================
12. CONFIDENCE LEVEL
==================================================

Assign confidence to overall analysis, each cluster, and savings estimate.

High:
- strong repeated patterns
- good description/comment quality
- status history available
- sufficient volume
- reliable metrics

Medium:
- patterns are visible
- some data is missing
- status history or worklogs are partial
- enough evidence exists for directional conclusions

Low:
- weak signals
- low volume
- vague summaries
- missing worklogs/comments/status details
- classification requires manual validation

Low confidence does not mean “not routine.”
It means the finding requires validation by PM / Tech Lead / AI Champion.

==================================================
13. VALIDATION RULES
==================================================

Before producing output, validate all calculations.

Mandatory checks:

1. Routine Subset must be less than or equal to Count.
   - If Routine Subset > Count, correct the calculation before producing output.

2. Routine Issues total in TABLE 1 must equal the sum of Routine Subsets across routine-classified clusters.

3. Total Issues split by project in TABLE 1 must equal Total Issues total.

4. Routine Issues split by project in TABLE 1 must equal Routine Issues total.

5. Cluster Count must represent all issues in that cluster.

6. Routine Subset must represent only issues inside that cluster classified as routine.

7. Clusters must not contain issues from more than one project.

8. If any math inconsistency exists, correct it before output.

9. Ensure excluded projects do NOT appear in:
   - TABLE 3 (clusters)
   - TABLE 5A / 5B (metrics)
   - TABLE 6 (savings)
   - TABLE 7 (use cases)
   - any Jira links

Do not output inconsistent totals.

==================================================
14. METRICS RULES
==================================================

Always calculate if possible:

- Total issues
- Routine issues
- Routine ratio
- Total issues per project
- Routine issues per project
- Routine percentage per project
- Cluster count
- Routine subset per cluster

If timestamps/status history are available:
- Median Cycle Time for routine issues
- Median Lead Time for routine issues
- Rework Rate

Definitions:
- Lead Time = Done date - Created date
- Cycle Time = Done date - first transition to active work status
- Rework Rate = Reopened or returned-to-active issues / total issues

If worklogs are available:
- Worklog coverage
- Worklog hours for routine issues
- Median worklog hours per routine issue
- Effort-based savings estimates

If worklogs are missing:
- Do NOT calculate hours saved.
- Use cycle-time reduction opportunity only.
- Clearly state that cycle time is elapsed delivery time and may include waiting time.

==================================================
15. SAVINGS GUARDRAIL
==================================================

Do not overstate AI ROI.

All savings must include:
- baseline used
- assumption used
- savings type
- confidence level
- impact type

Impact Type must be one of:
- Confirmed
- Proxy-based
- Directional
- Not estimable

Savings types:
- Hours saved
- Cycle-time reduction opportunity
- Throughput increase
- Rework reduction
- Not estimable

Rules:

If worklogs or reliable effort baseline are available:
- Conservative = 10% effort reduction
- Moderate = 20% effort reduction
- Optimistic = 30% effort reduction

If only cycle time is available:
- Conservative = 5% cycle-time reduction
- Moderate = 10% cycle-time reduction
- Optimistic = 20% cycle-time reduction

If neither worklogs nor reliable cycle time are available:
- do not estimate savings
- mark as Not estimable
- explain what data is needed

Important:
- Hours saved can be reported only when effort data exists.
- Cycle-time reduction is not the same as effort savings.
- Throughput increase must be measured using ticket volume per comparable period.

==================================================
16. BASELINE PERIOD GUARDRAIL
==================================================

Before/after KPI comparison is valid only if baseline and post-AI periods are comparable.

Comparable periods must use:
- same project scope
- same issue types
- same done statuses
- same assignee scope
- same cluster definition
- same or normalized period length
- similar operational context where possible

If periods are not comparable:
- mark result as Directional only
- do not present as confirmed AI impact

The output must include:
- Baseline Period
- Post-AI Period
- Comparability Check
- Measurement Confidence

Comparability Check values:
- Comparable
- Partially comparable
- Not comparable

==================================================
17. OUTPUT FORMAT
==================================================

Return all tables below.

If a value is unavailable:
- write “Not available”
- explain why in Notes, Impact, or Assumption columns

Do not remove rows because of missing data.

==================================================
TABLE 1 — EXECUTIVE SUMMARY
==================================================

| Field | Value |
|---|---|
| Projects | List all identified projects: primary and secondary |
| Excluded Projects | list or None |
| Period | |
| Total Issues | Total + split per project |
| Routine Issues | Total + split per project |
| Routine Ratio | |
| Workload Distribution | % of total issues per project |
| Data Mode | Overall mode + explanation |
| Top Cluster #1 | |
| Top Cluster #2 | |
| Top Cluster #3 | |
| Confidence | Overall confidence + explanation |

Example for Total Issues:
214 total
→ DEVOPS-PLATFORM: 90
→ MONITORING: 60
→ INCIDENTS: 40
→ SUPPORT: 24

Example for Routine Issues:
132 total
→ DEVOPS-PLATFORM: 58
→ MONITORING: 41
→ INCIDENTS: 23
→ SUPPORT: 10

==================================================
TABLE 2 — DATA QUALITY PER PROJECT
==================================================

| Data Element | Overall Status | Project A | Project B | Project C | Project D | Impact |
|---|---|---|---|---|---|---|
| Summary | | | | | | |
| Issue Type | | | | | | |
| Labels | Ignored | Ignored | Ignored | Ignored | Ignored | Labels are not used for clustering |
| Status History | | | | | | |
| Dates | | | | | | |
| Worklogs | | | | | | |
| Comments | | | | | | |

Use actual identified project names as columns.

==================================================
TABLE 3 — PROJECT-ISOLATED CLUSTERS
==================================================

| ID | Cluster Name | Project | SDLC Phase | Count | Routine Subset | Routine Score | Risk | Risk Details | Classification | Classification Details | Confidence |
|---|---|---|---|---:|---:|---:|---|---|---|---|---|

Definitions:
- Count = total issues in the cluster
- Routine Subset = number of routine issues inside that cluster
- Routine Score = sum of 9 criteria, each scored 0–2, max 18
- Routine Subset must always be <= Count
- Count and Routine Subset SHOULD be rendered as Jira links (JQL queries) pointing to exact issue sets when possible.

==================================================
TABLE 4 — CLUSTER EVIDENCE
==================================================

| ID | Pattern Description | Evidence | Missing Data | AI Opportunity | Validation Required |
|---|---|---|---|---|---|

Validation Required examples:
- Engineer light review
- Tech Lead mandatory validation
- Security review
- Incident Manager mandatory HITL
- PM/Delivery validation

==================================================
TABLE 5A — AGGREGATED METRICS
==================================================

| Metric | Value | Availability | Notes |
|---|---|---|---|
| Total issues | | | |
| Routine issues | | | |
| Routine ratio | | | |
| Median Cycle Time (Routine Issues) | | | Calculated across routine issues, not across clusters |
| Median Lead Time (Routine Issues) | | | |
| Worklog Hours (Routine Issues) | | | |
| Rework Rate | | | |

==================================================
TABLE 5B — METRICS BY PROJECT
==================================================

| Project | Data Mode | Total Issues | Routine Issues | Routine % | Median Cycle Time | Median Lead Time | Worklog Coverage | Status History Coverage | Rework Rate | Measurement Confidence |
|---|---|---:|---:|---:|---|---|---|---|---|---|

==================================================
TABLE 6 — AI SAVINGS SCENARIOS
==================================================

| ID | Cluster | Project | Volume | Baseline Per Unit | Conservative Saving | Moderate Saving | Optimistic Saving | Savings Type | Assumption Used | Impact Type | Confidence |
|---|---|---|---:|---|---|---|---|---|---|---|---|

Rules:
- Volume = number of routine tickets in the cluster or Routine Subset
- Baseline Per Unit = effort per ticket if worklogs exist; otherwise cycle time per ticket
- Conservative / Moderate / Optimistic values must use the assumptions from Section 15
- If savings cannot be estimated, mark as Not estimable

==================================================
TABLE 7 — AI USE CASES + KPI
==================================================

| ID | Use Case | Cluster | Project | AI Type | Expected Benefit | KPI | KPI Formula | Baseline Period | Post-AI Period | Comparability Check | Measurement Method | Measurement Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Examples of KPI formulas:

Cycle Time Reduction:
Median Cycle Time Before AI - Median Cycle Time After AI

Throughput Increase:
Issues Completed Per Sprint After AI - Issues Completed Per Sprint Before AI

Time Saved:
Total Worklog Hours Before AI - Total Worklog Hours After AI

Rework Reduction:
Rework Rate Before AI - Rework Rate After AI

Rework Rate:
Reopened or returned-to-active issues / total completed issues

==================================================
TABLE 8 — NOT AUTOMATED TASKS
==================================================

| Cluster | Project | Reason | AI Allowed | Control |
|---|---|---|---|---|

AI Allowed values:
- No
- Yes, AI-assisted only
- Yes, with mandatory HITL

==================================================
TABLE 9 — IMPROVEMENTS
==================================================

| Improvement | Purpose | Priority |
|---|---|---|

Only recommend practical improvements.
Do not recommend excessive Jira process changes.

Examples:
- Track worklogs for pilot clusters only
- Define active vs waiting statuses
- Track reopen reason
- Add optional AI usage field for pilot scope
- Standardize done statuses for analysis
- Improve comment quality for operational tickets

==================================================
TABLE 10 — FINAL RECOMMENDATIONS
==================================================

| Area | Recommendation | Priority |
|---|---|---|
| Top AI Pilot Cluster | | |
| Baseline Metric | | |
| AI Tracking Setup | | |
| Validation Owner Role | | |
| Risks to Monitor | | |
| Next Evaluation | | |

==================================================
18. FINAL RESPONSE RULES
==================================================

The final answer must be:
- table-first
- evidence-based
- project-isolated
- clear about missing data
- clear about proxy vs confirmed metrics
- clear about risk and validation
- free from individual performance evaluation

Do not:
- include excluded projects anywhere
- rank engineers
- assume worklogs if missing
- calculate hours saved without effort data
- mix clusters across projects
- hide data quality issues
- present directional estimates as confirmed impact

Do:
- analyze full workload across projects
- use assignee-only contributor expansion
- keep clusters project-specific
- provide project-level splits
- validate all totals before output
- use conservative/moderate/optimistic scenarios
- include KPI formulas and baseline guardrails

After completing all required sections, output exactly:

End of report
