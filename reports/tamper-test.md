# Tamper Test (Intentional Falsification Attempt)

Generated: `2026-02-16T19:23:05.698596+00:00`

## Procedure

1. Copy the bundle to a temporary workspace.
2. Modify one byte in `artifacts/zenodo/agice-demo-replay-v1/bundles/20260216_150059/A3/hard2_complex_transform/events.jsonl`.
3. Run strict verifier:

```bash
python -B verification/verify_offline.py --bundle-root . --strict
```

## Result (strict verifier)

- Exit code: `1`
- Expected: non-zero (`FAIL`)

### Output excerpt

```text
Verified OK
MISMATCH: bundles/20260216_150059/A3/hard2_complex_transform/events.jsonl
FAIL /tmp/agice_tamper_ahhaq1_c/bundle/bundles/20260216_150059/A3/hard2_complex_transform: event_hash mismatch at line 1
============================================================
Files checked: 220, file mismatches: 1, malformed checksum lines: 0
Strict coverage: unhashed extras=0, missing referenced files=0
Bundles checked: 39, bundles passed: 38
VERDICT: FAIL
```

## Hash-chain specific check

- `verify_hash_chain` result for tampered `events.jsonl`:

```json
{
  "valid": false,
  "count": 0,
  "error": "event_hash mismatch at line 1"
}
```

## Conclusion

Tampering is detected by checksum mismatch and hash-chain validation failure.
