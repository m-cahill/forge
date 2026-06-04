"""Run manifest builder for local evaluation and validation runs."""

from __future__ import annotations

from typing import Any


def build_run_manifest(
    *,
    run_id: str,
    created_at_utc: str,
    git_commit: str,
    branch: str,
    run_type: str,
    candidate_id: str,
    examples_path: str,
    predictions_path: str,
    examples_sha256: str,
    predictions_sha256: str,
    metric_version: str,
    local_score: float,
    local_score_by_category: dict[str, float],
    artifact_paths: list[str],
    notes: str = "",
    git_warning: str | None = None,
) -> dict[str, Any]:
    """Build a run manifest dictionary with deterministic score fields."""
    manifest: dict[str, Any] = {
        "run_id": run_id,
        "created_at_utc": created_at_utc,
        "git_commit": git_commit,
        "branch": branch,
        "run_type": run_type,
        "candidate_id": candidate_id,
        "examples_path": examples_path,
        "predictions_path": predictions_path,
        "examples_sha256": examples_sha256,
        "predictions_sha256": predictions_sha256,
        "metric_version": metric_version,
        "local_score": local_score,
        "local_score_by_category": dict(sorted(local_score_by_category.items())),
        "artifact_paths": sorted(artifact_paths),
        "notes": notes,
    }
    if git_warning:
        manifest["git_warning"] = git_warning
    if git_commit == "unknown":
        manifest["git_warning"] = git_warning or "git commit could not be determined"
    return manifest
