"""Unit tests for submission package validator.

Tests use programmatically generated fixture zips.
These are STRUCTURAL FIXTURES ONLY, not Kaggle-valid adapters.

Validator pass on a fixture does NOT mean "Kaggle-ready".
Real package readiness requires actual adapter files and Kaggle evidence.
"""

from __future__ import annotations

import json
import tempfile
import zipfile
from pathlib import Path

import pytest

from forge_nemotron.packaging.validate_submission import (
    ValidationResult,
    validate_submission_zip,
)


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as td:
        yield Path(td)


def create_test_zip(
    path: Path,
    *,
    include_config: bool = True,
    include_weights: bool = True,
    config_content: dict | None = None,
    extra_files: dict[str, bytes] | None = None,
    weight_filename: str = "adapter_model.safetensors",
) -> Path:
    """Create a test submission.zip with specified contents.

    This creates STRUCTURAL TEST FIXTURES only, not real adapters.

    Args:
        path: Directory to create the zip in
        include_config: Whether to include adapter_config.json
        include_weights: Whether to include adapter weight file
        config_content: Content for adapter_config.json (default has r=32)
        extra_files: Additional files to include {name: bytes_content}
        weight_filename: Name of the weight file

    Returns:
        Path to created submission.zip
    """
    zip_path = path / "submission.zip"

    with zipfile.ZipFile(zip_path, "w") as zf:
        if include_config:
            config = config_content or {"r": 32, "base_model_name_or_path": "test"}
            zf.writestr("adapter_config.json", json.dumps(config))

        if include_weights:
            # Write a small dummy weight file (not a real safetensor)
            zf.writestr(weight_filename, b"dummy_weights_for_testing")

        if extra_files:
            for name, content in extra_files.items():
                zf.writestr(name, content)

    return zip_path


class TestValidSubmission:
    """Tests for valid submission packages."""

    def test_valid_rank_32_submission(self, temp_dir: Path) -> None:
        """Accept a structurally valid rank-32 submission."""
        zip_path = create_test_zip(temp_dir, config_content={"r": 32})

        report = validate_submission_zip(zip_path)

        assert report.valid is True
        assert report.result == ValidationResult.VALID
        assert report.rank == 32
        assert len(report.errors) == 0
        assert "adapter_config.json" in report.files
        assert "adapter_model.safetensors" in report.files
        assert report.sha256  # Should have a hash

    def test_valid_rank_16_submission(self, temp_dir: Path) -> None:
        """Accept a structurally valid rank-16 submission."""
        zip_path = create_test_zip(temp_dir, config_content={"r": 16})

        report = validate_submission_zip(zip_path)

        assert report.valid is True
        assert report.rank == 16

    def test_valid_rank_8_submission(self, temp_dir: Path) -> None:
        """Accept a structurally valid rank-8 submission."""
        zip_path = create_test_zip(temp_dir, config_content={"r": 8})

        report = validate_submission_zip(zip_path)

        assert report.valid is True
        assert report.rank == 8

    def test_rank_from_nested_config(self, temp_dir: Path) -> None:
        """Extract rank from nested peft_config."""
        config = {"peft_config": {"r": 32, "lora_alpha": 64}}
        zip_path = create_test_zip(temp_dir, config_content=config)

        report = validate_submission_zip(zip_path)

        assert report.valid is True
        assert report.rank == 32


class TestInvalidSubmission:
    """Tests for invalid submission packages."""

    def test_reject_missing_config(self, temp_dir: Path) -> None:
        """Reject submission missing adapter_config.json."""
        zip_path = create_test_zip(temp_dir, include_config=False)

        report = validate_submission_zip(zip_path)

        assert report.valid is False
        assert any("adapter_config.json" in err for err in report.errors)

    def test_reject_missing_weights(self, temp_dir: Path) -> None:
        """Reject submission missing adapter weights."""
        zip_path = create_test_zip(temp_dir, include_weights=False)

        report = validate_submission_zip(zip_path)

        assert report.valid is False
        assert any("weight" in err.lower() for err in report.errors)

    def test_reject_rank_33(self, temp_dir: Path) -> None:
        """Reject submission with rank > 32."""
        zip_path = create_test_zip(temp_dir, config_content={"r": 33})

        report = validate_submission_zip(zip_path)

        assert report.valid is False
        assert any("rank" in err.lower() and "33" in err for err in report.errors)

    def test_reject_rank_64(self, temp_dir: Path) -> None:
        """Reject submission with rank = 64."""
        zip_path = create_test_zip(temp_dir, config_content={"r": 64})

        report = validate_submission_zip(zip_path)

        assert report.valid is False
        assert any("rank" in err.lower() for err in report.errors)

    def test_reject_invalid_json(self, temp_dir: Path) -> None:
        """Reject submission with invalid JSON config."""
        zip_path = temp_dir / "submission.zip"

        with zipfile.ZipFile(zip_path, "w") as zf:
            zf.writestr("adapter_config.json", "not valid json {{{")
            zf.writestr("adapter_model.safetensors", b"dummy")

        report = validate_submission_zip(zip_path)

        assert report.valid is False
        assert any("json" in err.lower() for err in report.errors)

    def test_reject_non_zip_file(self, temp_dir: Path) -> None:
        """Reject file that is not a .zip."""
        txt_path = temp_dir / "submission.txt"
        txt_path.write_text("not a zip")

        report = validate_submission_zip(txt_path)

        assert report.valid is False
        assert any(".zip" in err for err in report.errors)

    def test_reject_nonexistent_file(self, temp_dir: Path) -> None:
        """Reject nonexistent file."""
        fake_path = temp_dir / "does_not_exist.zip"

        report = validate_submission_zip(fake_path)

        assert report.valid is False
        assert any("exist" in err.lower() for err in report.errors)

    def test_reject_corrupted_zip(self, temp_dir: Path) -> None:
        """Reject corrupted zip file."""
        bad_zip = temp_dir / "submission.zip"
        bad_zip.write_bytes(b"not a real zip file content")

        report = validate_submission_zip(bad_zip)

        assert report.valid is False


class TestWarnings:
    """Tests for warning conditions."""

    def test_warn_full_model_file(self, temp_dir: Path) -> None:
        """Warn when full-model files are present."""
        zip_path = create_test_zip(
            temp_dir,
            extra_files={"pytorch_model.bin": b"suspicious"},
        )

        report = validate_submission_zip(zip_path)

        # Should still be valid but with warning
        assert report.valid is True
        assert any("pytorch_model.bin" in warn for warn in report.warnings)

    def test_warn_model_safetensors(self, temp_dir: Path) -> None:
        """Warn when model.safetensors is present."""
        zip_path = create_test_zip(
            temp_dir,
            extra_files={"model.safetensors": b"suspicious"},
        )

        report = validate_submission_zip(zip_path)

        assert report.valid is True
        assert any("model.safetensors" in warn for warn in report.warnings)

    def test_warn_unknown_rank(self, temp_dir: Path) -> None:
        """Warn when rank cannot be determined."""
        config = {"base_model": "test", "no_rank_field": True}
        zip_path = create_test_zip(temp_dir, config_content=config)

        report = validate_submission_zip(zip_path)

        # Valid but with warning about unknown rank
        assert report.valid is True
        assert report.rank is None
        assert any("rank" in warn.lower() for warn in report.warnings)


class TestSHA256:
    """Tests for SHA256 hash computation."""

    def test_sha256_computed(self, temp_dir: Path) -> None:
        """SHA256 is computed for valid zip."""
        zip_path = create_test_zip(temp_dir)

        report = validate_submission_zip(zip_path)

        assert report.sha256
        assert len(report.sha256) == 64  # SHA256 hex length
        assert all(c in "0123456789abcdef" for c in report.sha256)

    def test_sha256_deterministic(self, temp_dir: Path) -> None:
        """SHA256 is deterministic for same file."""
        zip_path = create_test_zip(temp_dir)

        report1 = validate_submission_zip(zip_path)
        report2 = validate_submission_zip(zip_path)

        assert report1.sha256 == report2.sha256


class TestReportSerialization:
    """Tests for report JSON serialization."""

    def test_to_dict(self, temp_dir: Path) -> None:
        """Report converts to dictionary."""
        zip_path = create_test_zip(temp_dir)

        report = validate_submission_zip(zip_path)
        d = report.to_dict()

        assert isinstance(d, dict)
        assert d["valid"] is True
        assert d["result"] == "valid"
        assert isinstance(d["errors"], list)
        assert isinstance(d["warnings"], list)
        assert isinstance(d["files"], list)

    def test_to_json(self, temp_dir: Path) -> None:
        """Report converts to JSON string."""
        zip_path = create_test_zip(temp_dir)

        report = validate_submission_zip(zip_path)
        json_str = report.to_json()

        # Should be valid JSON
        parsed = json.loads(json_str)
        assert parsed["valid"] is True


class TestLenientMode:
    """Tests for lenient (non-strict) validation mode."""

    def test_lenient_missing_config(self, temp_dir: Path) -> None:
        """Lenient mode treats missing config as warning."""
        zip_path = create_test_zip(temp_dir, include_config=False)

        report = validate_submission_zip(zip_path, strict=False)

        # In lenient mode, missing files are warnings, not errors
        assert any("adapter_config.json" in warn for warn in report.warnings)

    def test_lenient_missing_weights(self, temp_dir: Path) -> None:
        """Lenient mode treats missing weights as warning."""
        zip_path = create_test_zip(temp_dir, include_weights=False)

        report = validate_submission_zip(zip_path, strict=False)

        assert any("weight" in warn.lower() for warn in report.warnings)


class TestAlternateWeightFiles:
    """Tests for alternate weight file names."""

    def test_adapter_model_bin(self, temp_dir: Path) -> None:
        """Accept adapter_model.bin as weight file."""
        zip_path = create_test_zip(
            temp_dir,
            weight_filename="adapter_model.bin",
        )

        report = validate_submission_zip(zip_path)

        assert report.valid is True

    def test_other_safetensors_file(self, temp_dir: Path) -> None:
        """Accept other .safetensors files as weights."""
        zip_path = create_test_zip(
            temp_dir,
            weight_filename="lora_weights.safetensors",
        )

        report = validate_submission_zip(zip_path)

        assert report.valid is True


class TestRankDetection:
    """Tests for rank detection from various config formats."""

    def test_rank_from_r_field(self, temp_dir: Path) -> None:
        """Detect rank from 'r' field."""
        zip_path = create_test_zip(temp_dir, config_content={"r": 16})
        report = validate_submission_zip(zip_path)
        assert report.rank == 16

    def test_rank_from_rank_field(self, temp_dir: Path) -> None:
        """Detect rank from 'rank' field."""
        zip_path = create_test_zip(temp_dir, config_content={"rank": 24})
        report = validate_submission_zip(zip_path)
        assert report.rank == 24

    def test_rank_from_lora_r_field(self, temp_dir: Path) -> None:
        """Detect rank from 'lora_r' field."""
        zip_path = create_test_zip(temp_dir, config_content={"lora_r": 8})
        report = validate_submission_zip(zip_path)
        assert report.rank == 8

    def test_rank_from_nested_lora_config(self, temp_dir: Path) -> None:
        """Detect rank from nested lora_config."""
        config = {"lora_config": {"r": 32}}
        zip_path = create_test_zip(temp_dir, config_content=config)
        report = validate_submission_zip(zip_path)
        assert report.rank == 32
