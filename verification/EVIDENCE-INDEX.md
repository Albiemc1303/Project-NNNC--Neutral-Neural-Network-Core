# NNNC verification evidence archive

**Purpose:** preserve inspectable evidence of bounded reference-model testing, not claim universal proofs or production readiness. The record is split by phase, and original code is kept distinct from historical reports.

| Phase | Evidence currently in GitHub | Status / limitations |
|---|---|---|
| [0](phase-00/README.md) | Step 9/10 Python reference code, bounded explorer, closure and audit reports | Historical reported 15 targeted tests and depth-5 exploration (550 states); scripts have not been freshly rerun as part of this archive. Protected-effect deployment obligations remain open. |
| [1](phase-01/README.md) | Historical Build 4 runner, execution JSON, traceability CSVs and Build 5 closure report | The Build 1–3 sources referenced by the runner are absent from this GitHub snapshot; no independent reproduction claim. |
| [2](phase-02/README.md) | Adopted D2 mathematical contract; original test scripts located in project files but **not yet imported** into GitHub | Reported finite checks are not a universal proof; code provenance and source-to-output pairing must be checked before upload. |
| [3](phase-03/README.md) | Adopted D2 mathematical contract; original reference-model package not confirmed in GitHub | No new executable claim. |
| [4](phase-04/README.md) | Conditionally adopted D2 mathematical contract; no standalone verified executable package in GitHub | Conditions and verification duties remain open. |
| [5](phase-05/README.md) | Original bounded 11-fixture Python checker and historical result log recovered from project files | Illustrative finite fixture outcomes only, not independent formal proof. |

## Evidence labels

- **REPRODUCED:** source and outputs rerun in the present environment, with commands and environment recorded.
- **ARCHIVED-ORIGINAL:** original source or report copied without substantive changes; no fresh execution claim.
- **REPORTED-HISTORICAL:** an earlier report states a result, but reproduction has not been completed.
- **MISSING/UNVERIFIED:** source, execution context, or result linkage is incomplete.

Do not infer that a reported passing count establishes unbounded correctness, implementation safety, consciousness, individual identity persistence, or authorization for physical protected effects. New artifacts must include a manifest, source/version linkage, test commands, expected outcomes, actual output, and known limits.
