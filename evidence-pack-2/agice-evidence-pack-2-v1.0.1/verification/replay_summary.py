#!/usr/bin/env python3
"""Render a compact replay summary from packaged executive metrics."""

from __future__ import annotations

import argparse
import csv
import os
from typing import Dict, List


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
    summary_path = os.path.join(root, "reports", "demo-replay-executive-summary.csv")
    rows = load_rows(summary_path)
    if not rows:
        print(f"No replay executive summary found at: {summary_path}")
        return 1

    print("=" * 72)
    print("Agice evidence pack 2 — Replay Summary")
    print("=" * 72)
    print(f"{'Metric':32} {'A1':>10} {'A2':>10} {'A3':>10}")
    for row in rows:
        if row.get("task_name") != "All Tasks (combined)":
            continue
        metric = row.get("metric", "")
        a1 = row.get("A1", "")
        a2 = row.get("A2", "")
        a3 = row.get("A3", "")
        print(f"{metric:32} {a1:>10} {a2:>10} {a3:>10}")
    print("=" * 72)
    print("See full details in reports/demo-replay-executive-summary.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
