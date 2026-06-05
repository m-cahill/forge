"""Reproduction plan manifest builder and validator.

Defines metadata for a future public baseline reproduction attempt.
Passing validation does NOT authorize training, submission, or reproduction.
"""

from __future__ import annotations

import json
from enum import Enum
from pathlib import Path
from typing import Any

DEFAULT_BASELINE_REPO = "https://github.com/tonghuikang/nemotron"
COPYING_POLICY_NO_CODE = "no_code_copy"

REQUIRED_NON_CLAIMS = frozenset(
    {
        "not_trained",
        "not_submitted",
        "not_reproduced",
    }
)

REQUIRED_TOP_LEVEL_KEYS = frozenset(
    {
        "plan_id",
        "baseline_repo",
        "baseline_commit",
        "license_status",
        "copying_policy",
        "compute_path",
        "training_authorized",
        "kaggle_submission_authorized",
        "requires_external_credentials",
        "required_credentials",
        "data_sources",
        "expected_artifacts",
        "blockers",
        "non_claims",
    }
)

LICENSE_POLICIES_ALLOWING_COPY = frozenset(
    {
        "permissive_license_observed",
        "owner_license_clearance",
    }
)


class ReproductionPlanStatus(str, Enum):
    """Lifecycle status for a reproduction plan."""

    PREFLIGHT = "preflight"
    READY_FOR_TRAINING = "ready_for_training"
    REJECTED = "rejected"


class SchemaInspectionStatus(str, Enum):
    """External baseline schema inspection gate status."""

    COMPLETE = "complete"
    INCOMPLETE = "incomplete"
    BLOCKED_OWNER_AUTHORIZATION_REQUIRED = "blocked_owner_authorization_required"
    WAIVED = "waived"


DATA_SOURCE_OBJECT_KEYS = frozenset({"name", "sha256", "row_count", "notes_path"})

CREDENTIAL_READINESS_STATUS_VALUES = frozenset({"ready", "blocked", "tbd"})

OPTIONAL_CREDENTIAL_STATUS_KEYS = frozenset(
    {
        "modal_account_status",
        "modal_credential_status",
        "tinker_account_status",
        "tinker_credential_status",
        "cloud_gpu_credential_status",
    }
)


def _is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _is_nullable_string(value: Any) -> bool:
    return value is None or _is_non_empty_string(value)


def build_preflight_reproduction_plan(
    *,
    plan_id: str = "public_control_repro_plan_v1",
    baseline_repo: str = DEFAULT_BASELINE_REPO,
    notes: str | None = None,
) -> dict[str, Any]:
    """Build a minimal M05 preflight reproduction plan (no training authorization)."""
    plan: dict[str, Any] = {
        "plan_id": plan_id,
        "baseline_repo": baseline_repo,
        "baseline_commit": None,
        "license_status": "no_license_observed",
        "copying_policy": COPYING_POLICY_NO_CODE,
        "compute_path": "local_5090_preflight",
        "status": ReproductionPlanStatus.PREFLIGHT.value,
        "training_authorized": False,
        "kaggle_submission_authorized": False,
        "requires_external_credentials": True,
        "required_credentials": ["modal", "tinker"],
        "data_sources": [],
        "expected_artifacts": [
            "dataset_manifest",
            "training_config_hash",
            "adapter_sha256",
            "package_sha256",
            "local_eval_run_id",
        ],
        "blockers": [
            "submit_ui_zip_constraints_open",
            "no_training_authorization",
        ],
        "non_claims": sorted(REQUIRED_NON_CLAIMS),
    }
    if notes is not None:
        plan["notes"] = notes
    return plan


def validate_reproduction_plan(data: dict[str, Any]) -> list[str]:
    """Validate reproduction plan dict. Returns errors; empty means valid."""
    errors: list[str] = []

    if not isinstance(data, dict):
        return ["reproduction plan must be a JSON object"]

    missing = sorted(REQUIRED_TOP_LEVEL_KEYS - set(data.keys()))
    if missing:
        errors.append(f"missing required keys: {', '.join(missing)}")
        return errors

    for key in ("plan_id", "baseline_repo", "license_status", "copying_policy"):
        if not _is_non_empty_string(data.get(key)):
            errors.append(f"{key} must be a non-empty string")

    if not _is_nullable_string(data.get("baseline_commit")):
        errors.append("baseline_commit must be null or a non-empty string")

    status_raw = data.get("status", ReproductionPlanStatus.PREFLIGHT.value)
    if status_raw is not None:
        try:
            status = ReproductionPlanStatus(status_raw)
        except ValueError:
            errors.append(
                f"status must be one of: {', '.join(s.value for s in ReproductionPlanStatus)}"
            )
            return errors
    else:
        status = ReproductionPlanStatus.PREFLIGHT

    training_authorized = data.get("training_authorized")
    if not isinstance(training_authorized, bool):
        errors.append("training_authorized must be a boolean")

    kaggle_authorized = data.get("kaggle_submission_authorized")
    if not isinstance(kaggle_authorized, bool):
        errors.append("kaggle_submission_authorized must be a boolean")

    requires_creds = data.get("requires_external_credentials")
    if not isinstance(requires_creds, bool):
        errors.append("requires_external_credentials must be a boolean")

    required_credentials = data.get("required_credentials")
    if not isinstance(required_credentials, list) or not all(
        _is_non_empty_string(item) for item in required_credentials
    ):
        errors.append("required_credentials must be a list of non-empty strings")

    for list_key in ("expected_artifacts", "blockers"):
        value = data.get(list_key)
        if not isinstance(value, list) or not all(_is_non_empty_string(item) for item in value):
            errors.append(f"{list_key} must be a list of non-empty strings")

    data_sources = data.get("data_sources")
    if not isinstance(data_sources, list):
        errors.append("data_sources must be a list")
    else:
        errors.extend(_validate_data_sources(data_sources))

    schema_status_raw = data.get("schema_inspection_status")
    if schema_status_raw is not None:
        try:
            SchemaInspectionStatus(schema_status_raw)
        except ValueError:
            errors.append(
                "schema_inspection_status must be one of: "
                f"{', '.join(s.value for s in SchemaInspectionStatus)}"
            )

    credentials_ready = data.get("credentials_ready")
    if credentials_ready is not None and not isinstance(credentials_ready, bool):
        errors.append("credentials_ready must be a boolean when present")

    cost_accepted = data.get("cost_accepted")
    if cost_accepted is not None and not isinstance(cost_accepted, bool):
        errors.append("cost_accepted must be a boolean when present")

    ready_for_training = data.get("ready_for_training")
    if ready_for_training is not None and not isinstance(ready_for_training, bool):
        errors.append("ready_for_training must be a boolean when present")

    non_claims = data.get("non_claims")
    if not isinstance(non_claims, list) or not all(
        _is_non_empty_string(item) for item in non_claims
    ):
        errors.append("non_claims must be a list of non-empty strings")
    elif not REQUIRED_NON_CLAIMS.issubset(set(non_claims)):
        missing_claims = sorted(REQUIRED_NON_CLAIMS - set(non_claims))
        errors.append(f"non_claims must include: {', '.join(missing_claims)}")

    if errors:
        return errors

    errors.extend(_validate_compute_path_field(data, status, ready_for_training))
    errors.extend(
        _validate_ready_for_training_field(data, status, training_authorized, ready_for_training)
    )
    errors.extend(_validate_copying_policy(data))
    errors.extend(_validate_credential_readiness_notes(data))
    errors.extend(_validate_authorization_rules(data, status))
    return errors


def _validate_compute_path_field(
    data: dict[str, Any],
    status: ReproductionPlanStatus,
    ready_for_training: Any,
) -> list[str]:
    errors: list[str] = []
    compute_path = data.get("compute_path")
    needs_path = status == ReproductionPlanStatus.READY_FOR_TRAINING or ready_for_training is True
    if needs_path:
        if not _is_non_empty_string(compute_path):
            errors.append("compute_path must be a non-empty string when ready for training")
    elif not _is_nullable_string(compute_path):
        errors.append("compute_path must be null or a non-empty string")
    return errors


def _validate_ready_for_training_field(
    data: dict[str, Any],
    status: ReproductionPlanStatus,
    training_authorized: Any,
    ready_for_training: Any,
) -> list[str]:
    errors: list[str] = []
    if ready_for_training is None:
        return errors
    if ready_for_training and training_authorized is False:
        errors.append("ready_for_training true requires training_authorized true")
    if ready_for_training and status != ReproductionPlanStatus.READY_FOR_TRAINING:
        errors.append("ready_for_training true requires status ready_for_training")
    if status == ReproductionPlanStatus.READY_FOR_TRAINING and ready_for_training is not True:
        errors.append("status ready_for_training requires ready_for_training true")
    return errors


def _validate_data_sources(data_sources: list[Any]) -> list[str]:
    errors: list[str] = []
    for idx, item in enumerate(data_sources):
        if _is_non_empty_string(item):
            continue
        if not isinstance(item, dict):
            errors.append(f"data_sources[{idx}] must be a string or object")
            continue
        missing = sorted(DATA_SOURCE_OBJECT_KEYS - set(item.keys()))
        if missing:
            errors.append(f"data_sources[{idx}] missing keys: {', '.join(missing)}")
            continue
        if not _is_non_empty_string(item.get("name")):
            errors.append(f"data_sources[{idx}].name must be a non-empty string")
        if not _is_non_empty_string(item.get("sha256")):
            errors.append(f"data_sources[{idx}].sha256 must be a non-empty string")
        if not _is_non_empty_string(item.get("notes_path")):
            errors.append(f"data_sources[{idx}].notes_path must be a non-empty string")
        row_count = item.get("row_count")
        if not isinstance(row_count, int) or row_count < 0:
            errors.append(f"data_sources[{idx}].row_count must be a non-negative integer")
    return errors


def _validate_ready_for_training_gates(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    schema_status_raw = data.get("schema_inspection_status")
    schema_waiver = data.get("schema_inspection_waiver")
    if isinstance(schema_waiver, bool) and schema_waiver:
        return errors

    if schema_status_raw is None:
        errors.append(
            "status ready_for_training requires schema_inspection_status or "
            "schema_inspection_waiver true"
        )
    elif schema_status_raw != SchemaInspectionStatus.COMPLETE.value:
        errors.append(
            "status ready_for_training requires schema_inspection_status complete "
            "or schema_inspection_waiver true"
        )

    credentials_ready = data.get("credentials_ready")
    credentials_waived = data.get("credentials_waived")
    if credentials_waived is True:
        pass
    elif credentials_ready is not True:
        errors.append(
            "status ready_for_training requires credentials_ready true or credentials_waived true"
        )

    cost_accepted = data.get("cost_accepted")
    cost_waived = data.get("cost_waived")
    if cost_waived is not True and cost_accepted is not True:
        errors.append("status ready_for_training requires cost_accepted true or cost_waived true")
    return errors


def _validate_credential_readiness_notes(data: dict[str, Any]) -> list[str]:
    """Validate optional Modal/Tinker/cloud credential status fields (M09+)."""
    errors: list[str] = []
    for key in OPTIONAL_CREDENTIAL_STATUS_KEYS:
        value = data.get(key)
        if value is None:
            continue
        if not isinstance(value, str) or value not in CREDENTIAL_READINESS_STATUS_VALUES:
            allowed = ", ".join(sorted(CREDENTIAL_READINESS_STATUS_VALUES))
            errors.append(f"{key} must be one of: {allowed}")

    credentials_ready = data.get("credentials_ready")
    if credentials_ready is not True:
        return errors

    for key in (
        "modal_account_status",
        "modal_credential_status",
        "tinker_account_status",
        "tinker_credential_status",
    ):
        value = data.get(key)
        if value is None:
            continue
        if value != "ready":
            errors.append(f"credentials_ready true requires {key} ready when present")

    return errors


def _validate_copying_policy(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    copying_policy = data.get("copying_policy")
    license_status = data.get("license_status")

    if copying_policy == COPYING_POLICY_NO_CODE:
        return errors

    if copying_policy in ("code_copy_allowed", "vendor_allowed"):
        if license_status not in LICENSE_POLICIES_ALLOWING_COPY:
            errors.append(
                "copying_policy allowing copy requires license_status evidence "
                f"({', '.join(sorted(LICENSE_POLICIES_ALLOWING_COPY))})"
            )
    return errors


def _validate_authorization_rules(
    data: dict[str, Any], status: ReproductionPlanStatus
) -> list[str]:
    errors: list[str] = []

    training_authorized = data.get("training_authorized")
    kaggle_authorized = data.get("kaggle_submission_authorized")

    if training_authorized:
        owner_auth = data.get("owner_training_authorization")
        if not _is_non_empty_string(owner_auth):
            errors.append(
                "training_authorized true requires owner_training_authorization "
                "(non-empty string record)"
            )

    if kaggle_authorized:
        owner_kaggle = data.get("owner_kaggle_submission_authorization")
        if not _is_non_empty_string(owner_kaggle):
            errors.append(
                "kaggle_submission_authorized true requires "
                "owner_kaggle_submission_authorization (non-empty string record)"
            )

    if status == ReproductionPlanStatus.READY_FOR_TRAINING:
        if not training_authorized:
            errors.append("status ready_for_training requires training_authorized true")
        if not _is_non_empty_string(data.get("compute_path")):
            errors.append("status ready_for_training requires non-null compute_path")
        if not _is_non_empty_string(data.get("owner_training_authorization")):
            errors.append("status ready_for_training requires owner_training_authorization")
        errors.extend(_validate_ready_for_training_gates(data))

    requires_creds = data.get("requires_external_credentials")
    required_credentials = data.get("required_credentials")
    if requires_creds and not required_credentials:
        errors.append("requires_external_credentials true requires non-empty required_credentials")

    return errors


def reproduction_plan_to_json(plan: dict[str, Any], *, indent: int = 2) -> str:
    """Serialize reproduction plan to JSON string."""
    return json.dumps(plan, indent=indent, sort_keys=True) + "\n"


def parse_reproduction_plan_json(text: str) -> dict[str, Any]:
    """Parse JSON text into a reproduction plan dict."""
    loaded = json.loads(text)
    if not isinstance(loaded, dict):
        raise ValueError("reproduction plan must be a JSON object")
    return loaded


def load_reproduction_plan(path: Path) -> dict[str, Any]:
    """Load and parse a reproduction plan file."""
    return parse_reproduction_plan_json(path.read_text(encoding="utf-8"))
