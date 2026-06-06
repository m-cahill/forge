"""Unit tests for CUDA training feasibility helpers (no GPU required)."""

from __future__ import annotations

from forge_nemotron.readiness.cuda_training_feasibility import (
    FEASIBILITY_CLASSIFICATION_VALUES,
    build_feasibility_report,
    build_tiny_mlp,
    classify_feasibility_result,
    run_training_feasibility_loop,
    snapshot_cuda_memory,
)


class TestClassifyFeasibilityResult:
    def test_pass_on_cuda_success(self) -> None:
        assert (
            classify_feasibility_result(
                success=True,
                cuda_available=True,
                device_requested="cuda",
            )
            == "cuda_training_feasibility_pass"
        )

    def test_failed_on_cuda_error(self) -> None:
        assert (
            classify_feasibility_result(
                success=False,
                cuda_available=True,
                device_requested="cuda",
            )
            == "cuda_training_feasibility_failed"
        )

    def test_cuda_unavailable(self) -> None:
        assert (
            classify_feasibility_result(
                success=False,
                cuda_available=False,
                device_requested="cuda",
            )
            == "cuda_unavailable"
        )

    def test_blocked(self) -> None:
        assert (
            classify_feasibility_result(
                success=False,
                cuda_available=True,
                device_requested="cuda",
                blocked=True,
            )
            == "blocked"
        )

    def test_classification_values_complete(self) -> None:
        expected = {
            "cuda_training_feasibility_pass",
            "cuda_training_feasibility_failed",
            "cuda_unavailable",
            "not_run",
            "blocked",
        }
        assert FEASIBILITY_CLASSIFICATION_VALUES == expected


class TestSnapshotCudaMemory:
    def test_cpu_device_returns_nulls(self) -> None:
        stats = snapshot_cuda_memory("cpu")
        assert stats["memory_allocated_bytes"] is None
        assert stats["memory_reserved_bytes"] is None


class TestTinyMlpLoop:
    def test_cpu_loop_completes_three_steps(self) -> None:
        result = run_training_feasibility_loop(device="cpu", steps=3, seed=0)
        assert result["steps_completed"] == 3
        assert len(result["step_records"]) == 3
        assert result["final_loss"] is not None

    def test_tiny_mlp_builds(self) -> None:
        model = build_tiny_mlp()
        assert len(list(model.parameters())) == 4


class TestBuildFeasibilityReport:
    def test_cuda_unavailable_without_cpu_ok(self) -> None:
        report = build_feasibility_report(device="cuda", steps=1, seed=0, cpu_ok=False)
        if not report["cuda"]["torch_cuda_is_available"]:
            assert report["result"]["classification"] == "cuda_unavailable"
            assert report["result"]["success"] is False

    def test_cpu_ok_runs_on_cpu_when_no_cuda(self) -> None:
        report = build_feasibility_report(device="cuda", steps=1, seed=0, cpu_ok=True)
        if not report["cuda"]["torch_cuda_is_available"]:
            assert report["cuda"]["device_used"] == "cpu"
        else:
            assert report["result"]["success"] is True

    def test_report_has_non_claims(self) -> None:
        report = build_feasibility_report(device="cpu", steps=1, seed=0)
        assert "not_baseline_training" in report["non_claims"]
        assert "feasibility loop only" in report["notes"]
