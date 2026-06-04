"""Unit tests for boxed answer extraction and scoring.

Tests cover:
- Single boxed answer extraction
- Multiple boxed answers (last one wins)
- Missing boxed answer handling
- Malformed boxed expressions
- Nested braces
- Exact string matching
- Numeric tolerance matching
- Numeric mismatches
- Whitespace normalization
- Robustness against random/malformed input
"""

from __future__ import annotations

from forge_nemotron.metric.boxed import (
    answers_match,
    extract_boxed_answers,
    extract_final_boxed_answer,
    is_numeric_close,
    normalize_answer,
    score_prediction,
)


class TestExtractBoxedAnswers:
    """Tests for extract_boxed_answers function."""

    def test_single_boxed_answer(self) -> None:
        """Extract a single boxed answer."""
        text = r"The answer is \boxed{42}"
        result = extract_boxed_answers(text)
        assert result == ["42"]

    def test_single_boxed_with_text_around(self) -> None:
        """Extract boxed answer surrounded by text."""
        text = r"After calculation, we get \boxed{123} as the final result."
        result = extract_boxed_answers(text)
        assert result == ["123"]

    def test_multiple_boxed_answers(self) -> None:
        """Extract multiple boxed answers in order."""
        text = r"First \boxed{1}, then \boxed{2}, finally \boxed{3}"
        result = extract_boxed_answers(text)
        assert result == ["1", "2", "3"]

    def test_no_boxed_answer(self) -> None:
        """Return empty list when no boxed answer present."""
        text = "There is no boxed answer here"
        result = extract_boxed_answers(text)
        assert result == []

    def test_empty_string(self) -> None:
        """Handle empty string input."""
        assert extract_boxed_answers("") == []

    def test_empty_boxed(self) -> None:
        """Handle empty boxed expression."""
        text = r"\boxed{}"
        result = extract_boxed_answers(text)
        assert result == [""]

    def test_boxed_with_spaces(self) -> None:
        """Handle spaces inside boxed expression."""
        text = r"\boxed{  42  }"
        result = extract_boxed_answers(text)
        assert result == ["  42  "]

    def test_boxed_with_space_after_boxed(self) -> None:
        r"""Handle \boxed {x} with space before brace."""
        text = r"\boxed {42}"
        result = extract_boxed_answers(text)
        assert result == ["42"]

    def test_nested_braces_simple(self) -> None:
        """Handle simple nested braces like f(x)."""
        text = r"\boxed{f(x)}"
        result = extract_boxed_answers(text)
        assert result == ["f(x)"]

    def test_nested_braces_curly(self) -> None:
        """Handle nested curly braces."""
        text = r"\boxed{{1, 2, 3}}"
        result = extract_boxed_answers(text)
        assert result == ["{1, 2, 3}"]

    def test_nested_braces_deeper(self) -> None:
        """Handle deeper nested braces."""
        text = r"\boxed{\frac{a}{b}}"
        result = extract_boxed_answers(text)
        assert result == [r"\frac{a}{b}"]

    def test_malformed_unclosed_brace(self) -> None:
        """Handle unclosed brace gracefully."""
        text = r"\boxed{42"
        result = extract_boxed_answers(text)
        assert result == []

    def test_malformed_no_brace(self) -> None:
        """Handle boxed without braces."""
        text = r"\boxed42"
        result = extract_boxed_answers(text)
        assert result == []

    def test_boxed_in_latex_context(self) -> None:
        """Extract from realistic LaTeX context."""
        text = r"""
        Let $x = 5$ and $y = 3$.
        Then $x + y = \boxed{8}$.
        """
        result = extract_boxed_answers(text)
        assert result == ["8"]

    def test_multiline_content(self) -> None:
        """Handle multiline content inside boxed."""
        text = "\\boxed{line1\nline2}"
        result = extract_boxed_answers(text)
        assert result == ["line1\nline2"]


class TestExtractFinalBoxedAnswer:
    """Tests for extract_final_boxed_answer function."""

    def test_single_boxed_returns_it(self) -> None:
        """Single boxed answer is the final answer."""
        text = r"The answer is \boxed{42}"
        result = extract_final_boxed_answer(text)
        assert result == "42"

    def test_multiple_boxed_returns_last(self) -> None:
        """Multiple boxed answers, return the last one."""
        text = r"Intermediate: \boxed{10}. Final: \boxed{42}"
        result = extract_final_boxed_answer(text)
        assert result == "42"

    def test_no_boxed_returns_none(self) -> None:
        """No boxed answer returns None."""
        text = "No answer here"
        result = extract_final_boxed_answer(text)
        assert result is None

    def test_empty_string_returns_none(self) -> None:
        """Empty string returns None."""
        assert extract_final_boxed_answer("") is None


class TestNormalizeAnswer:
    """Tests for normalize_answer function."""

    def test_strips_whitespace(self) -> None:
        """Strip leading and trailing whitespace."""
        assert normalize_answer("  42  ") == "42"

    def test_collapses_internal_whitespace(self) -> None:
        """Collapse multiple internal spaces."""
        assert normalize_answer("a    b    c") == "a b c"

    def test_handles_newlines(self) -> None:
        """Handle newlines in answer."""
        assert normalize_answer("a\nb\nc") == "a b c"

    def test_handles_tabs(self) -> None:
        """Handle tabs in answer."""
        assert normalize_answer("a\tb\tc") == "a b c"

    def test_empty_string(self) -> None:
        """Handle empty string."""
        assert normalize_answer("") == ""

    def test_only_whitespace(self) -> None:
        """Handle whitespace-only string."""
        assert normalize_answer("   ") == ""


class TestIsNumericClose:
    """Tests for is_numeric_close function."""

    def test_exact_integers(self) -> None:
        """Exact integer match."""
        assert is_numeric_close("42", "42")

    def test_integer_and_float(self) -> None:
        """Integer equals float equivalent."""
        assert is_numeric_close("42", "42.0")

    def test_close_floats(self) -> None:
        """Close floating point values."""
        assert is_numeric_close("3.14159", "3.1416", rel_tol=1e-4)

    def test_not_close_floats(self) -> None:
        """Not close floating point values."""
        assert not is_numeric_close("3.14", "3.2", rel_tol=1e-4)

    def test_simple_fraction(self) -> None:
        """Simple fraction parsing."""
        assert is_numeric_close("1/2", "0.5")

    def test_negative_numbers(self) -> None:
        """Negative number comparison."""
        assert is_numeric_close("-42", "-42.0")

    def test_scientific_notation(self) -> None:
        """Scientific notation comparison."""
        assert is_numeric_close("1e10", "10000000000")

    def test_non_numeric_returns_false(self) -> None:
        """Non-numeric strings return False."""
        assert not is_numeric_close("abc", "123")
        assert not is_numeric_close("123", "abc")
        assert not is_numeric_close("abc", "xyz")

    def test_empty_strings_return_false(self) -> None:
        """Empty strings return False."""
        assert not is_numeric_close("", "42")
        assert not is_numeric_close("42", "")

    def test_division_by_zero_handled(self) -> None:
        """Division by zero in fraction handled."""
        assert not is_numeric_close("1/0", "0")


class TestAnswersMatch:
    """Tests for answers_match function."""

    def test_exact_match(self) -> None:
        """Exact string match."""
        assert answers_match("42", "42")

    def test_whitespace_normalized(self) -> None:
        """Whitespace is normalized by default."""
        assert answers_match("  42  ", "42")
        assert answers_match("a  b", "a b")

    def test_case_insensitive_default(self) -> None:
        """Case insensitive by default."""
        assert answers_match("ANSWER", "answer")
        assert answers_match("Answer", "ANSWER")

    def test_case_sensitive_when_requested(self) -> None:
        """Case sensitive when explicitly requested."""
        assert not answers_match("ANSWER", "answer", case_sensitive=True)
        assert answers_match("answer", "answer", case_sensitive=True)

    def test_numeric_comparison(self) -> None:
        """Numeric values compared with tolerance."""
        assert answers_match("3.14159", "3.1416")
        assert answers_match("42", "42.0")

    def test_numeric_disabled(self) -> None:
        """Numeric comparison can be disabled."""
        assert not answers_match("3.14159", "3.1416", try_numeric=False)

    def test_none_handling(self) -> None:
        """Handle None values."""
        assert answers_match(None, None)  # type: ignore[arg-type]
        assert not answers_match(None, "42")  # type: ignore[arg-type]
        assert not answers_match("42", None)  # type: ignore[arg-type]

    def test_empty_strings(self) -> None:
        """Handle empty strings."""
        assert answers_match("", "")
        assert not answers_match("", "42")
        assert not answers_match("42", "")


class TestScorePrediction:
    """Tests for score_prediction function."""

    def test_correct_boxed_answer(self) -> None:
        """Correct boxed answer scores True."""
        completion = r"The answer is \boxed{42}"
        assert score_prediction(completion, "42")

    def test_wrong_boxed_answer(self) -> None:
        """Wrong boxed answer scores False."""
        completion = r"The answer is \boxed{41}"
        assert not score_prediction(completion, "42")

    def test_no_boxed_answer(self) -> None:
        """Missing boxed answer scores False."""
        completion = "The answer is 42"
        assert not score_prediction(completion, "42")

    def test_multiple_boxes_uses_last(self) -> None:
        """Multiple boxes, use last one."""
        completion = r"First \boxed{wrong}. Final \boxed{42}"
        assert score_prediction(completion, "42")
        assert not score_prediction(completion, "wrong")

    def test_numeric_tolerance(self) -> None:
        """Numeric tolerance in scoring."""
        completion = r"Therefore, \boxed{3.14159}"
        assert score_prediction(completion, "3.1416")

    def test_whitespace_in_box(self) -> None:
        """Whitespace inside box is normalized."""
        completion = r"\boxed{  42  }"
        assert score_prediction(completion, "42")

    def test_case_insensitive_scoring(self) -> None:
        """Case insensitive by default."""
        completion = r"\boxed{HELLO}"
        assert score_prediction(completion, "hello")

    def test_realistic_reasoning_trace(self) -> None:
        """Score a realistic reasoning trace."""
        completion = """
        Let me solve this step by step.

        First, we have x = 5.
        Then, y = 3.

        Adding them together: x + y = 5 + 3 = 8

        Therefore, the answer is \\boxed{8}.
        """
        assert score_prediction(completion, "8")


class TestRobustness:
    """Tests for robustness against malformed input."""

    def test_random_text(self) -> None:
        """Handle random text without crashing."""
        random_texts = [
            "asdfghjkl",
            "12345!@#$%",
            "{}{}{}",
            "\\\\\\\\",
            "\n\n\n",
            "\t\t\t",
            "αβγδε",
            "日本語",
            "🎉🎊🎁",
        ]
        for text in random_texts:
            # Should not raise
            result = extract_boxed_answers(text)
            assert isinstance(result, list)

    def test_partial_boxed(self) -> None:
        """Handle partial boxed expressions."""
        partials = [
            r"\boxed",
            r"\boxed{",
            r"\boxed{}",
            r"\box{42}",
            r"boxed{42}",
            r"\BOXED{42}",
        ]
        for text in partials:
            # Should not raise
            result = extract_boxed_answers(text)
            assert isinstance(result, list)

    def test_very_long_input(self) -> None:
        """Handle very long input."""
        long_text = "x" * 100000 + r"\boxed{42}" + "y" * 100000
        result = extract_final_boxed_answer(long_text)
        assert result == "42"

    def test_many_boxes(self) -> None:
        """Handle many boxed expressions."""
        boxes = " ".join([f"\\boxed{{{i}}}" for i in range(1000)])
        result = extract_boxed_answers(boxes)
        assert len(result) == 1000
        assert result[-1] == "999"

    def test_deeply_nested_braces(self) -> None:
        """Handle deeply nested braces."""
        # This should extract the outer content correctly
        text = r"\boxed{{{{{nested}}}}}"
        result = extract_boxed_answers(text)
        assert len(result) == 1


class TestEdgeCases:
    """Additional edge case tests."""

    def test_boxed_with_latex_commands(self) -> None:
        """Handle LaTeX commands inside boxed."""
        text = r"\boxed{\sqrt{2}}"
        result = extract_final_boxed_answer(text)
        assert result == r"\sqrt{2}"

    def test_boxed_with_fractions(self) -> None:
        """Handle fractions inside boxed."""
        text = r"\boxed{\frac{1}{2}}"
        result = extract_final_boxed_answer(text)
        assert result == r"\frac{1}{2}"

    def test_numeric_with_units(self) -> None:
        """Numeric comparison with units fails (expected)."""
        # "42 meters" should not match "42" numerically
        assert not is_numeric_close("42 meters", "42")

    def test_percentage_as_string(self) -> None:
        """Percentage strings match as strings."""
        assert answers_match("50%", "50%")
        # But not numerically
        assert not is_numeric_close("50%", "0.5")

    def test_answer_with_equals(self) -> None:
        """Handle answers with equals signs."""
        text = r"\boxed{x = 5}"
        result = extract_final_boxed_answer(text)
        assert result == "x = 5"
