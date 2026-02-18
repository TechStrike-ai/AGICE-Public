# REPLAY_SCOPE

## Fully replayable offline in this package

- Signature verification of `checksums/SHA256SUMS.sig` against `checksums/SIGNING-PUBLIC-KEY.pem`
- Full file-level checksum verification from `checksums/SHA256SUMS.txt`
- Hash-chain validation for every `events.jsonl` in shipped bundles
- Manifest + integrity consistency checks per bundle
- Governance/policy artifact integrity via `manifests/policy-hashes.csv` and checksum coverage

## Requires external benchmark assets

- Full benchmark re-execution requiring external slices/dataset manifests
- Upstream benchmark cache reconstruction for all task families
- Re-running hidden/private benchmark test servers outside this package

## Intent

This release is designed for **offline integrity, auditability, and governance control evidence**.
It is not a complete mirror of all upstream benchmark datasets.
