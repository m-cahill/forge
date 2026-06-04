"""Unit tests for run manifest builder."""

from __future__ import annotations

from forge_nemotron.eval.scorer import METRIC_VERSION
from forge_nemotron.reports.run_manifest import build_run_manifest


class TestRunManifest:
    def test_required_fields(self) -> None:
        manifest = build_run_manifest(
            run_id="m02_fixture_eval",
            created_at_utc="2026-06-04T12:00:00+00:00",
            git_commit="abc123",
            branch="forge/M02-local-eval",
            run_type="local_eval",
            candidate_id="fixture_candidate",
            examples_path="tests/fixtures/eval/examples.jsonl",
            predictions_path="tests/fixtures/eval/predictions_good.jsonl",
            examples_sha256="e" * 64,
            predictions_sha256="p" * 64,
            metric_version=METRIC_VERSION,
            local_score=0.875,
            local_score_by_category={"b": 0.5, "a": 1.0},
            artifact_paths=["b.json", "a.json"],
            notes="fixture only",
        )
        assert manifest["run_id"] == "m02_fixture_eval"
        assert manifest["metric_version"] == METRIC_VERSION
        assert manifest["local_score"] == 0.875
        assert manifest["local_score_by_category"] == {"a": 1.0, "b": 0.5}
        assert manifest["artifact_paths"] == ["a.json", "b.json"]
        assert manifest["git_commit"] == "abc123"

    def test_unknown_git_commit_adds_warning(self) -> None:
        manifest = build_run_manifest(
            run_id="x",
            created_at_utc="2026-06-04T12:00:00+00:00",
            git_commit="unknown",
            branch="unknown",
            run_type="local_eval",
            candidate_id="fixture",
            examples_path="e.jsonl",
            predictions_path="p.jsonl",
            examples_sha256="e" * 64,
            predictions_sha256="p" * 64,
            metric_version=METRIC_VERSION,
            local_score=0.0,
            local_score_by_category={},
            artifact_paths=[],
        )
        assert "git_warning" in manifest
