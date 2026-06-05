"""Safe local GPU environment probes (no model load, no training).

Used by ``scripts/probe_local_5090.py``. Parsing helpers are unit-tested without a GPU.
"""

from __future__ import annotations

import platform
import shutil
import subprocess
from datetime import datetime, timezone
from typing import Any


def parse_nvidia_smi_csv_line(line: str) -> dict[str, str] | None:
    """Parse one ``nvidia-smi --query-gpu`` CSV line (no header).

    Expected fields: name, memory.total, driver_version.
    Returns None if the line is empty or does not have three fields.
    """
    stripped = line.strip()
    if not stripped:
        return None
    parts = [part.strip() for part in stripped.split(",")]
    if len(parts) < 3:
        return None
    return {
        "gpu_name": parts[0],
        "vram_total": parts[1],
        "driver_version": parts[2],
    }


def run_nvidia_smi() -> dict[str, Any]:
    """Run ``nvidia-smi`` query if the binary exists. Does not load models."""
    binary = shutil.which("nvidia-smi")
    if binary is None:
        return {"available": False, "error": "nvidia-smi not found on PATH"}

    cmd = [
        binary,
        "--query-gpu=name,memory.total,driver_version",
        "--format=csv,noheader,nounits",
    ]
    try:
        completed = subprocess.run(
            cmd,
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

    gpus: list[dict[str, str]] = []
    for line in completed.stdout.splitlines():
        parsed = parse_nvidia_smi_csv_line(line)
        if parsed is not None:
            gpus.append(parsed)

    return {"available": True, "gpus": gpus, "raw_stdout": completed.stdout.strip()}


def probe_torch_cuda() -> dict[str, Any]:
    """Import torch if installed and report CUDA availability (no model load)."""
    try:
        import torch
    except ImportError:
        return {"torch_installed": False, "error": "torch not installed"}

    cuda_available = bool(torch.cuda.is_available())
    result: dict[str, Any] = {
        "torch_installed": True,
        "torch_version": torch.__version__,
        "cuda_available": cuda_available,
    }
    if cuda_available and torch.cuda.device_count() > 0:
        result["device_count"] = torch.cuda.device_count()
        result["device_0_name"] = torch.cuda.get_device_name(0)
        props = torch.cuda.get_device_properties(0)
        result["device_0_total_memory_bytes"] = getattr(props, "total_memory", None)
    return result


def build_probe_report(*, machine: str = "local_5090") -> dict[str, Any]:
    """Assemble a JSON-serializable probe report without training or inference."""
    return {
        "probe_date_utc": datetime.now(timezone.utc).isoformat(),
        "machine": machine,
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "python": platform.python_version(),
        },
        "nvidia_smi": run_nvidia_smi(),
        "torch": probe_torch_cuda(),
        "notes": "Environment probe only; no model load, training, or inference.",
    }
