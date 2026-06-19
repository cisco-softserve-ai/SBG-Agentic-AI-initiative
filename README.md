# SBG Agentic AI Initiative

Simple workspace for analyzing Jira work patterns and finding practical areas where AI can help engineering teams.

## What This Repo Contains

- `Master prompt.md` — the source prompt for Jira routine-task and AI ROI analysis.
- `framework/` — early framework notes, defaults, and structure for repeatable team-based runs.
- `skills/jira-routine-analysis/` — Codex skill for running the framework.
- `reports/` — generated Markdown reports from individual analyses.

## Current Focus

The first version focuses on:

- team-level Jira analysis,
- project-isolated routine work clusters,
- AI assistance candidates,
- data-quality gaps,
- historical run comparison over time.

## Scope

- Primary analysis unit: team.
- Jira source: `cisco-sbg.atlassian.net`.
- Team/project metadata source: Confluence team information page.
- Default period: current Cisco fiscal quarter.
- Outputs stay local unless explicitly published.

## Notes

Generated run data and raw snapshots should stay out of git. The repo already ignores local run artifacts under `framework/runs/` and `framework/comparisons/`.

## Using The Codex Skill

Install the skill by copying or symlinking it into your Codex skills folder:

```bash
mkdir -p ~/.codex/skills
ln -s "$PWD/skills/jira-routine-analysis" ~/.codex/skills/jira-routine-analysis
```

Then verify setup from the repo root:

```bash
python3 skills/jira-routine-analysis/scripts/doctor.py
```

The verifier checks repo layout, Cisco fiscal-quarter defaults, generated output folders, Jira CLI discovery, and Jira authentication.
