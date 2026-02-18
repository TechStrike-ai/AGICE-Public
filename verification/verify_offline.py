#!/usr/bin/env python3
"""Offline verifier for AGICE Zenodo evidence bundles.

Checks:
1) RSA signature verification of checksums/SHA256SUMS.txt
2) SHA-256 verification of all files listed in SHA256SUMS.txt
3) Per-bundle hash-chain + integrity cross-check for events.jsonl/manifests
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def hash_event(prev_hash: str, event_obj: dict) -> str:
    payload = json.dumps(
        event_obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    inner = hashlib.sha256(payload).hexdigest()
    return hashlib.sha256((prev_hash + ":" + inner).encode("utf-8")).hexdigest()


def verify_signature(root: str) -> None:
    checksums = os.path.join(root, "checksums", "SHA256SUMS.txt")
    signature = os.path.join(root, "checksums", "SHA256SUMS.sig")
    pubkey = os.path.join(root, "checksums", "SIGNING-PUBLIC-KEY.pem")
    subprocess.run(
        ["openssl", "dgst", "-sha256", "-verify", pubkey, "-signature", signature, checksums],
        check=True,
    )


def load_checksum_entries(checksums_path: str) -> tuple[dict[str, str], int]:
    entries: dict[str, str] = {}
    malformed = 0
    with open(checksums_path, "r", encoding="utf-8") as f:
        for line_no, raw in enumerate(f, 1):
            line = raw.rstrip("\n")
            if not line.strip():
                continue
            parts = line.split("  ", 1)
            if len(parts) != 2:
                print(f"MALFORMED CHECKSUM ENTRY line {line_no}: {line}")
                malformed += 1
                continue
            digest, rel = parts[0].strip(), parts[1].strip()
            if rel.startswith("./"):
                rel = rel[2:]
            if len(digest) != 64:
                print(f"INVALID DIGEST line {line_no}: {digest}")
                malformed += 1
                continue
            entries[rel] = digest
    return entries, malformed


def verify_checksums(root: str) -> tuple[int, int, set[str], int]:
    checksums = os.path.join(root, "checksums", "SHA256SUMS.txt")
    entries, malformed = load_checksum_entries(checksums)
    total = 0
    mismatches = 0
    hashed_files = set(entries.keys())
    for rel, expected in entries.items():
        path = os.path.join(root, rel)
        total += 1
        if not os.path.exists(path):
            print(f"MISSING: {rel}")
            mismatches += 1
            continue
        actual = sha256_file(path)
        if actual != expected:
            print(f"MISMATCH: {rel}")
            mismatches += 1
    return total, mismatches, hashed_files, malformed


def collect_actual_files(root: str) -> set[str]:
    excluded = {
        "checksums/SHA256SUMS.sig",
        "checksums/SHA256SUMS.txt",
    }
    actual: set[str] = set()
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            abs_path = os.path.join(dirpath, name)
            rel = os.path.relpath(abs_path, root).replace(os.sep, "/")
            if rel in excluded:
                continue
            actual.add(rel)
    return actual


def verify_strict_coverage(root: str, hashed_files: set[str]) -> tuple[int, int]:
    actual_files = collect_actual_files(root)
    extra_unhashed = sorted(actual_files - hashed_files)
    missing_referenced = sorted(hashed_files - actual_files)
    if extra_unhashed:
        print("UNHASHED FILES PRESENT:")
        for rel in extra_unhashed:
            print(f"  + {rel}")
    if missing_referenced:
        print("HASHED FILES MISSING FROM PACKAGE:")
        for rel in missing_referenced:
            print(f"  - {rel}")
    return len(extra_unhashed), len(missing_referenced)


def verify_hash_chain(events_path: str) -> dict:
    prev_hash = "0" * 64
    count = 0
    with open(events_path, "r", encoding="utf-8") as f:
        for line_no, raw in enumerate(f, 1):
            raw = raw.strip()
            if not raw:
                continue
            event = json.loads(raw)
            recorded_prev = event.get("prev_hash")
            if recorded_prev != prev_hash:
                return {"valid": False, "count": count, "error": f"prev_hash mismatch at line {line_no}"}
            stored_hash = event.pop("event_hash", "")
            computed = hash_event(prev_hash, event)
            if computed != stored_hash:
                return {"valid": False, "count": count, "error": f"event_hash mismatch at line {line_no}"}
            prev_hash = stored_hash
            count += 1
    return {"valid": True, "count": count, "tip": prev_hash}


def iter_bundle_dirs(root: str):
    bundles_root = os.path.join(root, "bundles")
    for dirpath, _dirnames, filenames in os.walk(bundles_root):
        if "bundle_manifest.json" in filenames:
            yield dirpath


def verify_bundles(root: str) -> tuple[int, int]:
    total = 0
    passed = 0
    for bundle_dir in iter_bundle_dirs(root):
        total += 1
        events_path = os.path.join(bundle_dir, "events.jsonl")
        manifest_path = os.path.join(bundle_dir, "bundle_manifest.json")
        integrity_path = os.path.join(bundle_dir, "integrity.json")
        try:
            chain = verify_hash_chain(events_path)
            if not chain.get("valid", False):
                print(f"FAIL {bundle_dir}: {chain.get('error')}")
                continue
            with open(manifest_path, "r", encoding="utf-8") as f:
                manifest = json.load(f)
            with open(integrity_path, "r", encoding="utf-8") as f:
                integrity = json.load(f)
            expected_count = manifest.get("integrity", {}).get("events_count")
            expected_tip = manifest.get("integrity", {}).get("events_hash_chain_tip")
            files = integrity.get("files", {})
            events_file_ok = files.get("events.jsonl") == sha256_file(events_path)
            manifest_file_ok = files.get("bundle_manifest.json") == sha256_file(manifest_path)
            count_ok = (expected_count == chain.get("count")) if expected_count is not None else True
            tip_ok = (expected_tip == chain.get("tip")) if expected_tip else True
            if events_file_ok and manifest_file_ok and count_ok and tip_ok:
                passed += 1
            else:
                print(f"FAIL {bundle_dir}: integrity mismatch")
        except Exception as exc:
            print(f"FAIL {bundle_dir}: {exc}")
    return total, passed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bundle_root_positional", nargs="?", default=None, help="Optional bundle root positional path.")
    parser.add_argument("--bundle-root", default=".")
    parser.add_argument("--strict", action="store_true", help="Fail if file coverage differs from SHA256SUMS inventory.")
    args = parser.parse_args()
    root_arg = args.bundle_root_positional if args.bundle_root_positional is not None else args.bundle_root
    root = os.path.abspath(root_arg)
    verify_signature(root)
    total_files, mismatch_files, hashed_files, malformed_lines = verify_checksums(root)
    strict_extra = 0
    strict_missing = 0
    if args.strict:
        strict_extra, strict_missing = verify_strict_coverage(root, hashed_files)
    total_bundles, passed_bundles = verify_bundles(root)

    print("=" * 60)
    print(f"Files checked: {total_files}, file mismatches: {mismatch_files}, malformed checksum lines: {malformed_lines}")
    if args.strict:
        print(f"Strict coverage: unhashed extras={strict_extra}, missing referenced files={strict_missing}")
    print(f"Bundles checked: {total_bundles}, bundles passed: {passed_bundles}")
    all_ok = (
        mismatch_files == 0
        and malformed_lines == 0
        and total_bundles == passed_bundles
        and (not args.strict or (strict_extra == 0 and strict_missing == 0))
    )
    print("VERDICT:", "PASS" if all_ok else "FAIL")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
