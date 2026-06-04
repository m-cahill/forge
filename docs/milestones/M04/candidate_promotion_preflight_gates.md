# Candidate Promotion Preflight Gates

**Milestone:** M04  
**Applies to:** Control and specialist adapter candidates before submission consideration  
**Posture:** Evidence-oriented; unresolved gates are **blockers**

---

## Gate checklist

| # | Gate | Required evidence | Blocker if missing |
| - | ---- | ----------------- | ------------------ |
| 1 | Package validator pass | `scripts/validate_submission.py` report; `package_sha256` in candidate manifest | Yes |
| 2 | Rank compliance | `adapter_rank` ≤ 32 in manifest and `adapter_config.json` | Yes |
| 3 | Base model compatibility | `base_model` = `NVIDIA-Nemotron-3-Nano-30B` recorded | Yes |
| 4 | Adapter package hash | `adapter_sha256` recorded for non-preflight statuses | Yes |
| 5 | Dataset manifest hash | `dataset_manifest_sha256` for training-backed candidates | Yes |
| 6 | Training config hash | `training_config_sha256` for training-backed candidates | Yes |
| 7 | Local eval run manifest | `local_eval_run_id` + `reports/run_manifest.json` artifacts | Yes |
| 8 | Per-category local scores | `local_score` + `local_score_by_category` in manifest and CSV | Yes |
| 9 | Holdout contamination check | Documented pass; no holdout IDs in training data | Yes |
| 10 | Kaggle Submit UI constraints | Owner-recorded zip rules in `docs/kaggle/kaggle_setup_evidence.md` | **OPEN** — owner-action |
| 11 | Owner go/no-go | Explicit authorization before upload | Yes |
| 12 | Submission ledger update | Row in `docs/forge.md` § Submission Ledger after upload | Yes (post-submit) |

---

## Status progression (manifest)

```text
preflight → packaged → local_eval_complete → submitted
                    ↘ rejected (any stage)
```

| Status | Minimum evidence |
| ------ | ---------------- |
| `preflight` | Manifest schema valid; explicit `non_claims` |
| `packaged` | `package_path`, `package_sha256`, `adapter_sha256`; validator pass |
| `local_eval_complete` | Above + `local_eval_run_id`, local scores recorded |
| `submitted` | Above + `kaggle_submission_id`; submission ledger updated |
| `rejected` | `rejection_reason` or non-empty `notes` |

Validated by `forge_nemotron.adapters.candidate_manifest.validate_candidate_manifest`.

---

## M04 scope note

M04 implements gates **documentation** and a **mock preflight manifest** only. No real candidate satisfies gates 1, 4–9, or 11–12 until a future authorized training/packaging milestone.

**Submit UI zip constraints:** **OPEN** — not recorded; do not guess. See `docs/kaggle/kaggle_setup_evidence.md`.

**Kaggle API submission support:** **TBD**

---

## Non-claims

Passing manifest validation on the mock preflight file does not imply adapter existence, Kaggle acceptance, or baseline reproduction.
