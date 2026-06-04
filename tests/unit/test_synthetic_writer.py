"""Tests for synthetic JSONL writer rejection rules."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from forge_nemotron.data.synthetic import build_completion, write_synthetic_jsonl


def _raw_example(**overrides: object) -> dict:
    base = {
        "example_id": "m03_arithmetic_numeric_000001",
        "category": "arithmetic_numeric",
        "prompt": "Question: Compute 1 + 1.",
        "reasoning": "1 + 1 = 2.",
        "expected": "2",
        "source": "m03_synthetic",
        "generator_version": "arithmetic_v1",
        "solver_version": "arithmetic_v1",
        "seed": 1,
        "verified": True,
        "metadata": {},
    }
    base.update(overrides)
    return base


def test_write_rejects_unverified(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="rejected"):
        write_synthetic_jsonl(
            tmp_path / "out.jsonl",
            [_raw_example(verified=False)],
        )


def test_write_rejects_duplicate_ids(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="rejected"):
        write_synthetic_jsonl(
            tmp_path / "out.jsonl",
            [_raw_example(), _raw_example()],
        )


def test_write_deterministic_jsonl(tmp_path: Path) -> None:
    out = tmp_path / "out.jsonl"
    write_synthetic_jsonl(out, [_raw_example()])
    text1 = out.read_text(encoding="utf-8")
    write_synthetic_jsonl(out, [_raw_example()])
    text2 = out.read_text(encoding="utf-8")
    assert text1 == text2
    data = json.loads(text1.strip())
    assert "Final answer: \\boxed{2}" in data["completion"]


def test_build_completion_strips_duplicate_final_lines() -> None:
    completion = build_completion(
        reasoning="step\nFinal answer: \\boxed{old}",
        answer="42",
    )
    assert completion.endswith("Final answer: \\boxed{42}")
    assert completion.count("Final answer:") == 1
