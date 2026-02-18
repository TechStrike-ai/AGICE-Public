# A3 Branching Trajectory Pack (Valid Evidence)

- **Case ID:** AGICE Demo Replay
- **Ablation:** `A3`
- **Task family:** `livecodebench`
- **Task:** `hard2_complex_transform` (Complex Point Transform Chain)
- **Source:** `artifacts/zenodo/agice-demo-replay-v1/bundles/*/A3/hard2_complex_transform/events.jsonl`

Included trajectories:
- `traj_a3_delta_gain`: run `20260216_150059` seed `61`; selected round `1` projection `minus_i`; `rho=0.4462` `tau=0.0` `P=['base', 'minus_i']` `rotation_applied=True`. A3 minus_i solves while base still fails hard tests
- `traj_a3_tiebreak_shorter_code_seed60`: run `20260216_145630` seed `60`; selected round `1` projection `minus_i`; `rho=0.4462` `tau=0.0` `P=['base', 'minus_i']` `rotation_applied=True`. A3 base and minus_i both solve; minus_i selected by deterministic shorter-code tie-break
- `traj_a3_tiebreak_shorter_code_seed61`: run `20260216_145655` seed `61`; selected round `1` projection `minus_i`; `rho=0.4462` `tau=0.0` `P=['base', 'minus_i']` `rotation_applied=True`. A3 base and minus_i both solve; minus_i selected by deterministic shorter-code tie-break

| trajectory_id | run_id | seed | round_t | proj | axis_j | x_canonical_hash_prefix | patch_size_lines_tokens | bound_ok_le_limit_lines | v_tests_pass_total | failing_tests | v_tests_time_s | composite_loss | arbiter_accepted | hard_failed | selected | selection_rationale_recorded | projection_rho | projection_tau | projections_considered |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| traj_a3_delta_gain | 20260216_150059 | 61 | 0 | base (state) | 0 | init_state | — | — | 3/12 | private_0;private_1;private_2;private_3;private_4;private_5;private_6;private_7; | 0.132 | 0.75 | n/a | [V_tests] | True | Current incumbent before candidate arbitration. | 0.4462 | 0.0 | base\|minus_i |
| traj_a3_delta_gain | 20260216_150059 | 61 | 1 | base | 0 | 07e86dd280ac | 55/175 | True | 10/12 | private_6;private_8 | 0.138 | 0.16666666666666666 | False | [V_tests] | False | not selected: hard fail ['V_tests'] | 0.4462 | 0.0 | base\|minus_i |
| traj_a3_delta_gain | 20260216_150059 | 61 | 1 | minus_i | 1 | 1301b94e585f | 27/104 | True | 12/12 | — | 0.138 | 0.0 | True | [] | True | selected: lower loss / hard-pass advantage (0.0). | 0.4462 | 0.0 | base\|minus_i |
| traj_a3_tiebreak_shorter_code_seed60 | 20260216_145630 | 60 | 0 | base (state) | 0 | init_state | — | — | 3/12 | private_0;private_1;private_2;private_3;private_4;private_5;private_6;private_7; | 0.137 | 0.75 | n/a | [V_tests] | True | Current incumbent before candidate arbitration. | 0.4462 | 0.0 | base\|minus_i |
| traj_a3_tiebreak_shorter_code_seed60 | 20260216_145630 | 60 | 1 | base | 0 | 8a06eda16015 | 27/105 | True | 12/12 | — | 0.132 | 0.0 | True | [] | False | not selected: tie/loss inferior to minus_i/1. | 0.4462 | 0.0 | base\|minus_i |
| traj_a3_tiebreak_shorter_code_seed60 | 20260216_145630 | 60 | 1 | minus_i | 1 | c5f4d36a8907 | 27/105 | True | 12/12 | — | 0.14 | 0.0 | True | [] | True | selected: tie on loss/hard-pass; deterministic smaller-code tie-break (688 chars). | 0.4462 | 0.0 | base\|minus_i |
| traj_a3_tiebreak_shorter_code_seed61 | 20260216_145655 | 61 | 0 | base (state) | 0 | init_state | — | — | 3/12 | private_0;private_1;private_2;private_3;private_4;private_5;private_6;private_7; | 0.137 | 0.75 | n/a | [V_tests] | True | Current incumbent before candidate arbitration. | 0.4462 | 0.0 | base\|minus_i |
| traj_a3_tiebreak_shorter_code_seed61 | 20260216_145655 | 61 | 1 | base | 0 | c389260b4d05 | 37/102 | True | 12/12 | — | 0.133 | 0.0 | True | [] | False | not selected: tie/loss inferior to minus_i/1. | 0.4462 | 0.0 | base\|minus_i |
| traj_a3_tiebreak_shorter_code_seed61 | 20260216_145655 | 61 | 1 | minus_i | 1 | 1301b94e585f | 27/104 | True | 12/12 | — | 0.155 | 0.0 | True | [] | True | selected: tie on loss/hard-pass; deterministic smaller-code tie-break (710 chars). | 0.4462 | 0.0 | base\|minus_i |

CSV source: `Reports-archive/testing-drop1-a3-trajectory-pack.csv`
