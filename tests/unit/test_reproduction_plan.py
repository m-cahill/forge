"""Unit tests for reproduction plan manifest validation."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from forge_nemotron.baselines.reproduction_plan import (
    build_preflight_reproduction_plan,
    parse_reproduction_plan_json,
    reproduction_plan_to_json,
    validate_reproduction_plan,
)

SCHEMA_GATE_PATH = (
    Path(__file__).resolve().parents[2]
    / "docs/milestones/M06/evidence/reproduction_gate"
    / "public_control_repro_plan.schema_gate.json"
)
TRAINING_BLOCKED_PATH = (
    Path(__file__).resolve().parents[2]
    / "docs/milestones/M07/evidence/training_gate"
    / "public_control_repro_plan.training_blocked.json"
)
READINESS_PATH = (
    Path(__file__).resolve().parents[2]
    / "docs/milestones/M08/evidence/readiness"
    / "public_control_repro_plan.readiness.json"
)
MODAL_TINKER_GATE_PATH = (
    Path(__file__).resolve().parents[2]
    / "docs/milestones/M09/evidence/readiness"
    / "public_control_repro_plan.modal_tinker_gate.json"
)
LOCAL_5090_PROBE_PATH = (
    Path(__file__).resolve().parents[2]
    / "docs/milestones/M10/evidence/readiness"
    / "public_control_repro_plan.local_5090_probe.json"
)


@pytest.fixture
def preflight_plan() -> dict:
    return build_preflight_reproduction_plan()


class TestPreflightPlan:
    def test_preflight_valid(self, preflight_plan: dict) -> None:
        assert validate_reproduction_plan(preflight_plan) == []

    def test_training_authorized_without_owner_record_rejected(self, preflight_plan: dict) -> None:
        bad = copy.deepcopy(preflight_plan)
        bad["training_authorized"] = True
        errors = validate_reproduction_plan(bad)
        assert any("owner_training_authorization" in e for e in errors)

    def test_kaggle_authorized_without_owner_record_rejected(self, preflight_plan: dict) -> None:
        bad = copy.deepcopy(preflight_plan)
        bad["kaggle_submission_authorized"] = True
        errors = validate_reproduction_plan(bad)
        assert any("owner_kaggle_submission_authorization" in e for e in errors)

    def test_copying_allowed_without_license_rejected(self, preflight_plan: dict) -> None:
        bad = copy.deepcopy(preflight_plan)
        bad["copying_policy"] = "code_copy_allowed"
        bad["license_status"] = "no_license_observed"
        errors = validate_reproduction_plan(bad)
        assert any("copying_policy" in e for e in errors)

    def test_missing_non_claims_rejected(self, preflight_plan: dict) -> None:
        bad = copy.deepcopy(preflight_plan)
        bad["non_claims"] = ["not_trained"]
        errors = validate_reproduction_plan(bad)
        assert any("non_claims must include" in e for e in errors)

    def test_requires_credentials_empty_list_rejected(self, preflight_plan: dict) -> None:
        bad = copy.deepcopy(preflight_plan)
        bad["required_credentials"] = []
        errors = validate_reproduction_plan(bad)
        assert any("required_credentials" in e for e in errors)


class TestReadyForTraining:
    def test_ready_for_training_requires_authorization(self, preflight_plan: dict) -> None:
        bad = copy.deepcopy(preflight_plan)
        bad["status"] = "ready_for_training"
        bad["training_authorized"] = False
        errors = validate_reproduction_plan(bad)
        assert any("ready_for_training" in e for e in errors)

    def test_ready_for_training_valid_with_owner_record(self, preflight_plan: dict) -> None:
        plan = copy.deepcopy(preflight_plan)
        plan["status"] = "ready_for_training"
        plan["training_authorized"] = True
        plan["owner_training_authorization"] = "owner-2026-06-04-m06"
        plan["compute_path"] = "modal_tinker"
        plan["schema_inspection_status"] = "complete"
        plan["credentials_ready"] = True
        plan["cost_accepted"] = True
        plan["ready_for_training"] = True
        assert validate_reproduction_plan(plan) == []


class TestSerialization:
    def test_json_roundtrip(self, preflight_plan: dict) -> None:
        text = reproduction_plan_to_json(preflight_plan)
        loaded = parse_reproduction_plan_json(text)
        assert validate_reproduction_plan(loaded) == []


class TestSchemaGateManifest:
    def test_schema_gate_plan_file_valid(self) -> None:
        data = json.loads(SCHEMA_GATE_PATH.read_text(encoding="utf-8"))
        assert validate_reproduction_plan(data) == []
        assert data["schema_inspection_status"] == "complete"
        assert data["training_authorized"] is False
        assert data["kaggle_submission_authorized"] is False
        assert data["copying_policy"] == "no_code_copy"
        assert isinstance(data["data_sources"], list)
        assert all(isinstance(item, dict) for item in data["data_sources"])

    def test_blocked_schema_inspection_plan_valid(self, preflight_plan: dict) -> None:
        plan = copy.deepcopy(preflight_plan)
        plan["plan_id"] = "public_control_repro_plan_schema_gate_blocked"
        plan["schema_inspection_status"] = "blocked_owner_authorization_required"
        plan["data_sources"] = []
        plan["blockers"] = ["schema_inspection_not_authorized"]
        assert validate_reproduction_plan(plan) == []

    def test_ready_for_training_requires_schema_and_credentials(self, preflight_plan: dict) -> None:
        plan = copy.deepcopy(preflight_plan)
        plan["status"] = "ready_for_training"
        plan["training_authorized"] = True
        plan["owner_training_authorization"] = "owner-m07-gate"
        plan["compute_path"] = "modal_tinker"
        errors = validate_reproduction_plan(plan)
        assert any("schema_inspection" in e for e in errors)
        assert any("credentials_ready" in e for e in errors)

    def test_ready_for_training_valid_with_schema_and_credentials(
        self, preflight_plan: dict
    ) -> None:
        plan = copy.deepcopy(preflight_plan)
        plan["status"] = "ready_for_training"
        plan["training_authorized"] = True
        plan["owner_training_authorization"] = "owner-m07-gate"
        plan["compute_path"] = "modal_tinker"
        plan["schema_inspection_status"] = "complete"
        plan["credentials_ready"] = True
        plan["cost_accepted"] = True
        plan["ready_for_training"] = True
        assert validate_reproduction_plan(plan) == []

    def test_ready_for_training_requires_compute_path(self, preflight_plan: dict) -> None:
        plan = copy.deepcopy(preflight_plan)
        plan["status"] = "ready_for_training"
        plan["training_authorized"] = True
        plan["owner_training_authorization"] = "owner-m07-gate"
        plan["schema_inspection_status"] = "complete"
        plan["credentials_ready"] = True
        plan["compute_path"] = ""
        errors = validate_reproduction_plan(plan)
        assert any("compute_path" in e for e in errors)

    def test_ready_for_training_schema_waiver_allows_incomplete(self, preflight_plan: dict) -> None:
        plan = copy.deepcopy(preflight_plan)
        plan["status"] = "ready_for_training"
        plan["training_authorized"] = True
        plan["owner_training_authorization"] = "owner-m07-gate"
        plan["compute_path"] = "modal_tinker"
        plan["credentials_ready"] = True
        plan["cost_accepted"] = True
        plan["ready_for_training"] = True
        plan["schema_inspection_waiver"] = True
        assert validate_reproduction_plan(plan) == []

    def test_ready_for_training_requires_cost_accepted(self, preflight_plan: dict) -> None:
        plan = copy.deepcopy(preflight_plan)
        plan["status"] = "ready_for_training"
        plan["training_authorized"] = True
        plan["owner_training_authorization"] = "owner-m07-gate"
        plan["compute_path"] = "modal_tinker"
        plan["schema_inspection_status"] = "complete"
        plan["credentials_ready"] = True
        plan["ready_for_training"] = True
        plan["cost_accepted"] = False
        errors = validate_reproduction_plan(plan)
        assert any("cost_accepted" in e for e in errors)

    def test_null_compute_path_allowed_when_not_ready(self, preflight_plan: dict) -> None:
        plan = copy.deepcopy(preflight_plan)
        plan["compute_path"] = None
        plan["ready_for_training"] = False
        plan["cost_accepted"] = False
        assert validate_reproduction_plan(plan) == []


class TestTrainingGateManifest:
    def test_training_blocked_manifest_file_valid(self) -> None:
        data = json.loads(TRAINING_BLOCKED_PATH.read_text(encoding="utf-8"))
        assert validate_reproduction_plan(data) == []
        assert data["plan_id"] == "public_control_repro_plan_training_gate_v1"
        assert data["training_authorized"] is False
        assert data["ready_for_training"] is False
        assert data["status"] != "ready_for_training"
        assert data["schema_inspection_status"] == "complete"
        assert "training_not_authorized" in data["blockers"]


class TestReadinessManifest:
    def test_readiness_manifest_file_valid(self) -> None:
        data = json.loads(READINESS_PATH.read_text(encoding="utf-8"))
        assert validate_reproduction_plan(data) == []
        assert data["plan_id"] == "public_control_repro_plan_readiness_v1"
        assert data["compute_path"] is None
        assert data["cost_accepted"] is False
        assert data["credentials_ready"] is False
        assert data["ready_for_training"] is False
        assert "sq_corpus_001_open" in data["blockers"]


class TestModalTinkerGateManifest:
    def test_modal_tinker_gate_manifest_file_valid(self) -> None:
        data = json.loads(MODAL_TINKER_GATE_PATH.read_text(encoding="utf-8"))
        assert validate_reproduction_plan(data) == []
        assert data["plan_id"] == "public_control_repro_plan_modal_tinker_gate_v1"
        assert data["credentials_ready"] is False
        assert data["cost_accepted"] is False
        assert data["modal_account_status"] == "tbd"
        assert data["tinker_account_status"] == "tbd"
        assert "modal_status_tbd" in data["blockers"]

    def test_invalid_modal_status_rejected(self, preflight_plan: dict) -> None:
        bad = copy.deepcopy(preflight_plan)
        bad["modal_account_status"] = "unknown"
        errors = validate_reproduction_plan(bad)
        assert any("modal_account_status" in e for e in errors)

    def test_credentials_ready_with_tbd_modal_rejected(self, preflight_plan: dict) -> None:
        bad = copy.deepcopy(preflight_plan)
        bad["credentials_ready"] = True
        bad["modal_account_status"] = "tbd"
        bad["modal_credential_status"] = "tbd"
        bad["tinker_account_status"] = "tbd"
        bad["tinker_credential_status"] = "tbd"
        errors = validate_reproduction_plan(bad)
        assert any("credentials_ready true requires" in e for e in errors)


class TestLocal5090ProbeManifest:
    def test_local_5090_probe_manifest_file_valid(self) -> None:
        data = json.loads(LOCAL_5090_PROBE_PATH.read_text(encoding="utf-8"))
        assert validate_reproduction_plan(data) == []
        assert data["plan_id"] == "public_control_repro_plan_local_5090_probe_v1"
        assert data["local_5090_probe_status"] == "visible_no_torch_cuda"
        assert data["compute_path"] is None
        assert data["training_authorized"] is False
        assert data["ready_for_training"] is False
        assert "local_5090_torch_cuda_unavailable" in data["blockers"]

    def test_invalid_local_5090_probe_status_rejected(self, preflight_plan: dict) -> None:
        bad = copy.deepcopy(preflight_plan)
        bad["local_5090_probe_status"] = "unknown"
        errors = validate_reproduction_plan(bad)
        assert any("local_5090_probe_status" in e for e in errors)

    def test_cuda_ready_probe_requires_local_compute_path(self, preflight_plan: dict) -> None:
        bad = copy.deepcopy(preflight_plan)
        bad["local_5090_probe_status"] = "cuda_ready_probe_only"
        bad["compute_path"] = None
        errors = validate_reproduction_plan(bad)
        assert any("compute_path local_5090" in e for e in errors)

    def test_visible_no_torch_cuda_with_local_compute_path_rejected(
        self, preflight_plan: dict
    ) -> None:
        bad = copy.deepcopy(preflight_plan)
        bad["local_5090_probe_status"] = "visible_no_torch_cuda"
        bad["compute_path"] = "local_5090"
        errors = validate_reproduction_plan(bad)
        assert any("cuda-ready local_5090_probe_status" in e for e in errors)

    def test_ready_for_training_false_with_training_authorized_false(
        self, preflight_plan: dict
    ) -> None:
        plan = copy.deepcopy(preflight_plan)
        plan["local_5090_probe_status"] = "visible_no_torch_cuda"
        plan["ready_for_training"] = False
        plan["training_authorized"] = False
        assert validate_reproduction_plan(plan) == []
