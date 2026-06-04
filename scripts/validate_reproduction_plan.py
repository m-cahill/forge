#!/usr/bin/env python3
"""CLI wrapper for reproduction plan manifest validation.

Usage:
    python scripts/validate_reproduction_plan.py path/to/plan.json
    python scripts/validate_reproduction_plan.py --json path/to/plan.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from forge_nemotron.baselines.reproduction_plan import (
    load_reproduction_plan,
    validate_reproduction_plan,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate FORGE reproduction plan manifest JSON")
    parser.add_argument("plan", type=Path, help="Path to reproduction plan JSON")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print validation result as JSON",
    )
    args = parser.parse_args(argv)

    path = args.plan
    if not path.is_file():
        message = f"plan not found: {path}"
        if args.json:
            print(json.dumps({"valid": False, "errors": [message]}))
        else:
            print(message, file=sys.stderr)
        return 1

    try:
        plan = load_reproduction_plan(path)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        message = f"failed to load plan: {exc}"
        if args.json:
            print(json.dumps({"valid": False, "errors": [message]}))
        else:
            print(message, file=sys.stderr)
        return 1

    errors = validate_reproduction_plan(plan)
    valid = not errors

    if args.json:
        print(
            json.dumps(
                {
                    "valid": valid,
                    "errors": errors,
                    "plan_id": plan.get("plan_id"),
                    "training_authorized": plan.get("training_authorized"),
                },
                indent=2,
            )
        )
    elif valid:
        print(f"OK: {path} (plan_id={plan.get('plan_id')})")
    else:
        print(f"INVALID: {path}", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)

    return 0 if valid else 1


if __name__ == "__main__":
    sys.exit(main())
