# NNNC Phase 0 — Build 2, Step 10

## Purpose
Adversarial hardening of Step 9 resource authorization and logical crash recovery. The Step 9 implementation is included as `step9.py` for a reproducible baseline.

## Execute
From this folder:

```bash
python -m unittest -v test_step10
python explore.py
```

## Observed execution
15/15 targeted tests passed. Composite breadth-first exploration to depth 5: 550 states, 549 accepted event decisions, 1,794 rejected decisions, no detected invariant violations.

## Protocol
- `PREPARE_EFFECT`: trusted caller role `worker`, session fencing, unrevoked principal, ledger reservation, effect journal record.
- `COMMIT_EFFECT`: trusted caller role `system`, current session, matching prepared reservation, atomic in-memory ledger consumption and protected value update.
- `ACK_EFFECT`: transitions committed to acknowledged without re-consuming resources; can occur after restoration.
- `ABORT_EFFECT`: releases a held reservation; reservation identifier cannot be reused.
- `SUSPEND`/`STOP`/`RESTORE`: abort outstanding prepared effects, release their holds, fence old generations; committed effects and spending remain.
- Direct `STORE_WRITE`, `SETTLE_CONSUME`, `SETTLE_RELEASE` rejected at composite boundary.

## Critical limits and follow-up issues
1. This is an in-memory logical model. `COMMIT_EFFECT` does **not** atomically commit an actual external write and durable ledger. An external write can occur before a crash and be replayed after a restart unless the resource itself provides idempotency or a transactional protocol. Do not claim exactly-once physical effects.
2. The separately modeled effect journal is not persistent, signed, replicated, or independently verified. There is no real networked resource-side fencing, authenticated principals, or concurrency.
3. `ACK_EFFECT` models a logical receipt, not proof of delivery or durable storage.
4. Existing `step9.py` remains importable and still exposes its unsafe direct `STORE_WRITE`; the security property applies only when all effectful calls are forced through `model.act`. A production integration must remove or restrict the bypass at the actual API boundary.
5. Restoring a checkpoint does not restore arbitrary domain state. It only fences the old session and aborts outstanding prepared operations.
6. The explorer checks a selected alphabet from one initial state to depth five. It does not prove unbounded safety, liveness, or distributed consistency. No independent full formal transition oracle was built.
7. Effect payload is stored in the journal before commit. Actual write authorization and binding to a named resource, owner and payload must be authenticated at a real resource boundary.
8. A cancellation after a commit cannot roll back that committed effect. Compensation requires a separate explicitly governed operation.

## Next milestone
Step 11: independent transition oracle/formal refinement, actual persistent write-ahead log design and failure injection at every durable I/O boundary, and strict API elimination of the direct-write bypass.
