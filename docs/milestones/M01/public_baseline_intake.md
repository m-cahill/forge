# Public Baseline Intake — tonghuikang/nemotron

**Inspection date:** 2026-06-04  
**Repository URL:** https://github.com/tonghuikang/nemotron  
**Branch inspected:** `master`  
**Claimed purpose:** Progress Prize winning submission for NVIDIA Nemotron Model Reasoning Challenge  
**Status:** **Inspection only — not reproduced in M01**

---

## 1. Overview

This document records FORGE's read-only inspection of the public Progress Prize winning repository. It does NOT constitute reproduction, validation, or endorsement of the code.

**M01 posture:**
- Inspection and documentation only
- No code copied into FORGE
- No reproduction claim without evidence
- Clean-room implementation for FORGE-owned components

---

## 2. Kaggle Resources

| Resource | URL |
| -------- | --- |
| Writeup | https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge/discussion/689915 |
| Notebook | https://www.kaggle.com/code/huikang/end-to-end-finetuning-for-lb-0-85 |

Claimed leaderboard score: **0.85** (per notebook title)

---

## 3. Repository Structure

### Core Python Scripts

| File | Size | Purpose |
| ---- | ---- | ------- |
| `reasoning.py` | 8.7 KB | Logic processing / reasoning generation |
| `augmentation.py` | 1.4 KB | Data augmentation |
| `corpus.py` | 9.7 KB | Dataset/corpus management |
| `train_sft.py` | 20.2 KB | Supervised fine-tuning training |
| `upload_adapter.py` | 6.6 KB | LoRA adapter upload (via Modal) |
| `train_common.py` | 3.6 KB | Common training utilities |
| `loss_config.py` | 13.5 KB | Loss configuration |
| `lr_schedule.py` | 1.0 KB | Learning rate scheduling |
| `generate_csv.py` | 4.4 KB | CSV generation |
| `notebook_tinker.py` | 55.5 KB | Tinker notebook integration |

### Data Files

| File | Size | Purpose |
| ---- | ---- | ------- |
| `corpus.jsonl` | 42.6 MB | Training corpus |
| `problems.jsonl` | 931 KB | Problem set |
| `generation.jsonl` | 4.8 MB | Generation outputs |
| `train.csv` | 3.1 MB | Training data CSV |
| `tokenizer.json` | 17.1 MB | Tokenizer |
| `vocab.json` | 2.6 MB | Vocabulary |
| `vocab.jsonl` | 5.7 MB | Vocabulary JSONL |

### Dashboard HTML Files

| File | Purpose |
| ---- | ------- |
| `base.html` | Base model evaluation grid |
| `synthetic.html` | Synthetic data investigation |
| `corpus.html` | Training corpus viewer |
| `training.html` | Training metrics |
| `metrics.html` | Run index and charts |

### Directories

| Directory | Contents |
| --------- | -------- |
| `augmentations/` | Augmentation artifacts |
| `augmenters/` | Augmenter modules |
| `corpus/` | Corpus data |
| `investigations/` | Investigation notes |
| `investigators/` | Investigator modules |
| `problems/` | Problem data |
| `raw/` | Raw data |
| `reasoners/` | Reasoner modules |
| `reasoning/` | Reasoning outputs |
| `skills/` | Skill modules |
| `trainer/` | Trainer modules |
| `training/` | Training outputs |

### Configuration Files

| File | Purpose |
| ---- | ------- |
| `pyproject.toml` | Python project config |
| `uv.lock` | UV lockfile (590 KB) |
| `.python-version` | Python version |
| `.mcp.json` | MCP configuration |
| `CLAUDE.md` | Claude Code instructions |

---

## 4. Documented Commands

From README.md:

```bash
# Execute training pipeline
uv run python3 reasoning.py
uv run python3 augmentation.py
uv run python3 corpus.py
uv run python3 train_sft.py
uv run modal run upload_adapter.py

# Serve dashboard locally
./serve.sh
```

**Package manager:** `uv` (not pip/venv)  
**External service:** Modal (for adapter upload)

---

## 5. License Status

**License file present:** **NOT OBSERVED** (no LICENSE file in repository root)

**Posture for FORGE:**
- Do NOT copy code into FORGE
- Use clean-room implementation for FORGE-owned components
- External wrapper scripts may reference this repo as a dependency
- If license is clarified (e.g., MIT/Apache), reassess copying policy

---

## 6. Reproduction Blockers

| Blocker | Category | Notes |
| ------- | -------- | ----- |
| `uv` package manager | Dependency | FORGE uses pip; may need adaptation |
| Modal service | External | Required for adapter upload; account/API needed |
| Tinker integration | External | `notebook_tinker.py` suggests Tinker service |
| 42.6 MB corpus | Data | Large corpus file; download/verification needed |
| GPU compute | Hardware | 30B model training requires significant GPU |
| Kaggle owner-action | Governance | BQ-001/BQ-003 unresolved |

---

## 7. Key Observations

### Strengths (from inspection)
- Comprehensive dashboard for debugging (5 visualization tabs)
- Per-problem and per-category analysis
- Token-level trace visualization
- Training metrics tracking (loss, logprob, gradient norm)
- Deterministic corpus generation approach

### Architecture Notes
- Modular design with separate reasoners/investigators/augmenters
- Static HTML dashboard (no server-side rendering)
- JSONL-based data interchange
- Training progress stored as artifacts

### Answer Format
- Uses `\boxed{}` format (competition standard)
- Answer extraction likely in training/eval code

---

## 8. FORGE Alignment

### Metric Module
- FORGE's `forge_nemotron.metric.boxed` provides clean-room `\boxed{}` extraction
- Should align with this repo's answer extraction behavior
- Test against known competition examples when available

### Package Validator
- FORGE's `forge_nemotron.packaging.validate_submission` validates structure
- This repo uses Modal for upload; FORGE validates locally first
- Ensure rank detection aligns with PEFT conventions

### Dashboard
- This repo's dashboard is useful for debugging
- FORGE may build similar visualization later
- No immediate need to reproduce dashboard in M01

---

## 9. Recommended Next Actions

### M01 (current)
- [x] Document repository structure (this file)
- [x] Implement clean-room boxed-answer metric
- [x] Implement structural package validator
- [ ] No reproduction claim without evidence

### M02+
- Consider cloning repo for local analysis (not vendoring)
- Test FORGE metric against this repo's examples
- Evaluate corpus format for FORGE compatibility
- Assess training approach for adaptation

---

## 10. Non-Claims (Explicit)

This document does NOT claim:
- Reproduction of the baseline
- Validation of training code
- Kaggle submission readiness
- Public score achievement
- Adapter validity
- License clearance for code copying

FORGE must produce its own evidence before claiming any of the above.

---

## 11. References

| Reference | Location |
| --------- | -------- |
| Repository | https://github.com/tonghuikang/nemotron |
| Kaggle writeup | https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge/discussion/689915 |
| Kaggle notebook | https://www.kaggle.com/code/huikang/end-to-end-finetuning-for-lb-0-85 |
| Dashboard | https://nemotron.huikang.dev/ |
| HuggingFace mirror | https://huggingface.co/datasets/Naribow/nvidia-nemotron-progress-prize |
