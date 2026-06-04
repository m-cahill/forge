"""Unit tests for reproduction plan manifest validation."""

from __future__ import annotations

import copy

import pytest

from forge_nemotron.baselines.reproduction_plan import (
    build_preflight_reproduction_plan,
    parse_reproduction_plan_json,
    reproduction_plan_to_json,
    validate_reproduction_plan,
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
        assert validate_reproduction_plan(plan) == []


class TestSerialization:
    def test_json_roundtrip(self, preflight_plan: dict) -> None:
        text = reproduction_plan_to_json(preflight_plan)
        loaded = parse_reproduction_plan_json(text)
        assert validate_reproduction_plan(loaded) == []
