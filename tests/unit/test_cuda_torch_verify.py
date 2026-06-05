"""Unit tests for CUDA PyTorch verification helpers (no GPU required)."""

from __future__ import annotations

from forge_nemotron.readiness.cuda_torch_verify import (
    build_cuda_torch_report,
    classify_cuda_torch_environment,
    parse_nvidia_smi_cuda_version,
    run_tiny_cuda_smoke,
)


class TestParseNvidiaSmiCudaVersion:
    def test_extracts_cuda_version(self) -> None:
        text = "| NVIDIA-SMI 591.86                 Driver Version: 591.86         CUDA Version: 12.8     |"
        assert parse_nvidia_smi_cuda_version(text) == "12.8"

    def test_missing_returns_none(self) -> None:
        assert parse_nvidia_smi_cuda_version("no cuda here") is None


class TestClassifyCudaTorchEnvironment:
    def test_install_failed(self) -> None:
        assert (
            classify_cuda_torch_environment(
                nvidia_smi_available=True,
                torch_installed=False,
                cuda_available=False,
                install_failed=True,
            )
            == "blocked_install_failed"
        )

    def test_not_visible(self) -> None:
        assert (
            classify_cuda_torch_environment(
                nvidia_smi_available=False,
                torch_installed=True,
                cuda_available=False,
            )
            == "not_visible"
        )

    def test_visible_no_torch_cuda(self) -> None:
        assert (
            classify_cuda_torch_environment(
                nvidia_smi_available=True,
                torch_installed=True,
                cuda_available=False,
            )
            == "visible_no_torch_cuda"
        )

    def test_cuda_ready_probe_only_without_smoke(self) -> None:
        assert (
            classify_cuda_torch_environment(
                nvidia_smi_available=True,
                torch_installed=True,
                cuda_available=True,
                tiny_smoke_passed=None,
            )
            == "cuda_ready_probe_only"
        )

    def test_cuda_smoke_failed(self) -> None:
        assert (
            classify_cuda_torch_environment(
                nvidia_smi_available=True,
                torch_installed=True,
                cuda_available=True,
                tiny_smoke_passed=False,
            )
            == "cuda_smoke_failed"
        )


class TestBuildReportWithoutGpu:
    def test_report_structure(self) -> None:
        report = build_cuda_torch_report(environment_path=".venv_cuda")
        assert report["environment_path"] == ".venv_cuda"
        assert "timestamp_utc" in report
        assert "classification" in report
        assert "no model load" in report["notes"]

    def test_tiny_smoke_on_cpu_only_does_not_crash(self) -> None:
        smoke = run_tiny_cuda_smoke()
        assert "passed" in smoke
