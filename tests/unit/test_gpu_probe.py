"""Unit tests for local GPU probe parsing (no GPU required)."""

from __future__ import annotations

from forge_nemotron.readiness.gpu_probe import (
    build_probe_report,
    parse_nvidia_smi_csv_line,
    probe_torch_cuda,
    run_nvidia_smi,
)


class TestParseNvidiaSmi:
    def test_valid_line(self) -> None:
        parsed = parse_nvidia_smi_csv_line("NVIDIA GeForce RTX 5090, 32607, 570.00")
        assert parsed == {
            "gpu_name": "NVIDIA GeForce RTX 5090",
            "vram_total": "32607",
            "driver_version": "570.00",
        }

    def test_empty_line_returns_none(self) -> None:
        assert parse_nvidia_smi_csv_line("   ") is None

    def test_short_line_returns_none(self) -> None:
        assert parse_nvidia_smi_csv_line("GPU only") is None


class TestProbeWithoutGpu:
    def test_build_probe_report_structure(self) -> None:
        report = build_probe_report(machine="local_5090")
        assert report["machine"] == "local_5090"
        assert "probe_date_utc" in report
        assert "platform" in report
        assert "nvidia_smi" in report
        assert "torch" in report
        assert "no model load" in report["notes"]

    def test_run_nvidia_smi_when_missing_binary(self, monkeypatch) -> None:
        monkeypatch.setattr("forge_nemotron.readiness.gpu_probe.shutil.which", lambda _: None)
        result = run_nvidia_smi()
        assert result["available"] is False

    def test_probe_torch_cuda_returns_dict(self) -> None:
        result = probe_torch_cuda()
        assert "torch_installed" in result
