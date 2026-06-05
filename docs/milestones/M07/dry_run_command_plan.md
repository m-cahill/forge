# Dry-Run Command Plan

**Milestone:** M07  
**Status:** **Future commands only — not executed in M07**  
**Authorization:** `M07_TRAINING_AUTHORIZED = no`

All commands below are **planned** for a future authorized milestone. Do not run without explicit owner Gate C and separate “run training now” instruction if applicable.

---

## 1. External clone path requirement

- Clone read-only: `https://github.com/tonghuikang/nemotron`
- Pin commit: `82bd1880aa8a8986ad572ccd17ae35b2b5c7da85` (M06 inspection SHA)
- Keep clone **outside** FORGE tree (no vendoring)
- M06 used `C:\coding\nemotron-inspect` — **do not assume** it still exists; re-clone if needed when authorized

---

## 2. Dependency setup approach (future)

```bash
# FUTURE ONLY — external clone directory
# git clone https://github.com/tonghuikang/nemotron.git <external_path>
# cd <external_path>
# git checkout 82bd1880aa8a8986ad572ccd17ae35b2b5c7da85
# uv sync   # or baseline-documented install — verify when authorized
```

FORGE repo (validation only — safe in M07):

```bash
pip install -e ".[dev]"
```

---

## 3. Schema inspection command (already complete in M06)

M07 does **not** re-run schema inspection. Reference:

- M06 derived notes under `docs/milestones/M06/external_schema_notes_*.md`
- Validate schema-gate manifest:

```bash
python scripts/validate_reproduction_plan.py \
  docs/milestones/M06/evidence/reproduction_gate/public_control_repro_plan.schema_gate.json
```

---

## 4. Dry-run / no-train command (future)

If baseline exposes a dry-run or config-print mode: **TBD** after authorized inspection of `train_sft.py` help/README.

Placeholder:

```bash
# FUTURE ONLY
# cd <external_path>
# uv run python train_sft.py --help
```

---

## 5. Training command placeholder (future)

```bash
# FUTURE ONLY — Gate C required
# cd <external_path>
# uv run python train_sft.py <args TBD>
```

Record exact command in `training_config_capture_template.md` when executed.

---

## 6. Artifact capture command (future)

After training (future):

```bash
# FUTURE ONLY — example FORGE-side capture
python scripts/eval_predictions.py --help
# Package adapter → submission.zip via future packaging script
# Record SHA256 in run manifest
```

---

## 7. Validation commands after training (future)

```bash
# FUTURE ONLY
python scripts/validate_candidate_manifest.py <candidate_manifest.json>
python scripts/validate_reproduction_plan.py \
  docs/milestones/M07/evidence/training_gate/public_control_repro_plan.ready_for_training.json
```

M07 blocked manifest (safe now):

```bash
python scripts/validate_reproduction_plan.py \
  docs/milestones/M07/evidence/training_gate/public_control_repro_plan.training_blocked.json
```

---

## 8. FORGE CI-style verification (documentation milestone)

Run during M07 closeout — **no training**:

```bash
ruff check .
ruff format --check .
mypy src tests
pytest tests/unit/test_reproduction_plan.py -q
pytest -q
python -m compileall src
python scripts/validate_reproduction_plan.py \
  docs/milestones/M07/evidence/training_gate/public_control_repro_plan.training_blocked.json
```

---

## Non-claims

- No command in sections 2–7 was executed as part of M07 unless explicitly noted as FORGE CI verification.
- Dry-run plan existence does not authorize training.
