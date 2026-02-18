#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

echo "[1/3] Running strict offline verification..."
python3 "$ROOT_DIR/verification/verify_offline.py" --bundle-root "$ROOT_DIR" --strict

echo
echo "[2/3] Showing native rollback event trace..."
python3 - <<'PY'
import json
from pathlib import Path

bundle = Path("bundles/20260216_150059/A3/hard2_complex_transform/events.jsonl")
rows = [json.loads(line) for line in bundle.read_text(encoding="utf-8").splitlines() if line.strip()]

rollback = next((r for r in rows if r.get("type") == "rollback_event"), None)
if rollback is None:
    raise SystemExit("No rollback_event found in demo bundle.")

print(f"bundle={bundle}")
print(f"rollback_event_id={rollback.get('event_id')}")
print(f"trigger={rollback.get('trigger_id')}")
print(f"action={rollback.get('action')}")
print(f"from_projection={rollback.get('from_projection')}")
print(f"to_projection={rollback.get('to_projection')}")
print(f"policy_sha256={rollback.get('policy_sha256')}")
PY

echo
echo "[3/3] Demo replay completed."
