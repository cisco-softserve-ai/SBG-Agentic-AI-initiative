# Framework Contract

Use this reference when implementing or updating automation around this repository's SBG Agentic AI framework.

## Required Behavior

- Prefer team-based runs.
- Allow direct Jira project-key runs.
- Default timeframe to current Cisco fiscal quarter.
- Use `Master prompt.md` as the analysis policy source.
- Use `cisco-sbg.atlassian.net` only.
- Verify setup before first data collection.
- Store raw/generated run artifacts under `framework/runs/`.
- Keep generated comparisons under `framework/comparisons/`.
- Produce team rollup reports with project-isolated clusters.
- Do not publish to Confluence or Jira unless explicitly requested.

## Minimal Run Inputs

```yaml
team: Unspecified
projects:
  - REDIS
period:
  start: "2026-05-01"
  end: "2026-07-31"
excluded_projects: []
```

## Minimal Metrics JSON

```json
{
  "team": "Unspecified",
  "projects": ["REDIS"],
  "period": {"start": "2026-05-01", "end": "2026-07-31"},
  "total_issues": 0,
  "routine_issues": 0,
  "routine_ratio": null,
  "clusters": [],
  "data_quality": {},
  "recommendations": []
}
```

