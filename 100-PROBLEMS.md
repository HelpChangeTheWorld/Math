# Math Frontiers: continuation ledger for the original 100 targets

Reconstructed from `Math_Frontiers_Work_Round_2.md` (dated 11 September 2026), read in full on 20 October 2026. These are the original catalog entries; they are not a replacement list.

## How to interpret this ledger

The status column repeats the prior record's assessment of its bounded attempt. It is neither a current literature-status audit of the parent problem nor a fresh validation of the old calculation. Each result remains limited to its stated model. The earlier report expressly states that no major catalog conjecture and no novelty claim was established.

New work on #49 and #81 supersedes their older next decisions when explicitly documented in the continuation report. In particular, a fixed common variable order and a class containing every order are different sampler models. A support valid for one must not be presented as a guarantee for the other.

## Prior attempt classifications

- Attempt remains unresolved: 2.
- Finite computation verified: 47.
- Restricted statement proved: 33.
- Attempted approach failed: 18.

## Reusable protocol

1. State the exact parent problem and the narrower quantified claim.
2. Freeze the mathematical model, admissible objects, arithmetic, input conventions, and criterion for failure.
3. Check current primary literature and compare with the strongest relevant known result.
4. Reproduce a known positive control and a deliberately invalid negative control.
5. Execute a bounded search or calculation; preserve exact inputs, outputs, and a verifier.
6. Search for counterexamples with a separately implemented procedure.
7. Convert the finite pattern into a precise lemma, or identify exactly why the proposed lemma fails.
8. Keep the bridge to the parent problem explicit; finite checks cannot silently supply a universal implication.
9. Stop a defeated method until a substantive new mechanism is stated.
10. Report the status of the claim, proof, computation, novelty, and external review separately.

## Current primary workstreams

- **#49 — sign-sequence extension:** the length-seven to length-nine exhaustive test now has maximum minimum repair radius three over all 336,140 valid normalized ordered parents. Twelve parents need three changes, so a universal one- or two-change rule fails in this finite model. Next: explain the obstruction and the three-change repair structurally, then state a precise longer-length claim; do not infer a uniform bound from one length.
- **#81 — samplers:** the fixed-common-order six-bit optimum is eight, using the stated bit convention and 18,664 functions. For the larger class allowing every variable order, a direct reconstructed lower-bound proof excludes every support size one through eleven; at least twelve are necessary. A complete all-order class contains 1,156,000 functions. Twelve-point sufficiency remains unresolved: bounded search did not find a passing construction, and no impossibility certificate was obtained. Next: construct and verify twelve points, or produce a valid size-twelve infeasibility certificate.
- **#93 — matrix multiplication:** all 211,876 four-to-three local replacements in the explicit standard 49-term Strassen square are impossible, with every certificate independently recomputed. Literature shows this successful reproduction is weaker than an existing reported eight-term border-rank barrier. Next: compare with that proof and known 48-term algorithms, and investigate a replacement changing at least nine complete original summands or another mechanism. The nine-change floor is necessary, not sufficient.

## Source refresh and new bounded checks on 20 October 2026

### #49 — Hadamard construction

The active target is the sign-sequence extension mechanism. The old finite order 668 should not be treated as an unresolved target: Epoch AI’s current solution update reports constructions for that order and all previously unknown admissible orders through 2000, while the general Hadamard conjecture remains open. The page’s old About text still says 668 is unknown, so its newer Solution update takes precedence. We have not independently validated those external matrices. Source: https://epoch.ai/frontiermath/open-problems/hadamard (accessed 20 October 2026).

The current root-agent experiment enumerated 336,140 valid normalized ordered length-seven complementary parents. The minimum sign-repair counts before an append-only length-nine extension were 0:259,844; 1:73,644; 2:2,640; 3:12. This closes that finite repair-radius test at three. It does not imply that the repair radius remains bounded at arbitrary lengths. See the separate `hadamard_audit/` evidence for the precise normalization, code, and witness data.

### #81 — fixed order and every order are distinct verified models

The fixed-order candidate is `S={0,4,13,14,26,31,33,35}` when `x1` is the most significant bit. Its exact optimum is eight in the fixed common order class. The larger class permits each program to use its own fixed variable order; the lower-bound argument rules out support sizes one through eleven individually, rather than inferring a monotone cardinality property. Its mathematical proof is in `proof_review/independent_lower_bound_proof.md`, with the 1,800-function and 20,475-case checks reproduced in the current run. Twelve-point feasibility is still unknown after the bounded search. Neither finite sampler model resolves P versus BPP, and originality remains unestablished.

### #93 — Matrix multiplication

The newly executed standard Strassen-square audit certifies all 211,876 four-term subtensors have flattening rank four. A second determinant implementation checked every certificate. Thus four fixed summands cannot be replaced by three while the other 45 complete summands remain unchanged.

A literature check then found this is a weaker instance of an existing reported theorem: Agarwal’s September 2026 preprint states border radius at least eight for the same standard 49-term Strassen Kronecker square. That is stronger than the newly reproduced four-term obstruction. It follows that further five-, six-, seven-, or eight-term scans would be benchmark reproduction, not a new advance under that theorem. See https://arxiv.org/html/2609.13596v1, Introduction, the paragraph on the 49-term Kronecker square. We have not reverified the full external theorem.

Rational 48-multiplication algorithms for 4×4 matrices already exist; 49 is not a global optimum. See Dumas–Pernet–Sedoglavic, https://arxiv.org/abs/2506.13242. The next useful decision is to compare against those 48-term constructions and the existing eight-term local barrier, then specify a replacement involving at least nine original complete summands or another structurally different approach. No new tensor-rank lower bound or matrix-multiplication exponent result has been established.

## Every original target and its next obligation

The prior status labels remain historical. Next actions for the three active tracks (#49, #81, #93) are updated below; the other 97 actions are the recorded obligations awaiting their next source and proof audit.

| # | Parent target | Prior bounded-attempt label | Next obligation |
|---:|---|---|---|
| 1 | Riemann hypothesis | Attempt remains unresolved | Keep the reflection stabilization; obtain rigorous enclosures before claiming a Rouché certificate. The numerical success does not prove RH. |
| 2 | P versus NP | Finite computation verified | Reject any order-independent high-width claim for these examples; retain the exact pair formula as an implementation control. |
| 3 | Birch and Swinnerton-Dyer conjecture | Restricted statement proved | Use torsion order 4 as one independently audited denominator input, then separately establish the still-missing BSD quantities. |
| 4 | Hodge conjecture | Restricted statement proved | Retain this fully explicit basis as the calibration; any extension must name a genuinely missing cycle construction. |
| 5 | Yang–Mills existence and mass gap | Restricted statement proved | Require explicit scaling and volume-uniform control in the selected gauge-theory estimate before interpreting its positive finite gap. |
| 6 | Collatz conjecture | Finite computation verified | Keep the exact branch inventory; require an adaptive covering argument before expanding the modulus. |
| 7 | Goldbach conjecture | Finite computation verified | Use the exported normalization controls to specify the missing residual inequality before another count scan. |
| 8 | Twin prime conjecture | Attempted approach failed | Park these tapers. Require a substantive structural change and a composite-mass argument before further tuning. |
| 9 | Legendre’s conjecture | Finite computation verified | Retain explicit prime-power subtraction in any positivity claim; compare kernels only after the analytic remainder is specified. |
| 10 | Landau’s n²+1 problem | Finite computation verified | Keep local obstructions explicit; do not infer control of b=1 from an average over several lines. |
| 11 | Infinitely many Mersenne primes | Finite computation verified | Use the missed composites as mandatory controls and stop interpreting a survivor count as a prime count. |
| 12 | Odd perfect number problem | Restricted statement proved | Use this certificate as a verified pruning rule; require complete branch hypotheses before compressing other chains. |
| 13 | Beal conjecture | Attempted approach failed | Stop adding isolated small moduli; identify a genuine global restriction excluding this local-survival mechanism. |
| 14 | Erdős–Moser conjecture | Restricted statement proved | Use the identities as exact controls for future congruence tables, and seek an argument that survives variable k. |
| 15 | Bunyakovsky conjecture | Finite computation verified | Retain the composite survivors as adversarial examples; require an explicit global statistic before fitting any classifier. |
| 16 | Bateman–Horn conjecture | Finite computation verified | Separate truncation sensitivity from count discrepancies before selecting a fixed pair for further analysis. |
| 17 | Artin’s primitive root conjecture | Finite computation verified | Use the explicit large-index failures to test any proposed truncation lemma rather than assuming small obstructions suffice. |
| 18 | Elliott–Halberstam conjecture | Finite computation verified | Keep all modulus bands and prime powers in subsequent formulas; derive a dispersion estimate before interpreting band sizes asymptotically. |
| 19 | Chowla’s conjecture | Attempted approach failed | Abandon monotonic improvement as a premise; any new conditional cancellation estimate must state and justify additional hypotheses. |
| 20 | Lindelöf hypothesis | Restricted statement proved | Demand independently proved zeta derivative or peak-width control before using a moment-to-pointwise argument. |
| 21 | Vinogradov’s least quadratic nonresidue conjecture | Finite computation verified | Keep the cancellation inequality as the explicit missing step; reject expansion-only arguments that pass these negative controls. |
| 22 | Lehmer’s conjecture on Ramanujan’s tau function | Finite computation verified | Use the three surviving primes to audit any additional filter and attach a valid theorem to each exclusion. |
| 23 | Lang–Trotter conjecture | Restricted statement proved | Use these genuine groups as baselines, then certify the next modular image before fitting trace predictions. |
| 24 | Leopoldt’s conjecture | Restricted statement proved | Use the nonzero valuation as a precision-control example before attempting the planned cubic fields. |
| 25 | Lehmer’s Mahler measure problem | Restricted statement proved | Require every auxiliary-resultant inequality to accommodate the cubic control before broader enumeration. |
| 26 | Lehmer’s totient problem | Finite computation verified | Use the full census as an oracle for future interval-pruning rules; require preservation of every positive control. |
| 27 | Carmichael’s totient conjecture | Finite computation verified | Use uncovered substitution patterns within these complete fibers to formulate one exact additional identity. |
| 28 | Zaremba’s conjecture | Finite computation verified | Keep the witness table as calibration and demand a symbolic denominator-preserving identity before proposing a repair mechanism. |
| 29 | Schanuel’s conjecture | Finite computation verified | Record these exclusions as calibration and seek a uniform symbolic argument before increasing polynomial cutoffs. |
| 30 | Four exponentials conjecture | Finite computation verified | Use the smallest determinant to test any proposed quantitative inequality, keeping its independence hypotheses explicit. |
| 31 | Irrationality of Euler’s constant | Restricted statement proved | Reject decimal accuracy as the objective; require an explicit construction that controls both denominators and residual logarithms. |
| 32 | Normality of π | Attempted approach failed | Abandon strict monotonicity and require a quantitatively justified error allowance in any future scale inequality. |
| 33 | Hadwiger’s conjecture | Attempted approach failed | Require any identification-transfer rule to use the chromatic hypothesis explicitly; do not promote arbitrary certificate transport to a lemma. |
| 34 | Erdős–Hajnal conjecture | Finite computation verified | Retain the non-dominated witness when testing strengthened structural claims; it shows why the anticomplete alternative is necessary. |
| 35 | Gyárfás–Sumner conjecture | Attempted approach failed | A usable absence certificate must exclude every possible root or justify a complete root-selection reduction. |
| 36 | Graph reconstruction conjecture | Finite computation verified | Use the verified deck table to check any future alignment procedure, especially its treatment of repeated cards. |
| 37 | Union-closed sets conjecture | Finite computation verified | Treat disjoint-block structure as a finite equality pattern requiring a separate general proof, not as an established classification at arbitrary size. |
| 38 | Caccetta–Häggkvist conjecture | Finite computation verified | Any proposed modular counting explanation must state where it uses translation symmetry before attempting extension to arbitrary neighborhoods. |
| 39 | Barnette’s conjecture | Finite computation verified | Analyze the successful prism exchanges for an explicit structural lemma before extrapolating this behavior to other planar cubic graphs. |
| 40 | Lovász’s Hamiltonian-path conjecture | Attempted approach failed | Permit orbit re-entry or prove existence of a suitable subgroup; endpoint matching alone cannot repair disconnected fibers. |
| 41 | Rota’s basis conjecture | Finite computation verified | Do not assume strict one-step descent. Any broader exchange argument must explain plateau navigation and its dependence on rank. |
| 42 | Hadwiger–Nelson problem | Finite computation verified | Require future imported modules to pass the same exact geometry and coloring checks before attempting five-color obstruction gluing. |
| 43 | Planar unit-distance problem: exact growth | Finite computation verified | Optimize R(A), then rescale its maximizing distance. Keep actual construction feasibility separate from this successful statistic calibration. |
| 44 | Hadwiger–Boltyanski illumination conjecture | Finite computation verified | Use these exact controls to distinguish geometric illumination failures from incompleteness of a future direction dictionary. |
| 45 | Lonely runner conjecture | Finite computation verified | Replace broad uniform speed sampling with explicitly structured tight families before interpreting arithmetic predictors. |
| 46 | 1/3–2/3 conjecture | Attempted approach failed | Discard this signature as a sufficient classifier; a stronger criterion must capture order information that distinguishes the witness pairs. |
| 47 | Erdős–Szekeres convex-polygon conjecture | Finite computation verified | Require the future orientation model to reproduce these positive and negative controls before attempting the seven-gon instance. |
| 48 | Conway’s thrackle conjecture | Finite computation verified | Keep these as crossing-rule controls; do not generalize the finite convex-cycle result to arbitrary thrackle drawings. |
| 49 | Hadamard matrix conjecture | Finite computation verified | Explain why 12 of the 336,140 normalized length-seven parents need three sign changes before extension to length nine, and why three suffice for all at that length. State and challenge the next longer-length claim; no arbitrary-length theorem follows. |
| 50 | Turán’s tetrahedron problem | Finite computation verified | Any stronger certificate must use additional consistency or positivity constraints; the enumerated edge-count table alone is insufficient. |
| 51 | Ryser’s hypergraph conjecture | Attempted approach failed | Abandon single-edge replacement for this seed; changing the neighborhood requires preserving matching number by a different explicit mechanism. |
| 52 | Ryser’s Latin-square transversal conjecture | Restricted statement proved | Retire cyclic near-transversals as exchange benchmarks; future tests need squares without this automatic completion identity. |
| 53 | Tutte’s 5-flow conjecture | Attempted approach failed | Permit controlled potential increases or change the move set; a proof cannot rely on unrestricted monotone coordinate descent. |
| 54 | Conway’s 99-graph problem | Restricted statement proved | Encode the full block system without extra symmetry restrictions; retain the rook instance as the positive control. |
| 55 | Tutte’s 3-flow conjecture | Finite computation verified | Separate failures of a chosen outdegree assignment from graph-level failure; a general argument still needs a complete structural reduction. |
| 56 | Smooth four-dimensional Poincaré conjecture | Restricted statement proved | Retain this calibration; a candidate-specific proof needs an actual handle description and justified simplifications. |
| 57 | Smooth four-dimensional Schoenflies conjecture | Restricted statement proved | Use these maps to validate boundary conventions before attempting a nonstandard embedding. |
| 58 | Andrews–Curtis conjecture | Finite computation verified | The move checker is ready; the next substantive input must be an independently specified candidate presentation. |
| 59 | Slice–ribbon conjecture | Restricted statement proved | Move to a specified slice knot only after its slicing certificate and diagram are available. |
| 60 | Crossing-number additivity conjecture | Restricted statement proved | Retain this exact control; a wider proof needs a lower bound effective when Jones breadth is deficient. |
| 61 | Purely cosmetic surgery conjecture for knots in the three-sphere | Finite computation verified | Apply stronger surgery invariants only to surviving pairs for a specified knot. |
| 62 | Volume conjecture | Attempt remains unresolved | Use this normalization control before evaluating a new knot; do not extrapolate a proof from the trend. |
| 63 | 11/8 conjecture | Restricted statement proved | Any realizability investigation must first apply the strongest known form-specific obstructions. |
| 64 | Borel rigidity conjecture | Restricted statement proved | Keep the lift argument as a control; the missing step is geometric identification of a general source manifold. |
| 65 | Novikov conjecture | Restricted statement proved | Any extension must address those higher characteristic classes rather than reuse dimension-two vanishing. |
| 66 | Farrell–Jones conjecture | Restricted statement proved | A nontrivial next attempt needs a specified group for which E_VCyc(G) is not already a point. |
| 67 | Inverse Galois problem over the rational numbers | Restricted statement proved | Use this example to validate a Galois-group certificate format before choosing a genuinely unresolved group-realization target. |
| 68 | Tate conjecture | Restricted statement proved | A non-split surface requires actual Frobenius and cycle calculations instead of this product argument. |
| 69 | Lefschetz standard conjecture | Restricted statement proved | Retain the correspondence certificate; extending to other varieties requires analogous algebraic inverse operators. |
| 70 | Abundance conjecture | Restricted statement proved | Use the exact count as a control; a non-product nef canonical divisor needs a different semiampleness argument. |
| 71 | Termination of flips conjecture | Attempted approach failed | A proposed geometric measure must also have a proved well-founded value set or another finite-descent mechanism. |
| 72 | Nagata’s conjecture on plane curves | Finite computation verified | Keep the exact minors; future work must introduce an argument controlling unbounded multiplicity. |
| 73 | Segre–Harbourne–Gimigliano–Hirschowitz conjecture | Finite computation verified | Use these positive and negative controls before interpreting a rank defect in a broader mixed system. |
| 74 | Hopf’s positive-curvature Euler-characteristic conjecture | Restricted statement proved | A broader argument must control the full curvature tensor in the Euler polynomial. |
| 75 | Hopf’s S2 × S2 problem | Restricted statement proved | Discard this conformal search family as a route to a positively curved counterexample. |
| 76 | Chern’s isoparametric conjecture for minimal hypersurfaces | Attempted approach failed | Any repaired argument must use constraints beyond this verified first-derivative system. |
| 77 | Symmetric Mahler conjecture in dimensions four and higher | Restricted statement proved | Remove this family from counterexample searches; a wider proof needs control beyond its special diagonal symmetry. |
| 78 | Zariski cancellation problem in characteristic zero | Attempted approach failed | A canonical invariant must account for all relevant derivations or extra justified structure. |
| 79 | Bounded negativity conjecture in characteristic zero | Restricted statement proved | Further attempts must seek an unbounded sequence on this same fixed surface, not move the ambient surface. |
| 80 | Four-dimensional sphere-packing problem | Restricted statement proved | Exclude this displacement path from improvement searches; different finite deformations require new certificates. |
| 81 | P versus BPP | Finite computation verified | Fixed common order: exact optimum 8. Every-order class: all supports of sizes 1–11 ruled out. Find a 12-point all-order sampler and verify all 1,156,000 functions, or produce an exact size-12 infeasibility certificate. Twelve-point sufficiency remains unresolved. |
| 82 | NP versus coNP | Finite computation verified | Determine which separator restrictions yield a provable sharing bound before extending the input family. |
| 83 | L versus NL | Restricted statement proved | Preserve the proven layered algorithm and specify what additional information would represent within-layer and backward reachability. |
| 84 | L versus BPL | Finite computation verified | Account for storage and recomputation costs before turning the error recurrence into a space-bounded algorithm. |
| 85 | P versus PSPACE | Finite computation verified | Construct an explicit adversarial family and derive its diagram-size recurrence before claiming an efficient general QBF method. |
| 86 | Existence of one-way functions | Finite computation verified | Analyze how the optimum changes with group order and query budget while preserving the same explicit oracle semantics. |
| 87 | Deterministic polynomial identity testing | Finite computation verified | Require a uniform cost bound for any proposed smaller substitution before counting common-factor examples as an efficiency improvement. |
| 88 | VP versus VNP | Attempted approach failed | Abandon raw flattening rank as an unrestricted circuit-size bound and test any replacement measure against reuse and products first. |
| 89 | Efficient classical integer factoring | Attempted approach failed | Select an explicit partial-information lattice theorem and compare its total cost with this fully charged enumeration control. |
| 90 | Polynomial-time graph isomorphism | Finite computation verified | Find a pair sharing this invariant to identify the next concrete information the proposed method would need. |
| 91 | Unique Games Conjecture | Finite computation verified | Use the saved optima to validate a precisely encoded SDP and distinguish numerical outputs from certified bounds. |
| 92 | Quantum PCP conjecture | Restricted statement proved | Determine the locality and promise-gap behavior under repeated application before proposing amplification of hard instances. |
| 93 | Matrix multiplication exponent | Restricted statement proved | The new four-to-three obstruction is a successful reproduction subsumed by a reported stronger eight-term barrier. Review that theorem and known rational 48-term algorithms before searching changes to at least nine original complete summands; nine is a necessary floor, not a proven sufficient move size. |
| 94 | Exponential Time Hypothesis | Attempted approach failed | Redesign the potential and prove its change symbolically for all permitted branch types before fitting a recurrence. |
| 95 | Planted clique conjecture | Finite computation verified | Use the derived signal-to-noise scaling to decide whether these baseline statistics merit a larger preregistered study. |
| 96 | Mandelbrot local-connectivity conjecture | Attempted approach failed | Identify a justified nonsummable modulus estimate for the proposed extension and retain a separate parameter-transfer proof obligation. |
| 97 | Density of hyperbolicity for complex quadratic polynomials | Finite computation verified | Preserve these exact certificates as controls when extending the search to higher periods or nearby unclassified parameters. |
| 98 | Furstenberg's ×2, ×3 measure conjecture | Attempted approach failed | Seek a mechanism forcing positive-density Fourier information or another stronger constraint, rather than repeating sparse-orbit counting. |
| 99 | Brennan's conjecture | Finite computation verified | Identify a concrete multiscale domain where summing the verified local contributions introduces a new controllable difficulty. |
| 100 | Hilbert's sixteenth problem, limit-cycle part | Restricted statement proved | Test and then prove simplicity or controlled multiplicity of the interior zero before interpreting it as a cycle bifurcation. |

## Execution discipline

The next obligation is a mathematical dependency, not a promise that another scan will solve the parent problem. Some entries need a concrete candidate, an exact source identity, a new inequality, or a new invariant before further computing is informative. Those inputs should be specified before increasing resource budgets.

The current local work uses parallel AI agents with separately assigned checks. This is not a claim of review by human mathematicians or formal proof-assistant certification.
