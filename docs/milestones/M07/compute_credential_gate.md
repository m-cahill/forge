# Compute and Credential Gate

**Milestone:** M07  
**Purpose:** Record compute/credential readiness for future training — **does not authorize training**

---

## Checklist

| Item | Status | Notes |
| ---- | ------ | ----- |
| local_5090 available | **yes** | Per `docs/forge.md` environment ledger |
| local_5090 CUDA details | **TBD** | Owner has not supplied driver/CUDA version |
| local_5090 VRAM | **TBD** | Not evidenced in M07 |
| Modal account | **TBD** | No account readiness recorded |
| Tinker account | **TBD** | No account readiness recorded |
| cloud fallback | **TBD** | Per M05 matrix |
| cost acceptance | **TBD** | Required before paid external training |
| credentials ready | **false** / TBD | Manifest uses `credentials_ready: false` |

---

## Storage policy

- **Never** commit API tokens, Modal tokens, Tinker keys, `.env`, or cloud credentials.
- Record only boolean/TBD readiness and required credential *names* in manifests.
- External clone paths used in M06 are **not** assumed available in M07.

---

## Compute path (training)

| Path | M07 status |
| ---- | ---------- |
| `local_5090` | Available for preflight; CUDA/VRAM **TBD** |
| `modal_tinker` | **TBD** — baseline-compatible path per M05 when authorized |
| `cloud_gpu` | **TBD** — fallback |
| Selected training path | **none** — Gate C not satisfied |

---

## Explicit non-claims

- FORGE does **not** claim CUDA stack verified on local_5090 in M07.
- FORGE does **not** claim Modal/Tinker accounts exist or work.
- Availability in the environment ledger is **not** training readiness.

---

## Next owner actions

1. Confirm CUDA/driver/VRAM on local_5090 when probing is authorized.
2. Confirm Modal/Tinker account status and budget (cost acceptance).
3. Set `credentials_ready: true` in a future manifest only with evidence.

See also M06 [`compute_readiness_checklist.md`](../M06/compute_readiness_checklist.md) and [`credential_readiness_checklist.md`](../M06/credential_readiness_checklist.md).
