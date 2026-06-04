# M01_plan.md — Public Control Reproduction Foundation

## Milestone

**Milestone:** M01  
**Title:** Public Control Reproduction Foundation  
**Branch:** `forge/M01-control-baseline`  
**Status:** **closed** — PR [#2](https://github.com/m-cahill/forge/pull/2); CI green; awaiting merge permission  
**Precondition:** M00 is merged to `main` (commit `27d0fed5b62cd3dbef95f8ba32afc6ef4e96d408`)  
**Primary goal:** Build the local metric, package validation, baseline-intake, and CI foundation required before any public control adapter submission.
**CI Strategy:** Option A — minimal CI in M01 (owner authorized)

---

## 1. Objective

M01 establishes the minimum trustworthy control-reproduction foundation for FORGE.

By the end of M01, the repo should have:

1. An installable Python package (`forge_nemotron`) without requiring ad hoc `PYTHONPATH=src`.
2. Minimal CI that runs on pull requests and proves nonzero tests execute.
3. A boxed-answer extraction and scoring module aligned with the competition's `\boxed{...}` final-answer requirement.
4. A structural LoRA `submission.zip` validator that rejects common invalid packages before Kaggle upload.
5. A documented public-baseline intake for `tonghuikang/nemotron`.
6. A Kaggle debug/probe notebook template with many diagnostic cells, committed in the repo and intended for reupload/resync to Kaggle.
7. Updated `docs/forge.md` and milestone artifacts.

M01 must **not** claim:
- a reproduced control baseline,
- a valid Kaggle submission,
- a public score,
- model training success,
- model inference quality,
- private leaderboard readiness.

M00's audit explicitly identified CI and editable package wiring as deferred follow-up items. M01 resolves those two local engineering gaps before any serious control submission work.

---

## 2. Required source context

Cursor must read these first:

- `docs/forge.md`
- `docs/FORGE_ANCHOR.md`
- `docs/kaggle_submission_bible.md`
- `docs/kaggle/notebook_debug_standard.md`
- `docs/kaggle/kaggle_setup_evidence.md`
- `docs/milestones/M00/M00_summary.md`
- `docs/milestones/M00/M00_audit.md`
- `docs/milestones/M01/M01_plan.md`

External references:

- Kaggle competition page: confirms LoRA adapter rank ≤32 packaged as `submission.zip`.
- `tonghuikang/nemotron`: recommended public Progress Prize control baseline.

---

## 3. Hard constraints

### 3.1 M00 merge / branch discipline

Before starting implementation:

1. Confirm whether M00 has been merged to `main`. ✓ Merged (`27d0fed`)
2. Branch from updated `main` or continue on existing `forge/M01-control-baseline`. ✓ Continuing on existing branch

Do not push new commits to the closed M00 branch.

### 3.2 Kaggle owner-action blockers

Do not attempt a Kaggle submission unless the owner has provided and recorded:

* daily submission limit,
* rules accepted / team joined status,
* any additional Submit UI constraints.

M00 left these as authenticated owner-action blockers. They affect submission budgeting and eligibility.

### 3.3 Notebook workflow

Do not edit notebooks directly on the Kaggle website as the default workflow.

Required workflow:

```text
Cursor edits notebook in repo
  → commit
  → owner/operator reuploads or resyncs to Kaggle
  → evidence recorded
```

Kaggle-site-only edits are emergency-only and must be backported into the repo before becoming project truth.

### 3.4 Public baseline code policy

Do not copy code from `tonghuikang/nemotron` into FORGE until license and permitted-use status are explicitly reviewed and documented.

M01 may:

* inspect the repo,
* document structure and commands,
* record reproducibility notes,
* implement clean-room equivalents for FORGE-owned metric/validator code,
* optionally create wrapper notes or scripts that assume the public repo exists outside FORGE.

M01 must not:

* vendor the repo,
* add it as a submodule,
* copy large artifacts,
* claim reproduction without a run manifest and evidence.

---

## 4. Scope

### In scope

* Create/update `pyproject.toml`.
* Add minimal dev dependencies.
* Add minimal CI workflow.
* Add import/test sanity checks.
* Implement boxed-answer extraction and scoring helpers.
* Implement structural `submission.zip` validator.
* Add tests for metric and validator behavior.
* Create a public baseline intake document.
* Create a Kaggle debug/probe notebook template.
* Update `docs/forge.md`.
* Update/expand `docs/milestones/M01/M01_plan.md`.
* Create `docs/milestones/M01/M01_toolcalls.md`.

### Out of scope

* Full 30B model training.
* Real LoRA adapter training.
* Kaggle upload/submission.
* Public leaderboard score.
* Reproducing `tonghuikang/nemotron` end-to-end.
* Adapter merge/compression.
* Synthetic solver factory.
* RL.
* Public notebook/write-up finalization.

---

## 5. Deliverables

## 5.1 Package and developer experience

Create `pyproject.toml` with minimal package metadata and tooling.

Recommended minimum:

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "forge-nemotron"
version = "0.1.0"
description = "FORGE utilities for NVIDIA Nemotron Model Reasoning Challenge"
requires-python = ">=3.10"
readme = "README.md"

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-q"

[tool.ruff]
line-length = 100
target-version = "py310"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]

[tool.mypy]
python_version = "3.10"
ignore_missing_imports = true
check_untyped_defs = true
warn_unused_ignores = true
no_implicit_optional = true
strict_equality = true
```

Add `requirements-dev.txt` if absent, with minimal M01 dependencies:

```text
pytest
ruff
mypy
```

Acceptance:

```bash
python -m pip install -e .
python - <<'PY'
import forge_nemotron
print(forge_nemotron.__version__)
PY
```

No `PYTHONPATH=src` should be required after this deliverable.

---

## 5.2 Minimal CI

Create `.github/workflows/ci.yml`.

Keep it small. Do not implement the full enterprise/security stack yet unless explicitly authorized.

Recommended:

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python: ["3.10", "3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python }}
          cache: "pip"
      - run: python -m pip install --upgrade pip
      - run: python -m pip install -e . -r requirements-dev.txt
      - name: Ruff
        run: |
          ruff check .
          ruff format --check .
      - name: MyPy
        run: mypy src tests
      - name: Pytest
        run: pytest
      - name: Summary
        if: always()
        run: |
          echo "## M01 CI" >> "$GITHUB_STEP_SUMMARY"
          echo "- Python: ${{ matrix.python }}" >> "$GITHUB_STEP_SUMMARY"
          echo "- Ruff, mypy, pytest completed." >> "$GITHUB_STEP_SUMMARY"
```

Acceptance:

* CI workflow file exists.
* Local equivalent commands pass.
* `docs/forge.md` records CI as configured but not green until a GitHub run actually passes.
* If a PR workflow run is available, record run ID/status in `docs/forge.md`.

---

## 5.3 Boxed-answer metric module

Create package area:

```text
src/forge_nemotron/metric/
  __init__.py
  boxed.py
```

Implement functions such as:

```python
extract_boxed_answers(text: str) -> list[str]
extract_final_boxed_answer(text: str) -> str | None
normalize_answer(answer: str) -> str
is_numeric_close(predicted: str, expected: str, rel_tol: float = 1e-4, abs_tol: float = 1e-8) -> bool
answers_match(predicted: str, expected: str) -> bool
score_prediction(completion: str, expected: str) -> bool
```

Behavior requirements:

* Extract final answer from the last valid `\boxed{...}` occurrence.
* Handle whitespace around answers.
* Handle malformed text without crashing.
* Support exact string matching after normalization.
* Support numeric tolerance for plain numeric answers.
* Do not evaluate arbitrary Python expressions.
* Do not use `eval`.
* Do not rely on model output format beyond `\boxed{...}`.

Tests:

```text
tests/unit/test_metric_boxed.py
```

Test cases:

* one boxed answer,
* multiple boxed answers uses final,
* missing boxed answer,
* malformed boxed expression,
* nested braces if implemented or documented as unsupported,
* exact string match,
* numeric tolerance match,
* numeric mismatch,
* whitespace normalization,
* answer extractor does not crash on random/malformed strings.

Acceptance:

```bash
pytest tests/unit/test_metric_boxed.py -q
```

---

## 5.4 Structural LoRA package validator

Create:

```text
src/forge_nemotron/packaging/
  __init__.py
  validate_submission.py
scripts/validate_submission.py
tests/unit/test_package_validator.py
```

Validator purpose:

Validate local candidate `submission.zip` structure before any Kaggle upload.

Minimum validation:

* Input file exists.
* Input file is `.zip`.
* Zip can be opened.
* Contains `adapter_config.json`.
* Contains at least one plausible adapter weight file:

  * `adapter_model.safetensors`, or
  * another `.safetensors` file documented as adapter weights.
* Parses `adapter_config.json`.
* Detects LoRA rank from common fields such as `r`, `rank`, or documented nested config.
* Rejects rank > 32.
* Warns/rejects likely full-model files:

  * `pytorch_model.bin`
  * `model.safetensors`
  * huge unrelated files if size is available and threshold configured.
* Emits a structured report with:

  * `valid`
  * `errors`
  * `warnings`
  * `rank`
  * `files`
  * `sha256`

Important:

* Fixture packages used in tests are **structural fixtures only**, not Kaggle-valid adapters.
* Validator pass on a fixture must not be worded as "Kaggle-ready."
* Real package readiness requires actual adapter files and later evidence.

CLI:

```bash
python scripts/validate_submission.py path/to/submission.zip
```

or:

```bash
python -m forge_nemotron.packaging.validate_submission path/to/submission.zip
```

Tests:

* accepts rank-32 structural fixture,
* rejects missing `adapter_config.json`,
* rejects missing adapter weights,
* rejects rank 33,
* rejects invalid JSON,
* computes SHA256,
* reports warnings/errors deterministically.

Acceptance:

```bash
pytest tests/unit/test_package_validator.py -q
```

---

## 5.5 Public baseline intake document

Create:

```text
docs/milestones/M01/public_baseline_intake.md
```

Document:

* Public repo URL: `https://github.com/tonghuikang/nemotron`
* Claimed purpose: Progress Prize winning submission.
* Repo elements observed:

  * `reasoning.py`
  * `augmentation.py`
  * `corpus.py`
  * `train_sft.py`
  * `upload_adapter.py`
  * training/dashboard/static artifacts
* Commands documented in README:

  * `uv run python3 reasoning.py`
  * `uv run python3 augmentation.py`
  * `uv run python3 corpus.py`
  * `uv run python3 train_sft.py`
  * `uv run modal run upload_adapter.py`
* License status:

  * record whether a license file exists.
  * if unclear/absent, state "do not copy code; use clean-room implementation or external wrapper only unless license clarified."
* Reproduction blockers:

  * dependencies,
  * compute,
  * external services such as Modal/Tinker if required,
  * Kaggle owner-action blockers,
  * adapter/package availability.
* Recommended M01/M02 next actions:

  * metric alignment first,
  * package validation first,
  * then controlled reproduction attempt.

Acceptance:

* Baseline intake doc exists.
* It makes no reproduction claim.
* It does not vendor or copy public repo code.
* It records license/copying posture.

---

## 5.6 Kaggle debug/probe notebook template

Create a notebook under:

```text
notebooks/forge_m01_kaggle_debug_probe.ipynb
```

Purpose:

* environment/path/debug probe only,
* no Kaggle submission,
* no model training,
* no model inference claim,
* no package-validity claim.

Notebook should include output-cleared cells for:

1. Run mode declaration.
2. Python/platform/cwd/sys.path.
3. Kaggle env vars.
4. `/kaggle`, `/kaggle/input`, `/kaggle/working` existence and listings.
5. Disk free space.
6. GPU visibility / `nvidia-smi`.
7. Torch/CUDA import/version if available, without requiring torch.
8. Competition/model/dataset path discovery.
9. Output artifact test path under `/kaggle/working/tmp/forge_debug/`.
10. SHA256 helper.
11. Timing helper.
12. Exception/traceback helper.

The notebook must clearly say:

```text
This is an environment probe only. It does not produce a scored submission and does not prove Kaggle submission readiness.
```

Acceptance:

* Notebook committed in repo.
* No outputs committed unless intentionally minimal and safe.
* Notebook follows `docs/kaggle/notebook_debug_standard.md`.
* README or docs link to it.

---

## 5.7 Documentation updates

Update:

* `docs/forge.md`
* `README.md`
* `docs/milestones/M01/M01_plan.md`
* `docs/milestones/M01/M01_toolcalls.md`
* `docs/kaggle/kaggle_setup_evidence.md` only if owner provides new authenticated facts or a debug notebook run occurs.

`docs/forge.md` updates should include:

* Active milestone set to M01.
* M01 branch.
* M01 planned deliverables.
* If `pyproject.toml` is completed, mark DEF-006 resolved or update risk table.
* If CI is added, update DEF-005 status to configured / pending run / green if verified.
* Owner-action blockers remain unchanged unless owner supplies evidence.
* No run/submission ledgers updated unless actual run/submission evidence exists.

---

## 6. Implementation phases

### Phase A — Branch and milestone setup

1. Confirm M00 merge/authorization. ✓
2. Create branch `forge/M01-control-baseline`. ✓ (exists)
3. Expand `docs/milestones/M01/M01_plan.md` with this plan. ✓
4. Create `docs/milestones/M01/M01_toolcalls.md`. ✓ (exists)
5. Update `docs/forge.md` Active milestone to M01.

Expected commit:

```bash
git add docs/forge.md docs/milestones/M01/
git commit -m "docs(milestones): expand M01 public control plan"
```

---

### Phase B — Package install and CI foundation

1. Add `pyproject.toml`.
2. Add `requirements-dev.txt`.
3. Add minimal CI workflow.
4. Add `tests/unit/test_import.py`.

Expected verification:

```bash
python -m pip install -e . -r requirements-dev.txt
ruff check .
ruff format --check .
mypy src tests
pytest
```

Expected commit:

```bash
git add pyproject.toml requirements-dev.txt .github/workflows/ci.yml tests/unit/test_import.py
git commit -m "chore(ci): add package metadata and minimal CI"
```

---

### Phase C — Boxed-answer metric

1. Implement `forge_nemotron.metric.boxed`.
2. Add unit tests.
3. Update package exports if appropriate.

Expected verification:

```bash
pytest tests/unit/test_metric_boxed.py -q
pytest -q
```

Expected commit:

```bash
git add src/forge_nemotron/metric tests/unit/test_metric_boxed.py
git commit -m "feat(metric): add boxed answer extraction and scoring"
```

---

### Phase D — Submission package validator

1. Implement validator.
2. Add script wrapper.
3. Add fixture generation in tests.
4. Add unit tests.

Expected verification:

```bash
pytest tests/unit/test_package_validator.py -q
python scripts/validate_submission.py <test_fixture_zip_if_created>
pytest -q
```

Expected commit:

```bash
git add src/forge_nemotron/packaging scripts/validate_submission.py tests/unit/test_package_validator.py
git commit -m "feat(packaging): add LoRA submission zip validator"
```

---

### Phase E — Public baseline intake

1. Inspect `tonghuikang/nemotron`.
2. Create `docs/milestones/M01/public_baseline_intake.md`.
3. Record license/copying posture.
4. Record reproduction blockers and safe next steps.

Expected commit:

```bash
git add docs/milestones/M01/public_baseline_intake.md
git commit -m "docs(baseline): document public control repository intake"
```

---

### Phase F — Kaggle debug notebook shell

1. Create `notebooks/forge_m01_kaggle_debug_probe.ipynb`.
2. Ensure outputs are cleared.
3. Link it from `notebooks/README.md` if useful.
4. Do not upload to Kaggle unless explicitly authorized.

Expected commit:

```bash
git add notebooks/forge_m01_kaggle_debug_probe.ipynb notebooks/README.md
git commit -m "docs(notebooks): add Kaggle debug probe notebook"
```

---

### Phase G — Final verification and closeout prep

Run:

```bash
git status --short
python -m pip install -e . -r requirements-dev.txt
ruff check .
ruff format --check .
mypy src tests
pytest -q
python -m compileall src
python - <<'PY'
import forge_nemotron
print("forge_nemotron import ok")
PY
```

If CI runs on GitHub, capture:

```bash
gh run list --branch forge/M01-control-baseline --limit 5
```

Do not close M01 until docs are updated and verification evidence is recorded.

---

## 7. Acceptance criteria

M01 is complete only when:

- [x] `forge/M01-control-baseline` branch exists from an authorized base.
- [x] `docs/milestones/M01/M01_plan.md` is expanded.
- [x] `docs/milestones/M01/M01_toolcalls.md` exists.
- [x] `pyproject.toml` exists.
- [x] `pip install -e .` works.
- [x] Importing `forge_nemotron` works without `PYTHONPATH`.
- [x] Minimal CI workflow exists.
- [x] `pytest` collects and runs nonzero tests (91).
- [x] Boxed-answer metric helpers exist.
- [x] Metric unit tests pass.
- [x] Structural `submission.zip` validator exists.
- [x] Validator unit tests pass, including rank >32 rejection.
- [x] Public baseline intake doc exists.
- [x] Baseline intake makes no reproduction claim.
- [x] Baseline intake documents license/copying posture.
- [x] Kaggle debug/probe notebook exists in repo.
- [x] Notebook follows debug standard and has no scored-submission claim.
- [x] `docs/forge.md` is updated.
- [x] No Kaggle submission is attempted unless separately authorized.
- [x] No public score is claimed.
- [x] Owner-action Kaggle blockers remain explicit unless resolved with evidence (BQ-001, BQ-003 open).

---

## 8. Optional stretch goals

Only attempt these if all required acceptance criteria are complete and time remains:

1. Add coverage reporting locally, without enforcing high thresholds yet.
2. Add a tiny JSON report output from package validator.
3. Add metric CLI for scoring a JSONL fixture.
4. Add a non-Kaggle structural fixture package under `tests/fixtures/`.

Do not add heavy dependency locking, full security scanning, adapter training, or notebook upload in M01 unless explicitly authorized.

---

## 9. Risks and handling

| Risk                                       | Handling                                              |
| ------------------------------------------ | ----------------------------------------------------- |
| M00 not merged                             | Stop or request explicit branch authorization         |
| CI too large for M01                       | Keep CI minimal: ruff, mypy, pytest                   |
| Public baseline license unclear            | Do not copy code; document clean-room/wrapper posture |
| Validator fixture mistaken as Kaggle-ready | Label tests as structural fixture only                |
| Kaggle owner-action blockers unresolved    | Do not submit; document blocker                       |
| Notebook uploaded directly on Kaggle       | Backport to repo immediately before treating as truth |
| Metric edge cases ambiguous                | Document known unsupported cases and add tests        |

---

## 10. Closeout prompt for Cursor

Use this when M01 implementation is complete:

```markdown
Close out milestone M01.

Tasks:
1. Ensure all documentation is updated as necessary.
2. Update `docs/forge.md` with completed work, decisions, CI/local verification status, unresolved blockers, risks, and next recommendation.
3. Create `docs/milestones/M01/M01_summary.md` using `docs/prompts/summaryprompt.md`.
4. Create `docs/milestones/M01/M01_audit.md` using `docs/prompts/unifiedmilestoneauditpromptV2.md`.
5. If GitHub Actions ran, analyze the workflow using `docs/prompts/workflowprompt.md` and create `docs/milestones/M01/M01_run1.md` or equivalent workflow evidence.
6. Confirm every acceptance criterion from `docs/milestones/M01/M01_plan.md` is satisfied or explicitly deferred with rationale and exit criteria.
7. Confirm no Kaggle submission, public score, training success, model inference, or reproduced-baseline claim is made without evidence.
8. Confirm owner-action blockers BQ-001 and BQ-003 are either resolved with evidence or remain explicitly blocked before any Kaggle submission.
9. Confirm the package validator rejects rank >32 and missing required files.
10. Confirm `pip install -e .`, `ruff check .`, `ruff format --check .`, `mypy src tests`, and `pytest -q` pass locally.
11. Confirm CI status and include run IDs if CI exists.
12. Prepare PR instructions for `forge/M01-control-baseline` → `main`.
13. Seed `docs/milestones/M02/M02_plan.md` as a stub for Exact local evaluation and artifact discipline.
14. Create `docs/milestones/M02/M02_toolcalls.md` if that convention remains active.
15. Do not merge, push extra closeout changes, start M02, upload to Kaggle, or submit anything without explicit user permission.
```
