# Drop4 Demo Fairness and Leakage Proof

- Source run: `runs/drop4_gmdt_stress_v1_full_parallel_pass2/*/20260220_095005`
- Selected tasks (after exclusions): adjacent_hanoi, hard2_angular_sort, ss_007, ss_010, wildcard_match
- Exclusions applied: all-modes `3/3`, all-modes `0/3`, and `staircase_nim`.

## 1) Same rounds budget across modes

- Config `configs/drop4_matched_compute_stress.yaml` sets `max_rounds_per_task: 6`.
- Empirical check over 15 seed-task triples: `rounds_equal=1` for all rows.
- Artifact: `reports/fairness.csv` (in Zenodo pack).

## 2) Same generator sample budget across modes

- Config sets matched per-round budgets: `a1_candidates_per_round=4`, `a2_total_candidates_per_round=4`, `a3_total_candidates_per_round=4`.
- A3 splits those 4 calls between `base` and `minus_i`; A1/A2 keep all 4 on `base`.
- Empirical check over 15 seed-task triples: `calls_equal=1` for all rows.
- Artifact: `reports/fairness.csv` contains `llm_calls_total` and `llm_calls_by_projection` per row.

## 3) Hard no-leak constraint from verifier

- Hidden/private tests are redacted in verifier payloads (`verifier/runner.py`).
- Leakage scan across selected bundles: hidden records=7916, verifier leaks=0, hint text leaks=0, feedback-json hidden payload leaks=0.
- Artifact: `reports/leakage-scan.csv` (bundle-level audit rows).

## 4) Interpretation

Given equal rounds + equal call budgets + zero hidden-test payload leakage, performance differences between A1/A2/A3 in this demo set are attributable to AGICE mode logic (structured feedback, arbitration, and A3 projection branching).
