# Agice evidence pack 2

Version: `1.0.1`

Canonical repository: `https://github.com/TechStrike-ai/AGICE-Public`
Source code branch used for this pack: `further-testing`
Source code commit used for this pack: `231130138905a7d8d4b9d79e9068b269e0cae324`

Testing cases reference paper: `arXiv:2602.06176`

This archive is structured for public replay and offline integrity verification.

## Contents

- `bundles/` — per-run AGICE evidence bundles
- `reports/executive-summary.csv` — paper-ready A1/A2/A3 summary
- `reports/overall-report.md` — overall narrative report
- `reports/replay-coverage.csv` — per-bundle replay report presence map
- `reports/demo-replay-executive-summary.csv` — replay-ready summary
- `reports/demo-replay-report.md` — replay verification report
- `manifests/run-evidence-hashes.csv` — per-run file hashes
- `manifests/task-evidence-hashes.csv` — per-task/per-mode aggregated evidence hashes
- `manifests/bundle-validation-report.json` — bundle schema/hash-chain validation results
- `manifests/demo-replay-manifest.json` — replay transaction index
- `manifests/demo-replay-validation-report.json` — replay validation status
- `manifests/report-hashes.json` — report-file hashes
- `checksums/SHA256SUMS.txt` — signed global checksum manifest
- `checksums/SHA256SUMS.sig` — SHA256SUMS signature
- `checksums/SIGNING-PUBLIC-KEY.pem` — public key for offline verification
- `verification/verify_offline.py` — offline verifier (signature + checksums + bundle integrity)
- `demo-replay.sh` — one-command offline verification + summary replay

## Dataset Scope

- Case ID: `AGICE Demo Replay`
- Runs included: `180`
- Bundles included: `180`

## Offline Verification

```bash
python verification/verify_offline.py --bundle-root . --strict
```

## Offline Demo Replay

```bash
bash demo-replay.sh
```

Replay is self-contained inside this package and does not require changing repository commits.

Pack-level provenance metadata is recorded in:

- `manifests/run_meta.json`

## Strict Checksum Coverage (No Extra Unhashed Files)

`checksums/SHA256SUMS.txt` and `checksums/SHA256SUMS.sig` are intentionally excluded from strict set-diff checks.

```bash
python verification/verify_offline.py --bundle-root . --strict

# Optional shell-level strict diff
comm -23 \
  <(find . -type f ! -path "./checksums/SHA256SUMS.sig" ! -path "./checksums/SHA256SUMS.txt" -printf "%P\\n" | sort) \
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
