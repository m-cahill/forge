"""Adapter candidate manifest builder and validator.

Defines metadata for FORGE LoRA adapter candidates before packaging,
local eval, or Kaggle submission. Passing validation does NOT imply
Kaggle-ready adapter or reproduced baseline.
"""

from __future__ import annotations

import json
from enum import Enum
from pathlib import Path
from typing import Any

EXPECTED_BASE_MODEL = "NVIDIA-Nemotron-3-Nano-30B"
MAX_ADAPTER_RANK = 32
DEFAULT_PACKAGE_VALIDATOR_VERSION = "structural_v1"

REQUIRED_TOP_LEVEL_KEYS = frozenset(
    {
        "candidate_id",
        "candidate_family",
        "created_at_utc",
        "base_model",
        "adapter_rank",
        "adapter_path",
        "adapter_sha256",
        "package_path",
        "package_sha256",
        "dataset_manifest_sha256",
        "training_config_sha256",
        "local_eval_run_id",
        "local_score",
        "local_score_by_category",
        "package_validator_version",
        "status",
        "non_claims",
        "notes",
    }
)


class CandidateStatus(str, Enum):
    """Lifecycle status for an adapter candidate."""

    PREFLIGHT = "preflight"
    PACKAGED = "packaged"
    LOCAL_EVAL_COMPLETE = "local_eval_complete"
    SUBMITTED = "submitted"
    REJECTED = "rejected"


def _is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _is_nullable_string(value: Any) -> bool:
    return value is None or _is_non_empty_string(value)


def build_preflight_candidate_manifest(
    *,
    candidate_id: str = "control_public_repro_preflight",
    candidate_family: str = "control_public_repro",
    created_at_utc: str = "2026-06-04T00:00:00+00:00",
    notes: str = "M04 mock preflight manifest only",
) -> dict[str, Any]:
    """Build a minimal preflight candidate manifest (no real adapter)."""
    return {
        "candidate_id": candidate_id,
        "candidate_family": candidate_family,
        "created_at_utc": created_at_utc,
        "base_model": EXPECTED_BASE_MODEL,
        "adapter_rank": MAX_ADAPTER_RANK,
        "adapter_path": None,
        "adapter_sha256": None,
        "package_path": None,
        "package_sha256": None,
        "dataset_manifest_sha256": None,
        "training_config_sha256": None,
        "local_eval_run_id": None,
        "local_score": None,
        "local_score_by_category": {},
        "package_validator_version": DEFAULT_PACKAGE_VALIDATOR_VERSION,
        "status": CandidateStatus.PREFLIGHT.value,
        "non_claims": [
            "not_trained",
            "not_submitted",
            "not_kaggle_validated",
        ],
        "notes": notes,
    }


def validate_candidate_manifest(data: dict[str, Any]) -> list[str]:
    """Validate manifest dict. Returns error messages; empty list means valid."""
    errors: list[str] = []

    if not isinstance(data, dict):
        return ["manifest must be a JSON object"]

    missing = sorted(REQUIRED_TOP_LEVEL_KEYS - set(data.keys()))
    if missing:
        errors.append(f"missing required keys: {', '.join(missing)}")
        return errors

    for key in (
        "candidate_id",
        "candidate_family",
        "created_at_utc",
        "base_model",
        "package_validator_version",
        "status",
        "notes",
    ):
        if not _is_non_empty_string(data.get(key)):
            errors.append(f"{key} must be a non-empty string")

    status_raw = data.get("status")
    try:
        status = CandidateStatus(status_raw)
    except ValueError:
        errors.append(f"status must be one of: {', '.join(s.value for s in CandidateStatus)}")
        return errors

    base_model = data.get("base_model")
    if base_model != EXPECTED_BASE_MODEL:
        errors.append(f"base_model must be {EXPECTED_BASE_MODEL!r}")

    rank = data.get("adapter_rank")
    if not isinstance(rank, int):
        errors.append("adapter_rank must be an integer")
    elif rank > MAX_ADAPTER_RANK:
        errors.append(f"adapter_rank must be <= {MAX_ADAPTER_RANK}")
    elif rank < 1:
        errors.append("adapter_rank must be >= 1")

    for field in (
        "adapter_path",
        "adapter_sha256",
        "package_path",
        "package_sha256",
        "dataset_manifest_sha256",
        "training_config_sha256",
        "local_eval_run_id",
    ):
        if not _is_nullable_string(data.get(field)):
            errors.append(f"{field} must be null or a non-empty string")

    local_score = data.get("local_score")
    if local_score is not None and not isinstance(local_score, (int, float)):
        errors.append("local_score must be null or a number")

    by_cat = data.get("local_score_by_category")
    if not isinstance(by_cat, dict):
        errors.append("local_score_by_category must be an object")
    elif by_cat:
        for cat, score in by_cat.items():
            if not _is_non_empty_string(cat):
                errors.append("local_score_by_category keys must be non-empty strings")
                break
            if not isinstance(score, (int, float)):
                errors.append("local_score_by_category values must be numbers")
                break

    non_claims = data.get("non_claims")
    if not isinstance(non_claims, list) or not all(
        _is_non_empty_string(item) for item in non_claims
    ):
        errors.append("non_claims must be a list of non-empty strings")

    if errors:
        return errors

    return _validate_status_rules(data, status)


def _validate_status_rules(data: dict[str, Any], status: CandidateStatus) -> list[str]:
    errors: list[str] = []

    package_sha = data.get("package_sha256")
    package_path = data.get("package_path")
    adapter_sha = data.get("adapter_sha256")
    local_eval_run_id = data.get("local_eval_run_id")
    kaggle_submission_id = data.get("kaggle_submission_id")
    rejection_reason = data.get("rejection_reason")

    if status == CandidateStatus.PREFLIGHT:
        return errors

    if status == CandidateStatus.REJECTED:
        notes = data.get("notes", "")
        has_reason = _is_non_empty_string(rejection_reason)
        has_notes = _is_non_empty_string(notes)
        if not has_reason and not has_notes:
            errors.append("status rejected requires rejection_reason or non-empty notes")
        return errors

    if not package_sha:
        errors.append(f"status {status.value} requires package_sha256")
    if status in (
        CandidateStatus.PACKAGED,
        CandidateStatus.LOCAL_EVAL_COMPLETE,
        CandidateStatus.SUBMITTED,
    ):
        if not package_path:
            errors.append(f"status {status.value} requires package_path")

    if status == CandidateStatus.LOCAL_EVAL_COMPLETE:
        if not local_eval_run_id:
            errors.append("status local_eval_complete requires local_eval_run_id")

    if status == CandidateStatus.SUBMITTED:
        if not _is_non_empty_string(kaggle_submission_id):
            errors.append("status submitted requires kaggle_submission_id")

    if not adapter_sha:
        errors.append(f"status {status.value} requires adapter_sha256")

    return errors


def candidate_manifest_to_json(manifest: dict[str, Any], *, indent: int = 2) -> str:
    """Serialize manifest to JSON string."""
    return json.dumps(manifest, indent=indent, sort_keys=True) + "\n"


def parse_candidate_manifest_json(text: str) -> dict[str, Any]:
    """Parse JSON text into a manifest dict."""
    loaded = json.loads(text)
    if not isinstance(loaded, dict):
        raise ValueError("candidate manifest must be a JSON object")
    return loaded


def load_candidate_manifest(path: Path) -> dict[str, Any]:
    """Load and parse a candidate manifest file."""
    return parse_candidate_manifest_json(path.read_text(encoding="utf-8"))
