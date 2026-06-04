"""Basic import and version sanity tests for forge_nemotron package."""

from __future__ import annotations


def test_package_imports() -> None:
    """Verify the forge_nemotron package can be imported."""
    import forge_nemotron

    assert forge_nemotron is not None


def test_version_exists() -> None:
    """Verify __version__ is set and non-empty."""
    import forge_nemotron

    assert hasattr(forge_nemotron, "__version__")
    assert forge_nemotron.__version__
    assert isinstance(forge_nemotron.__version__, str)


def test_version_format() -> None:
    """Verify __version__ follows semver-like format."""
    import forge_nemotron

    version = forge_nemotron.__version__
    parts = version.split(".")
    assert len(parts) >= 2, f"Version {version} should have at least major.minor"
    assert parts[0].isdigit(), f"Major version should be numeric: {parts[0]}"
    assert parts[1].isdigit(), f"Minor version should be numeric: {parts[1]}"
