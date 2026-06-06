"""CUDA training feasibility dry-run helpers (toy MLP, no model load).

Used by ``scripts/run_cuda_training_feasibility.py``. Pure helpers are unit-tested
without a GPU.
"""

from __future__ import annotations

import platform
import sys
import time
import traceback
from datetime import datetime, timezone
from typing import Any

FEASIBILITY_CLASSIFICATION_VALUES = frozenset(
    {
        "cuda_training_feasibility_pass",
        "cuda_training_feasibility_failed",
        "cuda_unavailable",
        "not_run",
        "blocked",
    }
)

DEFAULT_INPUT_DIM = 64
DEFAULT_HIDDEN_DIM = 128
DEFAULT_OUTPUT_DIM = 32
DEFAULT_BATCH_SIZE = 32
DEFAULT_LEARNING_RATE = 1e-3


def classify_feasibility_result(
    *,
    success: bool,
    cuda_available: bool,
    device_requested: str,
    blocked: bool = False,
) -> str:
    """Map dry-run outcome to M13 classification."""
    if blocked:
        return "blocked"
    if device_requested == "cuda" and not cuda_available:
        return "cuda_unavailable"
    if success:
        return "cuda_training_feasibility_pass"
    return "cuda_training_feasibility_failed"


def snapshot_cuda_memory(device: str) -> dict[str, int | None]:
    """Return allocated/reserved CUDA memory in bytes, or nulls on CPU."""
    if device != "cuda":
        return {
            "memory_allocated_bytes": None,
            "memory_reserved_bytes": None,
        }
    try:
        import torch
    except ImportError:
        return {
            "memory_allocated_bytes": None,
            "memory_reserved_bytes": None,
        }
    if not torch.cuda.is_available():
        return {
            "memory_allocated_bytes": None,
            "memory_reserved_bytes": None,
        }
    return {
        "memory_allocated_bytes": int(torch.cuda.memory_allocated()),
        "memory_reserved_bytes": int(torch.cuda.memory_reserved()),
    }


def snapshot_cuda_peak_memory(device: str) -> dict[str, int | None]:
    """Return peak allocated/reserved CUDA memory in bytes."""
    if device != "cuda":
        return {
            "peak_memory_allocated_bytes": None,
            "peak_memory_reserved_bytes": None,
        }
    try:
        import torch
    except ImportError:
        return {
            "peak_memory_allocated_bytes": None,
            "peak_memory_reserved_bytes": None,
        }
    if not torch.cuda.is_available():
        return {
            "peak_memory_allocated_bytes": None,
            "peak_memory_reserved_bytes": None,
        }
    return {
        "peak_memory_allocated_bytes": int(torch.cuda.max_memory_allocated()),
        "peak_memory_reserved_bytes": int(torch.cuda.max_memory_reserved()),
    }


def build_tiny_mlp(
    *,
    input_dim: int = DEFAULT_INPUT_DIM,
    hidden_dim: int = DEFAULT_HIDDEN_DIM,
    output_dim: int = DEFAULT_OUTPUT_DIM,
):
    """Construct a tiny FORGE-owned MLP (no external weights)."""
    import torch.nn as nn

    return nn.Sequential(
        nn.Linear(input_dim, hidden_dim),
        nn.ReLU(),
        nn.Linear(hidden_dim, output_dim),
    )


def run_training_feasibility_loop(
    *,
    device: str,
    steps: int,
    seed: int,
    input_dim: int = DEFAULT_INPUT_DIM,
    hidden_dim: int = DEFAULT_HIDDEN_DIM,
    output_dim: int = DEFAULT_OUTPUT_DIM,
    batch_size: int = DEFAULT_BATCH_SIZE,
    learning_rate: float = DEFAULT_LEARNING_RATE,
) -> dict[str, Any]:
    """Run tiny forward/backward/optimizer loop; return step telemetry."""
    import torch
    import torch.nn as nn

    torch.manual_seed(seed)
    if device == "cuda" and torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

    model = build_tiny_mlp(
        input_dim=input_dim,
        hidden_dim=hidden_dim,
        output_dim=output_dim,
    ).to(device)
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
    criterion = nn.MSELoss()

    step_records: list[dict[str, Any]] = []
    for step_index in range(steps):
        inputs = torch.randn(batch_size, input_dim, device=device)
        targets = torch.randn(batch_size, output_dim, device=device)

        start = time.perf_counter()
        optimizer.zero_grad(set_to_none=True)
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        elapsed_ms = (time.perf_counter() - start) * 1000.0

        step_records.append(
            {
                "step": step_index + 1,
                "loss": float(loss.item()),
                "elapsed_ms": round(elapsed_ms, 3),
            }
        )

    return {
        "steps_completed": steps,
        "step_records": step_records,
        "final_loss": step_records[-1]["loss"] if step_records else None,
    }


def build_feasibility_report(
    *,
    device: str,
    steps: int,
    seed: int,
    environment_path: str = "active",
    cpu_ok: bool = False,
    input_dim: int = DEFAULT_INPUT_DIM,
    hidden_dim: int = DEFAULT_HIDDEN_DIM,
    output_dim: int = DEFAULT_OUTPUT_DIM,
    batch_size: int = DEFAULT_BATCH_SIZE,
    learning_rate: float = DEFAULT_LEARNING_RATE,
) -> dict[str, Any]:
    """Assemble full JSON-serializable feasibility report."""
    command_parts = [
        "scripts/run_cuda_training_feasibility.py",
        f"--device {device}",
        f"--steps {steps}",
        f"--seed {seed}",
    ]
    if cpu_ok:
        command_parts.append("--cpu-ok")

    report: dict[str, Any] = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "command": " ".join(command_parts),
        "authorization": {
            "M13_LOCAL_TRAINING_FEASIBILITY_AUTHORIZED": "yes",
            "M13_FULL_BASELINE_TRAINING_AUTHORIZED": "no",
            "M13_INFERENCE_AUTHORIZED": "no",
            "KAGGLE_SUBMISSION_AUTHORIZED": "no",
        },
        "environment": {
            "host_os": f"{platform.system()} {platform.release()} ({platform.machine()})",
            "python_version": platform.python_version(),
            "python_executable": sys.executable,
            "environment_path": environment_path,
        },
        "workload": {
            "kind": "tiny_mlp_synthetic",
            "input_dim": input_dim,
            "hidden_dim": hidden_dim,
            "output_dim": output_dim,
            "batch_size": batch_size,
            "learning_rate": learning_rate,
            "optimizer": "SGD",
            "dtype": "float32",
            "steps_requested": steps,
            "seed": seed,
            "uses_competition_data": False,
            "uses_baseline_code": False,
            "writes_model_artifacts": False,
        },
        "cuda": {},
        "memory": {},
        "telemetry": {},
        "result": {
            "success": False,
            "classification": "not_run",
            "error": None,
            "traceback": None,
        },
        "non_claims": [
            "not_baseline_training",
            "not_adapter_training",
            "not_inference",
            "not_model_loading",
            "not_kaggle_submission",
            "not_training_readiness",
        ],
        "notes": (
            "Tiny toy CUDA training-like feasibility loop only; not real model training, "
            "baseline training, or adapter training."
        ),
    }

    try:
        import torch
    except ImportError as exc:
        report["result"] = {
            "success": False,
            "classification": "cuda_training_feasibility_failed",
            "error": f"torch not installed: {exc}",
            "traceback": None,
        }
        return report

    cuda_available = bool(torch.cuda.is_available())
    report["cuda"] = {
        "pytorch_version": torch.__version__,
        "pytorch_cuda_build_version": _torch_cuda_build_version(),
        "torch_cuda_is_available": cuda_available,
        "device_requested": device,
        "device_used": None,
        "cuda_device_count": torch.cuda.device_count() if cuda_available else 0,
        "gpu_name": torch.cuda.get_device_name(0) if cuda_available else None,
        "vram_total_mib": _vram_total_mib() if cuda_available else None,
        "cpu_ok": cpu_ok,
    }

    if device == "cuda" and not cuda_available and not cpu_ok:
        report["result"] = {
            "success": False,
            "classification": "cuda_unavailable",
            "error": "CUDA requested but torch.cuda.is_available() is false; use --cpu-ok for CPU debug",
            "traceback": None,
        }
        return report

    device_used = device
    if device == "cuda" and not cuda_available and cpu_ok:
        device_used = "cpu"

    report["cuda"]["device_used"] = device_used

    memory_before = snapshot_cuda_memory(device_used)
    report["memory"]["before"] = memory_before

    if device_used == "cuda":
        torch.cuda.reset_peak_memory_stats()

    try:
        loop_result = run_training_feasibility_loop(
            device=device_used,
            steps=steps,
            seed=seed,
            input_dim=input_dim,
            hidden_dim=hidden_dim,
            output_dim=output_dim,
            batch_size=batch_size,
            learning_rate=learning_rate,
        )
        memory_after = snapshot_cuda_memory(device_used)
        peak_memory = snapshot_cuda_peak_memory(device_used)
        report["memory"]["after"] = memory_after
        report["memory"]["peak"] = peak_memory
        report["telemetry"] = loop_result
        classification = classify_feasibility_result(
            success=True,
            cuda_available=cuda_available,
            device_requested=device,
        )
        if device_used == "cpu" and device == "cuda":
            classification = "cuda_unavailable"
        report["result"] = {
            "success": True,
            "classification": classification,
            "error": None,
            "traceback": None,
        }
    except Exception as exc:  # noqa: BLE001 — record failure for evidence
        memory_after = snapshot_cuda_memory(device_used)
        peak_memory = snapshot_cuda_peak_memory(device_used)
        report["memory"]["after"] = memory_after
        report["memory"]["peak"] = peak_memory
        report["telemetry"] = {"steps_completed": 0, "step_records": [], "final_loss": None}
        report["result"] = {
            "success": False,
            "classification": classify_feasibility_result(
                success=False,
                cuda_available=cuda_available,
                device_requested=device,
            ),
            "error": str(exc),
            "traceback": traceback.format_exc(),
        }

    return report


def _torch_cuda_build_version() -> str | None:
    try:
        import torch
    except ImportError:
        return None
    cuda_build = getattr(torch.version, "cuda", None)
    return str(cuda_build) if cuda_build else None


def _vram_total_mib() -> int | None:
    try:
        import torch
    except ImportError:
        return None
    if not torch.cuda.is_available():
        return None
    props = torch.cuda.get_device_properties(0)
    return int(props.total_memory / (1024 * 1024))
