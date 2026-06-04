"""Unit tests for adapter candidate manifest validation."""

from __future__ import annotations

import copy

import pytest

from forge_nemotron.adapters.candidate_manifest import (
    MAX_ADAPTER_RANK,
    build_preflight_candidate_manifest,
    candidate_manifest_to_json,
    parse_candidate_manifest_json,
    validate_candidate_manifest,
)


@pytest.fixture
def preflight_manifest() -> dict:
    return build_preflight_candidate_manifest()


class TestPreflightManifest:
    def test_preflight_valid_without_hashes(self, preflight_manifest: dict) -> None:
        assert validate_candidate_manifest(preflight_manifest) == []

    def test_rank_over_32_rejected(self, preflight_manifest: dict) -> None:
        bad = copy.deepcopy(preflight_manifest)
        bad["adapter_rank"] = MAX_ADAPTER_RANK + 1
        errors = validate_candidate_manifest(bad)
        assert any("adapter_rank" in e for e in errors)

    def test_wrong_base_model(self, preflight_manifest: dict) -> None:
        bad = copy.deepcopy(preflight_manifest)
        bad["base_model"] = "other-model"
        errors = validate_candidate_manifest(bad)
        assert any("base_model" in e for e in errors)


class TestStatusRules:
    def _packaged_base(self, preflight_manifest: dict) -> dict:
        m = copy.deepcopy(preflight_manifest)
        m["status"] = "packaged"
        m["package_path"] = "submissions/candidate/submission.zip"
        m["package_sha256"] = "a" * 64
        m["adapter_path"] = "artifacts/adapter"
        m["adapter_sha256"] = "b" * 64
        return m

    def test_packaged_requires_package_fields(self, preflight_manifest: dict) -> None:
        bad = copy.deepcopy(preflight_manifest)
        bad["status"] = "packaged"
        errors = validate_candidate_manifest(bad)
        assert any("package_sha256" in e for e in errors)

    def test_local_eval_complete_requires_run_id(self, preflight_manifest: dict) -> None:
        m = self._packaged_base(preflight_manifest)
        m["status"] = "local_eval_complete"
        errors = validate_candidate_manifest(m)
        assert any("local_eval_run_id" in e for e in errors)

    def test_submitted_missing_package_hash_rejected(self, preflight_manifest: dict) -> None:
        bad = copy.deepcopy(preflight_manifest)
        bad["status"] = "submitted"
        bad["kaggle_submission_id"] = "sub-123"
        errors = validate_candidate_manifest(bad)
        assert any("package_sha256" in e for e in errors)

    def test_submitted_requires_submission_id(self, preflight_manifest: dict) -> None:
        m = self._packaged_base(preflight_manifest)
        m["status"] = "submitted"
        errors = validate_candidate_manifest(m)
        assert any("kaggle_submission_id" in e for e in errors)

    def test_submitted_valid_with_evidence(self, preflight_manifest: dict) -> None:
        m = self._packaged_base(preflight_manifest)
        m["status"] = "submitted"
        m["kaggle_submission_id"] = "kaggle-sub-001"
        assert validate_candidate_manifest(m) == []

    def test_rejected_requires_reason_or_notes(self, preflight_manifest: dict) -> None:
        bad = copy.deepcopy(preflight_manifest)
        bad["status"] = "rejected"
        bad["notes"] = ""
        errors = validate_candidate_manifest(bad)
        assert errors

    def test_rejected_with_notes_valid(self, preflight_manifest: dict) -> None:
        bad = copy.deepcopy(preflight_manifest)
        bad["status"] = "rejected"
        bad["notes"] = "rank policy violation"
        assert validate_candidate_manifest(bad) == []


class TestJsonRoundtrip:
    def test_roundtrip(self, preflight_manifest: dict) -> None:
        text = candidate_manifest_to_json(preflight_manifest)
        loaded = parse_candidate_manifest_json(text)
        assert loaded == preflight_manifest
        assert validate_candidate_manifest(loaded) == []
