"""Unit tests for local evaluation scorer."""

from __future__ import annotations

import pytest

from forge_nemotron.eval.records import EvaluationExample, EvaluationPrediction
from forge_nemotron.eval.scorer import score_examples
from forge_nemotron.metric.boxed import score_prediction


def _example(
    example_id: str,
    expected: str,
    category: str,
    *,
    split: str = "fixture",
) -> EvaluationExample:
    return EvaluationExample(
        example_id=example_id,
        expected=expected,
        category=category,
        source="fixture",
        split=split,
        prompt=None,
    )


class TestScoreExamples:
    def test_exact_match(self) -> None:
        examples = [_example("a", "42", "arithmetic_numeric")]
        preds = [EvaluationPrediction("a", r"\boxed{42}")]
        report = score_examples(examples, preds)
        assert report.correct == 1
        assert report.accuracy == 1.0
        assert report.failed_examples == ()

    def test_final_boxed_selected(self) -> None:
        examples = [_example("a", "99", "multiple_boxed")]
        preds = [EvaluationPrediction("a", r"First \boxed{1} then \boxed{99}")]
        report = score_examples(examples, preds)
        assert report.correct == 1

    def test_no_boxed_fails(self) -> None:
        examples = [_example("a", "7", "no_boxed")]
        preds = [EvaluationPrediction("a", "seven")]
        report = score_examples(examples, preds)
        assert report.correct == 0
        assert report.failed_examples[0].error_type == "no_boxed"

    def test_numeric_tolerance(self) -> None:
        assert score_prediction(r"\boxed{3.14159}", "3.1416")
        examples = [_example("a", "3.1416", "arithmetic_numeric")]
        preds = [EvaluationPrediction("a", r"\boxed{3.14159}")]
        report = score_examples(examples, preds)
        assert report.correct == 1

    def test_missing_prediction_incorrect(self) -> None:
        examples = [_example("a", "1", "string_exact")]
        report = score_examples(examples, [])
        assert report.correct == 0
        assert report.missing_prediction_count == 1
        assert report.failed_examples[0].error_type == "missing_prediction"

    def test_extra_predictions_warn_by_default(self) -> None:
        examples = [_example("a", "1", "string_exact")]
        preds = [
            EvaluationPrediction("a", r"\boxed{1}"),
            EvaluationPrediction("extra", r"\boxed{9}"),
        ]
        report = score_examples(examples, preds)
        assert report.extra_prediction_count == 1
        assert any("extra predictions" in w for w in report.warnings)

    def test_strict_extra_predictions_raises(self) -> None:
        examples = [_example("a", "1", "string_exact")]
        preds = [
            EvaluationPrediction("a", r"\boxed{1}"),
            EvaluationPrediction("extra", r"\boxed{9}"),
        ]
        with pytest.raises(ValueError, match="extra predictions"):
            score_examples(examples, preds, strict_extra_predictions=True)

    def test_category_aggregation(self) -> None:
        examples = [
            _example("a", "1", "cat_a"),
            _example("b", "2", "cat_b"),
            _example("c", "3", "cat_a"),
        ]
        preds = [
            EvaluationPrediction("a", r"\boxed{1}"),
            EvaluationPrediction("b", r"\boxed{wrong}"),
            EvaluationPrediction("c", r"\boxed{3}"),
        ]
        report = score_examples(examples, preds)
        by_cat = {cs.category: cs for cs in report.category_scores}
        assert by_cat["cat_a"].correct == 2
        assert by_cat["cat_a"].total == 2
        assert by_cat["cat_b"].correct == 0
        assert by_cat["cat_b"].total == 1

    def test_deterministic_ordering(self) -> None:
        examples = [
            _example("z", "1", "z_cat"),
            _example("a", "2", "a_cat"),
            _example("m", "3", "m_cat"),
        ]
        preds = [
            EvaluationPrediction("z", r"\boxed{0}"),
            EvaluationPrediction("a", r"\boxed{0}"),
            EvaluationPrediction("m", r"\boxed{0}"),
        ]
        report = score_examples(examples, preds)
        failed_ids = [r.example_id for r in report.failed_examples]
        assert failed_ids == ["a", "m", "z"]
        assert [cs.category for cs in report.category_scores] == ["a_cat", "m_cat", "z_cat"]

    def test_duplicate_example_ids_rejected(self) -> None:
        examples = [
            _example("a", "1", "string_exact"),
            _example("a", "2", "string_exact"),
        ]
        with pytest.raises(ValueError, match="duplicate example_id"):
            score_examples(examples, [])
