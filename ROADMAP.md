# AGICE Public Release Roadmap

This repository follows a staged public release:
publish concept + evidence first, then ship replay/verifiers and demos once hardened.

## v0 (now): Public home base + evidence
- [x] Public repo skeleton (README, docs, roadmap, citation)
- [x] Evidence pack DOI published: https://doi.org/10.5281/zenodo.18608886
- [ ] Preprint v1 live (arXiv): link here
- [ ] Papers with Code + HF paper pages: link here

## v0.1: Replay verifier (trust without hype)
Goal: anyone can validate an evidence bundle locally.

- [ ] CLI: `agice replay --evidence <bundle>`
- [ ] Verify: schema + hash chain integrity + bundle file hashes
- [ ] Output: `verification_report.json` (deterministic summary)
- [ ] CI: GitHub Actions runs replay on a tiny sample bundle
- [ ] Tag release `v0.1.0` + archive to Zenodo

## v0.2: Lite evaluation harness (reproduce in 1 command)
Goal: run a small suite and emit evidence bundles.

- [ ] CLI: `agice eval --suite lite`
- [ ] Pinned configs + seeds + minimal runtime
- [ ] Output: `results.json` + `evidence_bundle/`
- [ ] Tag release `v0.2.0`

## v0.3: Demo (interactive proof)
- [ ] Hugging Face Space minimal demo
- [ ] Short hero demo video + deep technical demo
- [ ] “Show HN” launch kit (paper + repo + demo)

## v1.0: Stabilization
- [ ] Stable plugin interface for verifiers/arbitration/evidence
- [ ] Expanded benchmark suite + ablations
- [ ] Documentation polish + governance/rollback examples
