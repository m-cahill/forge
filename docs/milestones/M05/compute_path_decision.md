# Compute Path Decision Matrix

**Milestone:** M05  
**Purpose:** Compare execution environments for future baseline reproduction  
**Status:** Decision matrix and recommendation — **does not authorize training**

---

## Summary recommendation

| Role | Recommended path |
| ---- | ---------------- |
| Preflight / dry-run | **local_5090** |
| Baseline-compatible full training (future) | **Modal/Tinker** or equivalent external GPU |
| Public notebook / submit evidence | **Kaggle notebook** (not primary training) |
| Fallback | **Other cloud GPU** if local or Modal/Tinker not viable |

M05 recommends **local_5090 for preflight** and **Modal/Tinker (or equivalent) for baseline-compatible training** only after explicit owner authorization in a future milestone.

---

## Option comparison

| Option | Expected capability | Blockers | Credentials | Artifact capture | Reproducibility risk | Cost/risk | M05 recommendation |
| ------ | ------------------- | -------- | ----------- | ---------------- | -------------------- | --------- | -------------------- |
| **local_5090** | Env checks; local eval; structural packaging tests; possible tiny QLoRA feasibility probe if later authorized | 30B full SFT may not fit; CUDA stack TBD | None for preflight | Run manifests under `artifacts/runs/` | Medium — local env drift | Low $; operator time | **Primary preflight/dry-run** |
| **Kaggle notebook** | Competition-aligned notebook; submit UI workflow; M01 CPU probe done | M01 probe: CPU-only, no base model paths; GPU path unconfirmed | Kaggle account | Notebook version + probe artifacts in `docs/kaggle/` | Medium — runtime may change | Low $; submission slots precious | **Evidence/submit workflow; not primary training** |
| **Modal/Tinker** | Matches public baseline `upload_adapter.py` / `notebook_tinker.py` path | External accounts; cost; FORGE uses pip not `uv` | Modal, Tinker API keys | External run logs + hashes in manifests | Lower for baseline parity if credentials work | Medium–high $; vendor lock-in | **Most baseline-compatible training (future authorized)** |
| **Other cloud GPU** | Full 30B SFT if VRAM sufficient | Cost; setup; reproducibility vs baseline | Cloud provider | Same as local + cloud billing records | Medium — may diverge from baseline commands | Medium–high $ | **Fallback** |

---

## Per-path notes

### local_5090

- **Use for:** validator smoke, fixture eval, reproduction-plan validation, environment verification, optional future tiny QLoRA feasibility (explicit authorization only).
- **Do not use for:** claiming baseline reproduction without training evidence.
- Record in run manifests: `environment_id: local_5090`.

### Kaggle notebook

- M01 interactive probe: Python 3.12, Linux, ~19.5 GB disk, **no GPU**, torch CPU-only, base model paths not attached.
- Useful for prize notebook and submission discipline; not assumed for heavy training until GPU/runtime confirmed.
- See [`docs/kaggle/kaggle_setup_evidence.md`](../../kaggle/kaggle_setup_evidence.md).

### Modal/Tinker

- Public baseline documents `uv run modal run upload_adapter.py` and Tinker notebook path.
- Requires owner authorization, credential setup, and cost acceptance before any FORGE training attempt.
- FORGE should not assume Modal/Tinker config matches without captured training config template.

### Other cloud GPU

- Consider if 5090 cannot run required training and Modal/Tinker is unavailable.
- Must still capture training config, hashes, and non-claims in manifests.

---

## Explicit non-authorization

This matrix **does not** authorize:

- SFT, QLoRA, or any model training in M05
- Nemotron inference
- Kaggle submission
- Baseline reproduction claims

Training authorization is a separate owner decision recorded in a future milestone and reproduction plan manifest (`training_authorized: true` with evidence).
