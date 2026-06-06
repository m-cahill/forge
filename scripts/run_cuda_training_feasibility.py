#!/usr/bin/env python3
"""Run tiny CUDA training feasibility dry run (synthetic toy MLP only).

Usage::

    .venv_cuda\\Scripts\\python scripts/run_cuda_training_feasibility.py \\
      --out docs/milestones/M13/evidence/local_training_feasibility/feasibility_run.json \\
      --steps 3 --device cuda

Does not load Nemotron, baseline checkpoints, or Hugging Face models.
Does not save model weights, adapters, or checkpoints.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from forge_nemotron.readiness.cuda_training_feasibility import build_feasibility_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Tiny CUDA training feasibility dry run (toy MLP, no model load)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        required=True,
        help="Path to write JSON feasibility report",
    )
    parser.add_argument(
        "--steps",
        type=int,
        default=3,
        help="Number of forward/backward/optimizer steps (default: 3)",
    )
    parser.add_argument(
        "--device",
        choices=("cuda", "cpu"),
        default="cuda",
        help="Target device (default: cuda)",
    )
    parser.add_argument(
        "--cpu-ok",
        action="store_true",
        help="Allow CPU fallback when CUDA unavailable (local debug only)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=0,
        help="Random seed for synthetic tensors (default: 0)",
    )
    parser.add_argument(
        "--environment-path",
        default="active",
        help="Label for the Python environment path (default: active)",
    )
    args = parser.parse_args(argv)

    if args.steps < 1:
        parser.error("--steps must be >= 1")

    report = build_feasibility_report(
        device=args.device,
        steps=args.steps,
        seed=args.seed,
        environment_path=args.environment_path,
        cpu_ok=args.cpu_ok,
    )

    classification = report["result"]["classification"]
    success = report["result"]["success"]
    print(f"Device requested: {args.device}")
    print(f"Device used: {report['cuda'].get('device_used')}")
    print(f"Steps: {args.steps}")
    print(f"Success: {success}")
    print(f"Classification: {classification}")
    if report.get("telemetry", {}).get("final_loss") is not None:
        print(f"Final loss: {report['telemetry']['final_loss']}")

    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(text, encoding="utf-8")
    print(f"Wrote report to {args.out}")

    if args.device == "cuda" and classification == "cuda_unavailable":
        return 2
    if not success:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
