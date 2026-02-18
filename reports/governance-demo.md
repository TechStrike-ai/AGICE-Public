# Governance, Control, Evidence, Audit, and Rollback Demo (v1.0.1)

This walkthrough shows mission-critical governance behavior and evidence linkage with native rollback evidence in shipped bundles.

## 1) Verify release integrity

```bash
python verification/verify_offline.py --bundle-root . --strict
```

Expected result: `VERDICT: PASS`.

## 2) Inspect governance policy and decision logic

- Policy: `policies/governance_policy.v1.0.1.yaml`
- Verifier pack spec: `policies/verifier_pack.v1.0.1.yaml`
- Decision function: `policies/decision_function.v1.0.1.md`
- Run→policy mapping: `manifests/policy-hashes.csv`

## 3) Validate rollback + escalation incidents

See `reports/rollback-case-study.csv`:

- `rollback-hard-regression-native-001`: native automatic rollback recorded in `events.jsonl`.
- `escalation-repeated-failure-overlay-001`: controlled human-approval escalation demonstration.

Native rollback evidence anchor:
- `bundles/20260216_150059/A3/hard2_complex_transform/events.jsonl`
- event sequence: `e000013` (hard-fail candidate), `e000014` (`rollback_event`), `e000015` (stop on rolled-back incumbent)

## 4) Verify ops-grade provenance and attestation

- Ops provenance: `manifests/ops-provenance.json`
- Build attestation: `manifests/build-attestation.json`
- Attestation signature: `manifests/build-attestation.sig`

## 5) Review anti-tamper demonstration

See `reports/tamper-test.md` for an intentional tamper attempt and detection evidence.

## 6) Replay scope boundaries

See `reports/REPLAY_SCOPE.md` for what is fully offline-replayable versus what requires external benchmark assets.
