#!/usr/bin/env python3
"""Verify CUDA-enabled PyTorch in the active Python environment (no model load).

Usage::

    python scripts/verify_cuda_torch.py
    python scripts/verify_cuda_torch.py --tiny-smoke
    python scripts/verify_cuda_torch.py --out docs/milestones/M12/evidence/local_cuda_env/cuda_torch_probe.json --tiny-smoke

Safe on CPU-only machines: reports CUDA unavailable without crashing.
Does not load models, train, or infer.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from forge_nemotron.readiness.cuda_torch_verify import build_cuda_torch_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Verify CUDA PyTorch environment (no training or inference)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        help="Optional path to write JSON verification report",
    )
    parser.add_argument(
        "--environment-path",
        default="active",
        help="Label for the Python environment path (default: active)",
    )
    parser.add_argument(
        "--tiny-smoke",
        action="store_true",
        help="Run tiny CUDA tensor allocation smoke when CUDA is available",
    )
    parser.add_argument(
        "--install-failed",
        action="store_true",
        help="Mark report classification as blocked_install_failed (evidence only)",
    )
    args = parser.parse_args(argv)

    report = build_cuda_torch_report(
        environment_path=args.environment_path,
        run_tiny_smoke=args.tiny_smoke,
        install_failed=args.install_failed,
    )

    print(f"Python: {report['python_version']} ({report['python_executable']})")
    print(f"PyTorch: {report.get('pytorch_version')}")
    print(f"torch.version.cuda: {report.get('pytorch_cuda_build_version')}")
    print(f"torch.cuda.is_available(): {report['torch_cuda_is_available']}")
    if report.get("cuda_device_count") is not None:
        print(f"CUDA device count: {report['cuda_device_count']}")
    if report.get("gpu_name"):
        print(f"GPU: {report['gpu_name']}")
    if report.get("vram_total_mib"):
        print(f"VRAM total (MiB): {report['vram_total_mib']}")
    print(f"Classification: {report['classification']}")

    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
        print(f"Wrote report to {args.out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
