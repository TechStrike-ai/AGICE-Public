# AGICE Public Evidence Packs

This folder publishes two offline-verifiable AGICE evidence bundles.

## Evidence pack 1

- Extracted bundle: `evidence-pack-1/agice-evidence-pack-1-v1.0.4`
- Archive: `evidence-pack-1/agice-demo-replay-v1.0.4.tar.gz`
- Archive SHA256: `evidence-pack-1/agice-demo-replay-v1.0.4.tar.gz.sha256`
- Source branch: `main`
- Source tag: `evidence-lcb-v1`

## Evidence pack 2

- Extracted bundle: `evidence-pack-2/agice-evidence-pack-2-v1.0.1`
- Archive: `evidence-pack-2/agice-evidence-pack-2-v1.0.1.tar.gz`
- Archive SHA256: `evidence-pack-2/agice-evidence-pack-2-v1.0.1.tar.gz.sha256`
- Source branch: `further-testing`
- Source commit: `231130138905a7d8d4b9d79e9068b269e0cae324`

Testing-cases reference for pack 2:
- `arXiv:2602.06176`

## Important

- Public replay is pack-local and self-contained: each pack has its own `verification/verify_offline.py`, `demo-replay.sh`, and helper scripts.
- Users do not need to checkout git commits to run packaged replay.
- Branch/tag/commit fields are provenance anchors for source-level regeneration only.

## Offline verification

For either extracted bundle root:

```bash
python verification/verify_offline.py --bundle-root . --strict
```

For archive checksum validation:

```bash
sha256sum -c <bundle>.tar.gz.sha256
```
