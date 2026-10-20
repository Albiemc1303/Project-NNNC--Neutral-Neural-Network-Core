# PROJECT NNNC — NEUTRAL NEURAL NETWORK CORE
## Phase 1 — Foundational Ontology
### Document 2 of 2 — Mathematical Formalization and Verification Contract

| Control | Value |
|---|---|
| Identifier | NNNC-P1-D2 |
| Revision | v0.2.1 — Targeted mathematical correction candidate |
| Status | PROPOSED; incorporates four bounded v0.1 peer reviews; not formally proved or executed |
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
