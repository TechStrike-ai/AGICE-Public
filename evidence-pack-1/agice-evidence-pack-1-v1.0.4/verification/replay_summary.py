#!/usr/bin/env python3
"""Render a compact offline replay summary from packaged reports."""

from __future__ import annotations

import argparse
import csv
import os
from typing import List, Dict


def load_rows(path: str) -> List[Dict[str, str]]:
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle-root", default=".")
    args = parser.parse_args()

    root = os.path.abspath(args.bundle_root)
    results_csv = os.path.join(root, "reports", "results-per-task.csv")
    rows = load_rows(results_csv)
    if not rows:
        print(f"No results table found at: {results_csv}")
        return 1

    print("=" * 72)
    print("AGICE Demo Replay — Per Task Summary")
    print("=" * 72)
    print(f"{'Task':30} {'A1':>8} {'A2':>8} {'A3':>8} {'A3-A1':>8}")
    for row in rows:
        task = row.get("task_id", "")[:30]
        a1 = row.get("A1_solved", "")
        a2 = row.get("A2_solved", "")
        a3 = row.get("A3_solved", "")
        print(f"{task:30} {a1:>8} {a2:>8} {a3:>8} {'':>8}")
    print("=" * 72)
    print("See full details in reports/results-per-task.csv and reports/trajectory-table.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
