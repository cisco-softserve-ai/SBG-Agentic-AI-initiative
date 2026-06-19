#!/usr/bin/env python3
"""Print Cisco fiscal quarter date range as JSON."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date, datetime


def parse_date(value: str | None) -> date:
    if not value:
        return date.today()
    return datetime.strptime(value, "%Y-%m-%d").date()


def quarter_for_day(day: date) -> tuple[int, int, date, date]:
    month = day.month
    year = day.year

    if month in (8, 9, 10):
        return year + 1, 1, date(year, 8, 1), date(year, 10, 31)
    if month in (11, 12):
        return year + 1, 2, date(year, 11, 1), date(year + 1, 1, 31)
    if month == 1:
        return year, 2, date(year - 1, 11, 1), date(year, 1, 31)
    if month in (2, 3, 4):
        return year, 3, date(year, 2, 1), date(year, 4, 30)
    return year, 4, date(year, 5, 1), date(year, 7, 31)


def quarter_for_label(label: str) -> tuple[int, int, date, date]:
    match = re.fullmatch(r"FY(\d{4})\s*Q([1-4])", label.strip(), re.IGNORECASE)
    if not match:
        raise ValueError("Quarter must look like FY2026 Q4")
    fiscal_year = int(match.group(1))
    quarter = int(match.group(2))
    if quarter == 1:
        return fiscal_year, quarter, date(fiscal_year - 1, 8, 1), date(fiscal_year - 1, 10, 31)
    if quarter == 2:
        return fiscal_year, quarter, date(fiscal_year - 1, 11, 1), date(fiscal_year, 1, 31)
    if quarter == 3:
        return fiscal_year, quarter, date(fiscal_year, 2, 1), date(fiscal_year, 4, 30)
    return fiscal_year, quarter, date(fiscal_year, 5, 1), date(fiscal_year, 7, 31)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="Date in YYYY-MM-DD format; defaults to today")
    parser.add_argument("--quarter", help="Cisco fiscal quarter label, for example FY2026 Q4")
    args = parser.parse_args()

    if args.quarter:
        fiscal_year, quarter, start, end = quarter_for_label(args.quarter)
    else:
        fiscal_year, quarter, start, end = quarter_for_day(parse_date(args.date))

    print(
        json.dumps(
            {
                "fiscal_year": fiscal_year,
                "quarter": quarter,
                "label": f"FY{fiscal_year} Q{quarter}",
                "start": start.isoformat(),
                "end": end.isoformat(),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

