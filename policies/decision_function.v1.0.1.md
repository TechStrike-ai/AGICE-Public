# AGICE Decision Function (v1.0.1)

This file defines the arbitration and rollback decision logic used for governance reporting in this package.

## 1) Eligibility

A candidate is **eligible for state advancement** only if all hard constraints pass.

Formally:
- Let `H(c)` be hard-constraint pass/fail for candidate `c`.
- Candidate is eligible iff `H(c)=PASS`.

If `H(c)=FAIL`, candidate can be logged and analyzed but cannot replace the active incumbent.

## 2) Ranking among eligible candidates

Eligible candidates are ranked by:
1. Composite soft loss / score (lower loss preferred)
2. Tie-breakers in order:
   - fewer hard warnings
   - smaller patch size
   - lower runtime
   - deterministic lexical fallback

## 3) Incumbent update rule

Incumbent is updated only when:
- candidate is eligible (`H(c)=PASS`), and
- confidence envelope constraints pass:
  - `confidence(c) >= min_to_advance`
  - `confidence(c) - confidence(incumbent) >= min_margin_over_incumbent`

## 4) Automatic rollback rule

If any rollback trigger fires, active state reverts to `last_known_good`:
- hard regression (`incumbent pass` -> `candidate fail`)
- confidence collapse below policy threshold
- rolling-window regression
- replay flakiness / non-determinism detected

Rollback is followed by:
- cool-down round freeze
- strictness increase
- escalation when rollback budget is exceeded

## 5) Evidence linkage

Every decision is expected to be traceable via:
- `events.jsonl` hash chain
- `integrity.json` file hashes
- `bundle_manifest.json` integrity summary
- signed `checksums/SHA256SUMS.txt` + `SHA256SUMS.sig`
