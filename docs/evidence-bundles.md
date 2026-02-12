# Evidence Bundles

The canonical evidence pack is published on Zenodo:
https://doi.org/10.5281/zenodo.18608886

Typical bundle contents:
- `events.jsonl` — trajectory log (hash‑chained)
- `bundle_manifest.json` — run metadata + summaries
- `replay.json` — replay parameters (where applicable)
- `integrity.json` — file hash metadata (where applicable)
- reports/configs for interpretation

Validation:
- Use the validator included in the Zenodo pack (instructions are inside the pack).
