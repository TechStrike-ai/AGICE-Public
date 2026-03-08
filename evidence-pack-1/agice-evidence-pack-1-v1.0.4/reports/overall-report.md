# Drop4 Demo Selection — Overall Report

- Case ID: `AGICE Demo Replay`
- Source slice: `gmdt_stress_v1`
- Seeds: `42,100,200`
- Exclusion policy: drop tasks where all modes are `3/3` or all `0/3`, plus `staircase_nim`.

## Included tasks

- `adjacent_hanoi` — A1 2/3, A2 2/3, A3 3/3
- `hard2_angular_sort` — A1 0/3, A2 3/3, A3 3/3
- `ss_007` — A1 2/3, A2 3/3, A3 3/3
- `ss_010` — A1 0/3, A2 0/3, A3 1/3
- `wildcard_match` — A1 2/3, A2 3/3, A3 3/3

## Artifacts in this bundle

- `reports/results-per-task.csv` — per-task solved counts and round stats by mode.
- `reports/trajectory-table.csv` and `reports/trajectory-table.md` — A3 minus_i trajectory trace (seed100/hard2_angular_sort).
- `reports/fairness-proof.md` and `reports/fairness.csv` — compute-budget fairness evidence.
- `reports/leakage-scan.csv` — hidden-test leakage audit results.
- `reports/gmdt-math-snippet.md` — direct code-level math implementation mapping.
- `reports/executive-summary.csv` — paper-ready aggregate metrics.

## Key takeaway

This demo subset is intentionally discriminative: it removes uniformly easy/hard tasks and preserves tasks where ablation differences are measurable under equal-budget, no-leakage constraints.
