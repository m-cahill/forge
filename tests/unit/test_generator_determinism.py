"""Determinism tests for synthetic generators."""

from __future__ import annotations

from forge_nemotron.data.synthetic import build_completion
from forge_nemotron.generators.arithmetic import generate_arithmetic_batch
from forge_nemotron.generators.formatting_stress import generate_formatting_stress_batch
from forge_nemotron.generators.string_transform import generate_string_transform_batch
from forge_nemotron.metric.boxed import extract_final_boxed_answer


def test_arithmetic_same_seed_same_ids() -> None:
    a = generate_arithmetic_batch(seed=123, count=5)
    b = generate_arithmetic_batch(seed=123, count=5)
    assert [x["example_id"] for x in a] == [x["example_id"] for x in b]
    assert [x["expected"] for x in a] == [x["expected"] for x in b]


def test_different_seeds_differ() -> None:
    a = generate_arithmetic_batch(seed=1, count=10)
    b = generate_arithmetic_batch(seed=2, count=10)
    assert [x["expected"] for x in a] != [x["expected"] for x in b]


def test_seeds_zero_through_nine_deterministic() -> None:
    for seed in range(10):
        first = generate_arithmetic_batch(seed=seed, count=3)
        second = generate_arithmetic_batch(seed=seed, count=3)
        assert first == second


def test_string_and_formatting_batches_verified() -> None:
    strings = generate_string_transform_batch(seed=99, count=5)
    stress = generate_formatting_stress_batch(seed=99, count=5)
    assert all(x["verified"] for x in strings + stress)


def test_writer_boxed_from_generated_reasoning() -> None:
    raw = generate_arithmetic_batch(seed=7, count=1)[0]
    completion = build_completion(reasoning=raw["reasoning"], answer=raw["expected"])
    assert extract_final_boxed_answer(completion) == raw["expected"]
