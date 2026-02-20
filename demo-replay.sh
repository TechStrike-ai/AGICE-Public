#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 "$ROOT_DIR/verification/verify_offline.py" --bundle-root "$ROOT_DIR" --strict
python3 "$ROOT_DIR/verification/replay_summary.py" --bundle-root "$ROOT_DIR"

echo "Demo replay finished: integrity PASS + summary rendered."
