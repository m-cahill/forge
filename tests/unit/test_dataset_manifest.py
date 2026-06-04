"""Tests for dataset manifest builder."""

from __future__ import annotations

from pathlib import Path

from forge_nemotron.data.manifest import build_dataset_manifest
from forge_nemotron.data.synthetic import write_synthetic_jsonl


def _raw() -> dict:
    return {
        "example_id": "m03_arithmetic_numeric_000001",
        "category": "arithmetic_numeric",
        "prompt": "Question: Compute 2 + 2.",
        "reasoning": "2 + 2 = 4.",
        "expected": "4",
        "source": "m03_synthetic",
        "generator_version": "arithmetic_v1",
        "solver_version": "arithmetic_v1",
        "seed": 5,
        "verified": True,
        "metadata": {},
    }


def test_manifest_injected_timestamp_and_hash(tmp_path: Path) -> None:
    dataset_path = tmp_path / "examples.jsonl"
    write_synthetic_jsonl(dataset_path, [_raw()])
    manifest = build_dataset_manifest(
        dataset_id="test_ds",
        dataset_path=dataset_path,
        seed=5,
        example_count=1,
        category_counts={"arithmetic_numeric": 1},
        generator_versions={"arithmetic_numeric": "arithmetic_v1"},
        solver_versions={"arithmetic_numeric": "arithmetic_v1"},
        verified_count=1,
        rejected_count=0,
        created_at_utc="2026-06-04T12:00:00+00:00",
    )
    assert manifest["created_at_utc"] == "2026-06-04T12:00:00+00:00"
    assert manifest["example_count"] == 1
    assert manifest["category_counts"]["arithmetic_numeric"] == 1
    assert len(manifest["dataset_sha256"]) == 64
