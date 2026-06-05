# Local CUDA Path Decision — M11

**Milestone:** M11  
**Probe evidence:** [M10 local_5090_probe_report.md](../M10/local_5090_probe_report.md) · [`local_5090_probe.json`](../M10/evidence/local_5090_probe/local_5090_probe.json)  
**Owner preference:** `prefer_local_cuda` (preference only — not Gate D authorization)

---

## M10 facts (unchanged in M11)

| Field | Value |
| ----- | ----- |
| GPU visible | **yes** |
| GPU | NVIDIA GeForce RTX 5090 |
| VRAM | 32607 MiB |
| Driver | 591.86 |
| PyTorch | 2.2.2+cpu |
| CUDA available to PyTorch | **false** |
| Classification | **visible_no_torch_cuda** |

---

## Decision

**Local CUDA path remains blocked by CPU-only PyTorch in the active environment.**

M11 does **not** install CUDA PyTorch (`M11_LOCAL_CUDA_SETUP_AUTHORIZED = no`).

Owner preference `prefer_local_cuda` records intent to pursue local CUDA enablement in a **future milestone** (likely M12), not in M11.

---

## Path options considered

| Option | M11 outcome |
| ------ | ----------- |
| Authorize CUDA PyTorch setup in future milestone | **Recommended next** — pending M12 Gate D |
| Use Modal/Tinker instead | **TBD** — credentials/cost not ready |
| Use cloud GPU fallback | **TBD** — credentials/cost not ready |
| Defer training | **Active** — Gate E not authorized |

---

## Non-claims

- Visible GPU is **not** training readiness.
- No CUDA package install was performed in M11.
- No training feasibility dry run was executed.
