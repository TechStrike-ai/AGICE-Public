# AGICE Demo Replay — Evidence Bundle

Version: `1.0.2`

DOI: `10.5281/zenodo.18678131`
Canonical repository: `https://github.com/TechStrike-ai/AGICE-Public`
Source build repository: `https://github.com/TechStrike-ai/AGICEv3_repo`


This archive is structured for public replay and offline integrity verification.

## Contents

- `bundles/` — per-run AGICE evidence bundles
- `reports/executive-summary.csv` — paper-ready A1/A2/A3 summary
- `reports/trajectory-table.md` — sample A3 branching trajectory table (markdown)
- `reports/trajectory-table.csv` — sample A3 branching trajectory table (csv)
- `reports/replay-coverage.csv` — per-bundle replay report presence map
- `reports/governance-demo.md` — governance/control audit walkthrough
- `reports/rollback-case-study.csv` — governed rollback/escalation incident table
- `reports/tamper-test.md` — intentional tamper detection demonstration
- `reports/REPLAY_SCOPE.md` — offline replay scope boundaries
- `manifests/run-evidence-hashes.csv` — per-run file hashes
- `manifests/bundle-validation-report.json` — bundle schema/hash-chain validation results
- `manifests/report-hashes.json` — report-file hashes
- `manifests/policy-hashes.csv` — run-to-policy hash mapping
- `manifests/policy-artifacts.csv` — policy artifact inventory and hashes
- `manifests/ops-provenance.json` — ops-grade provenance snapshot
- `manifests/build-attestation.json` — signed release attestation payload
- `manifests/build-attestation.sig` — detached signature for build attestation
- `checksums/SHA256SUMS.txt` — signed global checksum manifest
- `checksums/SHA256SUMS.sig` — SHA256SUMS signature
- `checksums/SIGNING-PUBLIC-KEY.pem` — public key for offline verification
- `verification/verify_offline.py` — offline verifier (signature + checksums + bundle integrity)
- `demo-replay.sh` — one-command public demo replay (integrity + native rollback trace)
- `policies/governance_policy.v1.0.1.yaml` — mission-critical governance policy
- `policies/verifier_pack.v1.0.1.yaml` — verifier pack control specification
- `policies/decision_function.v1.0.1.md` — arbitration and rollback decision spec

## Dataset Scope

- Case ID: `AGICE Demo Replay`
- Runs included: `39`
- Bundles included: `39`

## Offline Verification

```bash
python verification/verify_offline.py --bundle-root . --strict
```

## Demo Replay

Run the public demo replay from the package root:

```bash
./demo-replay.sh
```

This executes strict offline verification and then prints the native `rollback_event` trace from:
`bundles/20260216_150059/A3/hard2_complex_transform/events.jsonl`.

## Strict Checksum Coverage (No Extra Unhashed Files)

`checksums/SHA256SUMS.txt` and `checksums/SHA256SUMS.sig` are intentionally excluded from strict set-diff checks.

```bash
python verification/verify_offline.py --bundle-root . --strict

# Optional shell-level strict diff
comm -23 \
  <(find . -type f ! -path "./checksums/SHA256SUMS.sig" ! -path "./checksums/SHA256SUMS.txt" -printf "%P\n" | sort) \
  <(awk '{print $2}' checksums/SHA256SUMS.txt | sort)
```

## Replay Scope Clarification

### What you can verify offline

- Signature authenticity of `checksums/SHA256SUMS.txt`
- File-level checksum integrity for all hashed files in this package
- Per-bundle evidence hash-chain validity (`events.jsonl`)
- Manifest/integrity consistency checks for copied run bundles

### What requires external benchmark data

- Full benchmark task re-execution against upstream datasets/slice manifests
- End-to-end benchmark replay requiring caches/manifests not embedded in this archive

This package is intended for **offline integrity verification and evidence auditability**. Full benchmark reruns are possible with external benchmark assets.

## Governance Demonstration Entry Points

- Start with `reports/governance-demo.md`
- Inspect policy controls in `policies/`
- Review governed incidents in `reports/rollback-case-study.csv`
- Validate policy binding via `manifests/policy-hashes.csv`
- Inspect native rollback event at `bundles/20260216_150059/A3/hard2_complex_transform/events.jsonl`
- Validate per-bundle policy embedding in `bundle_manifest.json` (`provenance.policy_binding`) and `integrity.json` (`policy_binding`)
- Review signed attestation in `manifests/build-attestation.json` and `manifests/build-attestation.sig`
