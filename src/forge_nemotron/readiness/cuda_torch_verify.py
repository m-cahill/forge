"""CUDA PyTorch environment verification (no model load, no training).

Used by ``scripts/verify_cuda_torch.py``. Classification helpers are unit-tested
without a GPU.
"""

from __future__ import annotations

import platform
import re
import sys
from datetime import datetime, timezone
from typing import Any

from forge_nemotron.readiness.gpu_probe import probe_torch_cuda, run_nvidia_smi

CLASSIFICATION_VALUES = frozenset(
    {
        "not_visible",
        "visible_no_torch_cuda",
        "cuda_ready_probe_only",
        "cuda_smoke_failed",
        "blocked_install_failed",
        "unknown",
    }
)


def parse_nvidia_smi_cuda_version(raw_stdout: str) -> str | None:
    """Extract ``CUDA Version: X.Y`` from default ``nvidia-smi`` header text."""
    match = re.search(r"CUDA Version:\s*([0-9.]+)", raw_stdout)
    if match is None:
        return None
    return match.group(1)


def run_nvidia_smi_full() -> dict[str, Any]:
    """Run default ``nvidia-smi`` to capture driver/CUDA header lines."""
    import shutil
    import subprocess

    binary = shutil.which("nvidia-smi")
    if binary is None:
        return {"available": False, "error": "nvidia-smi not found on PATH"}

    try:
        completed = subprocess.run(
            [binary],
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"available": False, "error": str(exc)}

    if completed.returncode != 0:
        stderr = (completed.stderr or "").strip()
        return {
            "available": False,
            "error": stderr or f"nvidia-smi exit code {completed.returncode}",
        }

    stdout = completed.stdout.strip()
    return {
        "available": True,
        "raw_stdout": stdout,
        "cuda_version_reported": parse_nvidia_smi_cuda_version(stdout),
    }


def classify_cuda_torch_environment(
    *,
    nvidia_smi_available: bool,
    torch_installed: bool,
    cuda_available: bool,
    tiny_smoke_passed: bool | None = None,
    install_failed: bool = False,
) -> str:
    """Map probe inputs to M12 environment classification."""
    if install_failed:
        return "blocked_install_failed"
    if not nvidia_smi_available:
        return "not_visible"
    if not torch_installed or not cuda_available:
        return "visible_no_torch_cuda"
    if tiny_smoke_passed is False:
        return "cuda_smoke_failed"
    if tiny_smoke_passed is True or tiny_smoke_passed is None:
        if cuda_available:
            return "cuda_ready_probe_only"
    return "unknown"


def run_tiny_cuda_smoke() -> dict[str, Any]:
    """Allocate tiny CUDA tensors and add them (no model load)."""
    try:
        import torch
    except ImportError as exc:
        return {"ran": False, "passed": False, "error": str(exc)}

    if not torch.cuda.is_available():
        return {
            "ran": False,
            "passed": False,
            "error": "torch.cuda.is_available() is false",
        }

    try:
        device = torch.device("cuda:0")
        left = torch.tensor([1.0], device=device)
        right = torch.tensor([2.0], device=device)
        result = float((left + right).item())
        return {
            "ran": True,
            "passed": result == 3.0,
            "result": result,
            "error": None,
        }
    except Exception as exc:  # noqa: BLE001 — record smoke failure for evidence
        return {"ran": True, "passed": False, "error": str(exc)}


def build_cuda_torch_report(
    *,
    environment_path: str = "active",
    run_tiny_smoke: bool = False,
    install_failed: bool = False,
) -> dict[str, Any]:
    """Assemble JSON-serializable CUDA PyTorch verification report."""
    smi_query = run_nvidia_smi()
    smi_full = run_nvidia_smi_full()
    torch_info = probe_torch_cuda()

    tiny_smoke: dict[str, Any] | None = None
    tiny_smoke_passed: bool | None = None
    if run_tiny_smoke:
        tiny_smoke = run_tiny_cuda_smoke()
        tiny_smoke_passed = tiny_smoke.get("passed") if tiny_smoke.get("ran") else False

    cuda_available = bool(torch_info.get("cuda_available"))
    nvidia_available = bool(smi_query.get("available"))

    classification = classify_cuda_torch_environment(
        nvidia_smi_available=nvidia_available,
        torch_installed=bool(torch_info.get("torch_installed")),
        cuda_available=cuda_available,
        tiny_smoke_passed=tiny_smoke_passed,
        install_failed=install_failed,
    )

    driver_version: str | None = None
    gpu_name: str | None = None
    vram_total_mib: str | None = None
    if nvidia_available:
        gpus = smi_query.get("gpus") or []
        if gpus:
            first = gpus[0]
            gpu_name = first.get("gpu_name")
            vram_total_mib = first.get("vram_total")
            driver_version = first.get("driver_version")

    errors: list[str] = []
    if smi_query.get("error"):
        errors.append(str(smi_query["error"]))
    if torch_info.get("error"):
        errors.append(str(torch_info["error"]))
    if tiny_smoke and tiny_smoke.get("error"):
        errors.append(str(tiny_smoke["error"]))

    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "host_os": f"{platform.system()} {platform.release()} ({platform.machine()})",
        "python_executable": sys.executable,
        "python_version": platform.python_version(),
        "environment_path": environment_path,
        "pytorch_version": torch_info.get("torch_version"),
        "pytorch_cuda_build_version": _torch_cuda_build_version(),
        "torch_cuda_is_available": cuda_available,
        "cuda_device_count": torch_info.get("device_count"),
        "gpu_name": gpu_name or torch_info.get("device_0_name"),
        "vram_total_mib": vram_total_mib,
        "driver_version": driver_version,
        "cuda_version_nvidia_smi": smi_full.get("cuda_version_reported"),
        "tiny_cuda_smoke": tiny_smoke,
        "errors": errors,
        "warnings": [],
        "classification": classification,
        "notes": (
            "Environment probe only; no model load, training, inference, adapters, "
            "or Kaggle submission."
        ),
    }


def _torch_cuda_build_version() -> str | None:
    try:
        import torch
    except ImportError:
        return None
    cuda_build = getattr(torch.version, "cuda", None)
    return str(cuda_build) if cuda_build else None
