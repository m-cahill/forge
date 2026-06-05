#!/usr/bin/env python3
"""Safe local RTX 5090 / CUDA environment probe (no model load).

Requires owner authorization before running on hardware::

    M08_LOCAL_5090_PROBE_AUTHORIZED = yes

Usage::

    python scripts/probe_local_5090.py
    python scripts/probe_local_5090.py --out /tmp/forge_m08_local_5090_probe.json

Safe on CPU-only machines: reports missing GPU tools without failing.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from forge_nemotron.readiness.gpu_probe import build_probe_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Probe local GPU/CUDA environment (no training or inference)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        help="Optional path to write JSON probe report",
    )
    parser.add_argument(
        "--machine",
        default="local_5090",
        help="Machine label for the report (default: local_5090)",
    )
    args = parser.parse_args(argv)

    report = build_probe_report(machine=args.machine)
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    print(text, end="")

    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
