#!/usr/bin/env python3
"""CLI wrapper for adapter candidate manifest validation.

Usage:
    python scripts/validate_candidate_manifest.py path/to/manifest.json
    python scripts/validate_candidate_manifest.py --json path/to/manifest.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from forge_nemotron.adapters.candidate_manifest import (
    load_candidate_manifest,
    validate_candidate_manifest,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate FORGE adapter candidate manifest JSON")
    parser.add_argument("manifest", type=Path, help="Path to candidate manifest JSON")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print validation result as JSON",
    )
    args = parser.parse_args(argv)

    path = args.manifest
    if not path.is_file():
        message = f"manifest not found: {path}"
        if args.json:
            print(json.dumps({"valid": False, "errors": [message]}))
        else:
            print(message, file=sys.stderr)
        return 1

    try:
        manifest = load_candidate_manifest(path)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        message = f"failed to load manifest: {exc}"
        if args.json:
            print(json.dumps({"valid": False, "errors": [message]}))
        else:
            print(message, file=sys.stderr)
        return 1

    errors = validate_candidate_manifest(manifest)
    valid = not errors

    if args.json:
        print(
            json.dumps(
                {
                    "valid": valid,
                    "errors": errors,
                    "candidate_id": manifest.get("candidate_id"),
                    "status": manifest.get("status"),
                },
                indent=2,
            )
        )
    elif valid:
        print(f"OK: {path} (candidate_id={manifest.get('candidate_id')})")
    else:
        print(f"INVALID: {path}", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)

    return 0 if valid else 1


if __name__ == "__main__":
    sys.exit(main())
