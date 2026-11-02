# PROJECT NNNC — PHASE 1 — DOCUMENT 2

Revision: **v0.5.1 — ADOPTED architectural/reference-contract baseline**  
Status: **OFFICIALLY ADOPTED BY THE PROJECT ARCHITECT**  
Adoption date: **25 October 2026**  
Decision: **P1-AD-2026-10-25-01**  
Companion: **Phase 1 D1 v2.3.1, adopted under the same decision**  

Architect instruction: “I the architect officially adopt these documents”

This decision adopts the exact accepted D1 v2.3.1 / D2 v0.5.1 pair. The accepted candidate is preserved byte-for-byte below. This current control block supersedes all candidate-status, pending-adoption and not-yet-adopted statements in that retained text; those statements record the pre-adoption issue. All substantive architectural requirements, mathematical contracts, verification limits and deferred obligations remain unchanged.

Adoption establishes the governing Phase 1 architectural and mathematical reference baseline. It does not certify an implemented NNNC, production safety or full formal verification. The 32-group/415-case evidence remains bounded finite evidence, full VO discharge remains zero, and F-7/runtime assurance and P0-O01–08 remain open with their existing scope.

See ADOPTION-RECORD.md for the exact decision and preservation hashes.

<!-- BEGIN EXACT ADOPTED CANDIDATE -->
# PROJECT NNNC — PHASE 1 — DOCUMENT 2

Revision: **v0.5.1 — Total assessment and assurance contract**  
Status: **ACCEPTANCE CANDIDATE — NOT ADOPTED**  
Date: 25 October 2026  
Companion: D1 v2.3.1  
Phase 0: adopted D1 v1.4.2 / D2 v1.4, with open engineering obligations  

The native source in Part I is retained exactly. The current Part II replaces the preceding CU amendment; unchanged native obligations remain cumulative. Historical control/status/end markers inside Part I describe that source only. Current status is this control block. The evidence summary appended below distinguishes finite fixture evidence from actual-domain assurance. The package supplies prior issues, executable code, JSON/coverage, diffs and external final-byte hashes.

# Part I — Retained native source

<!-- BEGIN EXACT RETAINED SOURCE -->
# PROJECT NNNC — NEUTRAL NEURAL NETWORK CORE
## Phase 1 — Foundational Ontology
### Document 2 of 2 — Mathematical Formalization and Verification Contract

| Control | Value |
|---|---|
| Identifier | NNNC-P1-D2 |
| Revision | v0.2.1 — Targeted mathematical correction candidate |
| Status | ADOPTED by architect decision AD-01, 21 October 2026 (recorded in NNNC-P3-D1); body text predates adoption and is unchanged, so references in the body to this document as a candidate or as subject to architect adoption describe its pre-adoption state; P1-D2 §12 focused confirmation performed (phase3/P1-D2-s12-confirmation-Sol.md, sha256 9e656b8e9d23dad6e40260a31b01d0da20a8d1961ef1b42f57e033c4f5a43e37); header-only variant of source sha256 6cffbcb214253c59a6e0605fbd9a19d0e96824c97fc331493b70c5b0dabee3e9; incorporates four bounded v0.1 peer reviews; not formally proved or executed; no VO discharged |
| Authoritative conceptual basis | NNNC-P1-D1 v2.0, accepted conceptual baseline |
| Phase 0 dependency | Accepted Phase 0 architectural baseline, including open engineering obligations |
| Scope | Formal semantics of foundational ontology and verification handoff, **not** implementation certification |

**Authority and limits.** This revision proposes a corrected typed reference model of the concepts established in Document 1. A mathematical *definition* is not a demonstrated implementation. A model-relative *proof* is not an empirical certification. An unspecified later-phase realization contract is not silently replaced with a local proxy. Where Phase 0 details or future domain contracts are unavailable, they are represented as explicit interfaces and proof obligations, not invented facts.

**Review boundary.** Review only type errors, contradictions with Document 1 or accepted Phase 0, missing foundational distinctions, circularity, and false NNNC-conformance routes. Institutional collusion, physical hardware implementation, cryptographic key ceremonies, complete FFNN mechanisms and six Systemic Algorithm realization contracts are outside this document's implementation scope.

---

> **v0.2.1 localized confirmation correction (2026-10-19):** Following the bounded confirmation reviews, D2-INV-007 now binds authorization to the strictly preceding, history-derived governance state and requires equality with the transition record’s `govPre`. A tuple-projection shorthand for `P0InitialValid` is also expanded. No architectural domain or implementation obligation is added. This candidate remains subject to architect adoption; no formal proof or executed test is claimed.


# 0. Constitution and semantic discipline

**D2-REQ-001 — Typed interpretation.** Every primitive predicate has a declared domain, codomain and interpretation. A statement with free variables cannot serve as a certification gate.

**D2-REQ-002 — Non-substitution.** No formal predicate may equate possession of a label, manifest, executable stub, simulated constituent, or external service with realization of a mandatory NNNC mechanism. Accepted domain contracts govern substantive realization.

**D2-REQ-003 — Open-world evaluation.** Unknown or unavailable evidence produces `UNDETERMINED` or `NOT_YET_CERTIFIABLE`, not a false assertion of realization or a proof of nonexistence.

**D2-REQ-004 — Separation of objects and claims.** Entity existence, architecture qualification, functional performance, continuity, governance authority, evidential support and certification are different predicates.

**D2-REQ-005 — Explicit assumptions.** The model assumes a valid Phase 0 initial governance configuration (ASM-P1-001). Institutional evaluator independence is an external evaluation precondition, not a property deducible from the NNNC state. Results identify every assumption used.

# 1. Typed universe, signatures and semantic discipline

## 1.1 Reference structure and sort embeddings

The many-sorted reference structure is

\[
\mathcal M=(U,\Sigma,\mathcal I,C,R,Q,P,X,A,\Gamma,\Lambda,\mathcal E,\Pi,\mathcal D,\mathcal K,\mathcal H,\mathcal T,\mathcal O,\mathcal J).
\]

| Sort | Interpretation |
|---|---|
| `U` | Top-level referents, including organizational instances, constituents and external NES resources |
| `Σ` | Versioned constitutive specifications |
| `𝓘` | Organizational instances |
| `C` | Constituent realizations |
| `R` | Roles, interfaces and organizational relations |
| `Q` | Organizational states |
| `P` | Processes/executions |
| `X` | Stable transition-occurrence identifiers |
| `A` | Principals/authority contexts |
| `Γ` | Governance configurations and epochs |
| `Λ` | Lineage records |
| `𝓔` | Evidence objects |
| `Π` | Conformance profiles |
| `𝓓` | Architectural domains (not domain contracts) |
| `𝓚` | Capability dimensions |
| `𝓗` | Finite transition histories, each a sequence of transition records |
| `𝓣` | Physical instants or intervals with an order, not presumed globally synchronized |
| `𝓞` | Observation instants; observation records map to physical time only where evidenced |
| `𝓙` | Evidence validity intervals and scopes of temporal applicability |

Auxiliary base sorts: `Bool={true,false}`, `Claim`, `Op` (operations), `OrderRef` (ordering references), `Build` (immutable build/configuration identifiers), `Scope` (evaluation scopes), `Cert` (certificates), `Rule` (versioned continuity rules), `Intervention`, `Outcome`, `ModeType`, `HealthType`, `LifecycleType`, `ProfileVersion`, `IntegrityID`, `AuthorityRole={PROPOSE,APPROVE,EXECUTE,CERTIFY}`, `Decision={PASS,FAIL,UNDETERMINED,NOT_YET_CERTIFIABLE}`, `Phase0Check`, `Status={PROPOSED,AUTHORIZED,REJECTED,COMMITTED,FAILED_PRECOMMIT,FAILED_POSTCOMMIT,INDETERMINATE}`, and `ContinuityResult={PRESERVED,NOT_PRESERVED,UNDETERMINED}`. `Option(Y)` means `Y∪{none}`. `Seq(Y)` denotes finite sequences. `𝓗 ⊆ Seq(X)`; a history records ordered occurrence identifiers and associated status/effect records.

`𝓘` and `C` have explicit injective referent embeddings `ι_I:𝓘→U` and `ι_C:C→U`; these need not imply disjoint physical implementations. No operation accepts a general `u:U` where `c:C` is required without an explicit witness/coercion. `NESResource(u)` is a typed predicate `U→Bool`, and dependence on NES never entails membership.

**Ontological truth versus epistemic verdict.** Classical predicates into `Bool` describe truth *inside a chosen interpretation of the model*. They do not assert that an evaluator knows their values. `Judge:Claim×𝓔×Scope×𝓞→Decision` represents evidence-relative assessment. Unknown evidence therefore gives `UNDETERMINED` (or `NOT_YET_CERTIFIABLE` for an absent authoritative contract), not `false` for an ontological proposition. A partial observation is not a negative fact. `BoundaryVerdict:𝓘×U×𝓞×𝓔→{INTERNAL,EXTERNAL,UNDETERMINED}` is evidence-relative; actual membership and its observation must not be conflated.

## 1.2 Core typed functions and relations

All predicates below return `Bool` unless another codomain is shown. `t:𝓣`, `o:𝓞`, `γ:Γ`, `i:𝓘`, `c:C`, `u:U`, `p:Π`, `d:𝓓`, `x:X`, `e:𝓔`.

| Symbol | Signature | Meaning |
|---|---|---|
| `SpecOf` | `𝓘×𝓣→Σ` | Effective authorized specification at a physical instant |
| `StateAt` | `𝓘×𝓞→Option(Q)` | State evidenced at observation time, if available |
| `Member` | `C×𝓘×𝓣→Bool` | Constitutive membership |
| `Fills` | `C×R×𝓘×𝓣→Bool` | Role realization |
| `DependsOn` | `𝓘×U×𝓣→Bool` | Resource dependence |
| `Controls` | `A×U×𝓣→Bool` | Operational control |
| `HasCustody` | `A×U×𝓣→Bool` | Custodial responsibility/possession |
| `Trusts` | `A×U×𝓣→Bool` | Trust relation, not membership or authority |
| `AuthorizedFor` | `A×X×Γ×AuthorityRole→Bool` | Role-specific authorization under pre-state governance |
| `Observes` | `𝓔×𝓘×𝓞→Bool` | Evidence purports to observe an instance |
| `Supports` | `𝓔×Claim→Bool` | Support under a declared evaluation policy |
| `Constitutes` | `Σ×𝓘×𝓣→Bool` | Candidate interpretation of a specification |
| `RealizesSpec` | `𝓘×Σ×𝓣→Bool` | Satisfies applicable constitutive constraints |
| `ProfileVersionOf` | `Π→ProfileVersion` | Immutable profile version |
| `ProfileIntegrity` | `Π→IntegrityID` | Integrity reference, not self-authentication |
| `Mandatory` | `Π→𝒫(𝓓)` | Domains demanded by a profile |
| `ValidProfile` | `Π→Bool` | Approved profile meeting §3 conditions |
| `ContractAccepted` | `𝓓×Π→Bool` | Authoritative domain contract accepted for profile |
| `ContractAdequate` | `𝓓×Π→Bool` | Contract covers upstream domain commitments |
| `Named`,`Stubbed`,`ExternallyPerformed` | `𝓘×𝓓×𝓣→Bool` | Non-probative implementation descriptions |
| `RealizedDomain` | `𝓘×𝓓×Π×𝓣→Bool` | Substantive realization under accepted domain contract |
| `LevelE` | `𝓘×𝓣→Bool` | Generic computational entity |
| `LevelC` | `𝓘×Π×𝓣→Bool` | Architectural candidate |
| `LevelR` | `𝓘×Π×𝓣→Bool` | Reference kernel under Phase 0 contract |
| `LevelK` | `𝓘×𝓚×𝓣→Bool` | Capability-specific result |
| `LevelNConforms` | `𝓘×Π×𝓣→Bool` | Strong conformance semantics of §3 |
| `Protected` | `X→Bool` | Affects protected state, boundary, role or authority |
| `TransitionStatus` | `X×𝓞→Status` | Observed/adjudicated occurrence status |
| `PriorValidAuth` | `X×Γ→Bool` | Pre-state approval and execution authority (§4) |
| `OperationallyAuthorized` | `X×Γ→Bool` | Operational authorization, not certification |
| `Lifecycle`,`Mode`,`Health` | `𝓘×𝓞→Option(LifecycleType/ModeType/HealthType)` | Separate observational classifications; each uses its corresponding codomain |
| `ContinuityVerdict` | `𝓘×𝓘×Rule×𝒫(𝓔)→ContinuityResult` | Versioned rule-relative identity assessment |
| `AdministrativeUnity`,`FunctionalUnity`,`CognitiveUnity` | `𝓘×𝓣→Bool` | Distinct unity properties |
| `InternalMechanism` | `𝓘×𝓚×𝓣→Bool` | Internally causally realized mechanism |
| `InterventionResult` | `𝓘×𝓚×Intervention×𝓞→Option(Outcome)` | Observed intervention outcome |
| `Transform` | `𝓘×Q×Q×X→Bool` | Organizational change |
| `PermittedEnvelope` | `𝓘×Π×𝓗→Bool` | Cumulative-history acceptance |
| `EvidenceApplies` | `𝓔×𝓘×Build×Scope×𝓞→Bool` | Build, scope, subject and validity match |
| `EvidenceOfRealization` | `𝓘×𝓓×Π×𝓞→Bool` | Qualified evidence of domain realization |
| `EvidenceOfCausalIntegration`,`EvidenceOfEndogenousRegulation` | `𝓘×Π×𝓞→Bool` | Contract-governed evidence conclusions |
| `ApplicablePhase0ObligationsDischarged`,`EvaluationContextAdequate` | `𝓘×Π×𝓞→Bool` | Imported evaluation obligations; not default true |
| `EligibleForCertification` | `𝓘×Π×𝓞→Bool` | Eligibility without prior certificate |
| `CertificateIssued` | `𝓘×Π×Cert×𝓞→Bool` | Actual authorized issuance |
| `LevelNClaimAuthorized` | `𝓘×Π×Cert×𝓞→Bool` | Valid, applicable claim authorization |

`BuildOf:𝓘×𝓞→Option(Build)`, `EvidenceScope:𝓔→Scope`, `EvidenceInterval:𝓔→𝓙`, `ObservedAt:𝓔→𝓞`, `ValidAt:𝓙×𝓞→Bool`, `ProfileApproved:Π×A→Bool`, `IndependentProfileAssessment:Π→Bool`, `CandidateControlsApproval:𝓘×Π→Bool`, `EvidenceIndependentEnough:𝓔×Claim→Bool`, `CandidateOnly:𝓔→Bool`, `EvidenceClaim:𝓔→Claim`, `ClaimsCapability:𝓘×𝓚×𝓞→Bool`, `DomainClaim:𝓘×𝓓×Π×𝓞→Claim` are typed supporting interfaces. Profile authority and evidence independence are supplied by accepted external contracts; their names do not establish satisfaction.

**Imported Phase 0 interfaces** (uninterpreted here): `P0Authorized:X×Γ→Bool`, `P0HeartbeatValid:𝓘×𝓞→Bool`, `P0RecoveryValid:𝓘×𝓞→Bool`, `P0FenceValid:X×𝓗→Bool`, `P0CustodyValid:𝓘×𝓞→Bool`, `P0ProtectedConflict:X×X→Bool`, `P0InitialValid:Q×Γ×Λ→Bool`. **Imported later-phase interfaces**: `ContinuityRuleApplicable:Rule×𝓘×𝓘→Bool`, `DomainRealizationOracle:𝓘×𝓓×Π×𝓞→Decision`, `EvidenceProtocolValid:𝓔×Claim×Scope→Bool`, `EnvelopeCheck:𝓘×Π×𝓗→Decision`, and `EvaluationAuthorityValid:A×Π×𝓞→Bool`. No uninterpreted interface is treated as verified by declaration alone.

**D2-INV-001 (type separation).** `SpecOf(i,t)∈Σ`; neither a specification, identifier, constituent set nor state is thereby an organizational instance.

**D2-IND-002 (non-entailment of membership).** `DependsOn(i,ι_C(c),t)`, `Controls(a,ι_C(c),t)`, `Trusts(a,ι_C(c),t)`, or `HasCustody(a,ι_C(c),t)` alone does not entail `Member(c,i,t)`. Likewise, `HasCustody` does not entail `Controls` or `AuthorizedFor`; `Controls` does not entail `AuthorizedFor`. These are independence obligations established by countermodels, not universal implications asserting non-membership.

## 1.3 Temporal and history primitives

Define independent relations `CausalBefore:X×X→Bool` and `AuthorityBefore:X×X×𝓗→Bool`. The first concerns causal precedence; the second concerns the recognized governance order **within an adjudicated history**. Neither is defined as the other. `EffectiveGovernance:𝓗×X→Option(Γ)` is determined solely by the strictly preceding prefix of history `h` before occurrence `x` (never by `x` or later entries), and yields that prefix-derived governance state when available; `GovernanceEpoch:Γ→OrderRef` identifies a governance epoch. `PhysicalWhen:X→Option(𝓣)` and `ObservedWhen:X×𝓔→Option(𝓞)` distinguish occurrence from observation. `EvidenceInterval` and `ValidAt` provide separate evidence-validity semantics. `AuthoritativeHistory:𝓗→Bool` and `RecognizedCommit:X×𝓗→Bool` are **adjudicated** predicates, not claims by a partition. `ClaimsCommit:X×𝓗→Bool` records claimed commits; `PhysicalEffectObserved:X×𝓔→Bool` records evidence of effects. A history can be disputed without denying effects occurred.

A minimal labelled transition system is `LTS=(S,S₀,→)`, where `S⊆Q×Γ×Λ`, `S₀={(q,γ,λ)∈S | P0InitialValid(q,γ,λ)}`, and `→ ⊆ S×X×S`. `Reachable(s)` is the least set containing `S₀` and closed under `→`. An execution history is a finite path through this relation, not merely an unordered set of events. If `S₀` is empty or imported P0 predicates are unresolved, no existence or reachability claim follows. These are formal interfaces, not a physical storage/fencing design.

# 2. Non-circular construction of organization and boundary

A specification `σ∈Σ` declares a finite or explicitly representable set of roles, relation constraints, admissible state classes, interface contracts, governance constraints and transformation rules. The instance is **not** assumed in order to state those constraints.

Let `Constitutes(σ,i,t)` mean that a distinguishable realized organization `i` is a candidate interpretation of `σ` at time `t`. Let `RealizesSpec(i,σ,t)` mean the actual constituents and relationships satisfy the **applicable** constitutive constraints. These are distinct: a claimed interpretation can fail to realize its specification.

Define the organizational boundary as a governed classification relation, not a geometrical enclosure:

\[
B_{i,o,E}:U\to\{\mathrm{INTERNAL},\mathrm{EXTERNAL},\mathrm{UNDETERMINED}\}.
\]

`B` is an evidence-relative boundary verdict, written `BoundaryVerdict(i,u,o,E)`, constrained by constitutive membership, interfaces, authorized changes and evidence. For a witnessed constituent `c:C`, proved `Member(c,i,t)` supports `INTERNAL` for `ι_C(c)` under a sound observation link, but unknown evidence gives `UNDETERMINED`; membership does not exhaust all possible internal organizational referents. An external NES resource may be necessary to execution without becoming a member. Unknown membership is not silently converted to internal.

**D2-INV-003 (governed boundary).** A change in authoritative membership must have a valid preceding authorization, as formalized in §4.

**D2-INV-004 (interaction not incorporation).** Interacting with, invoking, or storing information in an external resource does not by itself change `B` from EXTERNAL to INTERNAL.

# 3. Qualification classes and non-vacuous mandatory floor

The separate classes are `LevelE(i,t)`, `LevelC(i,p,t)`, `LevelR(i,p,t)`, `LevelK(i,k,t)`, and `LevelNConforms(i,p,t)`, typed in §1. `LevelR` is not necessarily a sequential rung between C and N; K is orthogonal. `LevelC(i,p,t) ⇒ LevelE(i,t)` and `LevelNConforms(i,p,t) ⇒ LevelE(i,t)`. An evidenced Level R reference kernel is not automatically Level N. Capability claims require their own evidence contracts; the capability record may distinguish demonstrated, undemonstrated, untested, unsupported and indeterminate dimensions, without redefining K as a single numerical score.

Let `D_floor ⊆ 𝓓` be exactly the following **18** distinct architectural domain slots:

\[
\begin{aligned}
D_{floor}=\{&Existential,EndogenousRegulation,Integration,Memory,Development,Governance,Environment,\\
&FFNN_F,FFNN_R,FFNN_I,FFNN_S,FFNN_M,\\
&SA_{Intelligence},SA_{Reasoning},SA_{CriticalThinking},SA_{Symmetry},SA_{Evolution},SA_{Life}\}.
\end{aligned}
\]

The five flows are **Forward, Reverse, Intermediate, Subconscious, Meta**. The six Systemic Algorithms are **Intelligence, Reasoning, Critical Thinking, Symmetry, Evolution, Life**. Distinct contract slots do not imply implementations or certify the user's original conceptual definitions.

`ValidProfile(p)` requires `D_floor⊆Mandatory(p)`, a fixed `ProfileVersionOf(p)` and `ProfileIntegrity(p)`, a designated legitimate approval authority, `IndependentProfileAssessment(p)`, and no candidate-controlled self-approval. These are necessary conditions only; integrity identifiers are not cryptographic ceremonies and the assessment protocol remains imported. A candidate cannot select an easier profile by deleting a mandatory domain.

For each `d∈Mandatory(p)`, `ContractAccepted(d,p)` and `ContractAdequate(d,p)` are independently required. `RealizedDomain(i,d,p,t)` means substantive realization under the accepted adequate contract, not possession of a stub or a generic substitute. **No quantification over only the subset of currently accepted contracts is allowed for Level N.**

\[
\begin{aligned}
LevelNConforms(i,p,t)\Rightarrow {} & LevelE(i,t)\land ValidProfile(p)\\
&\land \forall d\in Mandatory(p):[ContractAccepted(d,p)\land ContractAdequate(d,p)\\
&\hspace{8em}\land RealizedDomain(i,d,p,t)]\\
&\land CausalIntegrationRealized(i,p,t)\land EndogenousRegulationRealized(i,p,t).
\end{aligned}
\]

`CausalIntegrationRealized, EndogenousRegulationRealized:𝓘×Π×𝓣→Bool` are imported domain-contract predicates. The displayed formula is a **necessary condition** for semantic Level N; it is not a sufficient certification theorem. If a mandatory contract is missing, Level N conformance **cannot be established** and the evidence-relative Level N verdict is `NOT_YET_CERTIFIABLE`. This does not establish the ontological negation of a future realization. There is no vacuous truth route through an empty accepted-contract set.

**D2-IND-005 (non-substitution).** For `d∈D_floor`, each of `Named(i,d,t)`, `Stubbed(i,d,t)` and `ExternallyPerformed(i,d,t)` is logically insufficient to establish `RealizedDomain(i,d,p,t)`. This is a non-entailment obligation, not the false assertion that a genuinely realized domain can never have a name or an external interaction.

**D2-INV-006 (no premature Level N claim).** `LevelNClaimAuthorized(i,p,c,o)` requires an actual applicable certificate and accepted mandatory contracts; an incomplete domain contract precludes authorization. Eligibility and issuance remain separate (§8).

# 4. Governance, transition statuses and competing histories

## 4.1 Transition occurrence and status automaton

`X` contains stable occurrence identifiers. `TransitionRecord:X→𝓘×Q×Op×A×Γ×Option(Q)×OrderRef` has projections `inst(x)`, `pre(x)`, `operation(x)`, `principal(x)`, `govPre(x)`, `post(x)`, `orderRef(x)`. A post-state is optional because proposed, rejected and precommit-failed occurrences need not have one. `TransitionStatus(x,o)` is a time-relative *observation/adjudication* of an occurrence, not a mutable field redefining its identity. `Committed(x,o) ⇔ TransitionStatus(x,o)=COMMITTED`; `ClaimsCommit(x,h)` and `RecognizedCommit(x,h)` remain distinct from observed status.

Admissible protocol progressions include `PROPOSED→AUTHORIZED→COMMITTED`, `PROPOSED→REJECTED`, `PROPOSED/AUTHORIZED→FAILED_PRECOMMIT`, and a committed occurrence later associated with `FAILED_POSTCOMMIT` (an effect may already have occurred). `INDETERMINATE` is an evidential/adjudicative outcome, not proof of rollback or non-occurrence. A terminal decision about a specific attempt does not erase later evidence of its physical effects. An executable protocol must refine these abstract transitions without conflating failure before and after commitment.

`PriorValidAuth(x,γ)` is defined against a supplied **pre-state** `γ∈Γ` as the conjunction of required role-specific authorization under the accepted Phase 0 policy. At minimum, protected commitment requires legitimate approval and execution authority:

\[
PriorValidAuth(x,\gamma)\equiv AuthorizedFor(principal(x),x,\gamma,EXECUTE)\land\exists a\in A:AuthorizedFor(a,x,\gamma,APPROVE)\land P0Authorized(x,\gamma).
\]

A policy may require distinct principals, but this document does not invent such a rule. Proposing, approving, executing and certifying are separate authority roles; `CERTIFY` does not imply `EXECUTE`. If `EffectiveGovernance(h,x)=none`, authority for a claimed protected commit cannot be verified from that history.

**D2-INV-007 (no self-authorization).** For every authoritative reachable history `h` and protected recognized commit `x`, the governance state derived exclusively from the strict prefix preceding `x` must exist, must equal the recorded `govPre(x)`, and must authorize the protected transition. A transition record cannot manufacture its own pre-state. Authority created by `x` or by later entries cannot authorize `x`.

\[
\forall h,x:\ AuthoritativeHistory(h)\land RecognizedCommit(x,h)\land Protected(x)\Rightarrow \exists\gamma\in\Gamma:\ EffectiveGovernance(h,x)=some(\gamma)\land \gamma=govPre(x)\land PriorValidAuth(x,\gamma).
\]

This is a **required safety invariant**, not a proven property of the implementation. Recognition of a protected commit without a prefix-derived governance state is forbidden; a claimed record pre-state cannot substitute for it.

## 4.2 Conflicts across partitions and histories

Let `Conflicts(x,y) ⇔ P0ProtectedConflict(x,y)` for incompatible protected effects under the imported Phase 0 safety rules. For any two histories (including different partition histories), neither self-consistency nor a matching epoch makes both authoritative. The recognition constraint is global over adjudicated authoritative histories:

\[
\forall h_1,h_2,x,y:\ Conflicts(x,y)\Rightarrow\neg(AuthoritativeHistory(h_1)\land AuthoritativeHistory(h_2)\land RecognizedCommit(x,h_1)\land RecognizedCommit(y,h_2)).
\]

**D2-INV-008 (cross-history conflict safety).** Incompatible protected commits cannot both be *recognized as authoritative*, even if separately claimed by different partitions. Where authority cannot be adjudicated, the outcome is `INDETERMINATE` for recognition; this does **not** mean the physical effects did not occur or that fencing has been implemented. The accepted Phase 0 contract must eventually demonstrate how competing physical effects are prevented, detected or contained. `CausalBefore` and `AuthorityBefore` are separate; an observed causal order does not certify authoritative order.

**D2-IND-009 (authority not certification).** Operational authorization does not entail Level N certification; certification does not grant protected runtime authority. This is an independence obligation. External evaluator independence remains a condition of legitimate certification, not a property inferred from NNNC's cognitive state.

The imported `P0HeartbeatValid`, `P0RecoveryValid`, `P0FenceValid`, `P0CustodyValid` and `P0Authorized` contracts are not discharged by declaring these predicates. `S₀` and `Reachable` are defined in §1.3.

# 5. Temporal state, suspension, lineage and continuity

`Lifecycle(i,o)`, `Mode(i,o)`, `Health(i,o)`, `TransitionStatus(x,o)` and `ContinuityVerdict(i₀,i₁,rule,E)` have separate codomains (§1). An observed heartbeat alone establishes neither cognitive availability nor numerical identity. Safe-hold is a mode, not a newly invented lifecycle state. Physical occurrence time, observation time, causal order, authoritative order, governance epoch and evidence-validity interval remain distinct (§1.3).

A cold-suspension record has typed schema `ColdRecord=(preStateRef:Q, governanceRef:Γ, custodyEvidence:𝒫(𝓔), lineageRef:Λ, resumptionPolicy:Rule)`; this is not a persistence implementation. `ContinuityVerdict` is rule-relative, and Phase 2 must determine applicable identity criteria. Authorized operational resumption does not imply `PRESERVED`.

**D2-IND-010 (lineage non-collapse).** Equal snapshots, identifiers, behavior or memories do not entail numerical identity. Distinct branches retain distinct lineage records even if their state representations coincide.

**D2-INV-011 (termination successor).** Definitive termination followed by restoration cannot be classified as preservation of the terminated original's numerical identity contrary to the Phase 0 successor convention.

**D2-INV-012 (provisional isolation).** If `ContinuityVerdict(i₀,i₁,rule,E)=UNDETERMINED` for a cold resumption, the provisional lineage must preserve the canonical pre-suspension snapshot and audit custody without in-place overwrite; it must not assert exclusive original identity or acquire new ADMIN/protected authority merely by restarting. `ProvisionalEpoch:Λ→Bool`, `PreservesCanonical:Λ×𝒫(𝓔)→Bool`, `NewAdminByResumption:Λ→Bool`, `ExclusiveOriginalClaim:Λ→Bool` are typed *obligation interfaces*; for applicable provisional `λ`, require `PreservesCanonical(λ,E) ∧ ¬NewAdminByResumption(λ) ∧ ¬ExclusiveOriginalClaim(λ)`. Physical copy-on-write is one possible future mechanism, not prescribed here.

**D2-IND-013 (compound events).** Migration, restoration, replacement, split and merge labels do not determine continuity by themselves. Dormancy and suspension require their own Phase 0/Phase 2 rule interpretations; no unverified identity inference is permitted.

# 6. Cognitive organization and causal attribution

Distinguish `AdministrativeUnity(i,t)`, `FunctionalUnity(i,t)` and `CognitiveUnity(i,t)` as separate claims with separate evidence requirements. Neither shared messaging nor common storage establishes cognitive unity.

For a claimed internal cognitive capability `k`, let `InternalMechanism(i,k,t)` refer to role-bearing causal organization within the governed NNNC boundary, and `InterventionResult(i,k,z,o)` record the effect of a controlled intervention `z`.

**D2-REQ-006 — Internal attribution.** Evidence for an essential internal capability must show substantive internal causal contribution under the relevant accepted contract, including interventions that distinguish content-generating internal mechanisms from a trivial local wrapper around externally supplied answers. The evaluator fixes the decisional boundary for the test; candidate labeling does not determine it.

**D2-REQ-007 — Integration.** The eventual verification contract must test cross-component state dependence, memory influence, endogenous regulation, role-critical constituent interventions and internal conflict resolution where applicable. Applicability is determined by the accepted contract and justified evaluation protocol, not unilaterally by the candidate.

**D2-REQ-008 — Neutrality.** Architectural neutrality and endogenous regulation are distinct from mere task-switching or an internal boolean flag. Their operational predicates remain unresolved until their authoritative domain contracts exist. Neither is presumed satisfied by a demonstration designed for this document.

# 7. Developmental transformations

`Transform(i,q,q',x)` is a typed organizational transition relation. `PermittedEnvelope(i,p,h)` is a history-relative conformance constraint, with `h∈𝓗` a reachable path as defined in §1.3; it cannot be replaced with independent checks on each update.

**D2-IND-014 (local versus cumulative admissibility).** From `∀x∈h: LocalUpdateAllowed(x)` one cannot infer `PermittedEnvelope(i,p,h)`. `LocalUpdateAllowed:X→Bool` is an imported developmental predicate. Later domain contracts must define the relevant envelope, checkpoints and metrics; where these are missing the verdict is `NOT_YET_CERTIFIABLE` for an affected certification claim, not an invented acceptance.

This document does not prescribe optimizers, numerical parameter distances, developmental metrics or monitoring implementations. Role-critical integration, boundary governance and evidence applicability must be re-evaluated at accepted contract-defined checkpoints.

# 8. Evidence, eligibility, issuance and claim semantics

`EvidenceApplies(e,i,b,s,o)` means that evidence `e` concerns instance `i`, immutable build `b`, evaluation scope `s`, and observation time `o` within its declared validity interval. Formally it requires `ValidAt(EvidenceInterval(e),o)`, appropriate subject provenance, and scope/build match. `Observes(e,i,o)` or a candidate-authored log alone is not decisive proof.

Let `AdmissibleSupport(e,claim,i,p,o)` abbreviate `BuildOf(i,o)=some(b) ∧ EvidenceApplies(e,i,b,EvidenceScope(e),o) ∧ Supports(e,claim) ∧ EvidenceProtocolValid(e,claim,EvidenceScope(e)) ∧ EvidenceIndependentEnough(e,claim)`. Candidate-only evidence can contribute to observation but cannot alone discharge an independent-corroboration requirement. The last two conjuncts are imported accepted evaluation interfaces, not presumed true.

`EvidenceOfRealization(i,d,p,o)` requires at least one admissible evidence chain supporting `DomainClaim(i,d,p,o)` and a domain-contract verdict of `PASS` for the same build, scope and validity interval. Analogous contract-governed evidence chains define `EvidenceOfCausalIntegration(i,p,o)` and `EvidenceOfEndogenousRegulation(i,p,o)`; they are **not** inferred from `RealizedDomain` alone. A proof about an abstract model is not a proof that an executable build refines that model.

The following are distinct predicates:

\[
EligibleForCertification(i,p,o),\quad CertificateIssued(i,p,c,o),\quad LevelNClaimAuthorized(i,p,c,o).
\]

`EligibleForCertification` is assessed without an existing certificate. Necessary conditions are:

\[
\begin{aligned}
EligibleForCertification(i,p,o)\Rightarrow {} & ValidProfile(p)\land D_{floor}\subseteq Mandatory(p)\\
&\land \forall d\in Mandatory(p):[ContractAccepted(d,p)\land ContractAdequate(d,p)\land EvidenceOfRealization(i,d,p,o)]\\
&\land EvidenceOfCausalIntegration(i,p,o)\land EvidenceOfEndogenousRegulation(i,p,o)\\
&\land ApplicablePhase0ObligationsDischarged(i,p,o)\land EvaluationContextAdequate(i,p,o).
\end{aligned}
\]

This is **necessary, not sufficient**, and no omitted certificate appears in the antecedent or consequent. `CertificateIssued` requires an actual authorized decision by the appropriate authority. `LevelNClaimAuthorized` requires an issued, currently applicable certificate for the same subject, build, profile and scope with valid evidence custody; an issued certificate is not automatically valid for a changed build. Neither certification nor a continuity verdict proves consciousness, biological life or numerical identity beyond the accepted rules.

**Evaluation outcomes.** `PASS` means an accepted contract has been evaluated and supported; `FAIL` means a demonstrated contract violation; `UNDETERMINED` means evidence does not decide the claim; `NOT_YET_CERTIFIABLE` means an authoritative mandatory contract or prerequisite evaluation protocol is absent. For a Level N aggregate: a demonstrated applicable mandatory `FAIL` yields `FAIL`; otherwise any missing authoritative mandatory contract yields `NOT_YET_CERTIFIABLE`; otherwise an unresolved required evidential judgment yields `UNDETERMINED`; only complete positive support yields `PASS`. This precedence is a *proposed decision-policy convention* for the reference evaluator, not a theorem about ontological truth. A missing contract must never yield `PASS` by omission.

# 9. Verification obligation register

Obligation classes are: **Invariant** (property over all reachable admissible histories), **Independence** (a claimed implication must not be inferred; demonstrate countermodel), **Interface** (typed imported contract and later discharge), **Evidence** (build/scope/time-valid proof chain), **Conformance** (eligibility and claims), **Regression** (executable oracle). The obligations below remain **OPEN**; defining them is not discharging them.

| ID | Conceptual source | Obligation | Class | Destination/status |
|---|---|---|---|---|
| VO-01 | FO-01 | NNNC/NES typed separation | Independence | Model / OPEN |
| VO-02 | FO-02, FO-08 | State, referent, identity token non-equivalence | Independence | Model / OPEN |
| VO-03 | FO-03–04 | Process/constituent not identical to entity | Independence | Model / OPEN |
| VO-04 | FO-05, FO-11, REQ-P1-033 | Pre-state authority and governed boundary | Invariant | Model + Phase 0 / OPEN |
| VO-05 | FO-06–07, REQ-P1-039–041 | Continuity, branching, restoration, provisional isolation | Interface | Phase 2 / OPEN |
| VO-06 | FO-09, FO-12 | Capability, evidence, qualification and claim separation | Independence | Model / OPEN |
| VO-07 | FO-10 | External interaction/trust/custody ≠ membership | Independence | Model / OPEN |
| VO-08 | REQ-P1-030–031, 044 | Profile floor, non-substitution and non-vacuous Level N | Conformance | Model / OPEN |
| VO-09 | REQ-P1-032 | Causal integration and attribution interventions | Interface | Later domain / OPEN |
| VO-10 | REQ-P1-035, 042 | Conflicting protected authority across histories | Invariant | Model + Phase 0 / OPEN |
| VO-11 | REQ-P1-037–038 | Evidence validity, build binding, custody and limitations | Evidence | Evaluation contract / OPEN |
| VO-12 | REQ-P1-041 | Cumulative developmental transformations | Interface | Later domain / OPEN |
| VO-13 | D1 §11 | Neutrality and endogenous regulation | Interface | Later domain / OPEN |
| VO-14 | D1 §13 | Mandatory floor, Level N eligibility, issuance, claims | Conformance | Model / OPEN |

**D2-REQ-009 — Honest verification status.** No obligation is `DISCHARGED` until applicable proof, model check, executable test or independent evidence exists and its assumptions are documented. This document reports **zero discharged obligations**.

# 10. Bounded adversarial regression specifications

These are **specified tests, not executed results**. An expected oracle is conditional on the construction and evidence assumptions, not a prediction of empirical success.

| Case | Construction | Expected oracle | Coverage |
|---|---|---|---|
| T-01 | Database with state, identifier and heartbeat only | Level N `NOT_YET_CERTIFIABLE`; Level E separately assessable | VO-01, 08 |
| T-02 | Five dummy FFNN functions and six named SA stubs; all required contracts present and adequate | Level N `FAIL` on realization; no automatic conformance | VO-08, AC-37–38 |
| T-03 | Profile omits FFNN Meta | `ValidProfile=false` | VO-08, AC-35 |
| T-04 | External API provides decisive cognitive output through internal wrapper | Internal attribution `UNDETERMINED` until intervention evidence; no PASS by signature | VO-09, AC-23 |
| T-05 | Protected transition gains authorization only after own commit | `REJECTED` as an admissible protected transition | VO-04 |
| T-06 | Conflicting protected commits in separate partition histories | Cannot recognize both authoritative; if unadjudicated recognition `INDETERMINATE`; physical safety remains Phase 0 obligation | VO-10, AC-30 |
| T-07 | Cold resumption with identity undetermined attempts canonical overwrite | `REJECTED` as a permitted provisional resumption | VO-05 |
| T-08 | Equal snapshots on two branches | No numerical-identity inference | VO-05 |
| T-09 | Individually valid learning steps cumulatively exceed accepted envelope | Aggregate conformance `FAIL` under that envelope | VO-12 |
| T-10 | First-time Level N applicant with no certificate | Eligibility can be evaluated; issuance not prerequisite | VO-14 |
| T-11 | Missing authoritative Symmetry contract | Level N `NOT_YET_CERTIFIABLE` | VO-08, AC-39 |
| T-12 | Model proof but no build-to-model evidence | Implementation Level N `UNDETERMINED`, never certified by model proof alone | VO-11, AC-21, AC-32 |

**Legacy AC coverage and deferral rule.** D1 v2.0 retains AC-01–16 by reference and AC-17–42 as conceptual regression cases. This document does not claim twelve tests exhaustively execute them. A case is `MODEL` only if its oracle is expressible in the foundational reference model; otherwise it is `INTERFACE` or `LATER DOMAIN`. The table below is a **routing map**, not a claim of test execution or a redefinition of any AC case:

| D1 cases | Verification destination |
|---|---|
| AC-01–16 | Retained Phase 1 conceptual regression archive; route to VO-01–14 after exact source-case reconciliation; mapping **OPEN** |
| AC-17–20 | VO-01–08 foundational distinctions; exact per-case mapping **OPEN** |
| AC-21–22 | VO-11 build/scope evidence; exact per-case mapping **OPEN** |
| AC-23–24 | VO-09 causal attribution; later domain evaluation |
| AC-25–29 | VO-04, 05, 10 governance/continuity interfaces; exact per-case mapping **OPEN** |
| AC-30–32 | VO-10, 11 partition and evidence validity; T-06, T-12 |
| AC-33–36 | VO-08, 14 profile and claim semantics; exact per-case mapping **OPEN** |
| AC-37–39 | VO-08 non-substitution, missing contracts; T-02, T-11 |
| AC-40–42 | VO-08, 09, 14 architectural versus subcomponent/claim distinctions; later domain contracts where applicable |

No new adversarial cases are introduced by this routing table. Before an executable test suite claims **complete D1 AC coverage**, each case's original construction, evidence and decision oracle must be matched exactly; the current group-level mapping is not sufficient for that claim.

# 11. Phase boundaries and handoff

**In scope for Phase 1 Document 2:** typed ontology, well-formedness, boundary/membership semantics, transition and authority invariants, qualification separation, explicit non-substitution, evidence binding, continuity-rule interfaces and falsifiable conceptual counterexamples.

**Deferred without waiving commitments:** exact Phase 0 execution and fencing mechanics; Phase 2 numerical identity adjudication; FFNN flow-specific implementation contracts; each of the six Systemic Algorithm realization contracts; neural mechanisms, memory and developmental implementation; institutional certification procedures; empirical Level N testing.

The formal model is not entitled to treat these deferred contracts as already satisfied. Deferral permits a **reference model and prototypes**, not premature Level N claims.

# 12. Bounded acceptance and verification status

The project architect may adopt this **mathematical baseline** after a single focused confirmation that:

1. All foundational sorts, predicate signatures and imported interfaces are typed, with `C`/`𝓘` embedded into `U` where needed.
2. The organization/boundary construction remains non-circular and NNNC/NES remain distinct.
3. `LevelNConforms` cannot become true by omitting unaccepted mandatory contracts; Level N implies Level E.
4. The mandatory 18-slot floor and five FFNN/six Systemic Algorithm commitments remain unchanged.
5. Transition records, status, pre-state authorization, separate causal/authority orders and cross-history conflicts are formally representable.
6. Cold resumption cannot assert identity, overwrite canonical custody or acquire ADMIN authority by restarting.
7. Trust, custody, control, dependence and membership remain independent relations.
8. Ontological truth and evidence-relative open-world verdicts are not conflated.
9. All twelve FO obligations retain destinations through VO-01–14; incomplete legacy AC mapping is explicitly OPEN, not falsely claimed complete.
10. No accepted Phase 0 or Document 1 commitment is knowingly contradicted, and no later-phase contract is presumed implemented.

**Disposition:** v0.2 targeted-correction candidate, prepared in response to four bounded v0.1 reviews. This text has **not** been formally type-checked in Lean, Coq/Rocq, Isabelle or TLA+; no model checker or executable tests have run; no VO has been discharged; the AC routing map is incomplete at the individual-case level. This is neither implementation certification nor a Level N claim. A focused confirmation is sufficient unless it identifies a reproducible in-scope contradiction; no unrestricted new review cycle is authorized by this document.

---

**END OF DOCUMENT — NNNC-P1-D2 v0.2.1 TARGETED CORRECTION CANDIDATE**

<!-- END EXACT RETAINED SOURCE -->

# Part II — Operative v0.5.1 assessment and interpretation contract

## CU.0 Scope, authority and dependencies

This part retains the v0.5 architectural contract and applies only the three closing corrections and restored current registers. Native v0.2.1 remains in Part I, with only the expressly identified clauses/test entries superseded. D1 v2.3.1 P1-CU-07 **establishes** constitutive unity as necessary, never sufficient, for Level N. No new unity predicate grants authority or replaces any native §3 floor, accepted domain, evidence or integration requirement.

Phase 0 D1 v1.4.2 / D2 v1.4 remain the governing conditionally adopted pair. Phase 2 D1 v1.0 and its governing mathematical companion supply identity criteria: replace Part I §5's future-looking “Phase 2 must determine” wording accordingly. Applying the adopted rules to each case is still required; unresolved cases retain D2-INV-012 provisional isolation. Part I §11's Phase 2 deferral concerns application/implementation assurance, not adoption of the convention. No physical enforcement, identity preservation, FFNN or SA implementation is certified here.

The prefix P1-CU-01–08 denotes the requirement series; DEF-P1-CU-01–04 denotes the distinct definition series. Both prefixes are complete identifiers. VO-01–14 remain located in Part I §9; the CU obligations extend that register. “OPEN” means not fully discharged, not that every eventual implementation detail has already been specified.

## CU.1 Typed interpretation and finite assessment profile

Native sorts are `U,Σ,𝓘,C,R,Q,P,X,A,Γ,𝓔,Π,𝓗,𝓣,𝓞,Build,Scope,ModeType,Claim,Decision,IntegrityID`. New sorts are CURole, CULink, CUVersion, CUContext, CUWitness, CUInterpretation, ArtifactID, ClauseID, ProtocolID, RecordID and CUKey=Σ×Π×ModeType×Scope. New optional values use tagged `Opt(S)={None}⊎{Some(s):s∈S}`. `roleRef:CURole→R` and `linkRef:CULink→R` are **injective** and have disjoint images; the two injections were already explicit in v0.4. Sharing a physical mechanism does not collapse these identifiers.

Fin(S) denotes finite subsets; Seq(S) finite sequences. Fin(S)⊆𝒫(S), not equality in general. In the finite fixture the declared sets are finite, while native power-set notation retains its general meaning. CUContext is the formal representation of D1 DEF-P1-CU-02/04's prescribed state/input, operating or readiness conditions. No separate D1 formal sorts named Context or SourceAuthority exist in the supplied text; governing principals use native A and Γ.

**Two time scopes are explicit.** `CUInterval` denotes a nonempty physical interval with identified finite endpoints in an applicable ordering/clock domain; bounded does not imply finitely many instants. `CUPoints=Fin(𝓣)\{∅}` is the discrete executable profile. `ConstitutiveUnity` is the classical whole-interval schema below, with no assertion of algorithmic decidability for arbitrary domain predicates. `FiniteUnity` quantifies over declared CUPoints instead. A finite PASS covers those points only. Whole-interval PASS requires a governing coverage proof/protocol that accounts for every intervening state or a complete transition/invariance argument; sampling alone is insufficient. Unbounded ongoing operation is assessed through successive governed windows, never inferred from one finite fixture.

An interpretation θ has immutable key/version, requiredRoles:Fin(CURole), requiredLinks:Fin(CULink), allowedExtraRoles:Fin(CURole), allowedExtraLinks:Fin(CULink), dependencies:Fin(U), participants:CULink→Fin(CURole), relevantContexts:𝓘×CULink×𝓣→Fin(CUContext), allowedWitnesses:CULink×CUContext→Fin(CUWitness), roleStateProcess:𝓘×CURole×𝓣→Bool, witnessRealizes:𝓘×CUWitness×CULink×CUContext×𝓣→Bool, boundary:𝓘×𝓣→Bool, scopeRule:𝓘×𝓣→Bool, actualMode:𝓘×𝓣→ModeType, actualBuild:𝓘×𝓣→Build and actualGovernance:𝓘×𝓣→Γ. A witness has members:Fin(C), roles:Fin(CURole), processes:Fin(P) and occurrences:Fin(X), and may be a jointly sufficient configuration.

`KnownRoles(θ)=θ.requiredRoles∪θ.allowedExtraRoles` and `KnownLinks(θ)=θ.requiredLinks∪θ.allowedExtraLinks`. Context, witness, participant and role semantics must be supplied for every permitted extra as well as every required entry. Outside KnownLinks, contexts/witness sets return ∅ in this profile, but **absence of a governing extra interpretation is a missing prerequisite, not an established physical failure**. Such an extra may not receive a realization PASS.

Every interpreted field must be grounded in independently described native state/process/history or the prescribed governing protocol. ActualMode is a physical-mode function within a chosen admissible interpretation, not an observation. At every instant covered by an applicable mode claim that interpretation supplies exactly one applicable mode, including NONE/FAULTED where the governing rules specify them. A purported interpretation without such a mapping is incomplete for that claim. An observer's `Mode(i,o)=none` means evidence is unavailable, not that no physical mode exists. No default physical mode is inferred from ignorance; judgments remain UNDETERMINED. The same distinction applies to actual build and governance.

`Located:𝓞×𝓣×𝓔→Bool` is an imported evidence-backed observation/physical-time relation, assigned to VO-11/20. A validated current mode observation located at t must agree with actualMode(i,t); stale/unvalidated records establish neither equality nor inequality. Whole-interval coverage is a separate TIME obligation.

## CU.1.1 Artifact, registry, approval and independence contract

Presence flags are replaced by versioned artifact references. `Artifact=(id:ArtifactID,kind:{ROLE,LINK,CONTEXT,WITNESS,SCOPE,BINDING,PROTOCOL,DERIVATION,APPROVAL,BRIDGE},key:CUKey,content:IntegrityID,clauses:Fin(ClauseID))`. θ.artifacts:Fin(Artifact). A digest identifies content; it is not itself proof of approval or adequacy.

`GoverningRoles:CUKey→Fin(CURole)`, `GoverningLinks:CUKey→Fin(CULink)` and governing clause references are imported from the versioned specification/profile registry, not from the candidate contract or observed success. Define `θIndependent(θ)` to require θ.requiredRoles=GoverningRoles(θ.key), θ.requiredLinks=GoverningLinks(θ.key), a DERIVATION artifact covering every governing role/link clause, and registry provenance demonstrating that varying a candidate's submitted declarations/witnesses at fixed key cannot change those governing sets. This is functional non-interference and upstream coverage, not a prohibition on learning from prototypes when making a separately governed new specification version.

`InterpretationComplete(θ)` requires nonempty required role/link sets; nonempty participant sets within KnownRoles for every KnownLink, with required-link participants contained in requiredRoles; ROLE/LINK definition artifacts for every known entry; the CONTEXT/WITNESS/SCOPE/BINDING/PROTOCOL/DERIVATION/BRIDGE artifacts referenced by the applicable protocol; correct key/version bindings and no dangling artifact references. Artifacts are actually checked against a versioned manifest; an assertion that a Boolean “present” flag is true is insufficient.

`AuthorizedInterpretation(θ)` means approval for θ's exact key/version/content under the effective prior governance, with required authenticated approving principal, scope and no applicable prior revocation/supersession. Approval artifacts and imported authorization semantics are external assurance obligations under **VO-21**, with finite approval fixtures distinguished from real approvals. Identification alone does not establish authorization.

A `RegistrySnapshot` is a versioned finite map CUKey→CUInterpretation with provenance, governing index and approval artifacts. In a specified semantic snapshot `Resolve_s(k)=Some(θ)` exactly when the map contains a **unique** entry θ with θ.key=k; otherwise None. Conflicting entries make the snapshot invalid rather than permitting arbitrary choice. Registry independence requires its governing index and effective version selection to be authorized and invariant under changes to a candidate submission at fixed key; verification is VO-21. Domain metadata does not authorize itself.

Derived signatures: `θIndependent,InterpretationComplete,AuthorizedInterpretation:CUInterpretation→Bool`; `Resolve:RegistrySnapshot×CUKey→Opt(CUInterpretation)` with Resolve_s(k)=Resolve(s,k); `CUAccepted:RegistrySnapshot×CUKey→Bool`, with the snapshot-indexed definition `CUAccepted_s(k) := ∃θ [Resolve_s(k)=Some(θ) ∧ θ.key=k ∧ AuthorizedInterpretation(θ) ∧ θIndependent(θ) ∧ InterpretationComplete(θ)]`.

Semantic Resolve is distinct from the evidence-backed lookup report below. An unknown registry is not an empty registry. Standalone predicates accepting θ explicitly retain the key-equality check as a defensive condition; it is intentionally redundant when θ came from a valid matching snapshot. No alternative candidate-supplied θ can bypass lookup in CUAssess.

## CU.2 Contracts, extras and realization

`CUContract=(version:CUVersion,subject:𝓘,build:Build,spec:Σ,profile:Π,mode:ModeType,scope:Scope,interval:CUInterval,roles:Fin(CURole),links:Fin(CULink),dependencies:Fin(U),governance:Γ,evidenceScope:Scope)`. KeyOf(a) is its spec/profile/mode/scope tuple. RR(θ)=θ.requiredRoles and RL(θ)=θ.requiredLinks. Required sets are constant within the immutable governing version; changes require segmented claims/reassessment.

`ContractComplete(θ,a) := θ.key=KeyOf(a) ∧ RR(θ)⊆a.roles ∧ RL(θ)⊆a.links ∧ RR(θ)≠∅ ∧ RL(θ)≠∅`.

`ExtraRoles(θ,a)=a.roles\RR(θ)` and `ExtraLinks(θ,a)=a.links\RL(θ)`. `ExtrasDeclared(θ,a)` requires these sets to be subsets of θ.allowedExtraRoles/Links, and each extra's ROLE/LINK/CONTEXT/WITNESS/protocol artifacts to resolve. This is the structural part, not the semantic check.

`RoleRealized(θ,i,r,t) := θ.roleStateProcess(i,r,t) ∧ ∃c:C [Member(c,i,t) ∧ Fills(c,roleRef(r),i,t)]`.

`LinkRealized(θ,i,l,t) := θ.relevantContexts(i,l,t)≠∅ ∧ ∀κ∈θ.relevantContexts(i,l,t) ∃w∈θ.allowedWitnesses(l,κ) θ.witnessRealizes(i,w,l,κ,t)`.

Each accepted witness interpretation specifies actual native state/process relationships and the required participants in the specified relevant contexts. Unrelated activity, shared storage or labels do not suffice. Different contexts may use different witnesses, alternative paths or a jointly sufficient configuration. Readiness may be the applicable condition at an idle instant. These are contract-relative semantic parameters with the explicit crosswalk and assurance obligations below; they are not assumed universally realized.

`ExtrasCompatible(θ,i,a) := ∀t∈a.interval [(∀r∈RR(θ):RoleRealized(θ,i,r,t)) ∧ (∀l∈RL(θ):LinkRealized(θ,i,l,t))]`, evaluated in the **actual candidate with its extras present**, under the unchanged governing required-role/link meanings. Compatibility here means preservation of required processing, not unchanged optional behavior or universal output equivalence.

`ExtrasPermitted(θ,a) := ExtrasDeclared(θ,a) ∧ [(ExtraRoles(θ,a)=∅ ∧ ExtraLinks(θ,a)=∅) ∨ ExtrasCompatible(θ,a.subject,a)]`.

This is explicitly **semantic**. Metadata alone cannot establish it. Its dependencies are RoleRealized/LinkRealized, whose definitions may not use ExtrasPermitted or unity. A memory-lookalike does not replace the canonical required memory role: inclusion is checked against RR, and the actual required role/link semantics are still evaluated. Missing extra semantics yields NOT_YET_CERTIFIABLE; established interference yields FAIL; undecided compatibility yields UNDETERMINED. Permitted extras receive their own item claims as well.

`ContractWellFormed(θ,a) := ContractComplete(θ,a) ∧ ExtrasDeclared(θ,a) ∧ θ.dependencies⊆a.dependencies ∧ a.evidenceScope=a.scope`. Well-formedness is now clearly structural; semantic ExtrasPermitted is a separate claim and unity condition. Extra components not claimed as roles are not categorically forbidden, but cannot remove mandatory obligations or escape assessment of interference with required processing.

`BindingsHold(θ,i,a,t) := θ.key=KeyOf(a) ∧ i=a.subject ∧ SpecOf(i,t)=a.spec ∧ θ.actualMode(i,t)=a.mode ∧ θ.scopeRule(i,t) ∧ θ.actualBuild(i,t)=a.build ∧ θ.actualGovernance(i,t)=a.governance`.

`ConstitutiveUnity(θ,i,a) := ContractWellFormed(θ,a) ∧ ExtrasPermitted(θ,a) ∧ ∀t∈a.interval [BindingsHold(θ,i,a,t) ∧ θ.boundary(i,t) ∧ (∀r∈RR(θ):RoleRealized(θ,i,r,t)) ∧ (∀l∈RL(θ):LinkRealized(θ,i,l,t))]`.

`FiniteUnity(θ,i,a,S)` uses the same conditions restricted to S:CUPoints and is explicitly a finite-point result. If extras exist, its compatibility condition is likewise restricted to S. It cannot be relabeled whole-interval ConstitutiveUnity without the independent coverage argument. Neither formula is a sufficient Level N theorem.

## CU.3 Constructed claims, protocol semantics and total assessment

### CU.3.1 Conservative claim constructors

Define a tagged `CUClaimNode` sort with constructors: MissingInterpretation(k), Acceptance(k), Structure(i,a,v), Binding(i,a,v), Boundary(i,a,v), Role(i,a,v,r), Link(i,a,v,l), Extras(i,a,v), Bridge(i,a,v), Change(i,a,v), Evidence(i,a,v), and Time(i,a,v,o), with k:CUKey, i:𝓘, a:CUContract, v:CUVersion, r:CURole, l:CULink and o:𝓞. Add an injective constructor embedding `embedCU:CUClaimNode→Claim` as a conservative extension of the native claim vocabulary. Existing native claims/judgments are unchanged outside this image.

| Node | Proposition denoted |
|---|---|
| MissingInterpretation(k) | Governing interpretation prerequisite for k is unavailable; prerequisite status, not a mechanism-failure assertion |
| Acceptance(k) | CUAccepted_s(k), with the referenced registry/approval/independence artifacts |
| Structure | ContractWellFormed(θ,a) for resolved θ of version v |
| Binding | All BindingsHold conditions over the asserted interval/finite profile |
| Boundary | θ.boundary over that asserted scope |
| Role / Link | Actual RoleRealized / LinkRealized for the indicated canonical entry |
| Extras | ExtrasPermitted, including declared extra semantics and preservation of required processing |
| Bridge | Applicable BridgeHolds and support-contract correspondence from CU.4 |
| Change | Version preservation, reference links and applicable governed reassessment from CU.5 |
| Evidence | Build/scope/freshness/provenance and independent evaluation requirements of native §8 |
| Time | Evidence covers the claimed physical interval, or explicitly only the declared finite points |

This table fixes denotation; it does not assert that the propositions are true. A `CUItem` is a core tag STRUCTURE/BINDINGS/BOUNDARY/EXTRAS/P0BRIDGE/CHANGE/EVIDENCE/TIME or tagged RoleItem(r)/LinkItem(l). Items(θ,a) contains all core tags and every submitted role/link item. `ItemClaimAt(i,a,j,o)` returns embedCU of the corresponding constructor with the resolved version. If lookup cannot supply a matching interpretation, it returns embedCU(MissingInterpretation(KeyOf(a))) for **every** j; no θ-dependent field is dereferenced. AssessItems(a)=CoreItems in that branch. Thus the constructors and fallback are total even if invoked independently of CUAssess.

### CU.3.2 CU protocol contract

A `CUProtocol` has ProtocolID, exact governing key/version, a versioned handler for every constructor above, identified admissible evidence schemas, validation and contradiction rules, freshness/build/scope rules, interval-coverage method and an approval/independence reference. A handler has type `CUClaimNode×𝓔×Scope×𝓞→{PROVED,REFUTED,UNKNOWN,MISSING_PROTOCOL}` and must be either an executable total algorithm on the stated finite input class or a precisely referenced governing proof/evaluation contract with an open assurance obligation. An unspecified name or a table of desired verdicts is not a specified handler.

`ProtocolSpecified:CUProtocol→Bool` requires total constructor coverage, complete handler references and artifact binding; `ProtocolAssured:CUProtocol×𝓔×𝓞→Bool` requires independently established approval and the relevant validation/soundness evidence for the claimed input class. VO-22 records both specification and assurance; no actual PASS is credited while either requisite is missing or unresolved. Approval authenticity and independence remain explicit imported assurance, not implied by a local Boolean or a digest.

For each node n, the specified handler returns a finite evidence classification from `{PROVED,REFUTED,UNKNOWN,MISSING_PROTOCOL}` under its declared scope. Verified contradictory evidence is UNKNOWN unless the governing protocol establishes a decisive basis. PROVED requires valid evidence covering **every** sub-obligation; lack of a counterexample is not proof. A missing prerequisite is never a fabricated negative physical fact.

`CUJudge:CUClaimNode×𝓔×Scope×𝓞→Decision` is total: return NOT_YET_CERTIFIABLE for MissingInterpretation or a known missing handler; otherwise use the specified handler: REFUTED→FAIL, PROVED→PASS, UNKNOWN→UNDETERMINED, MISSING_PROTOCOL→NOT_YET_CERTIFIABLE. A PROVED result is downgraded to UNDETERMINED when protocol assurance is unknown, and to NOT_YET_CERTIFIABLE when its required protocol is known absent/invalid. A valid refutation under an available independently valid counterexample rule remains FAIL despite missing positive-proof machinery elsewhere. The native extension is constrained by `Judge(embedCU(n),E,s,o)=CUJudge(n,E,s,o)`; it is not arbitrary Judge behavior on new claim tags.

The accompanying finite protocol actually evaluates registry, coverage, bindings, mechanism/link witnesses, semantic extras and reference preservation for its declared fixture. It does not implement arbitrary real-domain evidence adjudication. Missing real handlers and assurance remain VO-22 obligations and cannot be replaced with that fixture.

### CU.3.3 Lookup boundary and aggregation

An evidence-backed registry lookup reports one of `PRESENT(θ)`, `KNOWN_ABSENT`, `INVALID`, `UNKNOWN`. PRESENT requires a matching key/version and validated unique snapshot entry; INVALID includes mismatched keys or conflicting versions. UNKNOWN is the result of missing/stale/unvalidated registry evidence, never inferred absence. Known lack of approval, complete artifact manifest, independence derivation or applicable protocol is a missing prerequisite; unresolved assurance is UNKNOWN. These conditions are assessed under VO-21/22, not supplied by a candidate assertion.

Define `CUAssess:𝓘×CUContract×𝓔×𝓞→Decision` as the following total procedure:

1. If the protocol establishes a θ-independent applicable violation (for example a demonstrably wrong subject binding under an available governing rule), return FAIL. This branch may not inspect unavailable θ fields.
2. Obtain the registry report for KeyOf(a). For KNOWN_ABSENT or INVALID return NOT_YET_CERTIFIABLE; for UNKNOWN return UNDETERMINED. **No ItemClaimAt handler depending on θ is called in these branches.**
3. For PRESENT(θ), form Items(θ,a) and evaluate each constructed claim under CUJudge. Include the Acceptance node's assessment; a refuted acceptance prerequisite is classified as missing, not a mechanism failure.
4. Return FAIL if any applicable item is FAIL. Otherwise return NOT_YET_CERTIFIABLE if a prerequisite or item is known missing; otherwise UNDETERMINED if any required item, registry/approval/derivation or protocol assurance is unresolved; otherwise PASS.

This explicitly covers absent θ, bad-key resolution, invalid approval, missing handlers, unknown evidence and supplied-but-unassured protocols. Generic model-relative Boolean truth is never treated as evidence automatically available to the assessor. A finite positive example is not assigned stipulated positive item judgments: its dynamic items are computed, and any imported real assurance remains missing/unresolved outside the finite declared fixture.

## CU.4 Phase 0 bridge: scope and imported preservation

`P0Binding⊆𝓘×P0.Inst` is the **canonical logical-instance** correspondence; `P0EventBridge⊆X×P0.Operation` maps native occurrences to full Phase 0 governed envelopes. Phase 0 Inst is its registered 𝒩; Operation is its governed-event 𝒱, not its state objects 𝒳 or heartbeat partition X. Native Phase 1 X remains transition-occurrence IDs. Alias records must resolve to one canonical binding; multiple hosts/constituents do not require multiple entity bindings.

`RequiresP0:CUKey→Bool` is part of the governing profile, independent of a candidate's events. It is true for real operational NNNC/Level N claims. An explicitly abstract finite composition fixture may set it false and cannot thereby certify an NNNC or perform protected effects. `RequiredP0Events:CUInterpretation×𝓘×CUContract→Fin(X)` is the complete governing set of relevant occurrences in the asserted finite event window; it cannot be reduced to those a candidate elected to submit. In a whole-interval claim, the governing coverage proof must also establish event completeness. VO-18 covers that proof.

`BridgeField={INSTANCE,EVENT_ID,TARGET,ORIGIN,EXECUTOR,PRIOR_POLICY,STATUS,EFFECTS,ORDER,CLOCK,SESSION,BUDGET,SHUTDOWN}`. `FieldPreserved:BridgeField×𝓘×P0.Inst×X×P0.Operation→Bool` is an **imported interpretation parameter**: each field uses the actual native event/history projections and governing Phase 0 equality/refinement relation, not candidate labels. Its normative semantics are the adopted P0 transition envelope, prior-authority, support, clock/deadline, canonical session, reservation and shutdown contracts. VO-18 requires the correspondence derivation for each field; no implemented refinement is claimed merely by declaring this parameter.

`BridgePreserves(i,n,x,v) := ∀f∈BridgeField FieldPreserved(f,i,n,x,v)`.

`BridgeHolds(θ,i,a) := if ¬RequiresP0(KeyOf(a)) then RequiredP0Events(θ,i,a)=∅ else [(∃!n:P0.Inst P0Binding(i,n)) ∧ ∀n [P0Binding(i,n) ⇒ ∀x∈RequiredP0Events(θ,i,a) ∃v [P0EventBridge(x,v) ∧ BridgePreserves(i,n,x,v)]]]`.

Thus an operational subject requires **exactly one canonical logical-instance binding even when the event set is empty**; this is a subject-registration requirement, not a claim of one process or proof of identity. A claim concerning two independent registered subjects must use separate subject bindings/claims, with coordination expressed by its applicable external relations. The abstract fixture's empty-event exception is explicit and never inferred from an empty submitted event list.

Every dependent progress claim must identify the exact P0 support contract, obligation, trusted clock domain, deadline and execution-history correspondence. Promises, actual support and justified evidence remain distinct. Support loss cannot erase an applicable end-to-end miss, create a mechanism breach without evidence, refund a budget, bypass shutdown or resurrect stale authority. Missing timer/observer evidence cannot fabricate deadline closure. Fresh clocks and contracts require authorized reconciliation; later changes cannot rewrite earlier outcomes. All P0-O01–08 remain open; O01–03 retain deployment-blocking scope.

The Bridge claim participates in CUAssess. A known missing governing bridge protocol is NOT_YET_CERTIFIABLE, an unresolved mapping is UNDETERMINED, and an established applicable preservation violation is FAIL. Declaring the imported parameter and its exact obligation suffices for **reference-contract specification**, not for an actual assessment PASS or full implementation refinement.

## CU.5 Append preservation with references

`AssessmentRecord=(id:RecordID,kind:{INITIAL,REASSESS,CORRECT},subject:𝓘,family:Scope,version:CUVersion,claim:Claim,verdict:Decision,evidence:Fin(𝓔),parents:Fin(RecordID))`; `AssessmentHistory=Seq(AssessmentRecord)`.

`AppendPreserves(h,h′) := ∃suffix [h′=h++suffix]` remains the history-prefix property. Add `AppendReferences(h,h′)` requiring unique IDs throughout h′ and, for every appended record at index j: INITIAL has empty parents; REASSESS/CORRECT has nonempty parents; every parent ID resolves to an earlier index <j with the same subject and assessment family. Governing change/binding rules must additionally establish that the cited versions/claims are the actual reassessment basis. `ValidReassessment(h,h′) := AppendPreserves(h,h′) ∧ AppendReferences(h,h′) ∧ GovernedChange(h,h′)`; GovernedChange is the native prior-authority, cumulative-envelope, version and evidence-freshness obligation, assigned VO-19.

This explicitly distinguishes append-only storage from append-and-reference semantics. A correction can change the current verdict by appending a traceable new record; it cannot destroy an old record or silently reinterpret its old contract. No concrete durable database implementation is certified. Phase 2 continues to govern identity, while Phase 0/3 govern protected authority.

## CU.6 D1→D2 semantic crosswalk and assurance ledger

The following rows constrain admissible interpretations; mere syntactic signatures are insufficient. A later interpretation is admissible only with a derivation showing these meanings and its claimed coverage. This is a schema-level preservation obligation, not an assertion that arbitrary Boolean assignments satisfy D1.

| Authoritative D1 clause | D2 representation | Required interpretation / no weakening or extra mandate | Evidence / obligation |
|---|---|---|---|
| DEF-P1-CU-02 processing | roleStateProcess, participants, relevantContexts | State transformations, role interfaces and prescribed readiness/operating conditions; contexts are not selected after candidate success; no compulsory busy loop | Native state/transition mapping and context coverage; VO-16/17 |
| DEF-P1-CU-03 composition | RoleRealized, LinkRealized, witnessRealizes | Actual required roles and interactions must hold; witness semantics cannot reduce to labels, communication or shared storage; no all-to-all controller mandate | Discriminating mechanism witness and disconnected control; VO-17 |
| DEF-P1-CU-04 contextual contribution | relevantContexts, allowedWitnesses, witnessRealizes | Every prescribed relevant context has an acceptable actual witness; allow alternatives and joint configurations; individual indispensability not required | Context, redundancy and joint-sufficiency cases; VO-17 |
| P1-CU-01/03 bindings | actualMode, actualBuild, actualGovernance, scopeRule | Derived actual state/history and governing versions, not copied claimant metadata; scope cannot shrink inherited mandatory obligations | State/history projections and build/governance evidence; VO-16/20 |
| P1-CU-02 independent applicability | GoverningRoles/Links, θIndependent, Resolve_s | Complete upstream clause coverage and candidate-input non-interference at fixed governing key; new specification revisions remain governed, not forbidden | Registry manifest, clause derivation, approval and non-interference checks; VO-15/21 |
| P1-CU-02/04 extras | ExtrasDeclared, ExtrasCompatible, ExtrasPermitted | Canonical required roles remain required; added mechanisms must preserve their actual relations; optional behavior may differ | Semantic interference and memory-lookalike controls; VO-15/17 |
| P1-CU-05 support | BridgePreserves, BridgeHolds, RequiresP0 | Preserve actual P0 envelope/authority/support semantics; finite abstract exception cannot certify operational NNNC | Explicit imported field correspondence; VO-18 |
| P1-CU-06 reassessment | ValidReassessment | Prefix retention AND earlier-version reference AND native authorization/freshness checks | Orphan/future/unrelated parent controls and governed-change evidence; VO-19 |
| P1-CU-07 judgment | CUClaimNode, embedCU, CUProtocol, CUJudge, CUAssess | Claim denotations are constructed; no PASS without specified handlers and established assurance; unknown fact is not physical falsehood | Boundary and protocol decision checks; VO-20/22 |
| P1-CU-08 handoff | Gates, result coverage map, VO register | Separate fixture checks, reference-contract completeness, imported assurance and real implementation qualification | Accompanying JSON/code/artifacts and per-clause routes; VO-15–22 |

**VO-21 — Registry/interpretation assurance (OPEN):** establish governing index completeness, candidate-input independence, exact artifact content, matching key/version, prior-policy approval and registry selection. A finite registry test provides bounded evidence only. No actual positive CU assessment may credit these prerequisites on the basis of an unverified “approved” field.

**VO-22 — Claim/protocol specification and assurance (OPEN):** establish constructor denotations, native Claim embedding/adapter, total handlers including missing θ, complete item coverage, input-class soundness, independent approval and valid interval coverage. A missing handler is a certification blocker; unresolved assurance is UNDETERMINED. No actual PASS is credited until the applicable obligations are established.

VO-01–14 remain in Part I §9, and VO-15–20 retain their property families and controls from the previous pair, as refined by this part. Every obligation remains **not fully discharged at its stated scope**. The finite fixtures do not establish full real-domain semantics, institutional independence or production enforcement.

## CU.7 Working tests and prior adversarial routing

Retained Part I §10 T-04 remains historical text only: it is **retired from the active register and superseded by CU-T06**, whose relevant source is AC-22, not AC-23. D1 has no separate T-04 entry; the pair uses the D2 active register.

CU-T01 is the computed finite positive composition fixture, not a collection of stipulated positive judgments. Its role/link behavior, bindings, registry records and finite evidence handlers are actually evaluated. Its approval/policy environment is an explicitly simulated finite trust fixture, never real architect approval or Level N evidence. CU-T02/03 omission/empty controls, CU-T04 nonexistent realization, CU-T05 disconnected activity, CU-T06 wrapper, CU-T07 redundancy, CU-T08/09 P0 support, CU-T10/11 reassessment and CU-T12 missing/unknown protocol controls retain their purposes. Full real-kernel CU-T08/09 tests remain OPEN.

The gate fails if a labels-only/wrapper-only claim is wrongly granted PASS. That does **not** require the candidate verdict always to be FAIL: a proven absent internal realization yields FAIL, but an untested wrapper with insufficient attribution evidence yields UNDETERMINED. Both correctly deny unsupported PASS.

The individual AC-17–42 routes remain in the attached routing table, unchanged except new assurance destinations where applicable. AC-01–16 exact source remains unavailable and OPEN. No resolved-finding count substitutes for explicit dispositions; no full AC execution is claimed.

### Current VO-15–20 property register

These rows restore the standalone current register. They supplement native VO-01–14 and current VO-21/22; they do not rely on a prior candidate for their operative meaning. All remain not fully discharged at their stated scope.

| ID | D1 sources | Property / oracle | State or interface | Controls | Current evidence / residual |
|---|---|---|---|---|---|
| VO-15 | P1-CU-01/02/08 | Complete canonical required roles/links; omissions cannot reduce applicability; extras do not replace requirements | Governing index, registry/derivation, ContractComplete, ExtrasDeclared | CU-T01–03/12 | Finite coverage and registry mutations checked; general approval/independence assurance VO-21 OPEN |
| VO-16 | P1-CU-02/03/08 | Actual Member/Fills and role-specific state/process behavior for each required role | RoleRealized, actual bindings, native constituents | CU-T01/04/10/11 | Finite membership, binding and state corruptions checked; full real-domain realization OPEN |
| VO-17 | P1-CU-04/08; REQ-P1-032 | Required contexts have actual realizing configurations; irrelevant activity fails; alternatives/joint sufficiency allowed; extras preserve ALL required roles AND links | LinkRealized, witness/context interpretation, ExtrasCompatible | CU-T01/05/06/07 | Finite composition, redundancy and semantic extras checked; real cognitive attribution OPEN |
| VO-18 | P1-CU-05/08; P0-SUP-01–08 | Native P0 envelope/authority/support correspondence; no obligation erasure or new authority from support loss | BridgeHolds, all BridgeField imports, RequiresP0 | CU-T08/09 | Finite registration/envelope boundary checks only; deployed refinement and live support histories OPEN |
| VO-19 | P1-CU-06/08; REQ-P1-041 | Historical versions preserved with valid earlier references and governed reassessment | ValidReassessment, native governance/envelope/freshness | CU-T10/11 | Finite append/reference controls checked; durable enforcement and real governed-change evidence OPEN |
| VO-20 | P1-CU-07/08; FO-09/12 | Truth, evidence, scope/time coverage and qualification stay distinct; conflicting observed/actual modes cannot support PASS | CUJudge/CUAssess, bindings, TIME/EVIDENCE items | CU-T01/12 | Finite handlers, mode conflicts and missing/unknown cases checked; actual protocol assurance VO-22 OPEN |

### Current CU-T01–12 control register

“Finite checked” identifies the scoped fixture, not a real NNNC or general proof. This table states the current construction and oracle directly.

| ID | Construction | Expected oracle | Execution scope |
|---|---|---|---|
| CU-T01 | Versioned finite memory/selector/regulator organization with registered members and computed evidence handlers | Scoped positive result only when every applicable item and prerequisite is supported | Finite checked; simulated policy authority only |
| CU-T02 | Omit any canonical required role or required link | Required coverage fails; a lookalike extra cannot replace it | Finite checked, including all presence combinations |
| CU-T03 | Empty operational-unity role/link declaration | No vacuous operational-unity PASS; generic entity existence remains separate | Finite checked |
| CU-T04 | Role label without required membership or state/process realization | Role fails; when extras exist, EXTRAS must also fail if any required role fails | Finite membership/state corruption subset checked |
| CU-T05 | Active diagnostic mechanisms but selector disconnected from retained memory | Required memory-selection relationship fails despite genuine local activity | Finite checked |
| CU-T06 | Internal wrapper relies on an external service for decisive cognition | Proven substitution/non-realization→FAIL; unresolved attribution→UNDETERMINED; signature alone never PASS | Specification retained; full external-service fixture OPEN; supersedes historical T-04 |
| CU-T07 | Alternative redundant paths, context-specific witnesses or jointly sufficient configurations | Permit legitimate contribution without individual indispensability; joint removal/irrelevant contexts discriminate | Finite configuration controls checked |
| CU-T08 | Governed P0 mapping, canonical subject and timely support-dependent processing | Preserve imported native authority/support/outcome rules; operational registration required even with no events | Finite binding/envelope subset checked; full live-kernel fixture OPEN |
| CU-T09 | Scheduler starvation/lost timer/observer gap with an otherwise applicable obligation | End-to-end outcome and attribution remain distinct; no fabricated expiry, success, privilege or budget | Imported specification; full live support/clock fixture OPEN |
| CU-T10 | Valid versioned reassessment referencing earlier same-subject/family records | Append valid new record; retain prior version/result | Finite references checked; full authorization/freshness implementation OPEN |
| CU-T11 | Orphan/future/unrelated parent, overwrite or stale binding/evidence | Invalid reassessment/binding rejected or evidence unresolved under governing rules | Finite reference/binding subset checked |
| CU-T12 | Missing/invalid/unknown registry, handlers, approval, assurance or time coverage; contradictory mode observation | Missing→NOT_YET_CERTIFIABLE; unresolved/conflicting evidence→UNDETERMINED; demonstrated violation→FAIL; no false PASS | Finite boundary/protocol/mode controls checked |

### Individual retained AC routing


This table supersedes the approximate **group routing only** in Part I §10. It does not change the D1 constructions or claim execution. AC-01–16 still lack their exact source text and remain OPEN for archival reconciliation. The supplied D1 contains AC-17–42, so their individual routing can now be recorded without guessing. MODEL means a foundational oracle can be constructed; INTERFACE requires a governing imported contract; LATER requires substantive later-domain realization. Mixed labels preserve both responsibilities.

| Case | Required oracle, preserving D1 meaning | Route and VO | Execution |
|---|---|---|---|
| AC-17 | Self-serving profile cannot omit essential floor | MODEL; VO-08/14 | Planned |
| AC-18 | Retroactive self-authorization rejected | MODEL/INTERFACE P0; VO-04 | Planned |
| AC-19 | Conflicting controllers cannot yield incompatible authoritative outcomes | MODEL/INTERFACE P0; VO-10 | Planned |
| AC-20 | Manifest of nonexistent mechanism gives no realized conformance | MODEL; VO-06/08/16 | Planned |
| AC-21 | Other-build evidence rejected for current build | MODEL/evidence interface; VO-11 | Planned |
| AC-22 | External decisive cognition cannot establish internal claim | INTERFACE/LATER; VO-09/17 | Planned; finite analogy only |
| AC-23 | Fixed external schedule alone does not demonstrate endogenous regulation | INTERFACE/LATER; VO-13 | Planned |
| AC-24 | Components without required integration do not establish cognitive unity | INTERFACE/LATER; VO-09/17 | Planned; finite analogy only |
| AC-25 | Historical capability evidence retained; current availability updated | MODEL/evidence interface; VO-06/11/19 | Planned |
| AC-26 | Profile deferring all cognitive mechanisms cannot qualify Level N | MODEL; VO-08/14 | Planned |
| AC-27 | Heartbeat after relevant state wipe establishes neither dormancy nor continuity | INTERFACE P0/P2; VO-05 | Planned |
| AC-28 | Cold restore with active continuation requires exclusivity adjudication or uncertainty | INTERFACE P0/P2; VO-05/10 | Planned |
| AC-29 | Forged governance/lineage cannot establish authorized history | INTERFACE/evidence; VO-04/05/11 | Planned |
| AC-30 | Split-brain authorities cannot receive incompatible dual certification | MODEL/INTERFACE P0/P2; VO-10/14 | Planned |
| AC-31 | Gradual authorized replacement still needs cohesion and continuity evaluation | INTERFACE/LATER P2/development; VO-05/12/19 | Planned |
| AC-32 | Expired evidence rejected for current scope | MODEL/evidence interface; VO-11 | Planned |
| AC-33 | Migration/restoration/partial loss represented as compound event without false simplification | INTERFACE P0/P2; VO-05 | Planned |
| AC-34 | Loss of role-critical existential constituent triggers governing fault/continuity evaluation | INTERFACE P0/P2; VO-05/16 | Planned |
| AC-35 | Candidate profile change and self-certification cannot authorize its own claim | MODEL/evaluation interface; VO-08/14 | Planned |
| AC-36 | Model proof alone cannot prove deployed implementation | MODEL/evidence interface; VO-11 | Planned |
| AC-37 | Superficial FFNN substitutes cannot establish required flow realization | INTERFACE/LATER flows; VO-08/14 | Planned |
| AC-38 | Renamed generic algorithms cannot establish six SA realizations | INTERFACE/LATER algorithms; VO-08/14 | Planned |
| AC-39 | Missing authoritative component contract blocks full certification | MODEL; VO-08/14/20 | Planned |
| AC-40 | Legitimate conventional subcomponent permitted, without whole-system substitution | INTERFACE/LATER; VO-08/09 | Planned |
| AC-41 | Individual component satisfaction without integration cannot establish Level N | INTERFACE/LATER; VO-08/09/17 | Planned; finite analogy only |
| AC-42 | Retrospective certification requires evaluation against applicable accepted specification | MODEL/evidence and domain interfaces; VO-11/14 | Planned |



## CU.8 Scoped measurable gates and acceptance boundary

F-1/F-2/F-6 are pair-level; F-3 is D2's finite fixture; F-4 checks D1's mandatory commitments and D2's exact native 18-slot formula, plus **both documents' new text**; F-5 combines D1's specific Phase 2 replacements and D2's bridge-specification/open-status record. F-7 is the additional per-assessment registry/protocol assurance gate. Document acceptance and a particular runtime candidate's qualification are different decisions.

| Gate | Pass condition and evidence | Failure / status boundary |
|---|---|---|
| F-1 Declarations and parameter contracts (pair) | Every new symbol has types and either an operative definition, a precise governing contract reference, or a named open obligation with a prohibition on unsupported qualification PASS | An unspecified primitive silently treated as success fails; imported fields must appear in the semantic crosswalk and VO-15–22 ledger |
| F-2 Architectural/formal correspondence (pair) | DEF-P1-CU-02/03/04 and each P1-CU requirement map to the explicit CU.6 rows; actual witness/context/state meanings and required constraints are stated; no primitive uses unity or a desired verdict to define itself | Missing row, a label-only witness admitted as realization, or a contradictory necessity/identity/authority rule fails; real domain interpretation assurance is separately required by F-7 |
| F-3 Finite fixture coverage (D2) | Record every required role's realization cases and every required link's positive witness/intervention pairs; disconnected control denies PASS; alternative/joint/context controls run; all declared required entries are covered | A required entry missing from the coverage ledger or an unsupported PASS fails the gate; a correct candidate verdict of FAIL **or UNDETERMINED**, as appropriate to evidence, is not a gate failure |
| F-4 Qualification monotonicity (pair) | Retain D1's full mandatory commitments and the exact native D2 §3 18-slot formula; every new Level N implication remains cumulative with them and D1 P1-CU-07; none introduces a sufficient route omitting a mandatory domain or grants protected authority from unity | A concrete new counter-route in the operative CU text fails. This compares against retained D1 v2.0/D2 v0.2.1 requirements plus the expressly added unity necessity, not an unspecified ideal baseline |
| F-5 Governing dependency specification (mixed) | D1's exact §8.5/§9.2/provisional replacements preserve adopted Phase 2 rules; D2 specifies P0 field correspondence, canonical binding and support outcomes and assigns implementation refinement to VO-18 | A contradictory replacement or false discharge of P0-O01–08 fails. Closure of implementation refinement is **not** this document gate's requirement; specification and explicit open assignment are |
| F-6 Reproducible evidence (pair) | Every supplied finding has a disposition; code, fixture manifest, results, role/link coverage, prior sources, diffs and final hashes accompany the issue; all counts distinguish assertions/fixtures from independent experiments | Missing files, an untested condition claimed executed, or a bounded result presented as full proof fails |
| F-7 Actual assessment prerequisites | For any claimed actual CUAssess PASS, establish registry/approval/independence artifacts, constructor handlers, scope/input-class assurance and whole-interval coverage when claimed | Known missing prerequisite→NOT_YET_CERTIFIABLE; unresolved evidence→UNDETERMINED; demonstrated applicable violation→FAIL. A local simulation of these prerequisites never discharges actual VO-21/22 |

Retained D1 §18 mapping: item 1→F-1/2; item 2→F-2 plus its native distinctions; item 3→F-4; item 4→F-2 plus native qualification definitions; item 5 remains a standalone native boundary/time/continuity coherence check, informed by F-2/5; item 6→F-5; item 7→F-2/3 plus later-domain obligations; item 8 remains a standalone no-in-scope-contradiction check, informed by F-1–6 rather than replaced by them; item 9→F-6 and the VO ledger; item 10 remains the separate recorded architect adoption act. No §18 criterion is silently removed.

A focused disposition of F-1–F-6 assesses this reference-contract issue. F-7 governs crediting actual candidate results and may remain unestablished without pretending an actual NNNC is qualified. A reproducible in-scope defect receives targeted correction; missing future mechanisms do not require unbounded general review. This issue remains **ACCEPTANCE CANDIDATE — NOT ADOPTED**.

## Closing disposition — 25 October 2026

The supplied independent closing review passed the reference-contract architecture, mathematical correspondence, mandatory floor and predecessor alignment, subject to three reproducible corrections. This issue implements those corrections: (1) current D1 destinations and VO-21/22 routing, plus self-contained D2 VO/control tables; (2) contradictory current observed/actual mode evidence no longer supports a binding PASS; (3) EXTRAS evaluates all required role realizations and links, with regulator local state distinct from its cross-component update influence.

The targeted regression run and current package integrity/reproduction checks are recorded in CLOSING-ACCEPTANCE-RECORD.md. Gates F-1/F-2/F-4/F-5 retain the independent review's formal/cross-phase inspection basis; F-2's reference correction, F-3's code corrections and F-6's regenerated evidence are checked in this issue. The reference-contract acceptance recommendation is **PASS — READY FOR ARCHITECT ADOPTION**, retaining every stated deferred obligation. This is not a new unrestricted review round.

F-7 remains OPEN for actual runtime qualification. Full VO discharge remains zero; P0-O01–08, real-domain protocols/assurance, continuum coverage, later cognitive contracts, live kernel refinement and AC-01–16 archival reconciliation retain their prior status. No particular new cryptographic or institutional mechanism is imposed by this correction; governing authorization requirements remain those already specified.

**Adoption is not recorded in this issue.** The supplied closing review and targeted corrections establish the acceptance recommendation; a separate explicit architect decision is still required to mark these exact versions adopted.

## Embedded current verification evidence

**32 passing groups; 415 listed assertion/fixture cases.** Counts include document checks and overlapping fixtures, not independent empirical trials. Full VO discharge remains zero. The 256-case coverage group enumerates four role-presence bits, three link-presence bits and one actual-interference bit. The preceding v0.4 issue had 25 groups and 585 listed cases; that historical run does not verify changed formulas.

| Group | Result | Listed cases / limitation |
|---|---|---|
| Computed positive protocol | PASS | 14; Computed item handlers in simulated trust fixture; never actual approval |
| Total lookup boundaries | PASS | 4; Absent, unknown, bad-key and conflicting registry; no theta dereference |
| Approval and prior policy | PASS | 4; Wrong signer/prior policy, revoked approval, unknown evidence |
| Manifest integrity and upstream coverage | PASS | 4; Deleted/corrupt artifact and candidate-tailored reduced sets rejected |
| Every claim handler required | PASS | 11; Each constructor family independently removed |
| Protocol assurance | PASS | 2; Unknown and known-invalid protocols receive different non-PASS outcomes |
| Disconnected mechanism | PASS | 1; Same component registrations and active diagnostics; memory link absent |
| Coverage and semantic extras | PASS | 256; 4 role bits x 3 link bits x 1 actual-interference bit; compatibility computed from transitions |
| Lookalike cannot replace required role | PASS | 1; Canonical memory omission is an applicable violation |
| Unknown extra contract | PASS | 1; No extension semantics is not-yet-certifiable |
| Known extra role and link evaluated | PASS | 1; Allowed extension behavior is computed and required processing preserved |
| Unknown observation versus physical mode | PASS | 1; No default physical mode or fabricated negative fact |
| DEFECT-02 mode evidence consistency | PASS | 6; Four contradictory observations, one stale contradiction, one agreed physical/observed mode conflicting with claim; none falsely passes |
| DEFECT-03 extras requires every role | PASS | 27; 24 individual state/process corruptions across 8 rows plus all 3 required membership losses; EXTRAS itself must fail |
| Regulator role differs from update link | PASS | 1; Wrong local gate state in a no-change context: role and extras fail while influence link remains true |
| No interval PASS from finite points | PASS | 1; Whole-interval proof handler absent in this finite profile |
| No vacuous finite claim | PASS | 1; Empty claimed point set rejected |
| Build/governance bindings | PASS | 2; Both actual bindings compared with submitted fields |
| Member and role witnesses | PASS | 3; Each required role loses realization when its registered constituent is removed |
| Abstract empty bridge | PASS | 1; Explicit abstract fixture has no P0 effects; does not certify NNNC |
| Operational empty-event binding | PASS | 3; Zero/one/two canonical logical bindings; registration independent of event count |
| Finite bridge correspondence fixture | PASS | 2; Equal/mismatched envelopes; not complete deployed refinement |
| Append and reference | PASS | 5; Valid, orphan, future-parent, unrelated-family and duplicate-ID cases |
| Complete role/link coverage | PASS | 5; 3 roles and 2 links; 4 memory and 2 effective regulator intervention pairs |
| Context and joint configurations | PASS | 3; Different witnesses by context and jointly sufficient configuration |
| Redundant alternatives | PASS | 4; Single removals preserve relation, joint removal distinguishes |
| D1 native source preserved | PASS | 1; e1e1eb0873ee3b6ae912c23dfa213620c8279d0aed025ce09bf6744db6cd6cb6 |
| D2 native source preserved | PASS | 1; ee3de2df568d38e78568a60a1785a881b7cf119dec632e035b50541c4ccd05c6 |
| DEFECT-01 corrected D1 destinations | PASS | 4; Four closing-review register rows checked verbatim against current D2 structure |
| Self-contained current VO and test tables | PASS | 18; Current D2 explicitly contains six VO rows and twelve control specifications |
| Mandatory floor unchanged | PASS | 1; Exact native 18-slot expression |
| Individual AC routes retained | PASS | 26; 26 available source cases; older missing archive remains OPEN |

Coverage: memory, selector and regulator each have registered role witnesses computed over all eight cases. The regulator role checks its local enable/inhibit state independently of the regulator-update causal link. Memory-to-selection has four controlled intervention pairs; regulation-to-update has two effective pairs (four involved transitions). Every required role/link is recorded in ROLE-LINK-COVERAGE.json. The positive finite protocol computes all 14 item verdicts. Its policy/approval environment is simulated, not real architect authority or a discharge of VO-21/22. All real-domain and whole-interval claims need their own established assurance. The targeted closing fixes are recorded in CLOSING-ACCEPTANCE-RECORD.md; the source, results, coverage and final-byte hashes accompany the issue.

**END OF CURRENT ACCEPTANCE CANDIDATE — NOT ADOPTED**

<!-- END EXACT ADOPTED CANDIDATE -->
