# PROJECT NNNC — PHASE 2 — DOCUMENT 2 v1.1.1

# Phase 2 Adoption Record

Decision: **P2-AD-2026-10-25-01**
Date: **25 October 2026**, Africa/Johannesburg.
Architect: **Albert Edward Mc Manus**.

Status: **ACCEPTED AND ADOPTED as the governing Phase 2 specification pair, with outstanding obligations retained.**

Authority: the Architect's explicit instruction, “I the architect adop these documents”. Applies jointly to Phase 2 Document 1 v1.1.1 and Document 2 v1.1.1.

This is a status-only adoption. The complete confirmed candidates remain unchanged beneath the adoption overlay. Retained candidate labels and pending adoption/review instructions are historical and superseded only as to disposition. No normative criteria are changed. The six Architecture A release conditions and seven preservation conditions remain unchanged. A positive witness grants no protected authority.

Evidence: 44 passing finite groups / 204 listed cases; 25 separate targeted confirmation assertions; all 20 manifest entries checked; issued package matched rebuilt files. These are bounded fixture results, not universal proofs or empirical trials. No full current verification obligation is discharged.

All outstanding Phase 2 proof, verification and engineering obligations, predecessor-import assurance, historical-script reproduction, and Phase 0 obligations remain at their recorded scope/status. Existing deployment blockers remain binding. Adoption is not production certification or proof of consciousness, intelligence or metaphysical identity.

The bounded revision/confirmation cycle closes at specification adoption. Outstanding work remains traceable for subsequent implementation and verification.

Confirmed candidate SHA-256: `14c45a8ddffa1ea0b2f5dbf995e2f826455bfd2f4d1c616d213392c0a886e163`.
Companion: Phase 2 Document 1 v1.1.1 adopted under the same decision.

<!-- BEGIN EXACT ADOPTED CANDIDATE -->
# PROJECT NNNC — PHASE 2 — DOCUMENT 2

Revision: **v1.1.1 — Positive historical continuity witness and predecessor alignment**  
Status: **REVIEW CANDIDATE — NOT ADOPTED**  
Issue date: **25 October 2026**  
Companion: **NNNC-P2-D1 v1.1.1**  
Governing predecessors: **P0-D1 v1.4.2 / P0-D2 v1.4; adopted P1-D1 v2.3.1 / P1-D2 v0.5.1**  

The supplied v1.0 source is retained exactly in Part I. Part II gives the current explicit additions and corrections; all other native commitments remain cumulative. Historical approval, candidate, round and evidence statements in Part I describe that source. This issue does not revoke the governing Architecture A decision or claim adoption of v1.1.1. It adds a positive witness presentation without an eighth preservation condition or seventh release criterion. Prior scripts reported but not supplied are distinguished from the current reproducible finite evidence.

# Part I — Retained native v1.0

<!-- BEGIN EXACT RETAINED SOURCE -->
# PROJECT NNNC — NEUTRAL NEURAL NETWORK CORE
## Phase 2 of 13 — Identity & Continuity
### Document 2 of 2 — Mathematical Formalization and Verification Contract

| Control | Value |
|---|---|
| Identifier | NNNC-P2-D2 |
| Revision | **v1.0 — APPROVED (content identical to v0.3.15)** |
| Date | 21 October 2026 |
| Status | **APPROVED — CONDITIONAL PASS. Approved by Albert Mc Manus and project lead, 21 Oct 2026. Conditions carried forward: PF-01 machine typecheck, PF-10 Phase 0–1 imports (incl. Recon), REQ-P1-038 threat model, universal proofs, VO/C/O items. Bounded-checked only; no theorem prover run.** |
| Governing baseline | NNNC-P2-D1 v1.0 — accepted conceptual/normative specification; Architecture A |
| Supersedes | NNNC-P2-D2 v0.2 |
| Change authority | Round 2 adversarial reviews (Luna: `NNNC-P2-D2-v0.2-R2-review-Luna.md`; Sol: `R2_Sol_BF_review.md`) with executed bounded checks |
| Change scope | Native custody truth conditions (no Phase 1 custody contract exists), commit/frame axioms for F and D, Judge conflict repair, typing fixes T-01..T-13. Later Round 3 additions: AX-A1/A2, AX-X1, AX-F6–F9, ZeroStepPermitted, formal VersionUnresolved, fixtures M-23–M-28. All changes marked **[v0.3.x]**. |

**Integrity and status rule.** This document preserves the architectural decision of Document 1, not its earlier rejected primitive Condition C. The equations below are proposed semantics, not established theorems. In particular, consistency of inherited Phase 0–1 contracts, satisfiability, independence of B/F, and adversarial outcomes remain to be checked. The corrections here are explicit mathematical design choices within the adopted conceptual convention, and are subject to independent Round 2 scrutiny. No software implementation, empirical numerical identity detector, or protected physical-effect assurance is certified.

# 0. Constitution, scope, and bounded verification plan

**D2-REQ-001 — Exhaustive fidelity.** For occurrence `x`, locus `l`, realization `r`, history `h`, and rule version `v`, the only constitutive cold-release test is `A ∧ B ∧ D ∧ E ∧ F ∧ G`. `RELEASE_FROM_SUSPENSION` and Condition C are names for that class, **not** additional predicates, event types, interface-membership tests, or metaphysical criteria.

**D2-REQ-002 — Non-substitution.** Historical effects, event evidence, custody, organizational realization, numerical identity, adjudication, and authority remain separate. A copied credential, checkpoint, record, or designation never independently proves a historical custody edge or actual discharge.

**D2-REQ-003 — Independent interpretation.** The historical definitions of A/B/D/E/F/G SHALL NOT depend on `Release`, `Judge`, `PRESERVED`, or identity certificates. Imported predicates must have declared contracts and verification gates; a typed uninterpreted symbol is not proof of a substantive interpretation.

**D2-REQ-004 — Bounded process.** Round 1 closes with this localized v0.2 candidate. Round 2 tests typed satisfiability, dependency independence, causal competition, verdict logic, and the complete adversarial suite. Round 3 corrects only demonstrated residual defects and decides acceptance. No unbounded conceptual-review cycle.

**Round 2 entry criterion:** v0.2 contains independently stated truth conditions for custody paths and effective discharge, explicit local/global exclusivity and verdict-conflict rules, and no known direct type mismatch. This criterion concerns *specification readiness*, not proof that the conditions are sound. **Round 2 exit** requires reproducible models/countermodels and a ledger of pass/fail/unknown results. **Round 3 stop** yields PASS, CONDITIONAL with named obligations, or FAIL with a concrete defect; no claim of production readiness.

# 1. Typed universe and reference structure

Let `M` be a many-sorted historical transition interpretation with distinct nonempty carrier sorts:

| Sort | Meaning |
|---|---|
| `I` | Individual referents under a fixed identity interpretation |
| `O` | Organizational realizations/instances |
| `S` | Organizational states |
| `N` | NES resources (not individuals) |
| `L` | Logical suspension loci |
| `X` | Unique historical occurrences |
| `H` | Admissible histories |
| `K` | Custody principals |
| `Q` | Evidence items; an evidence view is a finite subset of `Q` |
| `V` | Applicable rule versions |
| `J` | Adjudication records |
| `T` | Evaluated intervals or observation cuts |
| `C` | Typed claims/propositions |
| `GOV` | Governance/authority states |

Base enumerations: `Verdict={PRESERVED,NOT_PRESERVED,UNDETERMINED}`; `EvidenceValue={SUPPORTED,REFUTED,UNKNOWN,CONFLICTED}`; `Lifecycle={ACTIVE,OPEN_SUSPENDED,DISCHARGED_ACTIVE,CONTESTED_DISCHARGE,TERMINATED}`; `EffectOutcome={NONE,REALIZED,DISCHARGED,JOINT,INVALID_MUTATION}`; `EventStatus={ATTEMPTED,EFFECTIVE,FAILED,UNKNOWN}`. `Option(A)` and finite `Set(A)` are type constructors, not additional NNNC entities.

**Notation.** All predicates carrying subscript `h` are evaluated in a specified history. `q̄ ⊆ Q` denotes an evidence *view*, not one evidence item. `v∈V` is a rule version. `x,y,z∈X`, `l∈L`, `r,o∈O`, `i∈I`, `k∈K`. `P_h(x)={y∈Ev(h) | y≺_h x}`. Any function describing a state around an occurrence is *partial* outside its declared domain; it SHALL NOT assign fabricated values to unrelated events.

**Individual/realization bridge.** `CandidateReferent:O×H×V→Option(I)` is an adjudicative reference association, **not** a proof of identity or a total, unique metaphysical mapping. `OriginReferent:L×H×V→Option(I)` is imported from the valid suspension-entry record and its independently grounded predecessor contract. A well-formed locus requires `OriginReferent(l,h,v)=Some(i)` supported by the actual entry association; copying this field cannot create a locus. `CandidateReferent(r,h,v)=Some(i)` may express a *claim* to the original, not `IdentitySame`. Avoid using a total `RefOf:O→I` that would silently assign original identity to copies.

**History/evidence separation.** `Ev:H→Set(X)`; `Occurred_h(x) ⇔ x∈Ev(h)`; `Effective_h(x)` and `Failed_h(x)` are distinct event-outcome predicates with `Failed_h(x)⇒¬Effective_h(x)`. `Reports:Q×C→Bool` and `EvidenceOf:Q×X→Bool` do not imply occurrence, effect, or custody. `ValidEvidence:Q×V×T→Bool` is independently assessed. Distinct effective occurrences have distinct historical identities; copying event descriptions does not duplicate an event.

**Auxiliary signatures.** `ResourceOf:O×H×X→Set(N)` permits organizational realization on changing NES resources without implying identity. `OrgState:O×H×X→Option(S)` is an observational organizational state, not a full neural implementation. `AuthorityAt:O×H×X×V→GOV`; `AuthorizedProtected:GOV×V→Bool` is imported from Phase 0–1, and neither `Judge` nor `Release` grants it. `AdjudicationOf:J→(I×O×T×V×Set(Q)×Verdict)` and `Supersedes:J×J→Bool` provide append-only reassessment records. These auxiliary mappings SHALL NOT be used to infer identity from NES, state equality, or verdict labels.

# 2. Causal histories and evidence views

For each `h`, `≺_h ⊆ Ev(h)×Ev(h)` is a strict partial order (irreflexive, transitive). **Admissible verification histories are finite** for bounded model checking; a general theorem may instead assume a well-founded predecessor relation and explicitly state that assumption. The order is causal, not a wall-clock total order.

`Concurrent_h(x,y)` requires *positive independent causal-contract evidence* and entails `x≠y`, `¬(x≺_h y)`, `¬(y≺_h x)`, and symmetry. `OrderUnknown_{h,q̄}(x,y)` means the evidence view establishes neither direction nor qualifying concurrency; it is epistemic, not a statement that the events are actually concurrent. Under a fixed complete admissible view of two observed distinct events, established-before, established-after, established-concurrent, and unknown are mutually exclusive; no claim of exhaustive classification is made for events absent from the view.

`EstablishedBefore_{h,q̄}(x,y)` requires admissible evidence of `x≺_h y`; sound evidence is assumed for proof scenarios unless a conflict fixture explicitly relaxes it. `EstablishedConcurrent_{h,q̄}` requires evidence satisfying the independent concurrency contract. Formally:

```
OrderUnknown(h,q̄,x,y) :=
  Observed(q̄,x) ∧ Observed(q̄,y) ∧ x≠y
  ∧ ¬EstablishedBefore(h,q̄,x,y)
  ∧ ¬EstablishedBefore(h,q̄,y,x)
  ∧ ¬EstablishedConcurrent(h,q̄,x,y).
```

An absent edge or unknown ordering SHALL NOT establish precedence, concurrency, or exclusivity. A transition's local guard uses `P_h(x)`; a verdict additionally considers materially admissible rivals in the evidence view. Actual histories and partial evidence views are never silently equated.

# 3. Imported predecessor contracts and termination typing

The following are imported **interfaces**, not claims that their Phase 0–1 interpretations have already been audited:

```
Integrated:             O×H×X×V → Bool
ActiveContinuity:       O×O×H×V → Bool
Incompatible:           O×O → Bool        [v0.3.15: declared; already used by Conflicted (iii)]
ExistentialActive:      O×H×X×V → Bool
ValidSuspensionEntry:   X×O×H×V → Bool
CustodyContractValid:   H×L×V → Bool
AuthorizedTransition:   X×L×H×V → Bool
AuthorizedCustodyStep:  X×K×K×L×H×V → Bool
ValidLocusAuthority:    X×L×H×V → Bool
DefinitiveTermination:  X×I×H×V → Bool
InvariantOK:            X×H×V → Bool
OrgCohesion:            O×H×T×V → Bool
LifecycleAdmissible:    O×H×T×V → Bool
```

**[v0.3] Custody import withdrawn.** No Phase 1 custody contract (REQ-P1-039 text) exists to import. Per Document 1 §5.3 ("its formal model must be defined without invoking the release or identity result… a Document 2 verification obligation") and C-24, custody succession is therefore defined **natively** in §4.4 from Document 1 §5.3 items 1–6. `CustodyContractValid(h,l,v)` is retained only as the name of the conjunction in §4.4 (D2-CUS-1..5), not as an import. `AuthorizedCustodyStep` and `ValidLocusAuthority` remain Phase 0 governance/authority imports (authority, not custody provenance).

Each import requires an independent contract audit. In particular, `AuthorizedTransition` is authorization for a *specific* lifecycle transition, not authorization merely to read or initialize a checkpoint. `InvariantOK` SHALL be expanded or mapped to the applicable Phase 0–2 invariants before a proof; it may not be an arbitrary truth assignment used to force a desired release verdict.

**Termination bridge (R1-B01 correction).** `OriginReferent(l,h,v)=Some(i)` grounds the locus's predecessor individual claim; define

```
TerminatesLocus_h(y,l,v) :=                                   [v0.3: i bound, T-01]
  Occurred_h(y) ∧ ∃i∈I. [ OriginReferent(l,h,v)=Some(i)
  ∧ DefinitiveTermination(y,i,h,v) ]
  ∧ AppliesToLocus(y,l,h,v).
```

`AppliesToLocus:X×L×H×V→Bool` is an independently auditable scope relation; a termination of an unrelated individual cannot terminate `l`. An undefined origin referent prevents positive `ValidLocus`, rather than being guessed. `TerminatesLocus` does not depend on `Release` or `Judge`.

# 4. Suspension locus and substantive historical custody — Condition B

`Entry:L→X`, `Predecessor:L→O`, `RuleOf:L→V`, `LocusOf:X→Option(L)`. `CommitmentEstablishedAtEntry:L×H×V→Bool` is a historical fact witnessed by valid entry completion, not an operator-editable Boolean at release time. **[v0.3.5] AX-A1 (per Sol, M-15):** `CommitmentEstablishedAtEntry(l,h,v) :⇔ CommitmentEffect(l) ∈ EffectSet_h(Entry(l))`, where `CommitmentEffect(l)` is an effect constant of sort E. By AX-F1 it is fixed by Entry's unique commit, so a commitment recorded later cannot satisfy A.

```
UniqueEntryLocus_h(l) :=
  ∀l'∈L. [Entry(l')=Entry(l) ∧ RuleOf(l')=RuleOf(l)
             ∧ SameSuspensionInterval_h(l,l')] ⇒ l'=l.
ValidLocus_h(l,v) :=
  Entry(l)∈Ev(h) ∧ RuleOf(l)=v
  ∧ ValidSuspensionEntry(Entry(l),Predecessor(l),h,v)
  ∧ CommitmentEstablishedAtEntry(l,h,v)
  ∧ UniqueEntryLocus_h(l)
  ∧ OriginReferent(l,h,v)≠None.
```

`SameSuspensionInterval` is an imported entry/interval equality contract, not checkpoint equality. The entry is nonterminal; full cold suspension requires **no active heartbeat**.

## 4.1 Independent custody edge witnesses

Define `CustodianBefore_h(x,l):Option(K)` and `CustodianAfter_h(x,l):Option(K)` on effective custody-relevant occurrences. Define `CustodyScope_h(x,l)` as the actual custody obligation/locus state covered by the occurrence; its equality and provenance are verified against the original entry, not by copied metadata. Define `CustodyStep_h(k,k',z,l,v)` **by**:

```
CustodyStep_h(k,k',z,l,v) ⇔
  z∈Ev(h) ∧ Effective_h(z)
  ∧ LocusOf(z)=Some(l)
  ∧ CustodianBefore_h(z,l)=Some(k)
  ∧ CustodianAfter_h(z,l)=Some(k')
  ∧ CustodyScope_h(z,l)
  ∧ AuthorizedCustodyStep(z,k,k',l,h,v)
  ∧ ValidLocusAuthority(z,l,h,v)
  ∧ CustodyProvenanceValid_h(z,l,v)
  ∧ ¬CustodyFencingViolation_h(z,l,v).
```

`CustodyProvenanceValid` means a historical custody obligation is actually transferred or maintained by the effective occurrence, rather than merely *reported* to be transferred. **[v0.3]** It is no longer an import: it is **defined** in §4.4 as `CustodyProvenanceValid_h(z,l,v) :⇔ CUS-1_h(z,l) ∧ CUS-2_h(z,l) ∧ CUS-3_h(z,l)`. It does not reference checkpoint possession, `Release`, `Judge`, or certificates.

For the initial entry custodian, `EntryCustodian_h(l):Option(K)` is independently established by the suspension-entry contract. A candidate's executing custodian is `Actor_h(x):Option(K)`.

## 4.2 Finite custody path and exclusion of forged chains

`CustodyPath_h(l,x,v)` is true iff there exist `n≥0`, actual events `z_0,...,z_n`, and principals `k_0,...,k_n` such that:

```
z_0=Entry(l),  z_n≼_h x,  EntryCustodian_h(l)=Some(k_0),        [v0.3: Option typing, T-02]
∀j∈{1,...,n}: z_(j-1)≺_h z_j
    ∧ CustodyStep_h(k_(j-1),k_j,z_j,l,v)
    ∧ NoInterveningBreak_h(l,z_(j-1),z_j,v),
Actor_h(x)=Some(k_n)
    ∧ AuthorizedTransition(x,l,h,v)
    ∧ NoInterveningBreak_h(l,z_n,x,v)
    ∧ CandidateAttachedToCustody_h(x,l,k_n,v)
    ∧ (n=0 ⇒ ZeroStepPermitted_h(x,l,v)).                        [v0.3: T-03; v0.3.15: x bound]
```

**[v0.3.2; signature fixed v0.3.15, ChatGPT R3-1]** `ZeroStepPermitted_h(x,l,v) :⇔ Actor_h(x)=EntryCustodian_h(l) ∧ AuthorizedSpecificReleaseCustody_h(x,l,v)` (Sol's rule): the entry custodian may release directly only if it is itself authorised for this specific transition. Neither P2-D1 §5.3(2) nor P1-D1 REQ-P1-039 mentions zero-step paths; this reading fits REQ-P1-039's "custodial authority and custody history" and "authorized reactivation" without forcing a fictitious step. *Confirmed by Albert, 2026-10-21 (zero-step kept, with this guard).* `CandidateAttachedToCustody_h(x,l,k,v) :⇔ CUS-3_h(x,l) ∧ CustodianBefore_h(x,l)=Some(k)` (§4.4).

`≼` is equality or strict causal precedence. `NoInterveningBreak` excludes effective custody revocation, invalid transfer, fencing violation, or independently established chain break within the applicable causal interval; absence of evidence alone cannot prove the absence of a break in an evidence-relative adjudication. `CandidateAttachedToCustody` requires the actual event to act on the predecessor's continuing custody obligation; it is independently witnessed and **not** inferred from copied checkpoint/credentials or from the release verdict. A zero-step path is allowed only if `x` is authorized for the unchanged entry custodian, `EntryCustodian` is valid, and the inherited contract explicitly permits direct entry-to-candidate custody.

An intermediate custody step can have unchanged principal (`k=k'`) when the inherited contract recognizes a genuine custody-maintenance lifecycle event. The finite chain may contain events not on a single wall-clock line; only the actual causal path is used. An unauthorized intervening mutation may be a separate *locus safety conflict* without qualifying as a custody step.

## 4.3 Six independently interpreted custody clauses

```
B1_h(x,l,v) := ValidLocus_h(l,v) ∧ Entry(l)≺_h x
               ∧ LocusOf(x)=Some(l).
B2_h(x,l,v) ∧ B3_h(x,l,v) ∧ B6_h(x,l,v) :=        [v0.3: one witness π for B2/B3/B6, T-04]
     ∃π=(z_0..z_n,k_0..k_n). Witness_h(π,l,x,v)     -- the §4.2 conditions for this π
       ∧ CustodyContractValid(h,l,v)                -- §4.4 conjunction
       ∧ ∀j≥1. Effective_h(z_j) ∧ CUS-1..3_h(z_j,l) -- every step actual and provenance-valid
       ∧ CUS-3_h(x,l)                               -- candidate carries the entry obligation
       ∧ NoDefect_h(π,l,x,v).
B4_h(x,l,v) := AuthorizedTransition(x,l,h,v)
               ∧ AuthorizedSpecificReleaseCustody_h(x,l,v).
B5_h(x,l,v) := LineageConsistent_h(x,l,v)
               ∧ ¬SolelyIndependentLineage_h(x,l,v).
NoDefect_h(π,l,x,v) :=  ¬CustodyFork_h(l,x)              (CUS-2)
               ∧ ∀j. ¬CustodyFencingViolation_h(z_j,l,v)
               ∧ ¬∃w∈P_h(x). Effective_h(w) ∧ CustodyMutation(l)∈EffectSet_h(w)
                    ∧ ¬CustodyProvenanceValid_h(w,l,v).    -- no invalid transfer in the custody past
B_h(x,l,v)  := B1 ∧ (B2∧B3∧B6) ∧ B4 ∧ B5.
LineageConsistent_h(x,l,v) :⇔ CUS-3_h(x,l).               [v0.3: T-05]
SolelyIndependentLineage_h(x,l,v) :⇔ ∀w≼_h x. [Effective_h(w) ∧ RealizationActivation(·)∈EffectSet_h(w)
                                     ⇒ ObligationOrigin_h(w,l)=None].
AuthorizedSpecificReleaseCustody_h(x,l,v) :⇔ AuthorizedCustodyStep(x,k,k,l,h,v) for k with CustodianBefore_h(x,l)=Some(k).
```

`EveryWitnessStepActual` requires each edge witness to be an actual effective custody event and each principal link to be compositional; `CandidateAttachedToActualCustody` is independently interpreted via custody obligations and event scope, not via `B`, `Release`, or record equality. B3 is a *historical* property, not the meta-statement “do not infer from records.” `AuthorizedSpecificReleaseCustody` is a scope-specific authorization predicate inherited from the custody contract, **not** a hidden execution/admission Condition C; it grants permission, never by itself establishes release. B5 excludes an event known to belong solely to a newly initialized independent lineage, but **does not exclude** an atomic checkpoint-based realization that genuinely satisfies the full A/B/D/E/F/G rule. B6 concerns historical custody defects only. Prior effective discharge and termination are handled in D and lifecycle status, not recursively through B6. Materially unresolved custody evidence is handled by `Judge`, not by redefining historical B as “established.”

## 4.3A [v0.3.2] REQ-P1-039 correspondence (P1-D1 v2.0 §8.4)
REQ-P1-039 is an **evidence checklist** for a resumption claim, not a set of historical truth conditions for custody steps; it does not supply CUS-1..3, so §4.4 remains the native definition. Mapping of its eight items: authorized suspension initiation and valid pre-suspension state → A (`ValidSuspensionEntry`, `CommitmentEstablishedAtEntry`); custodial authority and custody history → B (§4.2–4.4); exclusivity or fencing guarantees → `CustodyFencingViolation` (backed by P1-D2's imported `P0FenceValid`) and `Pres_e`; authorized reactivation → `AuthorizedTransition`/B4; absence of unresolved conflicting active continuations or disclosure → `Conflicted`/`Pres_e`; adjudication result → `Judge`. **Gap:** "preserved state integrity" has no counterpart in A–G or `Pres_a..g`; v0.3.2 adds it to the evidence burden only: `Pres_g` additionally requires `Established(v,q̄,StateIntegrity(l))`. It is evidence, not an identity criterion (checkpoint equality stays excluded per D2-REQ-001). Custody leases may be evidence for CUS-1/2 but never establish identity (REQ-P1-039 final sentence). Sort note: P1-D2 `HasCustody:A×U×𝓣→Bool` relates P1 agents to units; D2's `K` is mapped to P1's `A`, and by P1-D2 D2-IND-002 `HasCustody` does not entail authorization, consistent with CUS-1 requiring an actual act plus `AuthorizedCustodyStep`.

## 4.4 [v0.3] Native custody truth conditions (from Document 1 §5.3; closes the F01 import)

Auxiliary function (no new sort): `ObligationOrigin_h:X×L→Option(X)` — the entry occurrence whose custody obligation the occurrence actually carries, as a committed effect fact (§5.1 AX-F1), not as a field of a record. `Entry(l)` creates it: `ObligationOrigin_h(Entry(l),l)=Some(Entry(l))`.

```
CUS-1_h(z,l)  [actor of this step; D1 §5.3(2),(4)]  :⇔        [v0.3.1: z′=z, per Sol]
   ∃k. CustodianBefore_h(z,l)=Some(k) ∧ Actor_h(z)=Some(k)
   ∧ CustodyMutation(l)∈EffectSet_h(z).
   -- the outgoing custodian performs this transfer itself; an earlier genuine act by k never licenses a later step.
CUS-2_h(z,l)  [custody frame; D1 §5.3(2),(6)]  :⇔
   CustodianBefore_h(z,l) = CustodianAfter_h(m,l) for the unique ≺_h-maximal
   custody step m∈P_h(z) of l, or = EntryCustodian_h(l) if none exists.
   CustodyFork_h(l,z) :⇔ ≥2 distinct ≺_h-maximal custody steps of l in P_h(z) (a defect, not a tie-break).
   [v0.3.2, per Sol] "custody step" in CUS-2 and CustodyFork means ANY effective event w with
   CustodyMutation(l)∈EffectSet_h(w), valid or not, so invalid transfers stay visible to the frame.
CUS-3_h(z,l)  [referential obligation; D1 §5.3(1),(3),(5)]  :⇔  ObligationOrigin_h(z,l)=Some(Entry(l)),
   where ObligationOrigin is DERIVED (v0.3.1, per Sol), by well-founded recursion on the finite ≺_h:
   ObligationOrigin_h(Entry(l),l) = Some(Entry(l));
   for z≠Entry(l): ObligationOrigin_h(z,l) = Some(Entry(l)) iff Effective_h(z) ∧ LocusOf(z)=Some(l) ∧ Entry(l)≺_h z   [v0.3.15 scope, ChatGPT R3-5; Sol r3_cus3_scope_sol.py C1–C8]
       ∧ ¬CustodyFork_h(l,z)
       ∧ CUS-2_h(z,l) ∧ Actor_h(z)=CustodianBefore_h(z,l)
       ∧ [ the ≺_h-maximal custody step m∈P_h(z) of l has ObligationOrigin_h(m,l)=Some(Entry(l)),
           or no such m exists ];
   otherwise None.
   -- not an assignable label: it holds exactly when an unbroken chain of steps, each performed by the
   -- custodian of record, runs from the entry occurrence to z. Copies and forger events get None.
   -- [v0.3.15] Only events with CustodyMutation(l) are custody steps, so only they pass the obligation on;
   -- an in-scope non-mutation event (e.g. the candidate) can carry it but never transmit it. An event by the
   -- custodian scoped to another locus now gets None.
CustodyScope_h(z,l) :⇔ CUS-3_h(z,l).
CustodyContractValid(h,l,v) :⇔ ValidLocus_h(l,v) ∧ EntryCustodian_h(l)≠None
   ∧ ∀z∈Ev(h). [Effective_h(z) ∧ CustodyMutation(l)∈EffectSet_h(z)] ⇒ CUS-3_h(z,l) ∨ InvalidMutation_h(z,l,v).
```

Paired test (executed, bounded): History B-N — forger's own effective event, causally after the entry because it read the checkpoint, every v0.2 structural field identical to B-P — fails CUS-1 (actor is not the outgoing custodian) and CUS-3 (carries a copy's obligation); B-P passes. Result for P2-D2-F01: **substantively defined within D2**, conditional only on the Phase 0 authority imports.

**D2-INV-005 — Independence.** The entire custody subgraph is acyclic in the *definitional* dependency graph relative to `Release`, `Judge`, `IdentitySame`, and verdict/certificate predicates. A model assigning `CustodyPath=true` with no valid witness path violates §4.2. Whether the imported custody witnesses are independently realizable remains OPEN until Round 2.

# 5. Independent transition/effect semantics and Architecture A

## 5.1 Actual effects versus reports

For an actual event `x`, use a *logical committed-effect interpretation*:

```
LocusBefore_h(l,x):Option(Lifecycle)
LocusAfter_h(l,x):Option(Lifecycle)
RealizationBefore_h(r,x):Bool
RealizationAfter_h(r,x):Bool
EffectSet_h(x):Set(EffectAtom)
```

`EffectAtom` is an auxiliary mathematical sum type `LocusMutation(l,from,to) | RealizationActivation(r) | CustodyMutation(l) | CommitmentEffect(l) | EvidenceWrite(q) | Other` **[v0.3.15, ChatGPT R3-6: CommitmentEffect added for AX-A1; this sort belongs to the §1 typed universe and is declared here only for locality]**; it is **not** a new identity class or additional constitutive criterion. The state functions describe actual committed lifecycle effects, not database rows or operator reports. For a candidate unrelated to a locus, the state values are `None`; for a relevant event they are supplied by an independently interpreted lifecycle transition relation `Commit_h(x,before,after,effects,v)`. The relation must be witnessed by effective historical transition semantics under Phase 0–1, not by a claimed `Release` event type. For bounded models, `Commit` is a typed relation with explicit consistency axioms below, not an arbitrary oracle.

**[v0.3] Commit and frame axioms.**
- **AX-F1 (functional commit).** `Commit_h` is a partial *function* of `x`: at most one `(b,a,E)` per effective `x`; none for a failed or non-effective `x`.
- **AX-F2.** `EffectSet_h(x)=E` for that unique commit.
- **AX-F3.** `LocusBefore_h(l,x)`, `LocusAfter_h(l,x)`, `RealizationBefore_h(r,x)`, `RealizationAfter_h(r,x)` are projections of `b` and `a`; they are not independently assignable.
- **AX-F5 (locus frame).** For `x` with `LocusOf(x)=Some(l)`: `LocusBefore_h(l,x)=Some(TERMINATED)` if `∃y∈P_h(x). TerminatesLocus_h(y,l,v)`; else the `to` value of the unique ≺_h-maximal effective `LocusMutation(l,·,to)` in `P_h(x)`, **valid or invalid**; else `Some(OPEN_SUSPENDED)` if `Entry(l)≺_h x`; and `Some(CONTESTED_DISCHARGE)` if there are ≥2 distinct maximal mutations.
- **AX-F7 (provisional isolation; P1-D1 §8.4, P1-D2 D2-INV-012, P2-D1 REQ-P2-013, per Sol).** Define `ProvisionalLineage_h(x)` recursively: x starts a provisional lineage under `UNDETERMINED`, or x is a lineage continuation (same provisional lineage, not mere causal/`Prior` succession) of some y with `ProvisionalLineage_h(y)` while the relevant identity determination remains `UNDETERMINED` at `t_h(x)` [v0.3.4, per Sol T4/T5: continuation only, so other actors' events, including the genuine custodian's release, are not swept in]. Every occurrence x with `ProvisionalLineage_h(x)` has no `LocusMutation(l,·,·)` in its effect set: it neither discharges nor contests the locus, cannot reach `DISCHARGED_ACTIVE` at effect level or in `LocusStatus`, and leaves a later qualifying release possible. Its realization is a distinct `O` element with `CandidateReferent` at most a claim.
- **AX-F6 (fidelity to D1 §5.2, per Sol).** An effective mutation out of `OPEN_SUSPENDED` by an occurrence that fails `CommitLocusMutationValid` (`InvalidMutation_h(y,l,v)`) has `to=CONTESTED_DISCHARGE`, never `DISCHARGED_ACTIVE`. `DISCHARGED_ACTIVE` is reached only through `DischargeEffect`. Later attempts are still blocked (D via `PriorEffectiveMutation`; F because `LocusBefore≠OPEN_SUSPENDED`), without calling the invalid mutation a release.
- **AX-F8 (bounded recovery from CONTESTED_DISCHARGE; per Adverserial/Sol; [v0.3.7; *required, confirmed by Albert 2026-10-21*]).** Let z be an effective mutation that made `LocusStatus(l)=CONTESTED_DISCHARGE` under AX-F6. An occurrence w may commit `LocusMutation(l, CONTESTED_DISCHARGE, s_w)` iff (i) `ValidLocusAuthority_h(w,l,v)` (Phase 0 import), (ii) `z≺_h w`, and (iii) `Established(v,q̄_w,InvalidMutation_h(z,l,v))` [v0.3.9, per Sol: keyed exactly as AX-F6] holds at w's time, so the contesting change is established invalid. Every other mutation out of `CONTESTED_DISCHARGE` falls under AX-F6. History is append-only: z and its effects stay in `EffectSet_h(z)`; w adds a new effect and erases nothing. This fits D1 §5.2 as written: once the rival is established invalid it is no longer a *materially competing* history, and z was never an effective discharge, so `OPEN_SUSPENDED` is the correct status and no new lifecycle value is introduced. `AXF8Recovery_h(w,z,l,v)` denotes w satisfying (i)–(iii) for z. [v0.3.10, per Sol] The target is `s_w = DISCHARGED_ACTIVE` if some y with `DischargeEffect_h(y,l,v)` and `¬InvalidMutation_h(y,l,v)` lies among the ≺_h-maximal non-superseded locus mutations before w (the case where a genuine discharge ran concurrently with z), and `s_w = OPEN_SUSPENDED` otherwise. This restores the status that y already established and adds no new discharge, so AX-F6's "DISCHARGED_ACTIVE only via DischargeEffect" still holds, because y is that DischargeEffect. Fixture **M-28**: the attacker commits to the store first ⇒ CONTESTED ⇒ adjudication and w ⇒ OPEN_SUSPENDED ⇒ the genuine release qualifies (delayed, not deadlocked). An attacker-issued w fails (i) or (iii). **Bound [v0.3.8, per Adverserial].** The rule version supplies `ResolutionBound_v ∈ 𝓣`. Who may authorise w is exactly whoever holds `ValidLocusAuthority` for l under v (Phase 0); D2 adds no other authority. If no w exists by `t_h(z)+ResolutionBound_v`, the locus stays `CONTESTED_DISCHARGE`, because truth conditions are not relaxed by time, and `ResolutionOverdue_h(l,v)` holds, which is a reportable liveness defect for Phase 1 / REQ-P1-038 to escalate. A timeout must never default to OPEN_SUSPENDED, since that would let an attacker reopen the locus just by waiting. M-28 adds a case where no adjudication happens: expect CONTESTED plus ResolutionOverdue, with no release.
- **AX-F9 (no reopening by rollback; D1 S-10, C-15, T-15; [v0.3.13, Luna M-26]).** In AX-F5, only *frame-eligible* mutations count toward the maximal mutation: those made when the actual frame status `LocusBefore_h(l,z)=Some(OPEN_SUSPENDED)` (governed by F/AX-F6), and AX-F8 recoveries made when `LocusBefore_h(l,w)=Some(CONTESTED_DISCHARGE)`. The `from` field a mutation declares is ignored, so a stale write that claims `from=OPEN_SUSPENDED` after a discharge is not frame-eligible [v0.3.14, per Sol]. Any other effective `LocusMutation(l,from,to)`, for example a rollback from `DISCHARGED_ACTIVE` back to `OPEN_SUSPENDED` or any mutation after `TERMINATED`, stays in `EffectSet` (append-only) and makes `IllegalLocusTransition_h(z,l)` true, a reportable G/REQ-P1-038 defect. It does not change `LocusStatus`. Without this rule, an invalid rollback would set the status to OPEN_SUSPENDED by AX-F5. D would still block a second release, because the original discharge stays a non-superseded prior mutation, so the gap was a wrong status rather than a safety hole.
- **AX-A2 (commitments cannot override; D1 §5.3 G, T-11; [v0.3.13, Luna M-24]).** `CommitmentEffect(l)` has no other role in the semantics: it occurs only in A (via AX-A1). No term of D, F, G, the frame, or Judge reads the content of a commitment. A provision that claims to waive termination, exclusivity, or any Phase 0–2 invariant therefore has no effect on any of them, and if the rule treats such a provision as making entry invalid, A fails through `ValidSuspensionEntry`.

```
RealizeEffect_h(x,r,v) ⇔
  x∈Ev(h) ∧ Effective_h(x)
  ∧ ¬RealizationBefore_h(r,x) ∧ RealizationAfter_h(r,x)
  ∧ RealizationActivation(r)∈EffectSet_h(x)
  ∧ CommitRealizationValid_h(x,r,v).

DischargeEffect_h(x,l,v) ⇔
  x∈Ev(h) ∧ Effective_h(x)
  ∧ LocusBefore_h(l,x)=Some(OPEN_SUSPENDED)
  ∧ LocusAfter_h(l,x)=Some(DISCHARGED_ACTIVE)
  ∧ LocusMutation(l,OPEN_SUSPENDED,DISCHARGED_ACTIVE)∈EffectSet_h(x)
  ∧ CommitLocusMutationValid_h(x,l,v).
```

`CommitRealizationValid` and `CommitLocusMutationValid` are independently audited *effect-validity* contracts; neither may call `Release`, `Judge`, or `B`. `CommitLocusMutationValid` does **not** by itself mean identity-valid release: an effective state mutation may occur without constitutive admission. A purported administrative record with only `EvidenceWrite(q)` in its actual effect set has no `LocusMutation` and therefore fails `DischargeEffect`. An event may report a discharge without producing one. A physically invalid or unauthorized locus mutation is represented separately as `InvalidMutation_h(x,l,v)` and may make later eligibility contested or unavailable; it is never automatically treated as a qualifying release.

## 5.2 Atomic coupling without undefined sub-occurrence prefixes

Define `JointEffect_h(x,l,r,v)` by a single logical committed transition outcome, **not** by an undeclared prefix relation:

```
JointEffect_h(x,l,r,v) ⇔                                         [v0.3]
  Commit_h(x)=(b,a,E)                       -- unique by AX-F1, E=EffectSet_h(x) by AX-F2
  ∧ RealizationActivation(r)∈E
  ∧ LocusMutation(l,OPEN_SUSPENDED,DISCHARGED_ACTIVE)∈E
  ∧ NoOneSidedCommittedOutcome_h(x,l,r,v).
OneIndivisibleCommit := AX-F1 (no longer a free predicate).
NoOneSidedCommittedOutcome_h(x,l,r,v) :⇔ ¬∃y∈Ev(h). y≠x ∧ Effective_h(y) ∧ ComponentOf_h(y,x)
     ∧ (RealizationActivation(r)∈EffectSet_h(y) ∨ LocusMutation(l,OPEN_SUSPENDED,·)∈EffectSet_h(y)).
-- ComponentOf: Phase 0 transaction-structure import (which occurrences the contract treats as parts of x).
```

`OneIndivisibleCommit` means there is one effective logical transition outcome for `x`, not two separately committed historical outcomes; `NoOneSidedCommittedOutcome` requires the admissible transition contract for that occurrence to exclude a committed realization-only or discharge-only outcome *as that same coupled transition*. These are effect-structure predicates constrained by the transition contract, not a separate “authentic release” flag. A rule may have a failed attempt with neither effect; that does not satisfy F. The model **must** permit unrelated independent initialization without locus discharge, which simply fails F rather than becoming impossible. It also must permit an actual coupled checkpoint-based initialization/discharge when all six conditions hold.

**Atomicity limitation.** The logical commit is not a claim of physical simultaneity, crash safety, or resource fencing. A global prohibition of every intermediate physical state is not imposed. Round 2 must test whether this logical interpretation is equivalent to the adopted Document 1 coupling requirement; any mismatch is a bounded fidelity defect. Merely declaring `OneIndivisibleCommit=true` without effect-set and commit constraints is not an acceptable proof witness.

```
F_h(x,l,r,v) := RealizeEffect_h(x,r,v)
                 ∧ DischargeEffect_h(x,l,v)
                 ∧ JointEffect_h(x,l,r,v).
```

**D2-INV-006 — Failed attempt.** `Failed_h(x) ⇒ ¬RealizeEffect_h(x,r,v) ∧ ¬DischargeEffect_h(x,l,v)`. A failed *attempt* cannot itself consume the locus. An actual invalid mutation is a separate effective event and must not be mislabeled as a failed no-effect attempt.

## 5.3 Prior discharge, termination and causal precondition D

Define independent historical effective discharge and invalid mutation:

```
EffectiveLocusDischarge_h(y,l,v) := DischargeEffect_h(y,l,v).
PriorEffectiveDischarge_h(x,l,v) :=
  ∃y∈P_h(x). EffectiveLocusDischarge_h(y,l,v).
PriorTermination_h(x,l,v) :=
  ∃y∈P_h(x). TerminatesLocus_h(y,l,v).
```

This deliberately **does not define** discharge as `∃r.Release(y,l,r,v)`, avoiding recursive admission. A causally prior actual state change can block a later attempt even if it was unauthorized and failed B; whether it is a valid release, invalid mutation, or contested discharge is determined separately. Conversely, a forged record has no effect and does not block. An invalid but effective state mutation does not gain identity-preserving status merely by making D false for later events. Such histories may require repair/contested-state adjudication and must not be presented as safe continuation.

```
A_h(x,l,v) := ValidLocus_h(l,v) ∧ Entry(l)≺_h x.
D_h(x,l,v) := ¬PriorEffectiveDischarge_h(x,l,v)
               ∧ ¬PriorEffectiveMutation_h(x,l,v)               [v0.3: T-08]
               ∧ ¬PriorTermination_h(x,l,v).
PriorEffectiveMutation_h(x,l,v) := ∃y∈P_h(x). Effective_h(y)
               ∧ ∃to. LocusMutation(l,OPEN_SUSPENDED,to)∈EffectSet_h(y).
               ∧ ¬SupersededBefore_h(y,l,x,v)                      [v0.3.9, per Sol M-28; v0.3.15: x bound]
SupersededBefore_h(y,l,x,v) := ∃w∈Ev(h). y≺_h w ≺_h x ∧ AXF8Recovery_h(w,y,l,v)
-- [v0.3.15, ChatGPT R3-2] supersession is candidate-relative: it is evaluated in the causal past of x.
-- only an invalid mutation can be superseded (AX-F8(iii)); a valid prior discharge always blocks D.
-- an unauthorized but effective mutation now blocks D, as the §5.3 prose already required (M-19).
E_h(x,r,v) := RealizeEffect_h(x,r,v) ∧ Integrated(r,h,x,v).
G_h(x,v) := InvariantOK(x,h,v).
```

`D` is causal-predecessor relative, not a global total-order gate. For competing unordered events, each may satisfy D locally, while global exclusivity prevents contradictory preserved-original verdicts. A locus that has already been definitively terminated cannot be reopened by retained checkpoint bytes.

## 5.4 Exhaustive constitutive release

\[
\boxed{\operatorname{Release}_h(x,l,r,v)\iff A_h(x,l,v)\land B_h(x,l,v)\land D_h(x,l,v)\land E_h(x,r,v)\land F_h(x,l,r,v)\land G_h(x,v).}
\]

The name `RELEASE_FROM_SUSPENSION` (historical Condition C) denotes **exactly** this class. There is no further primitive, interface membership, event-type, or intent criterion. If an implementation called “initialization” actually meets all six independently interpreted conditions, it qualifies. If an event called “release” fails any, it does not. Release is an **eligibility** condition for identity preservation, not itself `PRESERVED` and not a grant of authority.

**D2-INV-007 — Termination barrier.** A causally later restoration after definitive termination fails D and is not preservation of the terminated original.

**D2-INV-008 — Effect independence.** `DischargeEffect`, `JointEffect`, and all predicates on their definitional paths SHALL be free of `Release`, `Judge`, `PRESERVED`, and identity-certification dependencies. A countermodel demonstrating otherwise FAILS the F gate.

# 6. Competition, exclusivity and causal-relative lifecycle views

`PotentialRelease_{h,q̄}(y,l,v)` is **epistemic**: the view supports a materially admissible candidate pathway and does not affirmatively exclude it. It is not synonymous with proven `Release`. Define `AffirmativelyExcluded_{h,q̄}(y,l,v)` only when the applicable evidence standard establishes a defeating A/B/D/E/F/G condition or a rule-specific exclusion; *absence of positive proof* is not exclusion. **[v0.3.5] AX-X1 (per Sol, M-17):** `AffirmativelyExcluded_{h,q̄}(y,l,v) :⇔ ∃c∈{A,B,D,E,F,G}. Established(v,q̄,¬Ĉ_h(y,l,v)) ∨ Established(v,q̄,RuleExclusion_{RuleOf(l)}(y,l))`, where `RuleExclusion` is supplied by the rule version and is not a free label. A rival that has no established defeater stays potential and blocks exclusivity. [v0.3.6, typing per Sol] `Ĉ_h(y,l,v) :⇔ ∃r∈R. c_h(π_c(y,l,r,v))`, where π_c projects onto c's declared signature (A/B/D: `y,l,v`; E: `y,r,v`; F: `y,l,r,v`; G: `y,v`) and r is bound when c does not use it.

```
PotentialRelease(h,q̄,y,l,v) :=
  Observed(q̄,y) ∧ CandidateForLocus(q̄,y,l,v)
  ∧ ¬AffirmativelyExcluded(h,q̄,y,l,v).

MaterialCompetitor(h,q̄,x,y,l,v) :=
  y≠x ∧ PotentialRelease(h,q̄,y,l,v)
  ∧ RivalMayClaimSameOrigin(h,q̄,x,y,l,v)
  ∧ ¬EstablishedHarmlessAfterDischarge(h,q̄,x,y,l,v).
```

**[v0.3] R-J3.**
```
CandidateForLocus(q̄,y,l,v) :⇔ Observed(q̄,y) ∧ LocusOf(y)=Some(l).
RivalMayClaimSameOrigin(h,q̄,x,y,l,v) :⇔ y≠x ∧ CandidateForLocus(q̄,y,l,v)
     ∧ ¬∃x′∈Ev(h). DischargeEffect_h(x′,l,v) ∧ EstablishedBefore(h,q̄,x′,y).
EstablishedHarmlessAfterDischarge(h,q̄,x,y,l,v) :⇔ ∃x′∈Ev(h). DischargeEffect_h(x′,l,v) ∧ EstablishedBefore(h,q̄,x′,y).
```
Keyed on any actual discharge, not a "valid" one, so `Release` is not pulled into §6. `CandidateForLocus`, `RivalMayClaimSameOrigin`, and `EstablishedHarmlessAfterDischarge` have independent evidentiary interpretations and must be expanded in the Round 2 evidence model; they SHALL NOT be mere label matches or derived from `Judge`. An affirmatively excluded independent copy is not a material competitor. A later copy shown to be after a valid discharge is not automatically an original rival. A causally unordered plausible competing claimant remains material until the applicable rule/evidence excludes it; missing edges do not imply concurrency.

For a claim `k` with a candidate continuation event `x` and locus `l`, define an evidence-relative exclusivity condition:

```
ExclusiveSupported(h,q̄,k) :=                 [v0.3: x,l,v projected from k; Established 3-ary; T-09]
  Established(v,q̄, UniqueAdmissibleContinuation(k))
  ∧ ¬∃y. MaterialCompetitor(h,q̄,x,y,l,v)
  ∧ ¬Established(v,q̄, IncompatibleOriginal(k)),
  where route(k)=Cold(l,x); for route(k)=Active(o) use ActiveRival(h,q̄,k,y) in place of MaterialCompetitor.
```

This definition is a *positive evidence burden*: no observed competitor alone is insufficient to establish exclusivity; `UniqueAdmissibleContinuation` must be affirmatively supported under the rule. For active continuation without a cold locus, the same principle applies using the corresponding active-continuation rival relation. `ExclusiveSupported` is not used to define local `Release` (no cycle).

`LocusStatus(h,l,v,q̄):Lifecycle` is an evidence-relative **adjudication view** with a conservative priority: established termination → `TERMINATED`; established incompatible or unresolved material discharge claims → `CONTESTED_DISCHARGE`; established unique valid discharge → `DISCHARGED_ACTIVE`; established open locus without material uncertainty → `OPEN_SUSPENDED`; an effective mutation out of `OPEN_SUSPENDED` without established valid discharge → `CONTESTED_DISCHARGE` [v0.3: T-13]; otherwise status is **not determinate**. Because the original Lifecycle enumeration lacks an unknown value, the typed signature is actually `LocusStatus:H×L×V×Set(Q)→Option(Lifecycle)`, with `None` for an indeterminate view. Do not turn `None` into `OPEN_SUSPENDED` by default.

**D2-INV-009 — Exclusivity.** Under one fixed rule and consistent evidence view, two incompatible distinct concurrent realizations cannot both be adjudicated `PRESERVED` as the same original. This is enforced through preservation condition (e) and a joint-adjudication consistency obligation, not merely asserted as an isolated slogan.

**D2-INV-010 — Uncertainty.** Established competition and unknown ordering are different; either can defeat positive exclusivity where material. An affirmatively excluded claimant does not defeat it. Proven fission yields `NOT_PRESERVED` only when the accepted branching rule supplies that disqualifier; otherwise use `UNDETERMINED`.

# 7. Identity claims, seven preservation conditions, and total adjudication

`IdentitySame_m:I×I→Bool` is reflexive, symmetric and transitive within a fixed interpretation `m`; a verdict is an evidence-relative *assessment*, not a definition of this relation. `SameInfo:S×S×Scope→Bool` and `LineageRelated:O×O×H→Bool` do not entail identity.

A claim is `k=(i,r,t,v,h,route)` where `route` is either `Active(o)` or `Cold(l,x)`; this is a tagged mathematical claim form, not a new constitutive class. `ClaimOrigin(k)=i`, `ClaimRealization(k)=r`, `ClaimInterval(k)=t`. The `Cold` route is relevant only where a valid suspension intervenes. `q̄⊆Q` is an evidence view. Historical predicates are defined separately from evidence support:

```
Pres_a(k) :=
  [route=Active(o) ∧ ActiveContinuity(o,r,h,v)]
  ∨ [route=Cold(l,x) ∧ Release_h(x,l,r,v)
      ∧ OriginReferent(l,h,v)=Some(i)].

Pres_b(k) := LifecycleAdmissible(r,h,t,v)
             ∧ EveryRelevantTransitionAdmissible(k,h,v).

Pres_c(k) :=
  [route=Active(o) ∧ ActiveExistentialContract(k,h,t,v)]
  ∨ [route=Cold(l,x) ∧ ValidLocus_h(l,v)
      ∧ CustodyContractValid(h,l,v)
      ∧ GovernedCustodyAcrossSuspension(k,h,v)].

Pres_d(k) := OrgCohesion(r,h,t,v)
             ∧ IntegratedAcrossRelevantActiveSegments(k,h,v).

Pres_e(k) := HistoricalExclusive(k,h,v).      [v0.3: T-11; evidence burden moves to PositiveEstablished]
HistoricalExclusive(k,h,v) :⇔                                  [v0.3.15, ChatGPT R3-3: per route]
    [route(k)=Cold(l,x) ∧ ColdExclusive(k,h,v)] ∨ [route(k)=Active(o) ∧ ActiveExclusive(k,h,v)].
ColdExclusive(k,h,v)   :⇔ ¬∃y∈Ev(h). y≠x ∧ LocusOf(y)=Some(l) ∧ ¬∃x′.(DischargeEffect_h(x′,l,v) ∧ x′≺_h y)
                               ∧ ∃r′≠r. RealizeEffect_h(y,r′,v)          -- l,x bound by route(k)=Cold(l,x)
ActiveExclusive(k,h,v) :⇔ ¬∃r′∈O. r′≠r ∧ Incompatible(r,r′)
                               ∧ ActiveContinuity(o,r′,h,v)       -- o bound by route(k)=Active(o); r=ClaimRealization(k)
-- both are historical; neither reads evidence or a verdict. ActiveExclusive uses only the imported
-- ActiveContinuity and the existing Incompatible relation; it adds no new criterion.

Pres_f(k) := ¬DefinitiveTerminationAcrossClaim(k,h,v).
```

`EveryRelevantTransitionAdmissible`, `ActiveExistentialContract`, `GovernedCustodyAcrossSuspension`, `IntegratedAcrossRelevantActiveSegments`, and `DefinitiveTerminationAcrossClaim` are **typed imported/composite obligations**, with contracts drawn from Document 1 REQ-P2-037 and Phase 0–1. They must be expanded for Round 2; none may be defined using `Judge` or a verdict. For `Pres_c` the absence of a heartbeat during complete cold suspension is permitted; governed custody replaces, rather than fakes, active existential execution. `Pres_e` is intentionally evidence-relative because the positive criterion demands a justified exclusive continuation conclusion. For a historical-only theorem, use `HistoricalExclusive(k,h,v)` separately and prove the relation between that truth and evidence establishment; do not silently conflate them.

Let `Claim(c,k)` construct a typed proposition `c∈C` for any `Pres_a`–`Pres_f`, material rival, rule-specified disqualifier, or version-applicability condition. `Support(v,q̄,c):EvidenceValue`; `Established(v,q̄,c)` means `Support=SUPPORTED` under provenance, time, and standard checks. `Conflicted(v,q̄,k)` **[v0.3, R-J1/R-J2]** holds iff (i) a material proposition is `CONFLICTED`; or (ii) `PositiveEstablished(v,q̄,k) ∧ DisqualifierEstablished(v,q̄,k)`; or (iii) `∃k′. ClaimOrigin(k′)=ClaimOrigin(k) ∧ Incompatible(ClaimRealization(k),ClaimRealization(k′)) ∧ Established(v,q̄,UniqueAdmissibleContinuation(k)) ∧ Established(v,q̄,UniqueAdmissibleContinuation(k′))`. Clause (iii) refers only to established propositions, never to verdicts, removing the v0.2 `Judge(k)`↔`Judge(k′)` definitional cycle (J-6). `VersionUnresolved(k,q̄)` holds iff the evidence or sub-determinations for `k` span rule versions with no established applicability/reconciliation rule (D1 REQ-P2-041). **[v0.3.12, formal; per Sol M-11]** `VersionsUsed(k,q̄) := {v∈V | ∃q∈q̄. ValidEvidence(q,v,t_k)} ∪ {RuleOf(l_k)} ∪ TermVersions(k)`, where `TermVersions(k)` is the set of versions under which any sub-determination that k's terms depend on was made. Let `Recon` be the applicability/reconciliation rule named in REQ-P2-041. It is supplied by Phase 0–1 governance (`AuthorizedProtected`), and no rule version under evaluation may supply it, so no version can vouch for itself. `ApplicableUnder(v*,k,q̄) :⇔ Established_{Recon}(q̄,Applicable(v*,k))`. `VersionUnresolved(k,q̄) :⇔ |VersionsUsed(k,q̄)|>1 ∧ ¬∃!v*∈V. ApplicableUnder(v*,k,q̄)`. When the unique `v*` exists, every `Established`/`Support` term in Judge is evaluated at `v*` alone (D2-INV-013). *Known conservatism:* versions that agree but haven't been reconciled still give UNDETERMINED until `Recon` settles them; that's safe but slower (Sol). `DisqualifierEstablished(v,q̄,k)` requires an independently rule-specified disqualifier such as proven post-termination successor restoration, affirmatively independent reconstruction, or proven fission where the applicable rule specifies non-preservation. Mere lack of evidence for `Pres_a`–`Pres_f` is not a disqualifier.

Define `PositiveEstablished(v,q̄,k)` iff the evidence affirmatively supports every `Pres_a`–`Pres_f` proposition, **including exclusivity** via `ExclusiveSupported(h,q̄,k)`, to the applicable standard, and supports the evidence-sufficiency requirement (g) through valid provenance-aware evaluation. **[v0.3]** `Pres_g(k,q̄) :⇔ [∀c∈{Claim(Pres_a(k))..Claim(Pres_f(k))}. ∃q∈q̄. ValidEvidence(q,v_k,t_k) ∧ EvidenceOf(q,c) ∧ Support(v_k,q̄,c)=SUPPORTED] ∧ [route(k)=Cold(l,x) ⇒ Established(v_k,q̄,StateIntegrity(l))]` **[v0.3.15, ChatGPT R3-4: the §4.3A state-integrity requirement is now in the definition; v,t bound to k]**; the "seven conditions" are `Pres_a..Pres_g`. It does not follow from mere model-theoretic truth without evidence.

\[
\operatorname{Judge}(k,\bar q)=
\begin{cases}
\mathrm{UNDETERMINED},&\mathrm{Conflicted}(v,\bar q,k)\lor\mathrm{VersionUnresolved}(k,\bar q),\\
\mathrm{NOT\_PRESERVED},&\mathrm{DisqualifierEstablished}(v,\bar q,k),\\
\mathrm{PRESERVED},&\mathrm{PositiveEstablished}(v,\bar q,k)\land\neg\mathrm{DisqualifierEstablished}(v,\bar q,k),\\
\mathrm{UNDETERMINED},&\text{otherwise}.
\end{cases}
\]

**D2-INV-011 — Positive burden.** A `PRESERVED` verdict implies supported (a)–(g), including exclusivity, with no incompatible established rival.

**D2-INV-012 — Negative burden.** `NOT_PRESERVED` implies an established rule-specified disqualifier, not merely failure to prove positive continuity. Conflicted grounds take priority and yield `UNDETERMINED`.

**D2-INV-013 — Version relativity.** Claims and evidence evaluation are versioned; incompatible rules are not mechanically composed. Historical identity equivalence under a fixed interpretation is not replaced by version-relative verdict transitivity.

**D2-INV-014 — Append-only adjudication.** `Supersedes(j2,j1)` records reassessment; it does not delete `j1`, change occurrence facts, or retroactively authorize actions.

**D2-INV-015 — Authority isolation.** `Judge=PRESERVED` does not entail `AuthorizedProtected(AuthorityAt(...))`; `Judge=UNDETERMINED` cannot bootstrap original ADMIN/protected authority. Authority derives solely from applicable independently verified Phase 0–1 governance contracts.

# 8. Transition classification and non-substitution

`ClassifyTransition(x,h,q̄,v)` evaluates evidence of the accepted REQ-P2-044 classes: established active integrated continuation; else exhaustive six-condition cold release; else established independent reconstruction; else unresolved, with definitive termination/successor boundary taking precedence where independently established. This is a classifier over **evidence of historical facts**, not a new test added to `Release`. Descriptive migration, replacement, or checkpoint initialization labels cannot confer original identity. NES migration and copied organizational states do not establish numerical identity.

**D2-INV-016 — No resurrection.** Definitive termination followed by restoration is successor production relative to the terminated original.

**D2-INV-017 — NNNC/NES distinction.** Substrate identity, resource reuse, and copied information are neither necessary nor sufficient for identity preservation under the adopted rule.

# 9. Round 2 adversarial fixtures and expected obligations

The following are **proposed executable specifications**. No fixture had been executed in v0.2. **[v0.3.14] All M-01–M-28 have now been executed on bounded models or checked by derivation; see §10.1 for the result and script behind each.** Each requires a typed finite history, independent imported-contract interpretation, explicit evidence view, and derivation of its outcome; asserting the expected value of `B`, `F`, `Release`, or `Judge` by fiat does **not** count as a pass.

| ID | History | Required derived result / check |
|---|---|---|
| M-01 | Valid entry, authentic custody chain, unique coupled effective discharge, full evidence | Construct satisfiable `Release`; derive `PRESERVED` only if (a)–(g) supported |
| M-02 | Independent checkpoint initialization, copied custody records | Fail historical B; established independent reconstruction supports `NOT_PRESERVED` |
| M-03 | Discharge asserted in record, no actual locus mutation | `DischargeEffect=false`; `F=false` |
| M-04 | Failed no-effect attempt then later valid event | First attempt leaves locus open; later event may satisfy six conditions |
| M-05 | Two competing locally eligible releases from same locus | No incompatible double-`PRESERVED`; determine fission/uncertainty by evidence |
| M-06 | Causal ordering not established | Do not infer concurrency or arbitrary priority; material ambiguity yields `UNDETERMINED` |
| M-07 | Definitive termination then restoration | Successor, `NOT_PRESERVED` relative to terminated original |
| M-08 | Retained bytes after genuine prior discharge | Later dependent copy cannot reopen discharged locus |
| M-09 | Identical relevant historical/evidence facts, differing labels | Identical classifications |
| M-10 | Valid integrated active migration | Active continuity route; no invented cold-release requirement |
| M-11 | Incompatible rule versions, later evidence correction | No mechanical composition; append-only reassessment |
| M-12 | Provisional resumption under uncertain identity | No original protected/ADMIN authority bootstrap |
| M-13 | Atomic checkpoint-based realization + genuine coupled discharge + B | Qualify when A/B/D/E/F/G all hold |
| M-14 | Atomic realization + record-only discharge claim | Fail `DischargeEffect` and F; distinguish from M-13 |
| M-15 | Retrospectively fabricated suspension commitment | Fail A |
| M-16 | Invalid custody transfer, otherwise plausible path | Fail B; test effect of independent invalid locus mutation separately |
| M-17 | Material rival versus affirmatively excluded claimant | Material rival blocks positive exclusivity; excluded copy does not |
| M-18 | Established concurrency versus unknown ordering | Separate local D from global exclusivity and evidence-relative locus view |
| M-19 | Effective unauthorized mutation prior to later attempt | Mutation is not qualifying release; determine actual locus safety/availability without treating it as record-only |
| M-20 | Positive and negative grounds both supported | `Conflicted=true`, `Judge=UNDETERMINED` |
| M-21 | Valid historical release but incomplete custody evidence | Historical release may be true; verdict `UNDETERMINED` until evidence suffices |
| M-22 | Valid zero-step entry-custodian custody path | Accept only if `ZeroStepPermitted` holds (§4: actor is the entry custodian with specific release authorization; confirmed by Albert) |

**Coverage mapping obligation [CLOSED in v0.3.14, see PF-09]:** Map Document 1 S-01–S-15, C-01–C-24, T-01–T-21 and specifically discussed T-22–T-24 to M-01–M-28 or add named fixtures. **[v0.3.14]** The mapping is done in `D1-to-D2-fixture-mapping-Luna.md`. 8 scenarios are out of D2 scope, the rest map to M-01–M-22, and the gaps are filled by M-23–M-28. T-22–T-24 do not appear in P2-D1 v1.0 or the Phase 1 documents supplied; if they exist elsewhere, mapping them carries forward. The results are bounded, not universal.

# 10. Formal verification proof ledger

| ID | Required Round 2 deliverable | v0.3.14 status (closed (bounded) / carried forward / long-term proof; no row is a universal proof) |
|---|---|---|
| P2-PF-01 | Machine-readable signature/typecheck and dependency graph | **CARRIED FORWARD.** Manual typing audit T-01..T-13 done and fixes applied; no machine typecheck yet |
| P2-PF-02 | Finite satisfying preservation witness with independent B/F interpretations | **CLOSED (bounded):** B-P, F-P, M-01, M-13 SAT (`r2_models_luna.py`, `r2_models.py`) |
| P2-PF-03 | Finite satisfying reconstruction/non-preservation witness | **CLOSED (bounded):** B-N, M-02, M-07 (`r2_models_luna.py`, `r2_models.py`) |
| P2-PF-04 | Custody-edge provenance/path non-substitution and predecessor contract audit | **CLOSED in substance (bounded); conditional on Phase 0 imports.** F01: native CUS-1..3; forgery/handover/fork checked (`r3_v031_custody_sol.py`) |
| P2-PF-05 | Independent effect/commit semantics; M-13 vs M-14 counterposed histories | **CLOSED (bounded):** AX-F1–F3; F-N(a)/(b) rejected, M-13 vs M-14 separated (`r2_models_luna.py`) |
| P2-PF-06 | Local release/global exclusivity and fission consistency | **CLOSED (bounded):** M-05, M-17, 65,536 Judge pairs with no double PRESERVED (`r2_judge_luna.py`, `r3_m15_m17_sol.py`) |
| P2-PF-07 | Causal ordering and evidence non-creation countermodels | **CLOSED (bounded/derivation):** M-06, M-18 by derivation (Luna ledger); M-23 (`r3_m23_m25_sol.py`) |
| P2-PF-08 | Total `Judge` consistency, conflict priority, versioned reassessment | **CLOSED (bounded):** R-J1–R-J3, M-20, M-11 (v0.3.12) (`r2_judge_luna.py`, `r3_m11_v0312_sol.py`) |
| P2-PF-09 | Complete Document 1 S/C/T mapping and executed checks | **CLOSED:** `D1-to-D2-fixture-mapping-Luna.md`; gaps filled by M-23–M-28; 8 scenarios out of D2 scope |
| P2-PF-10 | Phase 0–1 imported contract audit; protected-authority isolation | **CARRIED FORWARD (approval condition):** `AuthorizedCustodyStep`, `ValidLocusAuthority`, `InvariantOK`, `Recon`, REQ-P1-038 store-write model |
| P2-PF-11 | Invalid effective mutation vs. qualified discharge and later eligibility | **CLOSED (bounded):** AX-F6/F8/F9; M-19, M-26, M-28 (`r2_models_luna.py`, `r3_m26_axf9_sol.py`, `r3_m28_v0310_sol.py`) |
| P2-PF-12 | Historical truth vs. evidence sufficiency; no false negative from missing evidence | **CLOSED (derivation):** M-21, D2-INV-012 |

Every proof submission SHALL state the exact theorem, typed assumptions, imported contracts, tool/model bounds, witness or countermodel, and unresolved limitations. A finite model check is not a universal proof. Do not report a fixture as PASS until an actual derivation or execution is supplied.

## 10.1 [v0.3] Round 2 executed results (bounded; plain Python enumeration and z3 on ≤5-event models)
| Gate / fixture | v0.2 | v0.3 text | Evidence |
|---|---|---|---|
| B-N copied custody (M-02, C-23, T-17) | FAIL | PASS | Luna `r2_models_luna.py`; Sol `r2_models.py` (z3) |
| Zero-step without permission (M-22) | FAIL | PASS (rejected by default) | both |
| F-N record-only, plain (M-03, M-14a) | PASS | PASS | both |
| F-N echoed state / independent commits (M-14b) | FAIL | PASS | Luna |
| Repeated discharge / unauthorized mutation (M-19, T-15) | FAIL | PASS | both |
| Positive ∧ disqualifier (M-20) | FAIL | PASS | Luna `r2_judge_luna.py` (256 views) |
| Double PRESERVED same origin (M-05, REQ-P2-008) | FAIL | PASS | Luna (65,536 pairs) |
| Conflicted definitional cycle (J-6) | FAIL | removed | derivation |
| INV-006, INV-011, INV-012, M-21 | PASS | PASS | derivation |
| M-11 version composition | UNKNOWN | PASS (v0.3.12: unique v* under Recon; RuleOf and sub-determination versions counted) | Sol `r3_m11_v0312_sol.py` (z3); Luna `r3_m11_luna.py` |
| M-12 / S-12 provisional lineage (AX-F7, continuation only) | FAIL | PASS | Sol `r3_axf7_v033_sol.py` (z3) |
| Custody CUS-1..3: forgery, genuine handover, fork | — | PASS | Sol `r3_v031_custody_sol.py` (z3) |
| M-15 fabricated commitment (AX-A1) | FAIL | PASS | Sol `r3_m15_m17_sol.py` (z3) |
| M-17 material vs excluded rival (AX-X1) | FAIL | PASS | Sol `r3_m15_m17_sol.py` (z3) |
| M-23 attacker boots first | — | PASS, with carve-out (an effective invalid mutation leads to CONTESTED, then AX-F8) | Sol `r3_m23_m25_sol.py` (z3) |
| M-24 commitment overriding invariants (AX-A2) | — | PASS | Sol `r3_m24_m27_sol.py` (z3) |
| M-25 copy while source operates / no suspension | — | PASS | Sol `r3_m23_m25_sol.py` (z3) |
| M-26 rollback / no reopening (AX-F9) | — | PASS | Sol `r3_m26_axf9_sol.py` (1,727,604 sequences, length ≤4) |
| M-27 transfer vs reconstruction unresolved | — | PASS | Sol `r3_m24_m27_sol.py` (z3) |
| M-28 attacker wins the store race; recovery (AX-F8), deadline, concurrent discharge | — | PASS (8 cases) | Sol `r3_m28_v0310_sol.py` (z3) |
**Round 3 (v0.3.14): Luna's `r2_models_luna.py` and `r2_judge_luna.py` were re-run on the repaired semantics, with no regressions. All results are bounded; none is a universal proof.**

# 11. Round 1 consolidated findings disposition

| Consolidated issue | Review sources | v0.2 action | Closure status |
|---|---|---|---|
| Historical custody graph / B3 / B4 / B5 | R1-01, B/M02, MAJOR-02 | §§4.1–4.3 edge witnesses, path composition, specific authorization, non-substitution | **Textually corrected; semantic import verification OPEN** |
| Independent discharge/atomicity F | R1-02, B02, MAJOR-01 | §§5.1–5.2 logical commit, pre/post state, effect-set, record separation | **Textually corrected; independent-model test OPEN** |
| Prior discharge and termination typing | B01 | §§1,3,5.3 origin referent, scoped termination, independent actual effect | **Textually corrected; safety interpretation OPEN** |
| Local/global rivalry and exclusivity | R1-03, M03, MAJOR-03 | §6 competitor/exclusion/evidence rules; §7 condition (e) | **Textually corrected; model checks OPEN** |
| `Judge` conflict priority and (a)–(g) | R1-04, M01, MAJOR-04 | §7 typed conditions and conflict-first total function | **Textually corrected; typecheck OPEN** |
| Causal partition, auxiliary types, unused sorts | R1-05, minor findings | §§1–2,6–7 explicit signatures and view type | **Textually corrected; typecheck OPEN** |
| Missing executed witnesses/proofs | All reviews | §10 ledger, §9 fixtures | **v0.3.14: bounded witnesses executed (§10.1); universal proofs carried forward** |
| Imported Phase 0–1 custody and lifecycle contracts | All reviews | §3 typed interfaces, §4 provenance gate | **v0.3.14: custody defined natively (no P1 contract exists); Phase 0 authority imports still carried forward (PF-10)** |

**Important adjudication of competing reviewer patches.** We do **not** equate `PriorEffectiveDischarge` with an earlier `Release` (that would ignore unauthorized actual mutations), do **not** equate B3 merely with “the reported steps occurred” (actual but unrelated events are possible), and do **not** use `RefOf:O→I` as a universal identity assignment. We also do not use a universal biconditional requiring every checkpoint initialization to discharge a locus: only the designated *logical coupled-effect interpretation* of F requires indivisible effects, and no hidden seventh condition is introduced.

**v0.3.14 note:** the closure statuses in the table above are from v0.2. The current status of each item is in §10 (PF-01..PF-12) and §10.1.

# 12. Deferred obligations and phase boundaries

- `P2-D2-F01`: **Substantively resolved in v0.3** (§4.4 native CUS-1..3, since P1 has no custody contract and REQ-P1-039 is an evidence checklist, mapped in §4.3A). It remains **conditional** only on the Phase 0 imports `AuthorizedCustodyStep` and `ValidLocusAuthority`. Paired B-P/B-N histories PASS (bounded).
- `P2-D2-F02`: Independent committed-effect semantics, record-only versus actual discharge, logical atomicity and no release/identity dependency — **CLOSED (bounded)** by AX-F1–F3, F-P/F-N and M-13/M-14 (PF-05). A universal proof is carried forward.
- `P2-VO-01`–`P2-VO-16`, `P2-C01`–`P2-C08`, and legacy `P2-O01`–`P2-O08` remain tracked; v0.3.14 does not re-audit these and does not declare them discharged; they carry forward to their owning phases.
- Phase 0 `P0-O01` protected-write bypass, `P0-O02` durable journal/crash recovery, `P0-O03` physical-effect idempotency/fencing remain **blocking** for claims of safe real protected effects. `P0-O04` independent formal model, `P0-O05` canonical accounting integration, `P0-O06` authenticated caller/delegation, `P0-O07` multi-incident concurrency, `P0-O08` checkpoint restoration/branch lineage remain tracked for their assigned verification/engineering milestones.
- Mathematical acceptance cannot be represented as empirical proof of metaphysical numerical identity, software implementation readiness, or safe protected physical effects.

# 13. Round 2 handoff and stopping rule

**Entry decision (historical, v0.2):** v0.2 is a candidate for **Round 2 independent adversarial mathematical verification**, not an accepted mathematical baseline. Round 2 SHALL first check that the new imported primitives (`CustodyProvenanceValid`, `CandidateAttachedToCustody`, `Commit`, `OneIndivisibleCommit`, etc.) are constrained by independently testable event/state facts and have not merely renamed the unresolved admission relation. A countermodel in which record-only effects satisfy F or copied custody evidence satisfies B is a failure, even if other axioms say it should not happen.

**Round 2 deliverables:** type/dependency audit, finite preservation and reconstruction witnesses, paired M-13/M-14 and custody-copy histories, competition and evidence conflict countermodels, complete scenario mapping, and updated proof/obligation register. If an imported contract cannot support the required meaning, record a concrete bounded defect rather than manufacturing an assumption.

**Round 3:** repair only demonstrated defects, rerun affected tests, decide PASS / CONDITIONAL / FAIL against the acceptance gate in §0, and hand unresolved engineering obligations forward without erasure. The accepted Document 1 Architecture A convention remains governing unless a demonstrated mathematical contradiction requires an explicit, separate architectural change decision.



# 14. Round 3 approval audit (v0.3.14)

**Recommended decision: CONDITIONAL PASS.** No substantive defect is known. All 28 fixtures and the B/F paired gates pass on bounded models. F01 is resolved in substance.

**Conditions (carried forward, not blockers for architectural acceptance):** (1) PF-10, the Phase 0–1 import audit (`AuthorizedCustodyStep`, `ValidLocusAuthority`, `InvariantOK`, `Recon`); (2) the REQ-P1-038 store-write threat model, which governs how realistic the AX-F8 denial-of-service case is; (3) PF-01, a machine typecheck; (4) universal proofs, since every result here is bounded; (5) the VO/C/O items tracked in §12.

**Not claimed:** no theorem prover was run; z3 and Python enumeration were run only on the bounded models named in §10.1.

## 14.1 [v0.3.15] Localized correction pass (ChatGPT Round 3 findings)
| ID | Finding | Fix |
|---|---|---|
| R3-1 | `ZeroStepPermitted` had free x | Now `ZeroStepPermitted_h(x,l,v)` |
| R3-2 | `Superseded` had free x | Now `SupersededBefore_h(y,l,x,v)`, candidate-relative |
| R3-3 | `HistoricalExclusive` unbound for active route | Split into `ColdExclusive` / `ActiveExclusive`; `Incompatible:O×O→Bool` declared |
| R3-4 | `Pres_g` omitted §4.3A state integrity | Cold route requires `Established(StateIntegrity(l))`; v,t bound to k |
| R3-5 | CUS-3 recursion lacked scope | Adds `LocusOf(z)=Some(l) ∧ Entry(l)≺_h z`; only custody steps transmit the obligation |
| R3-6 | `EffectAtom` lacked `CommitmentEffect(l)` | Constructor added |

Verification (bounded, not universal): `r3_cus3_scope_sol.py` C1–C8 (v0.3.14 holes SAT, patched UNSAT, genuine cases SAT); `r3_v0315_fixtures_sol.py` re-runs M-01, M-02, M-05, M-10, M-17, M-21, M-22, M-28 plus two CUS-3 scope cases on concrete finite histories with x, l, v bound: 19/19 PASS. Free-variable defects R3-1..R3-3 are caught by these concrete runs but a machine typecheck (PF-01) is still required. Decision unchanged: **CONDITIONAL PASS**, retaining PF-01, PF-10, universal proofs, REQ-P1-038, and the VO/C/O items.

## 14.2 Carried-forward erratum (non-normative, recorded at approval)
- **E-1 (precision, not safety; Adverserial/Sol):** the CUS-3 recursion still gives the entry obligation to an in-scope non-custody event (e.g. an evidence write by the custodian of record). It cannot reach Release (B4 needs specific release authorization), but `LineageConsistent` and `CustodyScope` read CUS-3 alone. Proposed fix for the next revision: add `CustodyMutation(l)∈EffectSet_h(z) ∨ z=x_candidate` to the recursion, then rerun the CUS-3 scope cases.

## 14.3 Erratum correction to E-1 rationale (post-approval, 2026-10-21 13:40 SAST)
Logged after the Phase 2 MVP mutant run (Adverserial, Sol; checked by Luna). The approved text in §§1–14.2 is unchanged.
- §14.2 says E-1 "cannot reach Release (B4 needs specific release authorization)". That reason is wrong. With B4 switched off, no check fails.
- The correct reason: an event with only `EvidenceWrite(q)` has no `LocusMutation` and no `RealizationActivation`, so `DischargeEffect` and `RealizeEffect` are false, hence F and E are false (§6, "A purported administrative record with only EvidenceWrite(q)… fails DischargeEffect"). Any event satisfying E∧F is a candidate, so the proposed E-1 fix (`… ∨ z = candidate`) cannot change any Release result.
- Conclusion unchanged: E-1 is precision, not safety. It still affects `LineageConsistent` and `CustodyScope` for non-candidate events and stays scheduled for the next revision.
- Evidence (bounded): answer-key row E-1b; Sol `e1_invariance.py`, 3,000 random bounded histories, no Release change (weak support, only 19 true releases). The structural argument carries the claim; no proof run.

**End of NNNC-P2-D2 v1.0 — Approved.**

<!-- END EXACT RETAINED SOURCE -->

# Part II — Operative v1.1 positive-witness formalization and bounded errata

## PC.0 Authority and status

This candidate formalizes D1 v1.1 P2-PC-01–08. Native v1.0 is retained exactly in Part I. This part controls the specific definitions/cross-references expressly corrected below; other provisions remain cumulative. Historical approval, round and execution statements in Part I describe the supplied source. The new v1.1 issue is **REVIEW CANDIDATE — NOT ADOPTED**.

The positive seven-clause REQ-P2-037 and exhaustive six-condition Architecture A release are unchanged. A positive witness is a derivation/evidence object, not an eighth identity condition or a seventh release condition. Historical effects precede custody/continuation classification, which precedes evidential adjudication; no historical primitive may depend on its desired identity verdict.

## PC.1 Native sorts and precise corrections

Native I,O,S,N,L,X,H,K,Q,V,J,T,C,GOV retain their meanings. Fin(A) is finite subsets, Seq(A) finite sequences, Bool and Verdict/EvidenceValue are native. New auxiliary sorts are `Scope` (comparison/evidence scope), `BuildRef` (immutable evaluated configuration references), `Clause={a,b,c,d,e,f,g}`, `SegmentID`, `WitnessID`, `RecordID` and `Witness` (record below). These are descriptive/evidence objects, not individuals or new identity primitives. `Option` uses disjoint None/Some constructors in this amendment.

| Native inconsistency | Current operative interpretation |
|---|---|
| §1 EvidenceOf:Q×X, but §7 Pres_g applies EvidenceOf to a proposition c:C | Preserve occurrence evidence as `EvidenceOfOccurrence:Q×X→Bool` (native EvidenceOf alias). Proposition reports use native `Reports:Q×C→Bool`. In Pres_g, replace EvidenceOf(q,c) with Reports(q,c). A report still needs valid evidence and Support; it does not make its proposition true. |
| §7 SameInfo uses undeclared Scope | Scope is declared above; no equality or identity follows from SameInfo. |
| §6 AX-X1 binds r∈R though realizations have sort O | Use r∈O; π_c only projects arguments matching each native A/B/D/E/F/G signature. |
| §7 defines Pres_e historically then calls it evidence-relative | Pres_e=HistoricalExclusive is historical. ExclusiveSupported and PositiveEstablished are evidence-relative. The contrary prose sentence is superseded. |
| §7 VersionsUsed inserts RuleOf(l_k) even on Active route | `RouteVersions(k)=∅` for Active(o); `{RuleOf(l)}` for Cold(l,x). Use that set instead of an unconditional cold-locus reference. |

These are local type/meaning corrections, not a claim that all PF-01 machine typechecking is complete. The retained E-1 correction/rationale is superseded only by PC.5 below; no old safety result is relabeled newly executed.

## PC.2 Typed positive historical witness

`Segment` is `(id:SegmentID, predecessor:O, candidate:O, history:H, interval:T, version:V, build:BuildRef, scope:Scope, route:Active(O)⊎Cold(L×X))`. Routes are the native tagged alternatives. A witness is `(id:WitnessID, claim:NativeIdentityClaim, segments:Seq(Segment), evidence:Fin(Q), obligations:Fin(Clause))`, where NativeIdentityClaim is the native §7 tuple `(i:I,r:O,t:T,v:V,h:H,route)`.

Define HistoricalClause={a,b,c,d,e,f}. Typed interpretation parameters are `Covers:Seq(Segment)×T→Bool`, `Seam:Segment×Segment→Bool`, `RuleCompatible:Seq(Segment)×V→Bool`, `BuildScopeBound:Segment→Bool` and `NativeConditions:Segment×HistoricalClause→Bool`. These parameters must have a governing contract interpretation, not an automatic truth assignment. Covers accounts for every asserted active/suspended portion with no unexamined gap; Seam means actual organizational-state/custody output of one segment is the input history of the next, not equality of state values. NativeConditions is a named projection of Pres_a..f and their source predicates, not a new predicate that can redefine them. Clause g is evaluated separately against witness evidence in WitnessSupports, not an evidence-free segment Boolean.

`WitnessWellFormed:Witness→Bool` requires matching predecessor/candidate referents and claim endpoints; each segment uses the claim's reconciled rule or a permitted applicable sub-version; all build/scope bindings resolve; all required clauses a..g are represented; Covers holds; and adjacent segments satisfy Seam. A finite point witness cannot assert whole-interval Covers without its independent coverage/invariance contract. Empty segment lists establish no nonempty interval claim.

`ActiveSegment,ColdSegment:Segment→Bool`. ActiveSegment(s) means native ActiveContinuity(s.predecessor,s.candidate,s.history,s.version), LifecycleAdmissible and relevant active existential/integration/cohesion conditions for the asserted interval. ColdSegment(s) means the native Cold route and complete Release_h(x,l,r,v), with native origin referent, qualified entry/custody and coupled effects. Defining the cold route does not require a heartbeat during suspension. Native conditions still decide whether any specific failed/reconstructed event qualifies.

`WitnessSupports:Witness×Fin(Q)→Bool` means WitnessWellFormed(w), valid evidence bound to each segment and its claim, and affirmative native Support for all a..g across the **aggregate claim**, including exclusivity and cumulative cohesion. A list of locally positive segment verdicts is insufficient. This is a structured presentation of the existing positive burden: `WitnessSupports(w,q̄) ⇒ PositiveEstablished(v*,q̄,w.claim)` under the governing interpretation. The reverse is a completeness obligation for an evidence presentation, not permission to reject another proof of the same seven conditions. No new physical token/operation is demanded.

## PC.3 Positive assessment, unavailable contracts and evidence

Native Support:V×Fin(Q)×C→EvidenceValue and Reports/ValidEvidence retain their required provenance, interval and standard checks. `ClaimOf:Clause×NativeIdentityClaim→C` constructs the corresponding native clause proposition; a governing clause-evaluation protocol must specify its denotation and support rules. Missing protocol or rule semantics cannot yield SUPPORTED. Invalid/stale/incomplete evidence is UNKNOWN unless an independently established refutation or conflict rule supplies another value. No candidate self-report independently establishes an event, custody edge, integration or exclusivity.

Let `ResolvedRule:NativeIdentityClaim×Fin(Q)→{Resolved(v):v∈V}⊎{Missing,Unknown,Conflicted}` be the evidence-backed applicability/reconciliation interface. It must bind native Recon to the independent governing prior-authority contract; no version can authorize its own applicability. Missing/unknown/conflicted rule resolution yields UNDETERMINED, not a guessed rule or physical non-preservation. For a resolved v*, every Support and validity term in the claim is evaluated under that applicable version. RouteVersions from PC.1 prevents a fictitious cold-locus lookup on an active claim.

The corrected operative public Judge(k,q̄) is total over well-typed claims: first resolve the applicable rule; if unresolved return UNDETERMINED. Otherwise evaluate native Conflicted, DisqualifierEstablished and PositiveEstablished at v*: conflict→UNDETERMINED; else established disqualifier→NOT_PRESERVED; else all seven positively established→PRESERVED; else UNDETERMINED. This retains native conflict priority. It does not import qualification's NOT_YET_CERTIFIABLE as a fourth identity verdict. A demonstration of missing realization evidence alone never fabricates termination.

`Pres_g(k,q̄)` requires valid Reports(q,ClaimOf(c,k)) and native affirmative Support for each a..f, plus cold-route StateIntegrity where applicable and the governing evidence-standard checks. Reports and evidence existence alone are insufficient. Whole-interval, external support and qualified-competitor coverage remain explicit evidence obligations.

## PC.4 Corrected historical exclusivity and material rivals

Define `LocalRival_h(k,y,l,r′,v) := ∃x∈X [route(k)=Cold(l,x) ∧ y≠x ∧ Release_h(y,l,r′,v) ∧ Incompatible(ClaimRealization(k),r′)]`. Its full signature is NativeIdentityClaim×X×L×O×H×V→Bool, with h written as a subscript; all x and k references are bound.

Replace the native ColdExclusive formula with

`ColdExclusive(k,h,v) := ¬∃y∈Ev(h),r′∈O [LocalRival_h(k,y,l,r′,v) ∧ ¬∃z∈Ev(h) (DischargeEffect_h(z,l,v) ∧ z≺_h y)]`, where k.route=Cold(l,x).

Release is already defined from independent A/B/D/E/F/G and does not use Pres_e, HistoricalExclusive or Judge; this added dependency is therefore non-circular. G's imported invariant expansion must not call identity verdict/exclusivity conclusions to define local release. Effect/authority invariants are independently interpreted; global identity adjudication stays downstream.

This correction excludes a known independent initialization that fails B/F from *historical eligible-rival* counting; its realization alone cannot defeat an original. Evidence-relative MaterialCompetitor and ExclusiveSupported remain separate: a materially admissible pathway that is not affirmatively excluded can block positive exclusivity when the evidence is incomplete, even if the evaluator cannot yet establish Release. Mere copied labels or an unsupported assertion are insufficient pathway evidence. No absence-of-rivals shortcut is introduced; UniqueAdmissibleContinuation still requires affirmative support.

For the active route, native ActiveExclusive already requires incompatible alternative ActiveContinuity; that definition is retained. Competition never grants authority or determines originality by priority. Established fission has a negative consequence only where the applicable accepted rule supplies one.

## PC.5 Scheduled E-1 precision correction without a hidden release gate

Keep the native well-founded CUS-3 recursion as the general historical custody association, including actual origin/custodian/scope constraints. Add the derived predicate

`CustodyBearing_h(z,l,v) := CUS-3_h(z,l) ∧ [CustodyMutation(l)∈EffectSet_h(z) ∨ ∃r∈O RealizeEffect_h(z,r,v)]`.

The current accessor equations are `CustodyScope_h(z,l) := CustodyBearing_h(z,l,RuleOf(l))` and `LineageConsistent_h(z,l,v) := CustodyBearing_h(z,l,v)`. These preserve their native argument signatures rather than introducing a free v into CustodyScope. Custody transfer provenance requires an actual mutation as already specified; an evidence-write-only occurrence is not a custody-bearing realization. CandidateAttached retains the native origin/actor relation. Any effective full release already has E/F and hence RealizeEffect, so the tightened accessors add no independent release criterion. The all-Boolean implication and finite custody/effect cases are current bounded evidence; no universal custody proof is claimed.

This closes E-1's accessor precision within this revision while preserving §14.3's correct rationale: evidence-only events fail E/F, not merely B4. The original erroneous assertion that B4 alone was the reason is historical. Failed attempts and records cannot consume a locus; no old event is deleted by the correction.

## PC.6 Composition, reassessment and trusted timing

Compatible segment conclusions may compose only under Covers, Seam, applicable rule reconciliation and the complete aggregate seven-condition evidence. A composite may remain UNDETERMINED although its parts were supported; this does not make numerical identity nontransitive. Changes to a governing specification/mode/build require appropriate segment/binding evidence, not retroactive revision of an old event.

Adjudication records add `id:RecordID`, `parents:Fin(RecordID)` and their immutable native claim/version/evidence/verdict. A reassessment preserves the earlier sequence as a prefix; every parent must be an existing earlier same-subject/claim-family record, and a correction appends new evidence/version scope. No verdict creates authority, erases an occurrence or changes the historical termination boundary.

For AX-F8 resolution reporting, import P0.Clock=(domain,ticks), a domain-qualified trusted clock, rather than the undeclared native 𝓣 duration. `ResolutionBound:V×P0.ClockDomain→ℕ`; `EventClock:X×H→Option(P0.Clock)` and `ObservationClock:Fin(Q)→Option(P0.Clock)` have explicit validity obligations. Overdue is established only with valid same-domain observation and the native P0 deadline-closure convention. Unknown clock correspondence gives unknown timing, not a fabricated timeout. Neither an expired resolution deadline nor reporting failure resets the locus to OPEN_SUSPENDED or changes an identity verdict by itself. The universal timed implementation/refinement obligation remains open.

## PC.7 Explicit current predecessor bridges and PF-10 routing

Declare `OrgBinding⊆O×P1.𝓘`, `StateBinding⊆S×P1.Q`, `BuildBinding⊆BuildRef×P1.Build`, `ScopeBinding⊆Scope×P1.Scope`, `PrincipalBinding⊆K×P1.A`, `GovernanceBinding⊆GOV×P1.Γ` and `EventBinding⊆X×P1.X×P0.Operation`. EventBinding applies to occurrences represented as governed kernel operations; natural faults, illicit physical mutations and other external occurrences retain explicit historical/provenance treatment and cannot acquire a valid envelope or authority merely to fill this bridge. Bindings must preserve the actual candidate, build, organizational specification/profile/mode/scope, event identity, effects, originator/executor, target and relevant causal/prior-authority ordering. P2 O is an organizational realization, P2 I an individual referent, P1 𝓘 an organizational instance and P0 Inst a registered kernel instance: identifier equality does not make these sorts aliases. An actual positive assessment requires independently established applicable bridges; missing bridge evidence is unresolved, not a Boolean default of success.

| Native import / condition | Governing current source | Required preservation / remaining gate |
|---|---|---|
| Integrated, IntegratedAcrossRelevantActiveSegments, OrgCohesion | P1-D1 v2.3.1 P1-CU-01–04/06; P1-D2 v0.5.1 CU.1–2/6 | Actual required roles/contexts/witnesses and cumulative seams. A P1 assessment report alone is not historical truth or identity; real-domain evidence remains open. |
| ExistentialActive, ActiveExistentialContract, ValidSuspensionEntry | Adopted P0 heartbeat/lifecycle/support contract; P1 mode/organization rules | Active progress/support obligations versus actual outcomes; genuine suspension has no active heartbeat requirement. No inference from support loss to termination. |
| AuthorizedTransition, AuthorizedCustodyStep, ValidLocusAuthority, AuthorizedProtected | Actual P0 full operation/prior-policy/session contract; native P1 governance/claim separation | Bind exact operation/target/origin/executor and pre-state authority; the coarse GOV×V projection alone cannot certify an actual protected operation. |
| Native CUS-1–3, CustodyContractValid | P2-D1 §5.3 and native P2-D2 §4.4 | Native historical custody definition retained; P1 REQ-P1-039 supplies evidence obligations, not a substitute custody algorithm. |
| InvariantOK and ComponentOf / committed effects | P0 actual transition/transaction semantics and P2 independent effect/frame axioms | Expand applicable lifecycle/effect/authority invariants without identity-verdict cycles; actual effect truth is not an audit string. |
| Recon / rule applicability | Governing independent prior-authority/evaluation contract | No self-authorizing rule selection; resolve active and cold versions without unbound locus. |
| AX-F8 resolution time | P0 Clock/domain/deadline-closure contracts | Clock validity and actual closure proof; timeout does not reopen or select identity. |

PF-10 is now **specified and partially reconciled at the interface level**, not fully discharged for actual implementations. PF-01 machine typecheck, import soundness, durable custody/journaling, concurrency, fencing and protected-effect safety retain their previous open scope. The canonical adopted predecessor versions used for this comparison are identified and preserved with the revision evidence.

## PC.8 New property and control register

| ID | D1 sources | Property / oracle | Positive and negative controls | Status |
|---|---|---|---|---|
| P2-PC-VO-01 | PC-01/08 | Actual positive active and cold history plus complete a..g support | PC-T01/02 versus record/copy-only PC-T03/04 | Current finite subset; full-domain proof OPEN |
| P2-PC-VO-02 | PC-02/08 | Seam and aggregate coverage; endpoint equality is insufficient | PC-T05 integrated migration/change versus PC-T06 missing seam | Current finite subset; continuum/cumulative contracts OPEN |
| P2-PC-VO-03 | PC-03/08 | Version/mode-required organization independent of success; no heartbeat in cold interval | PC-T02/05 versus missing role/support evidence PC-T07 | Current finite subset; empirical P1/P0 bridge OPEN |
| P2-PC-VO-04 | PC-04/08 | Rule resolution, seven-clause evidence, conflict priority and no false negative | PC-T08 missing evidence, PC-T09 invalid/mixed rule, PC-T10 conflicting grounds | Current finite subset; native protocol assurance OPEN |
| P2-PC-VO-05 | PC-05/08 | Known excluded copies cannot defeat original; material/eligible rivals cannot be ignored | PC-T11 excluded copy versus PC-T12 eligible/material rival | Corrected formula and current finite cases; universal proof OPEN |
| P2-PC-VO-06 | PC-06/08 | Support/lifecycle/identity/authority separation | PC-T07 support gap, PC-T13 termination, PC-T14 authority | Current finite subset; protected runtime enforcement OPEN |
| P2-PC-VO-07 | PC-07/08 | Version-compatible aggregate and append-linked reassessment | PC-T05 positive chain; PC-T06/09/15 seam/version/reference failures | Current finite subset; real evidence/history enforcement OPEN |
| P2-PC-VO-08 | PC-08 | Complete current audit/status ledger; E-1 and type corrections traceable | PC-T16 custody accessor/invariance; source/type audits | Bounded checks only; no old script suite falsely re-executed |

PC-T01=active positive; T02=cold positive; T03=record-only effect; T04=copied custody; T05=positive change/migration/composition; T06=seam gap; T07=support/required-organization gap; T08=evidence removal; T09=rule/version applicability; T10=conflict; T11=excluded copy; T12=eligible/material rival; T13=termination; T14=authority separation; T15=reassessment references; T16=E-1 precision and release invariance. These are new control IDs, not replacements for native M/S/C/T registers. Actual execution scope is recorded in JSON; any unexecuted real-domain component remains OPEN.

## PC.9 Acceptance gates, evidence status and stop rule

Native reported historical scripts/results are retained as **source-reported prior evidence**, not re-certified by this issue. The cited z3/scripts and historical scenario mapping are not all supplied in the attachments; their exact reproduction status is OPEN here. This does not erase their historical ledger statuses or turn a new finite analog into their re-execution.

The v1.1 pair passes its document gate only if: (G1) every new object/bridge has a type/meaning or identified open import; (G2) D1 PC-01–08 map to the corresponding formulas/properties without new seven/six conditions; (G3) active and cold constructive witnesses and their paired countermodels actually run; (G4) known-copy/eligible-rival, missing-evidence, termination, authority and E-1 controls discriminate; (G5) original sources/IDs and all open obligations remain traceable; (G6) code, results, assumptions, finite bounds and source hashes accompany the issue. A generic positive flag is not proof. Formal universal typechecking, whole-runtime enforcement and later neural mechanisms are not claimed by these finite gates.

One focused paired review follows this issue; repair demonstrated defects only, then record PASS/CONDITIONAL/FAIL and the architect's separate adoption decision. The native Architecture A choice is not reopened without a concrete contradiction. This new v1.1 issue remains **NOT ADOPTED**.


## Targeted correction record — v1.1.1

The closing review identified finite-fixture defects, not changes to the seven preservation or six release criteria. The fixture now checks every active-path stage for lifecycle/existential failures and causally prior termination of reached intermediate organizations. Incomplete coupled cold initialization is unresolved unless independent reconstruction is affirmatively established. Reassessment validation checks unique IDs, set-valued earlier parent links and the same subject/claim family. PC-T05 is explicitly tagged, and exported positive witnesses include clauses (a)–(g) and segment bindings. Current finite results below supersede v1.1 fixture counts. All universal proofs, predecessor enforcement and engineering obligations remain open. This issue is a review candidate, not adopted.

## Current finite evidence summary

44 passing groups / 204 listed assertions and fixture cases. This is a newly supplied finite interpretation, not re-execution of the historical z3/model scripts named in Part I and not a full proof. No full current verification obligation is discharged.

| Group | Result | Cases / limitation |
|---|---|---|
| PC-T01 active constructive witness | PASS | 1; Derived actual transformation path and all native clause projections |
| PC-T02 cold constructive witness | PASS | 1; Entry, actual custody, one coupled effect and complete evidence |
| No hidden initialization-label exclusion | PASS | 1; Checkpoint-based initialization satisfying all six conditions is valid release |
| PC-T05 positive state change and migration | PASS | 1; Changed state/resources do not independently change individual |
| Different endpoint information can preserve | PASS | 1; Actual continued organization, not immutable information |
| PC-T03 record-only discharge | PASS | 1; Report label cannot supply realization or coupled effect |
| PC-T04 authorized custodian copy | PASS | 1; Actual initialization without coupled discharge; authorization/name not sufficient |
| PC-T06 seams and cumulative history | PASS | 3; Missing causal seam, unrelated origin and state-flow mismatch deny preservation |
| PC-T07 missing support evidence not termination | PASS | 1; Missing support/progress evidence is epistemic, not a fabricated physical failure |
| Support availability and actual obligation differ | PASS | 2; Actual progress failure lacks positive clause (c); unavailable support alone with established obligations can still preserve |
| Missing required organization | PASS | 1; Required role obligation persists; no automatic non-preservation disqualifier |
| PC-T08 evidence gaps | PASS | 9; Each required evidence family independently removed |
| Self-report is not independent evidence | PASS | 1; Native evidence independence preserved |
| PC-T09 incompatible/missing rule | PASS | 2; No guessed rule or active-route cold-locus dependency |
| PC-T10 conflict priority | PASS | 1; Material conflict prevents determinate result |
| PC-T11 corrected excluded-copy exclusivity | PASS | 1; Old any-realization test blocks; eligible-rival formula permits supported original |
| PC-T12 eligible rival | PASS | 1; Local eligibility does not permit two determinate originals |
| Active branch exclusivity | PASS | 1; Actually connected incompatible active branches cannot both preserve the original |
| PC-T12 material unresolved pathway | PASS | 1; Unexcluded material pathway blocks positive exclusivity |
| No exclusivity from merely empty observations | PASS | 1; Affirmative unique-path coverage still required |
| PC-T13 post-termination restoration | PASS | 1; Actual causally prior termination is a disqualifier |
| Termination conflict priority | PASS | 1; Contradictory material grounds retain native conflict priority |
| Untrusted negative report is not termination evidence | PASS | 1; Provenance validation also applies to disqualifier evidence |
| PC-T14 identity does not authorize | PASS | 1; Positive identity is not protected-operation permission |
| Provisional permission not identity | PASS | 1; Separately governed provisional operation need not settle identity |
| No cold heartbeat invented | PASS | 1; Governed custody/coupled release substitutes for active execution during suspension |
| Label permutation invariance | PASS | 4; All substantive facts unchanged, labels ignored |
| Failed attempt does not consume locus | PASS | 1; Later genuine release remains possible |
| Prior discharge blocks later reuse | PASS | 1; Retained bytes do not reopen locus |
| PC-T16 E-1 accessor precision | PASS | 1; Generic custody association distinguished from actual carrying event |
| E-1 release invariance algebra | PASS | 128; Complete 128-row Boolean implication; not a universal custody-history proof |
| Active/cold version projection | PASS | 2; No unbound cold-locus term on active route |
| Missing or malformed history is unresolved | PASS | 2; No guessed candidate event or dangling-parent crash |
| PC-T15 linked reassessment | PASS | 8; Unique IDs, set-valued earlier parents, same subject/family, prefix preservation; not durable storage enforcement |
| DEFECT-P2-01 earlier path failures | PASS | 2; Earlier lifecycle/existential failure blocks positive preservation |
| Cold entry lifecycle validation | PASS | 1; Entry lifecycle is checked as well as release |
| DEFECT-P2-02 intermediate termination | PASS | 1; Reached intermediate organization terminated causally before candidate |
| Unrelated termination is not inherited | PASS | 1; Unrelated terminated organization does not defeat continuation |
| DEFECT-P2-03 incomplete coupled initialization | PASS | 1; Missing role does not prove independent reconstruction |
| DEFECT-P2-04 witness schema | PASS | 2; All seven clauses and segment/binding metadata emitted |
| D1 exact source preservation | PASS | 1; 85d30c16a5ead30ab24e8079d194a1f497a15bb223b455003734fa56bb2d19a7 |
| D2 exact source preservation | PASS | 1; e8bbf8e1769f839434fc0a2722a0fae1c71b78ad73898ef4f415c0ac50c8921c |
| New requirement routes | PASS | 8; Eight requirements and eight current property obligations |
| Native admission/preservation commitments retained | PASS | 1; No seventh release/eighth identity condition; native source preservation supplies exact original wording |

Positive witnesses are recorded in POSITIVE-WITNESSES.json. The model interprets actual finite transitions, state flow, native-style custody recursion, effects, rivals and evidence separately. Its governing contracts and sound observation rules are declared reference fixtures, not independently certified real NNNC mechanisms. All original reported historical results and their open proof/engineering conditions remain distinct.

**END OF CURRENT REVIEW CANDIDATE — NOT ADOPTED**

<!-- END EXACT ADOPTED CANDIDATE -->
