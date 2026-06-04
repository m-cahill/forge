# M01_plan.md — Control Baseline Preflight and Validation Harness

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M01 |
| **Title** | Control baseline preflight and validation harness |
| **Branch** | `forge/M01-control-baseline` |
| **Primary owner** | Cursor (implementation after owner authorization) |
| **Status** | planning — ready for review; **not implementing** until authorized |
| **Depends on** | M00 merged to `main` (complete) |
| **Baseline repo** | [tonghuikang/nemotron](https://github.com/tonghuikang/nemotron) (recommended; not reproduced) |

---

## 1. Objective

Establish the minimum executable control layer before reproducing or wrapping the public Progress Prize baseline: local `\boxed{...}` answer extraction, structural `submission.zip` validation contracts, read-only baseline-repo inspection notes, and a clear path to first control reproduction—**without training a model in M01**.

> M01 proves metric and packaging safety first. Full adapter reproduction and Kaggle submission are gated to later work within or after M01 only when validators pass and the owner authorizes submission.

---

## 2. Source-of-truth hierarchy

1. Kaggle competition rules, overview, evaluation, Submit UI  
2. `docs/forge.md` — Ultimate Truth  
3. `docs/FORGE_ANCHOR.md` — doctrine (canonical at `docs/`)  
4. `docs/kaggle_submission_bible.md` and `docs/kaggle/*`  
5. This plan and M01 milestone artifacts  
6. External baseline repo (inspection notes only until reproduced)

---

## 3. Scope

### In scope

- `src/forge_nemotron/metric/boxed_answer.py` — deterministic `\boxed{}` extraction  
- `tests/unit/test_boxed_answer.py`  
- `src/forge_nemotron/packaging/adapter_manifest.py` — manifest/dataclass for adapter/package metadata  
- `src/forge_nemotron/packaging/validate_submission.py` — structural zip validator (not full Kaggle validity claim)  
- `tests/unit/test_validate_submission.py` — zip fixture tests  
- `docs/baselines/tonghuikang_nemotron_inspection.md` — read-only inspection notes  
- Minimal `pyproject.toml` (or equivalent) so `pip install -e .` and `pytest` work without `PYTHONPATH=src`  
- **CI strategy decision** — implement minimal workflow in M01 **or** defer to M01A per owner choice (see § CI strategy)  
- Update `docs/forge.md` at M01 closeout with evidence, CI status, deferrals  

### Out of scope (M01)

- Model training (SFT, QLoRA, GRPO)  
- Kaggle submission or public score claims  
- Full reproduction of `tonghuikang/nemotron` adapter unless explicitly added with evidence  
- Solver implementation  
- Synthetic data generation  
- Claiming package is Kaggle-valid without validator + evidence  
- Resolving BQ-001 / BQ-003 without owner authenticated input  
- Editing notebooks on Kaggle site as default workflow  

---

## 4. Non-goals

- No leaderboard score  
- No “control reproduced” claim without adapter hash, local eval, and documented commands  
- No rank > 32 submission candidates  
- No holdout training  
- No fabricated daily submission limit or rules/team status  

---

## 5. Public baseline target

**Repository:** [tonghuikang/nemotron](https://github.com/tonghuikang/nemotron)  
**Claim level for M01:** inspection and alignment notes only unless reproduction is actually executed with recorded artifacts.

**Observed entry points (from public README; verify at implementation):**

- `reasoning.py`, `augmentation.py`, `corpus.py`  
- `train_sft.py`, `upload_adapter.py`  
- Training/dashboard flow referenced in Progress Prize materials  

**M01 inspection doc must record:**

- Clone URL and commit/tag inspected  
- Key files and commands  
- How they produce `submission.zip` / adapter layout  
- Gaps vs FORGE packaging contract  
- **No reproduction claim** unless artifacts exist  

---

## 6. Required reading

| Document | Purpose |
| -------- | ------- |
| `docs/forge.md` | Current truth, blockers, M00 merge record |
| `docs/FORGE_ANCHOR.md` | M01 anchor exit criteria, Lane A |
| `docs/kaggle_submission_bible.md` | `submission.zip`, rank ≤ 32, evidence rules |
| `.cursorrules` | Hard gates, milestone workflow |
| `docs/milestones/M00/M00_summary.md` | Prior milestone outcomes |
| `docs/milestones/M00/M00_audit.md` | Deferred registry DEF-005/006 |
| tonghuikang/nemotron README + repo tree | Baseline inspection |

---

## 7. Deliverables

### 7.1 Metric — boxed answer extraction

**File:** `src/forge_nemotron/metric/boxed_answer.py`

**Requirements:**

- Extract final answer from `\boxed{...}` in model output text  
- Handle common malformed cases deterministically (document behavior)  
- Handle multiple `\boxed{}` occurrences with explicit rule (e.g. last box wins, or first — document and test)  
- No ML dependencies required for core extraction  

**Tests:** `tests/unit/test_boxed_answer.py`

- Valid single box  
- Nested braces / escaped content edge cases  
- Multiple boxes  
- Missing box → explicit failure or `None` (document contract)  
- Malformed `\boxed{` without close  

### 7.2 Packaging — manifest model

**File:** `src/forge_nemotron/packaging/adapter_manifest.py`

- Dataclass or typed structure for: paths, adapter hash placeholder, rank, base model id, validator version  
- Serializable to JSON for future `run_manifest.json` alignment  

### 7.3 Packaging — structural validator

**File:** `src/forge_nemotron/packaging/validate_submission.py`

**Checks (local structural only):**

- Path exists and is a zip  
- Contains `adapter_config.json`  
- Contains expected weight file name(s) per PEFT convention (`adapter_model.safetensors` or documented equivalent)  
- If rank readable from config → assert ≤ 32  
- Reject obviously oversized archives (configurable threshold)  
- Return structured result object (pass/fail + reasons)  

**Do not claim:** full Kaggle compatibility, vLLM load success, or private LB performance.

**Tests:** `tests/unit/test_validate_submission.py`

- Minimal valid zip fixture (generated in test)  
- Missing config  
- Missing weights  
- Rank > 32 config fixture  

### 7.4 Baseline inspection notes

**File:** `docs/baselines/tonghuikang_nemotron_inspection.md`

- Inspection date, repo URL, commit SHA  
- File/command inventory  
- Mapping to FORGE modules  
- Open questions for reproduction milestone  
- Explicit: **not reproduced in M01** unless evidence added later  

### 7.5 Project packaging (DX)

**File:** `pyproject.toml` (recommended)

- Package name `forge_nemotron`  
- pytest discovery for `tests/`  
- Optional: ruff config aligned with anchor §16  

**Acceptance:** `pip install -e .` and `pytest -q` runs unit tests (not exit 5 empty collection).

### 7.6 CI strategy (owner decision required)

M00 confirmed **no** `.github/workflows`. Choose one:

| Option | Description | Pros | Cons |
| ------ | ----------- | ---- | ---- |
| **A — CI in M01** | Add `.github/workflows/ci.yml`: checkout, Python, `pip install -e .`, ruff (optional), `pytest -q` | Signal before more code | Slightly widens M01 scope |
| **B — M01A first** | M01A milestone: CI bootstrap only; M01 code after green CI | Clean separation | Extra milestone latency |

**Default recommendation:** **Option A** if owner wants fewer milestones; **Option B** if CI policy must land before any src changes.

**Cursor must ask owner which option before implementing M01 code** unless owner pre-authorizes Option A in kickoff message.

**Minimal CI job (if Option A):**

```yaml
# Illustrative — implement when authorized
on: [pull_request, push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: pip install -e ".[dev]"  # or equivalent
      - run: pytest -q
```

---

## 8. Verification

### Local (required at M01 closeout)

```bash
pip install -e .
pytest -q
python -m compileall src
# Manual: validate_submission on a test zip fixture
```

### CI (if Option A implemented)

- Record PR run URL in `docs/forge.md` and `M01_toolcalls.md`  
- If red: `M01_run1.md` using `docs/prompts/workflowprompt.md`  

### Honest reporting

- `pytest` must collect > 0 tests after M01  
- Do not claim green CI if workflow does not exist  
- Do not claim Kaggle submission readiness without validator pass + owner authorization  

---

## 9. Acceptance criteria

M01 implementation may close only when:

- [ ] `boxed_answer.py` exists with documented extraction rules  
- [ ] `test_boxed_answer.py` passes  
- [ ] `adapter_manifest.py` exists  
- [ ] `validate_submission.py` performs structural checks listed in §7.3  
- [ ] `test_validate_submission.py` passes with fixtures  
- [ ] `docs/baselines/tonghuikang_nemotron_inspection.md` exists; **no false reproduction claim**  
- [ ] `pyproject.toml` (or equivalent) enables installable package and pytest  
- [ ] CI Option A complete **or** M01A explicitly deferred with owner approval  
- [ ] `docs/forge.md` updated with M01 outcomes  
- [ ] `M01_summary.md` and `M01_audit.md` created  
- [ ] No Kaggle submission without explicit owner authorization  
- [ ] BQ-001 / BQ-003 remain owner-action unless owner supplied values  

---

## 10. Risks and deferrals

| ID | Risk | Mitigation | Exit criteria |
| -- | ---- | ---------- | ------------- |
| M01-R1 | Extractor diverges from Kaggle metric | Align tests to competition examples when available | Golden tests from overview/samples |
| M01-R2 | Validator passes but Kaggle rejects | Document “structural only”; expand in M02 | Kaggle upload evidence |
| M01-R3 | No CI → regressions | Option A or M01A | Green workflow on PR |
| M01-R4 | Scope creep into training | This plan non-goals | Audit scope control |
| DEF-001/002 | Owner Kaggle blockers | Do not guess | Owner updates `docs/forge.md` |

---

## 11. Closeout instructions

At M01 closeout, Cursor must:

1. **Ensure all documentation is updated as necessary** — `docs/forge.md`, bible cross-refs if packaging contract changed, inspection doc final.  
2. Update `docs/forge.md` — milestone ledger, run ledger if applicable, CI status, material decisions, deferrals.  
3. Create `docs/milestones/M01/M01_summary.md` using `docs/prompts/summaryprompt.md`.  
4. Create `docs/milestones/M01/M01_audit.md` using `docs/prompts/unifiedmilestoneauditpromptV2.md`.  
5. If GitHub Actions exist or were added, analyze runs with `docs/prompts/workflowprompt.md` → `M01_run1.md` (and increment if needed).  
6. Record all material evidence: commands, test output, commit SHAs, validator version, **non-claims**.  
7. **Do not** claim Kaggle submission readiness unless validator + evidence support it.  
8. **Do not** submit to Kaggle without explicit owner authorization.  
9. Do not merge or push after closeout without express permission (per `.cursorrules`).  
10. Seed M02 stub if authorized.

**Permission gates:** implementation, CI fixes, merge, push, closeout — per `.cursorrules` Phase 7.

---

## 12. Implementation phases (after authorization)

| Phase | Work |
| ----- | ---- |
| 0 | Owner locks CI Option A vs B |
| 1 | `pyproject.toml` + empty test that passes (CI green skeleton) |
| 2 | CI workflow if Option A |
| 3 | `boxed_answer` + tests |
| 4 | `adapter_manifest` + `validate_submission` + tests |
| 5 | Baseline inspection doc (read-only) |
| 6 | `docs/forge.md` governance update |
| 7 | Closeout summary/audit |

**Stop before Phase 1 until owner authorizes M01 implementation and CI option.**

---

## 13. Authorized next step (current)

- **Done:** M00 merged; this plan on `forge/M01-control-baseline`.  
- **Waiting:** Owner review of this plan + CI Option A/B decision + explicit authorization to implement.  
- **Not authorized:** Training, Kaggle submit, baseline reproduction claims.
