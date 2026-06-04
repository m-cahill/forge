"""Structural validator for LoRA submission.zip packages.

This module validates local candidate submission.zip packages before any
Kaggle upload. It performs structural checks only and does NOT claim
full Kaggle compatibility or vLLM load success.

Validation checks:
- File exists and is a .zip
- Zip can be opened and read
- Contains adapter_config.json
- Contains adapter weight file (adapter_model.safetensors or similar)
- LoRA rank from config is <= 32
- No obviously full-model files (pytorch_model.bin, model.safetensors)
- No files exceeding size threshold

Important: Passing validation does NOT guarantee Kaggle acceptance.
Real adapter validity requires actual Kaggle submission and scoring.
"""

from __future__ import annotations

import hashlib
import json
import zipfile
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any

# Expected adapter weight file names (PEFT convention)
EXPECTED_WEIGHT_FILES = {
    "adapter_model.safetensors",
    "adapter_model.bin",
}

# Files that indicate a full model (should not be in adapter-only submission)
FULL_MODEL_FILES = {
    "pytorch_model.bin",
    "model.safetensors",
    "model.bin",
}

# Default size threshold for suspicious large files (500 MB)
DEFAULT_SIZE_THRESHOLD_BYTES = 500 * 1024 * 1024

# Maximum allowed LoRA rank per competition rules
MAX_LORA_RANK = 32


class ValidationResult(Enum):
    """Validation outcome status."""

    VALID = "valid"
    INVALID = "invalid"
    WARNING = "warning"


@dataclass
class ValidationReport:
    """Structured report from submission validation.

    Attributes:
        valid: Whether the submission passes all required checks
        result: Overall validation status
        errors: List of critical errors that fail validation
        warnings: List of non-fatal warnings
        rank: Detected LoRA rank, or None if not found
        files: List of files in the zip
        sha256: SHA256 hash of the submission.zip file
        adapter_config: Parsed adapter_config.json content, or None
    """

    valid: bool
    result: ValidationResult
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    rank: int | None = None
    files: list[str] = field(default_factory=list)
    sha256: str = ""
    adapter_config: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert report to dictionary for JSON serialization."""
        return {
            "valid": self.valid,
            "result": self.result.value,
            "errors": self.errors,
            "warnings": self.warnings,
            "rank": self.rank,
            "files": self.files,
            "sha256": self.sha256,
            "adapter_config": self.adapter_config,
        }

    def to_json(self) -> str:
        """Convert report to JSON string."""
        return json.dumps(self.to_dict(), indent=2)


def _compute_file_sha256(path: Path) -> str:
    """Compute SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()


def _extract_rank_from_config(config: dict[str, Any]) -> int | None:
    """Extract LoRA rank from adapter config.

    Checks common fields where rank may be stored:
    - "r" (PEFT convention)
    - "rank"
    - "lora_r"
    - Nested under "peft_config" or "lora_config"

    Args:
        config: Parsed adapter_config.json content

    Returns:
        Detected rank as integer, or None if not found
    """
    # Direct rank fields
    for key in ["r", "rank", "lora_r"]:
        if key in config:
            try:
                return int(config[key])
            except (ValueError, TypeError):
                pass

    # Check nested configs
    for nested_key in ["peft_config", "lora_config", "config"]:
        if nested_key in config and isinstance(config[nested_key], dict):
            nested = config[nested_key]
            for key in ["r", "rank", "lora_r"]:
                if key in nested:
                    try:
                        return int(nested[key])
                    except (ValueError, TypeError):
                        pass

    return None


def validate_submission_zip(
    path: str | Path,
    *,
    size_threshold_bytes: int = DEFAULT_SIZE_THRESHOLD_BYTES,
    strict: bool = True,
) -> ValidationReport:
    """Validate a submission.zip package structure.

    Performs structural validation checks. Does NOT guarantee Kaggle
    acceptance or vLLM compatibility.

    Args:
        path: Path to the submission.zip file
        size_threshold_bytes: Threshold for warning about large files
        strict: If True, missing weights or config are errors; if False, warnings

    Returns:
        ValidationReport with validation results

    Examples:
        >>> report = validate_submission_zip("submission.zip")
        >>> if report.valid:
        ...     print(f"Valid submission, rank={report.rank}")
        >>> else:
        ...     print(f"Invalid: {report.errors}")
    """
    path = Path(path)
    errors: list[str] = []
    warnings: list[str] = []
    files: list[str] = []
    rank: int | None = None
    adapter_config: dict[str, Any] | None = None
    sha256 = ""

    # Check file exists
    if not path.exists():
        return ValidationReport(
            valid=False,
            result=ValidationResult.INVALID,
            errors=[f"File does not exist: {path}"],
        )

    # Check file is a .zip
    if path.suffix.lower() != ".zip":
        return ValidationReport(
            valid=False,
            result=ValidationResult.INVALID,
            errors=[f"File is not a .zip: {path.suffix}"],
        )

    # Compute SHA256
    try:
        sha256 = _compute_file_sha256(path)
    except OSError as e:
        warnings.append(f"Could not compute SHA256: {e}")

    # Try to open as zip
    try:
        with zipfile.ZipFile(path, "r") as zf:
            # Get file list
            files = zf.namelist()

            # Check for adapter_config.json
            has_config = "adapter_config.json" in files
            if not has_config:
                msg = "Missing required file: adapter_config.json"
                if strict:
                    errors.append(msg)
                else:
                    warnings.append(msg)

            # Check for adapter weights
            weight_files = [f for f in files if f in EXPECTED_WEIGHT_FILES]
            safetensor_files = [f for f in files if f.endswith(".safetensors")]

            has_weights = bool(weight_files) or bool(safetensor_files)
            if not has_weights:
                msg = "Missing adapter weight file (adapter_model.safetensors or similar)"
                if strict:
                    errors.append(msg)
                else:
                    warnings.append(msg)

            # Check for full-model files (should not be present)
            full_model_present = [f for f in files if f in FULL_MODEL_FILES]
            for fm in full_model_present:
                warnings.append(f"Suspicious full-model file present: {fm}")

            # Check for large files
            for info in zf.infolist():
                if info.file_size > size_threshold_bytes:
                    warnings.append(
                        f"Large file ({info.file_size / 1024 / 1024:.1f} MB): {info.filename}"
                    )

            # Parse adapter_config.json if present
            if has_config:
                try:
                    with zf.open("adapter_config.json") as cf:
                        adapter_config = json.load(cf)
                        rank = _extract_rank_from_config(adapter_config)

                        if rank is not None:
                            if rank > MAX_LORA_RANK:
                                errors.append(
                                    f"LoRA rank {rank} exceeds maximum allowed ({MAX_LORA_RANK})"
                                )
                        else:
                            warnings.append("Could not detect LoRA rank from adapter_config.json")

                except json.JSONDecodeError as e:
                    errors.append(f"Invalid JSON in adapter_config.json: {e}")
                except Exception as e:
                    errors.append(f"Error reading adapter_config.json: {e}")

    except zipfile.BadZipFile:
        return ValidationReport(
            valid=False,
            result=ValidationResult.INVALID,
            errors=["File is not a valid zip archive"],
        )
    except Exception as e:
        return ValidationReport(
            valid=False,
            result=ValidationResult.INVALID,
            errors=[f"Error opening zip file: {e}"],
        )

    # Determine overall validity
    is_valid = len(errors) == 0
    result = (
        ValidationResult.VALID
        if is_valid
        else ValidationResult.INVALID
        if errors
        else ValidationResult.WARNING
    )

    return ValidationReport(
        valid=is_valid,
        result=result,
        errors=errors,
        warnings=warnings,
        rank=rank,
        files=files,
        sha256=sha256,
        adapter_config=adapter_config,
    )


def main() -> int:
    """CLI entry point for submission validation."""
    import argparse

    parser = argparse.ArgumentParser(description="Validate LoRA submission.zip package structure")
    parser.add_argument("path", help="Path to submission.zip file")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON",
    )
    parser.add_argument(
        "--size-threshold",
        type=int,
        default=DEFAULT_SIZE_THRESHOLD_BYTES,
        help=f"Size threshold for large file warnings (bytes, default {DEFAULT_SIZE_THRESHOLD_BYTES})",
    )
    parser.add_argument(
        "--lenient",
        action="store_true",
        help="Treat missing files as warnings instead of errors",
    )

    args = parser.parse_args()

    report = validate_submission_zip(
        args.path,
        size_threshold_bytes=args.size_threshold,
        strict=not args.lenient,
    )

    if args.json:
        print(report.to_json())
    else:
        print(f"Validation: {'PASS' if report.valid else 'FAIL'}")
        print(f"SHA256: {report.sha256}")
        print(f"Rank: {report.rank if report.rank is not None else 'unknown'}")
        print(f"Files: {len(report.files)}")

        if report.errors:
            print("\nErrors:")
            for err in report.errors:
                print(f"  - {err}")

        if report.warnings:
            print("\nWarnings:")
            for warn in report.warnings:
                print(f"  - {warn}")

    return 0 if report.valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
