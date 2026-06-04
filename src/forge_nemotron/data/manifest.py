"""Dataset manifest builder for synthetic JSONL outputs."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from forge_nemotron.artifacts.hashing import sha256_file


def build_dataset_manifest(
    *,
    dataset_id: str,
    dataset_path: Path,
    seed: int,
    example_count: int,
    category_counts: dict[str, int],
    generator_versions: dict[str, str],
    solver_versions: dict[str, str],
    verified_count: int,
    rejected_count: int,
    created_at_utc: str | None = None,
    holdout_policy: str = "not_for_training_if_marked_holdout",
    notes: str = "",
) -> dict[str, Any]:
    """Build a dataset manifest with content hash and counts."""
    timestamp = created_at_utc or datetime.now(timezone.utc).isoformat()
    return {
        "dataset_id": dataset_id,
        "created_at_utc": timestamp,
        "generator_versions": dict(sorted(generator_versions.items())),
        "solver_versions": dict(sorted(solver_versions.items())),
        "seed": seed,
        "example_count": example_count,
        "category_counts": dict(sorted(category_counts.items())),
        "dataset_path": str(dataset_path),
        "dataset_sha256": sha256_file(dataset_path),
        "verified_count": verified_count,
        "rejected_count": rejected_count,
        "holdout_policy": holdout_policy,
        "notes": notes,
    }
