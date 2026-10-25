# Math Frontiers — Work Round 2

Actual mathematical attempts for all 100 catalog targets

**Date:** 11 September 2026. **Team:** the simulated research team, with computations and reviews performed within this AI workflow.

This round contains 100 bounded attempts: explicit arguments, exact finite enumerations, numerical experiments, and counterexamples to proposed methods. Each entry states what was attempted, what was obtained, its evidence, its precise limit, and the next decision. A completed entry means that a bounded attempt was performed; it does not mean its parent conjecture was solved.

**No major catalog conjecture has been resolved by this work, and no claim of previously unknown mathematics has been established.** Several smaller questions posed in the earlier round now have exact answers. Some other entries reproduce established special cases to test whether a proposed method actually has purchase.

## Results that change the next move

- **#81: the six-bit sampler optimum is exactly 8.** We found eight inputs whose uniform average has error at most 1/4 against every Boolean function computed by the specified ordered, width-two program. Two different enumeration methods agree on all 18,664 functions, and exact arithmetic verifies the candidate. An elementary affine-parity argument excludes every support of seven or fewer points. This repairs the previous product construction, which failed its six-bit test.
- **#93: every local three-to-two replacement is impossible in the tested construction.** All 18,424 triples in the fixed 49-term Strassen tensor-square decomposition have tensor rank exactly three. A separate audit saved a direct nonzero 3×3 flattening minor for each triple. With the other 46 terms fixed, even unrestricted rational or complex coefficients cannot compress a selected triple to two terms. Larger changes and other decompositions remain available.
- **#49: every valid normalized parent in the finite extension test extends.** All 108 valid length-three periodically complementary quadruples have a length-five extension in the prescribed append model. This resolves that finite test and supplies witnesses; it does not produce Hadamard matrices at every required order.
- **#53: the proposed descent rule has a certified trap.** At an explicit cube coefficient vector, every single-coordinate ±1 move increases the defect, even without a coefficient-box restriction. A saved escape path reaches a valid flow with a maximum defect of two, from an initial defect of one. The exact required barrier increase is one for this move rule; a general monotone-descent argument using it fails.
- **#100: the selected first-order perturbation has an interior Melnikov zero.** Exact endpoint integrals are 6/5 and 6/35, so the ratio moves from zero near the center to 1/7 at the separatrix. Continuity gives an interior ratio of 1/10. A simple zero, an actual perturbed cycle, and a global cycle bound have not been established.

## Coverage and meaning of the labels

| Label | Entries | What the label establishes |
|:--|--:|:--|
| Finite computation verified | 47 | An exact finite calculation for the stated model; no extension beyond that model is implied. |
| Restricted statement proved | 33 | A displayed argument for a special case or obstruction, often using established theorems; novelty is unclaimed. |
| Attempted approach failed | 18 | A calculation or witness defeats the particular attempted method or benchmark. |
| Attempt remains unresolved | 2 | An actual attempt was made, but the claimed implication or a rigorous certificate remains missing. |

The labels describe different types of output, not a ranking of conjectures by tractability. Counts do not measure new discoveries. Numerical observations are identified where they occur. The separate checks of #81, #93, and #100 used other members of this same AI workflow; they are not external peer review or proof-assistant certification.

## All 100 work records

Evidence filenames refer to files in the accompanying research archive. Source links provide mathematical background; they do not endorse the new calculations or establish their novelty.

### 1. Riemann hypothesis

**Status:** Attempt remains unresolved

**Attempt performed.** Computed completed-zeta values on 512 rectangle-boundary samples and degree 8–24 polynomial approximations using 128 Cauchy-circle samples, Euler–Maclaurin zeta, and Lanczos gamma.

**Result.** Sampled winding is 1. Direct-circle degree 24 error stalled near 7.24e-4; using xi(s)=xi(1−s) on the left half-plane reduced sampled error to 9.87e-16. Sampled minimum |xi| is 3.67e-5.

**Evidence.** `captain_riemann.json`; `captain_verify_and_refine.py`

**Limit.** All are double-precision observations. No uniform remainder, rounding enclosure, continuous-boundary bound, or certified zero count was obtained.

**Next decision.** Keep the reflection stabilization; obtain rigorous enclosures before claiming a Rouché certificate. The numerical success does not prove RH.

**Background.** [Background source 1](https://dlmf.nist.gov/25.2); [Background source 2](https://www.claymath.org/millennium/riemann-hypothesis/)

### 2. P versus NP

**Status:** Finite computation verified

**Attempt performed.** Exhausted all 40,320 variable orders for each of three eight-variable functions, with exact residual truth tables at every cut.

**Result.** Parity always has maximum width 2. Equality of four-bit blocks and conjunction of four paired disjunctions both have minimum maximum-width 3 and maximum 16; only 384 orders attain 3. Independently checked width=2^s+1_{c>0} on 512 masks, where s counts split pairs and c completed pairs.

**Evidence.** `captain_pnp.json`; `captain_verification.json`; `captain_calculations.py`

**Limit.** These are restricted ordered representations and finite calibration results, not lower bounds for unrestricted computation or claims of novelty.

**Next decision.** Reject any order-independent high-width claim for these examples; retain the exact pair formula as an implementation control.

**Background.** [Background source 1](https://www.claymath.org/millennium/p-vs-np/)

### 3. Birch and Swinnerton-Dyer conjecture

**Status:** Restricted statement proved

**Attempt performed.** Audited E:y²=x³−x with exact Weierstrass invariants, Nagell–Lutz torsion constraints, and point counts at four good primes.

**Result.** Discriminant 64 and c4=48 give j=1728. Nagell–Lutz reduces nonzero-y torsion to |y|≤2; exact substitution leaves only (−1,0),(0,0),(1,0). Including infinity, rational torsion is Z/2×Z/2.

**Evidence.** `captain_bsd.json`; `captain_calculations.py`

**Limit.** The torsion conclusion uses the standard Nagell–Lutz theorem. No rank, Sha, real period, Tamagawa factor, or L-function leading coefficient was computed; BSD was not assumed.

**Next decision.** Use torsion order 4 as one independently audited denominator input, then separately establish the still-missing BSD quantities.

**Background.** [Background source 1](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/)

### 4. Hodge conjecture

**Status:** Restricted statement proved

**Attempt performed.** Calculated intersections of the two fibers, diagonal, and graph of multiplication by i on E×E, for E:y²=x³−x.

**Result.** The exact matrix is [[0,1,1,1],[1,0,1,1],[1,1,0,2],[1,1,2,0]], with determinant −4. The final intersection 2 equals deg(i−1). Four independent rational divisor classes therefore span the rational(1,1) subspace, whose dimension is at most the complex Hodge number 4.

**Evidence.** `captain_hodge.json`; `captain_calculations.py`

**Limit.** This reproduces the established divisor case on one abelian surface; it neither establishes novelty nor constructs higher-codimension cycles generally.

**Next decision.** Retain this fully explicit basis as the calibration; any extension must name a genuinely missing cycle construction.

**Background.** [Background source 1](https://www.claymath.org/millennium/hodge-conjecture/)

### 5. Yang–Mills existence and mass gap

**Status:** Restricted statement proved

**Attempt performed.** Diagonalized the periodic one-particle Hamiltonian Hf(j)=[2f(j)−f(j−1)−f(j+1)]/a² exactly using Fourier modes, and tracked its gap through two limits.

**Result.** Eigenvalues are 4a^(−2)sin²(πk/N), so every finite N≥3 has positive gap 4a^(−2)sin²(π/N). At fixed spacing it vanishes as N→∞. At fixed physical length L=Na it approaches 4π²/L², which then vanishes as L→∞.

**Evidence.** `captain_gap.json`; `captain_calculations.py`

**Limit.** This is a toy quantum Hamiltonian, not a gauge theory or a Yang–Mills construction. It demonstrates why finite positivity cannot by itself certify an infinite-volume mass gap.

**Next decision.** Require explicit scaling and volume-uniform control in the selected gauge-theory estimate before interpreting its positive finite gap.

**Background.** [Background source 1](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)

### 6. Collatz conjecture

**Status:** Finite computation verified

**Attempt performed.** Executed all 4096 residue classes for twelve steps of the one-division shortcut S; derived each affine numerator and checked three positive representatives independently.

**Result.** All 12288 checks passed. In exactly 3302 classes, sufficiently large starting integers decrease at step twelve; 794 classes have no descent at that step. The largest integer threshold is 35, and contracting classes contain only two finite non-descending representatives.

**Evidence.** number_compute.py; number_6.json; S^12(n)=(3^a n+b)/4096; descent requires (4096−3^a)n>b.

**Limit.** This classifies a fixed twelve-step operation. It does not show that every trajectory eventually enters a descending class.

**Next decision.** Keep the exact branch inventory; require an adaptive covering argument before expanding the modulus.

**Background.** [Background source 1](https://arxiv.org/abs/1909.03562)

### 7. Goldbach conjecture

**Status:** Finite computation verified

**Attempt performed.** Reduced the proposed range to N≤2000 and computed exact ordered Goldbach counts for every even N, plus six worked local-factor comparisons.

**Result.** All 999 even integers had a representation. Among N≥1000 the minimum ordered count was 32. For example R(1000)=56 and R(1260)=136; their local products through prime seven are respectively 175/96 and 35/8.

**Evidence.** number_compute.py; number_7.json

**Limit.** No logarithmic-integral residual, smoothing kernel, or uniform error estimate was computed; the original cutoff was 200000.

**Next decision.** Use the exported normalization controls to specify the missing residual inequality before another count scan.

**Background.** [Background source 1](https://t5k.org/notes/conjectures/)

### 8. Twin prime conjecture

**Status:** Attempted approach failed

**Attempt performed.** Executed all three rational divisor tapers at R=30 and 100 on both prescribed intervals, with exact weight numerators, prime labels, and prime-factor-count bins.

**Result.** Every taper lost to the simple coprimality wheel on both intervals. The best taper assigned prime pairs about 7.94% of its initial mass and 5.83% of its holdout mass; the wheel achieved 17% and 249/1999, about 12.46%. All six improved on uniform weighting, but none improved the stronger baseline.

**Evidence.** number_compute.py; number_8.json

**Limit.** This rejects this finite taper family as a promising enrichment improvement, not weighted sieves or the twin-prime conjecture.

**Next decision.** Park these tapers. Require a substantive structural change and a composite-mass argument before further tuning.

**Background.** [Background source 1](https://arxiv.org/abs/math/0508185)

### 9. Legendre’s conjecture

**Status:** Finite computation verified

**Attempt performed.** Integrated the three polynomial kernels exactly, computed their squared derivative norms, and checked prime counts in the first 200 square intervals.

**Result.** All normalizations equal one; derivative energies are 120/7, 280/11, and 5040/143. Every checked interval contains a prime. In (25,36), the composite prime power 27 contributes log(3) times the kernel value to a von Mangoldt sum; for the first kernel that coefficient is 9720/14641.

**Evidence.** number_compute.py; number_9.json

**Limit.** The 200-interval census is smaller than proposed and supplies no short-interval zeta-zero estimate.

**Next decision.** Retain explicit prime-power subtraction in any positivity claim; compare kernels only after the analytic remainder is specified.

**Background.** [Background source 1](https://t5k.org/notes/conjectures/)

### 10. Landau’s n²+1 problem

**Status:** Finite computation verified

**Attempt performed.** Counted prime norms n²+b² exactly for n≤2000 on five Gaussian-integer lines, with root counts modulo primes through 31 and common-factor controls.

**Result.** For b=1,2,3,4,8, the prime counts were 209,217,144,218,213. All 1000 inputs sharing a factor with b=2,4,8 were composite; the same held for 666 such inputs at b=3. Local root counts differ between lines as expected.

**Evidence.** number_compute.py; number_10.json

**Limit.** The original cutoff was 20000. These are line counts, not a uniform strip estimate or an infinite prime-value result.

**Next decision.** Keep local obstructions explicit; do not infer control of b=1 from an average over several lines.

**Background.** [Background source 1](https://arxiv.org/abs/1807.08899)

### 11. Infinitely many Mersenne primes

**Status:** Finite computation verified

**Attempt performed.** Ran Lucas–Lehmer at all 31 prime exponents through 127 and compared it with every proper prime trial factor at most 1000.

**Result.** Twelve exponents passed the complete primality criterion. Twelve composite Mersenne numbers nevertheless survived the bounded factor sieve, beginning at exponent 41; the missed exponents are listed exactly. Thus bounded factor survival demonstrably fails as a primality surrogate on this reduced sample.

**Evidence.** number_compute.py; number_11.json

**Limit.** The proposed limits 1000 and one million were reduced to 127 and 1000 respectively; no divisor-tail bound was obtained.

**Next decision.** Use the missed composites as mandatory controls and stop interpreting a survivor count as a prime count.

**Background.** [Background source 1](https://t5k.org/mersenne/)

### 12. Odd perfect number problem

**Status:** Restricted statement proved

**Attempt performed.** Derived and checked an exact abundancy pruning certificate and factored four successive divisor sums under explicitly chosen exponent-two assumptions.

**Result.** For d=3²5²7²=11025, σ(d)=22971>22050=2d. Since σ(N)/N≥σ(d)/d whenever d divides N, no perfect N can contain this divisor. The separate conditional chain begins σ(3²)=13 and σ(13²)=3·61; its exponent choices remain visible.

**Evidence.** number_compute.py; number_12.json

**Limit.** This is an established local exclusion, not a complete factor-chain search. Other exponents and the special Euler prime are untouched.

**Next decision.** Use this certificate as a verified pruning rule; require complete branch hypotheses before compressing other chains.

**Background.** [Background source 1](https://arxiv.org/abs/2607.19746)

### 13. Beal conjecture

**Status:** Attempted approach failed

**Attempt performed.** Constructed one pairwise-coprime positive triple satisfying every proposed modulus for every exponent triple from three through seven, then checked all 750 congruences.

**Result.** With M=10810800, take A=M, B=M+1, C=2M+1. Their residues are 0,1,1 modulo each modulus, so every tested congruence holds. Their actual cubic equation has nonzero residual −7580970550234874192400. The construction works for any finite collection of moduli and all positive exponents.

**Evidence.** number_compute.py; number_13.json

**Limit.** It defeats elimination of entire exponent triples by these congruences alone, not stronger valuation constraints or global arithmetic methods.

**Next decision.** Stop adding isolated small moduli; identify a genuine global restriction excluding this local-survival mechanism.

**Background.** [Background source 1](https://www.ams.org/profession/prizes-awards/ams-supported/beal-prize)

### 14. Erdős–Moser conjecture

**Status:** Restricted statement proved

**Attempt performed.** Solved the k=1 and k=2 subcases algebraically and checked the quadratic power-sum identity independently for 99 integer values of m.

**Result.** For k=1, the equation reduces to m(m−3)=0, giving the intended solution m=3. For k=2, it reduces to m(2m²−9m+1)=0. The quadratic discriminant is 73, strictly between 64 and 81, so no positive integer m≥2 solves that subcase.

**Evidence.** number_compute.py; number_14.json

**Limit.** These are elementary established subcases; no uniform conclusion for arbitrary exponents follows.

**Next decision.** Use the identities as exact controls for future congruence tables, and seek an argument that survives variable k.

**Background.** [Background source 1](https://arxiv.org/abs/1011.2940)

### 15. Bunyakovsky conjecture

**Status:** Finite computation verified

**Attempt performed.** Factored all five polynomial families exactly at inputs 1≤n≤1000, recording primality, factor-count parity data, and survival of primes through 31.

**Result.** The three irreducible examples produced 112,581,74 primes; both reducible controls produced none. Yet (n+1)(n²+1) had 55 sieve survivors, all composite. Every value of n²+n+41 survived that small-prime sieve, while only 581 were prime, sharply separating local survival from actual primality.

**Evidence.** number_compute.py; number_15.json

**Limit.** The input cutoff was reduced from 10000. Controls were not locally matched, and these counts establish no uniform prime detector.

**Next decision.** Retain the composite survivors as adversarial examples; require an explicit global statistic before fitting any classifier.

**Background.** [Background source 1](https://arxiv.org/abs/1807.08899)

### 16. Bateman–Horn conjecture

**Status:** Finite computation verified

**Attempt performed.** Computed exact joint prime counts through input 1000 and rational local products through primes 31 and 101 for all ten prescribed coefficient pairs.

**Result.** The joint counts for a=4,10,16,22,28,34,40,46,52,58 were 42,37,35,67,70,23,36,26,38,92. Every local factor was positive. The admissibility argument extends to every prime: modulo two and three there are allowed inputs, and a degree-three polynomial has fewer roots than any prime at least five.

**Evidence.** number_compute.py; number_16.json

**Limit.** The larger input cutoffs, integrals, and Euler-product tails were not computed. Truncated products are not asymptotic constants.

**Next decision.** Separate truncation sensitivity from count discrepancies before selecting a fixed pair for further analysis.

**Background.** [Background source 1](https://arxiv.org/abs/1807.08899)

### 17. Artin’s primitive root conjecture

**Status:** Finite computation verified

**Attempt performed.** Computed exact multiplicative orders at every eligible odd prime through 10000 for bases two, three, five and the excluded controls one and four.

**Result.** The three admissible bases were primitive at 470,476,492 tested primes. Small-index tests missed six, eight, and eight failures respectively. For example ord_683(2)=22, so the index is 31 and none of 2,3,5,7,11,13 detects it. Both excluded controls produced zero primitive roots at odd primes.

**Evidence.** number_compute.py; number_17.json

**Limit.** The proposed million-prime cutoff was reduced; a finite tail list gives no asymptotic bound.

**Next decision.** Use the explicit large-index failures to test any proposed truncation lemma rather than assuming small obstructions suffice.

**Background.** [Background source 1](https://arxiv.org/abs/math/0412262)

### 18. Elliott–Halberstam conjecture

**Status:** Finite computation verified

**Attempt performed.** Reduced to x=100, computed every reduced-class progression error for q≤25, and enclosed logarithms rigorously using rational series with explicit tails.

**Result.** All 25 symbolic prime-power accounting identities passed. The summed maximum errors lie near 5.954689 for q=1, 113.255258 for moduli with largest prime factor at most 13, and 16.351010 for the remaining three moduli. Every displayed approximation has an outward rational enclosure in the output.

**Evidence.** number_compute.py; number_18.json

**Limit.** At this small scale the middle factorization band is empty. This is accounting calibration, not evidence for Elliott–Halberstam savings.

**Next decision.** Keep all modulus bands and prime powers in subsequent formulas; derive a dispersion estimate before interpreting band sizes asymptotically.

**Background.** [Background source 1](https://arxiv.org/abs/1407.4897)

### 19. Chowla’s conjecture

**Status:** Attempted approach failed

**Attempt performed.** Computed exact two-point Liouville correlations for shifts one through twenty at three cutoffs up to 100000, before and after removing primes at most seven.

**Result.** The proposed monotonic improvement fails: at X=1000 and shift one, the original signed sum is 14, while the rough-part sum is 236. Every factorization identity was checked, and the shift-zero control equals 100000 exactly. Removing small primes can therefore substantially increase the observed bias.

**Evidence.** number_compute.py; number_19.json

**Limit.** This rejects an unconditional monotonic-bias heuristic. It neither refutes Chowla nor proves that every conditional decomposition is unhelpful.

**Next decision.** Abandon monotonic improvement as a premise; any new conditional cancellation estimate must state and justify additional hypotheses.

**Background.** [Background source 1](https://arxiv.org/abs/1509.05422)

### 20. Lindelöf hypothesis

**Status:** Restricted statement proved

**Attempt performed.** Integrated an explicit family of triangular peaks exactly to test whether bounded moments alone could force bounded peak heights.

**Result.** For F_H(t)=max(H−H³|t|,0), the second-moment integral is exactly 2/3 for every positive H, while the peak height is H and its half-support width is H^−2. Worked cases H=2,4,8 give widths 1/4,1/16,1/64. The derivative bound grows precisely fast enough to conceal the peaks.

**Evidence.** number_compute.py; number_20.json

**Limit.** These are toy Lipschitz functions, not zeta functions. The result isolates a missing hypothesis rather than disproving a zeta estimate.

**Next decision.** Demand independently proved zeta derivative or peak-width control before using a moment-to-pointwise argument.

**Background.** [Background source 1](https://arxiv.org/abs/2606.02407)

### 21. Vinogradov’s least quadratic nonresidue conjecture

**Status:** Finite computation verified

**Attempt performed.** Tested the first 200 primes from 10007 through 11927 and enumerated all height-bounded 13-smooth integers for the three compatible primes.

**Result.** The compatible primes were 10391,10559,10799; their smooth sets had sizes 744,748,756, and their character sums equaled those sizes exactly. The modulo-17 residue subgroup also had the entire field as its sumset. Both calculations confirm that multiplicative containment and additive growth can coexist without cancellation.

**Evidence.** number_compute.py; number_21.json

**Limit.** The fixed smoothness threshold is calibration only. No contradictory character-sum estimate in the p^ε regime was obtained.

**Next decision.** Keep the cancellation inequality as the explicit missing step; reject expansion-only arguments that pass these negative controls.

**Background.** [Background source 1](https://arxiv.org/abs/1410.7073)

### 22. Lehmer’s conjecture on Ramanujan’s tau function

**Status:** Finite computation verified

**Attempt performed.** Expanded the defining q-product exactly through coefficient 200, checked fourteen prime-power Hecke recurrences, and tested the 691 congruence for every coefficient.

**Result.** All checks passed and no computed coefficient vanished. The prime-zero congruence reduces to p≡−1 modulo 691 because gcd(11,690)=1. Among primes through 10000, this necessary filter still admits 1381,5527,8291. They are filter survivors, not zeros of tau.

**Evidence.** number_compute.py; number_22.json

**Limit.** The original coefficient cutoff 50000 was reduced to 200. Neither a finite coefficient table nor one congruence excludes all possible zeros.

**Next decision.** Use the three surviving primes to audit any additional filter and attach a valid theorem to each exclusion.

**Background.** [Background source 1](https://arxiv.org/abs/2603.29970)

### 23. Lang–Trotter conjecture

**Status:** Restricted statement proved

**Attempt performed.** Derived the actual mod-two Galois images from the two cubics and enumerated their matrices; this is new work beyond the earlier point-count control.

**Result.** E1 has an irreducible cubic with discriminant −23, hence image S3≅GL2(F2). Two of its six matrices have trace one. E2 factors into a rational root and a quadratic of discriminant five, giving the order-two stabilizer; both matrices have trace zero. The exact local trace-one fractions are therefore 1/3 and zero.

**Evidence.** number_compute.py; number_23.json

**Limit.** Only modulus two is certified, with Frobenius comparisons restricted to good odd primes; higher moduli and growing resolution remain uncomputed.

**Next decision.** Use these genuine groups as baselines, then certify the next modular image before fitting trace predictions.

**Background.** [Background source 1](https://arxiv.org/abs/2006.11269)

### 24. Leopoldt’s conjecture

**Status:** Restricted statement proved

**Attempt performed.** Replaced the unprepared cubic computation with an explicit quadratic unit-log calibration in Q(√5) at the split prime eleven.

**Result.** Hensel lifting gives √5≡48 modulo 121, hence ε=(1+√5)/2≡85 and ε^10≡111=1+110. Thus v_11(ε^10−1)=1. Every higher term of log(1+u) has valuation at least two, proving v_11(log ε)=1 and a nonzero rank-one logarithm.

**Evidence.** number_compute.py; number_24.json

**Limit.** This reproduces an established quadratic case. No cubic unit basis, regulator matrix, or universal Leopoldt result was obtained.

**Next decision.** Use the nonzero valuation as a precision-control example before attempting the planned cubic fields.

**Background.** [Background source 1](https://arxiv.org/abs/1805.00131)

### 25. Lehmer’s Mahler measure problem

**Status:** Restricted statement proved

**Attempt performed.** Certified exact rational root intervals and Mahler measures for two explicit members of the proposed small-coefficient polynomial family.

**Result.** For x²−x−1, the measure lies between 1.618033 and 1.618034. For x³−x−1, it lies between 1.324717 and 1.324718: there is one real root ρ>1 and the conjugate pair has squared modulus 1/ρ<1. Thus an attempted universal lower bound of 1.4 already fails on this known cubic.

**Evidence.** number_compute.py; number_25.json

**Limit.** These are two established examples, not the minimum over the full coefficient box or a degree-independent lower bound.

**Next decision.** Require every auxiliary-resultant inequality to accommodate the cubic control before broader enumeration.

**Background.** [Background source 1](https://arxiv.org/abs/1810.13363)

### 26. Lehmer’s totient problem

**Status:** Finite computation verified

**Attempt performed.** Executed the complete prescribed census of all 65536 subsets of the first sixteen odd primes, testing totient divisibility with exact integer remainders.

**Result.** Exactly seventeen subsets passed: the empty subset n=1 and sixteen single-prime subsets. None of the 65519 composite subsets passed. The closest composite ratio (n−1)/φ(n) to an integer occurred at n=3717740976339, with exact distance 4084631/929437286400.

**Evidence.** number_compute.py; number_26.json

**Limit.** This is complete only for the chosen prime set. It does not test arbitrarily large factors or establish any pruning formula.

**Next decision.** Use the full census as an oracle for future interval-pruning rules; require preservation of every positive control.

**Background.** [Background source 1](https://arxiv.org/abs/2409.17076)

### 27. Carmichael’s totient conjecture

**Status:** Finite computation verified

**Attempt performed.** Implemented complete inverse-totient recursion for every target value at most 100, retaining the special cost-one branch for prime two.

**Result.** Exactly 38 target values had preimages; none had exactly one, and the largest preimage was 420. For instance φ^−1(8)={15,16,20,24,30}. Each returned preimage passed an independent totient evaluation. Completeness follows by enumerating every prime-power contribution p^(e−1)(p−1) dividing the remaining target.

**Evidence.** number_compute.py; number_27.json

**Limit.** The target cutoff was reduced from 10000. The recursion certifies bounded values, not a partner construction for every integer.

**Next decision.** Use uncovered substitution patterns within these complete fibers to formulate one exact additional identity.

**Background.** [Background source 1](https://arxiv.org/abs/math/9907204)

### 28. Zaremba’s conjecture

**Status:** Finite computation verified

**Attempt performed.** Produced an exact continued-fraction witness for every denominator two through 2000, checking each witness independently by the numerator and denominator recurrence.

**Result.** All 1999 denominators have a witness with digits at most five under the stated convention allowing both finite representations. A separate exhaustive test of the smaller digit bound two fails already at denominator six. The output preserves every successful numerator and digit word, making the finite coverage directly checkable.

**Evidence.** number_compute.py; number_28.json

**Limit.** No unbounded repair operation or all-denominator theorem was produced; the weaker bound-two failures do not challenge Zaremba.

**Next decision.** Keep the witness table as calibration and demand a symbolic denominator-preserving identity before proposing a repair mechanism.

**Background.** [Background source 1](https://arxiv.org/abs/2603.14116)

### 29. Schanuel’s conjecture

**Status:** Finite computation verified

**Attempt performed.** Used rational enclosures for e and π to evaluate every primitive normalized quadratic polynomial in the stated six-monomial basis with coefficients between minus two and two.

**Result.** All 7448 canonical polynomials were certified nonzero; none remained unresolved. The smallest certified separation was attained by 2+2e−2π+e²−eπ, whose value lies between 0.002700225995587155 and 0.002700225995587156. Tail bounds and all subsequent interval operations use exact rational arithmetic.

**Evidence.** number_compute.py; number_29.json

**Limit.** This excludes a finite coefficient-and-degree family only; it supplies no algebraic-independence or Schanuel theorem.

**Next decision.** Record these exclusions as calibration and seek a uniform symbolic argument before increasing polynomial cutoffs.

**Background.** [Background source 1](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/AWSLecture5.pdf)

### 30. Four exponentials conjecture

**Status:** Finite computation verified

**Attempt performed.** Reduced the logarithmic determinant search to integers two through ten, applied exact multiplicative-independence filters, and evaluated every retained determinant with rational intervals.

**Result.** All 4158 retained quadruples were certified nonzero. The smallest separation occurred for (a,b,c,d)=(4,5,6,8), with determinant between −0.001007536229224002 and −0.001007536229224001. The exact-zero control (2,4,3,9) was correctly excluded because two and four are multiplicatively dependent.

**Evidence.** number_compute.py; number_30.json

**Limit.** The original upper bound thirty was reduced to ten. No uniform logarithmic determinant bound or transcendence conclusion follows.

**Next decision.** Use the smallest determinant to test any proposed quantitative inequality, keeping its independence hypotheses explicit.

**Background.** [Background source 1](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/AWSLecture5.pdf)

### 31. Irrationality of Euler’s constant

**Status:** Restricted statement proved

**Attempt performed.** Derived elementary bounds for the harmonic approximation remainder and computed its exact denominator-clearing ledger for n=1 through twelve.

**Result.** The remainder lies between 1/[2(n+1)] and 1/(2n). At n=12, the common denominator is 27720 and the cleared remainder lies between 13860/13 and 1155, already exceeding 1000. Moreover denominator clearing leaves D_n log n, so the expression is not an integer linear form in γ.

**Evidence.** number_compute.py; number_31.json

**Limit.** This audits the naive harmonic baseline, not the still-unselected integral construction, and proves nothing about irrationality.

**Next decision.** Reject decimal accuracy as the objective; require an explicit construction that controls both denominators and residual logarithms.

**Background.** [Background source 1](https://arxiv.org/abs/1303.1856)

### 32. Normality of π

**Status:** Attempted approach failed

**Attempt performed.** Certified the first 4096 fractional binary digits of π from rational Machin bounds, then tested the explicit shortcut D_k(2N)≤D_k(N) on five scales and eight block lengths.

**Result.** The shortcut fails. For one-bit blocks, D_1(1024)=11/1024 but D_1(2048)=31/2048, which is larger. Four further increases occur in the tested grid. Every digit is certified because the upper and lower rational bounds yield the same scaled integer floor.

**Evidence.** number_compute.py; number_32.json

**Limit.** Normal sequences can show finite discrepancy increases. This refutes only the monotone-doubling shortcut, not π normality; no BBP orbit bound was proved.

**Next decision.** Abandon strict monotonicity and require a quantitatively justified error allowance in any future scale inequality.

**Background.** [Background source 1](https://arxiv.org/abs/math/0101055)

### 33. Hadwiger’s conjecture

**Status:** Attempted approach failed

**Attempt performed.** Constructed K7 with edge 01 subdivided by vertex 7, then identified the nonadjacent vertices 7 and 2.

**Result.** The original graph has a K7 minor by contracting 07. Identification produces K7 minus edge 01, which has no K7 minor. Both graphs have chromatic number six; there is no chromatic-number drop.

**Evidence.** discrete_graphs.py; discrete_graph_results.json, item33. On seven vertices every K7-minor branch set must be a singleton, so the missing edge is decisive.

**Limit.** This refutes unrestricted identification transfer. The example is outside the chromatic-number-at-least-seven case relevant to the proposed Hadwiger route.

**Next decision.** Require any identification-transfer rule to use the chromatic hypothesis explicitly; do not promote arbitrary certificate transport to a lemma.

**Background.** [Background source 1](https://arxiv.org/abs/2609.06867)

### 34. Erdős–Hajnal conjecture

**Status:** Finite computation verified

**Attempt performed.** Generated 300 random twelve-vertex graphs and forty independent-set blowups of C5; filtered for connectivity, clique number at most three, and absence of an induced P6.

**Result.** Forty-one graphs survived. Forty had a dominating set of size at most three. The remaining graph had no such set but had anticomplete triples {0,1,2} and {4,6,8}; no tested graph violated the proposed dichotomy.

**Evidence.** discrete_graphs.py; discrete_graph_results.json, item34, stores every accepted edge set and its witness.

**Limit.** This is a 340-proposal calibration, reduced from the larger planned sample. Forty accepted examples belong to the structured blowup family.

**Next decision.** Retain the non-dominated witness when testing strengthened structural claims; it shows why the anticomplete alternative is necessary.

**Background.** [Background source 1](https://arxiv.org/abs/2606.06258)

### 35. Gyárfás–Sumner conjecture

**Status:** Attempted approach failed

**Attempt performed.** Built the fifteen-vertex complete binary tree and added a sixteenth vertex adjacent to every tree vertex.

**Result.** Mapping the tree root to the universal vertex makes an induced embedding impossible: a depth-two tree vertex must be nonadjacent to the root. Nevertheless the other fifteen vertices explicitly induce the whole tree. The host has clique number and chromatic number three.

**Evidence.** discrete_graphs.py; discrete_graph_results.json, item35, lists the host and tree edges and the identity embedding.

**Limit.** The obstruction rejects inference from one failed rooted search. It neither refutes Gyárfás–Sumner nor supplies the missing bounded-color partition.

**Next decision.** A usable absence certificate must exclude every possible root or justify a complete root-selection reduction.

**Background.** [Background source 1](https://arxiv.org/html/2606.02030v1)

### 36. Graph reconstruction conjecture

**Status:** Finite computation verified

**Attempt performed.** Enumerated all 1,024 labeled graphs on five vertices, canonically identified their isomorphism types, and computed full vertex-deleted decks with multiplicity.

**Result.** There were 34 graph types, including 21 connected types, and 34 distinct decks: no nonisomorphic deck collision occurred. Every type had repeated isomorphic cards, so retaining card multiplicities was necessary throughout.

**Evidence.** discrete_graphs.py; discrete_graph_results.json, item36, contains the canonical graph-to-deck lookup table.

**Limit.** This exhausts five-vertex graphs only. It calibrates exact deck handling rather than implementing the previously unfinished separator-alignment protocol.

**Next decision.** Use the verified deck table to check any future alignment procedure, especially its treatment of repeated cards.

**Background.** [Background source 1](https://arxiv.org/abs/2504.02353)

### 37. Union-closed sets conjecture

**Status:** Finite computation verified

**Attempt performed.** Recomputed the four-element equality cases specifically to classify their structure, adding a new analysis beyond the earlier family count.

**Result.** All 51 families whose maximum element frequency is exactly one half are precisely unions of pairwise disjoint nonempty minimal blocks. Removing unused elements leaves eleven isomorphism types, classified by the integer partition of block sizes.

**Evidence.** discrete_algebra.py; discrete_algebra_results.json, item37, records every family, its minimal blocks, and exact regeneration by all block unions.

**Limit.** This classification is exhaustive on four ground elements only; it does not establish the equality characterization or the union-closed conjecture in general.

**Next decision.** Treat disjoint-block structure as a finite equality pattern requiring a separate general proof, not as an established classification at arbitrary size.

**Background.** [Background source 1](https://arxiv.org/abs/2211.09055)

### 38. Caccetta–Häggkvist conjecture

**Status:** Finite computation verified

**Attempt performed.** Exhausted all 39,363 oriented circulant step sets on orders three through nineteen, replacing the planned unrestricted SAT search with an exact modular enumeration.

**Result.** For every tested order n, the largest triangle-free step set had size floor((n−1)/3). Thus every tested oriented circulant at minimum outdegree ceil(n/3) contained a directed triangle.

**Evidence.** discrete_graphs.py; discrete_graph_results.json, item38. A triangle exists exactly when a+b+c=0 modulo n for steps a,b,c; repeated steps are included.

**Limit.** Circulants have a special translation symmetry. This does not exhaust all digraphs or address longer-cycle thresholds.

**Next decision.** Any proposed modular counting explanation must state where it uses translation symmetry before attempting extension to arbitrary neighborhoods.

**Background.** [Background source 1](https://arxiv.org/html/2604.13700v1)

### 39. Barnette’s conjecture

**Status:** Finite computation verified

**Attempt performed.** Enumerated every perfect matching and every graph cycle of length at most eight in the prisms over C10, C12, and C14.

**Result.** Across 1,294 perfect matchings, 1,252 had disconnected complementary two-factors. Every one admitted an alternating-cycle exchange of length at most eight that strictly reduced its number of complementary cycles; no local trap occurred.

**Evidence.** discrete_graphs.py; discrete_graph_results.json, item39. The three matching totals are 125, 324, and 845.

**Limit.** The result exhausts these three prisms, not all Barnette graphs. Their ladder structure may explain the easy exchanges.

**Next decision.** Analyze the successful prism exchanges for an explicit structural lemma before extrapolating this behavior to other planar cubic graphs.

**Background.** [Background source 1](https://arxiv.org/abs/2508.03531)

### 40. Lovász’s Hamiltonian-path conjecture

**Status:** Attempted approach failed

**Attempt performed.** Enumerated paths through the two cyclic-rotation orbits of the Petersen graph and checked the analogous complement orbits in the three-cube.

**Result.** The Petersen graph admits an explicit Hamiltonian path visiting each orbit contiguously. Each cube complement orbit consists of two nonadjacent vertices, so the same contiguous-fiber rule is impossible there, despite the cube's verified Hamiltonian path.

**Evidence.** discrete_graphs.py; discrete_graph_results.json, item40. Cube witness: 0,1,3,2,6,7,5,4.

**Limit.** The cube disproves this restricted orbit-assembly mechanism, not Lovász's conjecture. The obstruction depends on the chosen subgroup.

**Next decision.** Permit orbit re-entry or prove existence of a suitable subgroup; endpoint matching alone cannot repair disconnected fibers.

**Background.** [Background source 1](https://arxiv.org/abs/2606.09742)

### 41. Rota’s basis conjecture

**Status:** Finite computation verified

**Attempt performed.** For one seeded binary rank-four instance, exhaustively analyzed all 13,824 row arrangements modulo simultaneous column permutations, retaining every row-swap move.

**Result.** Every state reached zero rank defect without increasing defect. There were no positive-defect trap components; the longest shortest escape to a smaller defect required two swaps, including a possible plateau move.

**Evidence.** discrete_landscapes.py; discrete_landscape_results.json, item41, records the four binary bases and a zero-defect arrangement.

**Limit.** The budget was reduced from twenty instances to one exhaustive instance. Rank-four existence is already proved; this measures exchange geometry within a solved baseline.

**Next decision.** Do not assume strict one-step descent. Any broader exchange argument must explain plateau navigation and its dependence on rank.

**Background.** [Background source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SAT.2022.4)

### 42. Hadwiger–Nelson problem

**Status:** Finite computation verified

**Attempt performed.** Built a seven-vertex Moser spindle from two exact diamond modules, using arithmetic in Q(√3,√11), instead of the unavailable five-chromatic input modules.

**Result.** Checked all 21 squared distances exactly, obtained eleven unit edges, excluded every three-coloring, and exhibited a four-coloring. The two diamond endpoint constraints give a direct independent explanation of the three-color obstruction.

**Evidence.** discrete_geometry.py; discrete_geometry_results.json, item42, includes exact coordinate coefficients, all distances, and the coloring certificate.

**Limit.** This is a known four-chromatic construction and an exact module calibration. It does not supply the proposed five-chromatic inputs or improve the plane-coloring lower bound.

**Next decision.** Require future imported modules to pass the same exact geometry and coloring checks before attempting five-color obstruction gluing.

**Background.** [Background source 1](https://arxiv.org/abs/1804.02385)

### 43. Planar unit-distance problem: exact growth

**Status:** Finite computation verified

**Attempt performed.** Ran both repeated-distance and fixed-unit-distance greedy pruning on the explicit 9-by-9 integer grid, retaining fifty points; also checked 100 random fifty-point subsets.

**Result.** The original grid has 144 unit pairs but 224 pairs at squared distance five. Repeated-distance pruning retained 131 equal-distance pairs, versus 121 under fixed-unit pruning; random subsets ranged from 70 to 109.

**Evidence.** discrete_geometry.py; discrete_geometry_results.json, item43, stores retained coordinates and every deletion.

**Limit.** These are toy-grid computations, not instances of the 2026 number-field construction. No suitable small construction input was established; its feasibility remains unresolved.

**Next decision.** Optimize R(A), then rescale its maximizing distance. Keep actual construction feasibility separate from this successful statistic calibration.

**Background.** [Background source 1](https://arxiv.org/abs/2607.05374)

### 44. Hadwiger–Boltyanski illumination conjecture

**Status:** Finite computation verified

**Attempt performed.** Constructed exact vertex/facet coverage matrices for a cube, octahedron, and cuboctahedron using all 26 nonzero directions in {−1,0,1}³.

**Result.** Exhaustive finite set-cover search found minimum dictionary covers of eight, six, and four directions, respectively. Every selected direction satisfies every required strict incident-facet inequality; dominated coverage masks were removed without changing the optimum.

**Evidence.** discrete_geometry.py; discrete_geometry_results.json, item44, includes vertices, facets, directions, and coverage certificates.

**Limit.** This replaces fifty random polytopes with three explicit controls. Minimum cardinality is certified within this finite direction dictionary; no universal illumination theorem follows.

**Next decision.** Use these exact controls to distinguish geometric illumination failures from incompleteness of a future direction dictionary.

**Background.** [Background source 1](https://arxiv.org/abs/2501.10570)

### 45. Lonely runner conjecture

**Status:** Finite computation verified

**Attempt performed.** Computed exact rational permitted-time intersections for 500 seeded gcd-one sets of fourteen speeds at thresholds 1/15, 101/1500, and 1/14.

**Result.** All 500 sets had verified witnesses at all three thresholds. The structured control {1,…,14} instead had exactly eight isolated feasible times at 1/15 and none at 101/1500, exposing the sampling method's lack of near-tight examples.

**Evidence.** discrete_counts_flows.py; discrete_count_flow_results.json, item45, retains all speeds and rational witnesses.

**Limit.** The sampled sets do not discriminate near-tight behavior, so their additive-relation counts support no claimed correlation or structural reduction.

**Next decision.** Replace broad uniform speed sampling with explicitly structured tight families before interpreting arithmetic predictors.

**Background.** [Background source 1](https://arxiv.org/abs/2609.06259)

### 46. 1/3–2/3 conjecture

**Status:** Attempted approach failed

**Attempt performed.** Computed exact linear-extension probabilities for 3,618 ordered incomparable pairs across 100 new posets on eight to ten elements.

**Result.** Found a same-poset collision in the proposed seven-component local signature: pairs (2,7) and (4,7) in case25 have probabilities 2/3 and 25/36. One is balanced and the other is not, despite identical signatures.

**Evidence.** discrete_counts_flows.py; discrete_count_flow_results.json, item46, stores the full order relations, counts, signature, and both witnesses.

**Limit.** This decisively rejects the signature as a complete balanced-pair criterion. Every sampled poset still had a balanced pair, so it is no counterexample to the conjecture.

**Next decision.** Discard this signature as a sufficient classifier; a stronger criterion must capture order information that distinguishes the witness pairs.

**Background.** [Background source 1](https://arxiv.org/abs/1610.00809)

### 47. Erdős–Szekeres convex-polygon conjecture

**Status:** Finite computation verified

**Attempt performed.** Checked exact orientations in all five-point subsets of a 4-by-4 grid, then searched for an eight-point general-position set containing no convex pentagon.

**Result.** All 1,668 general-position five-point subsets contained a convex quadrilateral. After 4,438 eight-point proposals, found and verified a pentagon-free eight-point witness by checking all 56 five-point subsets.

**Evidence.** discrete_geometry.py; discrete_geometry_results.json, item47. Witness: (0,1),(1,15),(1,19),(2,16),(2,18),(3,8),(17,6),(19,5).

**Limit.** These are small known-threshold calibrations. No orientation encoding or UNSAT claim for either 33-point layer profile has been completed.

**Next decision.** Require the future orientation model to reproduce these positive and negative controls before attempting the seven-gon instance.

**Background.** [Background source 1](https://arxiv.org/abs/2512.24061)

### 48. Conway’s thrackle conjecture

**Status:** Finite computation verified

**Attempt performed.** Enumerated every Hamiltonian cycle, modulo cyclic shift and reversal, on fixed strictly convex point sets of sizes three through nine.

**Result.** Exactly one straight-line thrackle cycle occurred at each odd size and none at each even size. In total, 23,116 cycles were checked using exact alternating-endpoint crossing tests.

**Evidence.** discrete_geometry.py; discrete_geometry_results.json, item48, supplies every surviving cycle. Coordinates may be taken as (i,i²).

**Limit.** The result concerns cycles drawn with straight segments on these convex sets. It does not validate the unfinished crossing-order encoding for arbitrary curved edges or subdivided theta graphs.

**Next decision.** Keep these as crossing-rule controls; do not generalize the finite convex-cycle result to arbitrary thrackle drawings.

**Background.** [Background source 1](https://arxiv.org/abs/2506.11808)

### 49. Hadamard matrix conjecture

**Status:** Finite computation verified

**Attempt performed.** Tested all 256 normalized length-three sign quadruples against all 256 eight-sign append choices, covering 65,536 parent/extension pairs.

**Result.** Exactly 108 parents satisfied Σ_i C_(s_i)(t)=0 at every nonzero periodic shift. Every valid parent had a complementary length-five extension; their extension counts were 9, 27, 31, or 37, with respective parent frequencies 4, 32, 24, and 48.

**Evidence.** discrete_algebra.py; discrete_algebra_results.json, item49. C_s(t)=Σ_j s_j s_((j+t) mod n); appending preserves every original entry and its order.

**Limit.** This verifies only the explicit length-three-to-five append rule for periodic complementarity, not arbitrary lengths or Hadamard existence at all admissible orders.

**Next decision.** Seek an explanation of the finite extension classification before proposing any inductive construction.

**Background.** [Background source 1](https://arxiv.org/abs/2306.16812)

### 50. Turán’s tetrahedron problem

**Status:** Finite computation verified

**Attempt performed.** Enumerated all 1,024 labeled three-uniform hypergraphs on five vertices, tested tetrahedron exclusion, and canonically classified the survivors.

**Result.** Found 768 tetrahedron-free labeled systems in 23 isomorphism types. Their maximum edge count is seven, attained by one isomorphism type. Independently verified the cyclic three-part construction has 54 edges on nine vertices and 136 on twelve.

**Evidence.** discrete_algebra.py; discrete_algebra_results.json, item50, records edge-count frequencies and an extremal five-vertex witness.

**Limit.** The raw five-vertex edge bound averages only to density 7/10, above the desired asymptotic 5/9. Finite construction densities also require finite-size corrections.

**Next decision.** Any stronger certificate must use additional consistency or positivity constraints; the enumerated edge-count table alone is insufficient.

**Background.** [Background source 1](https://arxiv.org/abs/2609.08336)

### 51. Ryser’s hypergraph conjecture

**Status:** Attempted approach failed

**Attempt performed.** After all 100 sampled replacements violated ν=2, exhausted all 2,383 absent partite edges and all eighteen possible deletions from the specified seed.

**Result.** Every one of the 42,894 replacements has matching number exactly three. Each new edge avoids at least two seed edges in each copy; deleting one still leaves a disjoint edge from each copy, forming a three-edge matching with the new edge.

**Evidence.** discrete_obstructions.py; discrete_obstruction_results.json, item51, certifies every replacement and the avoidance counts.

**Limit.** The entire proposed one-edge neighborhood is empty under the matching-number-two constraint. This rejects that search design, not Ryser's inequality.

**Next decision.** Abandon single-edge replacement for this seed; changing the neighborhood requires preserving matching number by a different explicit mechanism.

**Background.** [Background source 1](https://arxiv.org/abs/2505.05339)

### 52. Ryser’s Latin-square transversal conjecture

**Status:** Restricted statement proved

**Attempt performed.** Enumerated all partial transversals of size n−1 in the cyclic Latin squares of orders five and seven, then derived the governing sum identity.

**Result.** All 75 and 931 partial transversals completed immediately, requiring zero exchanges. More generally, for odd n the sum of all residues is zero modulo n; comparing selected row, column, and symbol sums forces the missing symbol to equal the missing row plus missing column.

**Evidence.** discrete_landscapes.py; discrete_landscape_results.json, item52; discrete_restricted_lemmas.txt gives the proof.

**Limit.** The lemma applies to cyclic odd-order squares. It explains why this benchmark cannot measure exchange difficulty and does not prove the conjecture for arbitrary Latin squares.

**Next decision.** Retire cyclic near-transversals as exchange benchmarks; future tests need squares without this automatic completion identity.

**Background.** [Background source 1](https://arxiv.org/abs/1801.02893)

### 53. Tutte’s 5-flow conjecture

**Status:** Attempted approach failed

**Attempt performed.** Enumerated fundamental-cycle coefficient boxes for four graphs, then checked every unrestricted unit-coordinate move at a cube trap.

**Result.** At z=(−2,−2,−1,−1,0), the defect potential is one. All ten ±1 coordinate moves raise it to two or three, disproving monotone descent even without the box restriction. An explicit escape reaches a valid flow with maximum potential two, making the required barrier increase exactly one.

**Evidence.** discrete_obstructions.py; discrete_obstruction_results.json, item53, records the basis, edge flow, ten neighbors, and escape path.

**Limit.** This refutes this potential-and-move rule. The cube has valid five-flows; the obstruction is algorithmic, not a counterexample to Tutte.

**Next decision.** Permit controlled potential increases or change the move set; a proof cannot rely on unrestricted monotone coordinate descent.

**Background.** [Background source 1](https://arxiv.org/abs/2601.12036)

### 54. Conway’s 99-graph problem

**Status:** Restricted statement proved

**Attempt performed.** Verified every entry of the nine-vertex rook-graph matrix identity and derived exact block constraints for a hypothetical rooted 99-graph.

**Result.** The rook control passed all 81 identity entries. For the 99-graph, the unknown outside adjacency B must satisfy CB=2J−C−MC and B²+B=12I+2J−CᵀC, with row sum twelve; the block proof makes the source of these constraints explicit.

**Evidence.** discrete_graphs.py; discrete_graph_results.json, item54; discrete_restricted_lemmas.txt defines C and M and proves the reduction.

**Limit.** This is an exact necessary-and-sufficient rooted matrix reformulation with a small verified control. No 84-by-84 binary solution or impossibility certificate has been produced.

**Next decision.** Encode the full block system without extra symmetry restrictions; retain the rook instance as the positive control.

**Background.** [Background source 1](https://arxiv.org/abs/2308.02978)

### 55. Tutte’s 3-flow conjecture

**Status:** Finite computation verified

**Attempt performed.** Exhausted all 1,266 balanced outdegree-type assignments on four five-regular circulants and performed exact augmenting-path orientation and integral-flow lifting.

**Result.** The graphs on 6,8,10,12 vertices each had exact edge-connectivity five. Respectively 20,44,102,328 assignments were feasible; all 494 accepted orientations lifted to verified flows with signed values one and minus two and exact conservation.

**Evidence.** discrete_counts_flows.py; discrete_count_flow_results.json, item55, stores one complete flow certificate per graph and all assignment totals.

**Limit.** This verifies the orientation/lifting mechanism on four explicit graphs, not on arbitrary 4-edge-connected graphs or arbitrary degrees.

**Next decision.** Separate failures of a chosen outdegree assignment from graph-level failure; a general argument still needs a complete structural reduction.

**Background.** [Background source 1](https://arxiv.org/abs/2609.08377)

### 56. Smooth four-dimensional Poincaré conjecture

**Status:** Restricted statement proved

**Attempt performed.** Computed the critical points and pole-chart Hessians of the height function on the standard unit sphere S4 in R5, making the simplest handle certificate explicit.

**Result.** There are exactly two critical points. Their Hessians are I4 and −I4, so the Morse indices are 0 and 4 and the associated handle description has one handle of each index.

**Evidence.** h±(x)=±sqrt(1−|x|²); Hess h±(0)=∓I4.; geometry_calculations.json (item 56)

**Limit.** This verifies the standard sphere only; it extracts no certificate for an arbitrary homotopy sphere or a published four-dimensional candidate.

**Next decision.** Retain this calibration; a candidate-specific proof needs an actual handle description and justified simplifications.

**Background.** [Background source 1](https://arxiv.org/abs/2411.10051)

### 57. Smooth four-dimensional Schoenflies conjecture

**Status:** Restricted statement proved

**Attempt performed.** Constructed explicit parametrizations of both closed hemispheres bounded by the standard equatorial S3 in S4, and checked the sphere equation and inverses algebraically.

**Result.** Each hemisphere is smoothly diffeomorphic to the closed four-ball. The denominator in the inverse is at least one on its matching hemisphere, including the boundary.

**Evidence.** Φ±(y)=(2y/(1+r),±(1−r)/(1+r)), r=|y|²≤1.; 4r+(1−r)²=(1+r)²; inverse y=x/(1±t).; geometry_calculations.json (item 57)

**Limit.** The embedding is the standard equator. This gives no straightening map for a general smooth embedded three-sphere.

**Next decision.** Use these maps to validate boundary conventions before attempting a nonstandard embedding.

**Background.** [Background source 1](https://arxiv.org/abs/2212.02004)

### 58. Andrews–Curtis conjecture

**Status:** Finite computation verified

**Attempt performed.** Built a balanced two-generator presentation using eight elementary Andrews–Curtis moves from the trivial presentation, then executed and logged every inverse move with exact free reduction.

**Result.** The resulting presentation reduces back to the ordered relators x and y. The saved certificate contains the starting words, all eight reducing moves, and every intermediate state.

**Evidence.** geometry_calculations.py: apply_move, inverse_move, reduce_word; item 58 contains the replayable word certificate.; geometry_calculations.json (item 58)

**Limit.** This deliberately generated example is known trivial by construction. No hard published candidate or stabilization question was resolved.

**Next decision.** The move checker is ready; the next substantive input must be an independently specified candidate presentation.

**Background.** [Background source 1](https://arxiv.org/abs/2607.23611)

### 59. Slice–ribbon conjecture

**Status:** Restricted statement proved

**Attempt performed.** Examined the explicit disk (u,v,0,0) inside the unit four-ball and computed the radial Morse function to certify the ribbon condition for its boundary unknot.

**Result.** The restricted squared radius is u²+v². Its only interior critical point is a nondegenerate minimum; there are no interior maxima. Thus the disk is an explicit ribbon disk.

**Evidence.** ∇r²=(2u,2v), Hess(r²)=2I2; boundary u²+v²=1.; geometry_calculations.json (item 59)

**Limit.** This solves only the unknot calibration and says nothing about a nontrivial slice candidate. No failed search is being interpreted as non-ribbonness.

**Next decision.** Move to a specified slice knot only after its slicing certificate and diagram are available.

**Background.** [Background source 1](https://arxiv.org/abs/2603.23717)

### 60. Crossing-number additivity conjecture

**Status:** Restricted statement proved

**Attempt performed.** Multiplied the trefoil Jones polynomial by itself using exact integer convolution, then compared its breadth with the six-crossing connected-sum diagram.

**Result.** The product has lowest exponent 2 and highest exponent 8. Jones breadth gives a lower bound of six crossings, matching the diagram upper bound, so two trefoils have additive crossing number.

**Evidence.** (t+t³−t⁴)²=t²+2t⁴−2t⁵+t⁶−2t⁷+t⁸; 6≤c(T#T)≤6.; geometry_calculations.json (item 60)

**Limit.** This is a familiar alternating example. The polynomial breadth need not attain crossing number for general knots.

**Next decision.** Retain this exact control; a wider proof needs a lower bound effective when Jones breadth is deficient.

**Background.** [Background source 1](https://arxiv.org/abs/2511.18016); [Background source 2](https://arxiv.org/abs/0907.5374)

### 61. Purely cosmetic surgery conjecture for knots in the three-sphere

**Status:** Finite computation verified

**Attempt performed.** Derived the first homology of Dehn filling and applied it to every reduced slope p/q with −4≤p≤4 and 1≤q≤4.

**Result.** There are 23 slopes and 253 unordered pairs. Different absolute numerators eliminate 198 pairs for every knot; 55 pairs survive this necessary homological filter.

**Evidence.** H1(S3_{p/q}(K);Z)=Z/pZ because the longitude vanishes in exterior homology and filling kills pμ; p=0 gives Z.; geometry_calculations.json (item 61)

**Limit.** Equal homology does not imply homeomorphism, and the surviving pairs are not verified cosmetic surgeries. The filter ignores orientation-sensitive invariants.

**Next decision.** Apply stronger surgery invariants only to surviving pairs for a specified knot.

**Background.** [Background source 1](https://arxiv.org/abs/2512.20511)

### 62. Volume conjecture

**Status:** Attempt remains unresolved

**Attempt performed.** Evaluated the figure-eight colored Jones root-of-unity product formula at N=20,40,80 using independently repeated 70-digit and 130-digit Decimal calculations.

**Result.** The scaled logarithms are approximately 3.36473742636, 2.85816821563, and 2.52511086864. Both precision runs agree within 10^−65; these finite values remain above the known volume 2.02988321282.

**Evidence.** J_N=Σ(k=0..N−1) Π(j=1..k)4sin²(πj/N); output is (2π/N)log J_N.; geometry_calculations.json (item 62)

**Limit.** Precision agreement is numerical validation, not a rigorous interval enclosure. Three terms do not prove convergence, and the figure-eight case is already known.

**Next decision.** Use this normalization control before evaluating a new knot; do not extrapolate a proof from the trend.

**Background.** [Background source 1](https://arxiv.org/abs/2502.18575)

### 63. 11/8 conjecture

**Status:** Restricted statement proved

**Attempt performed.** Translated the 11/8 inequality and the older Furuta 10/8+2 inequality into exact integer conditions for forms 2k(−E8)⊕lH, then tabulated k=1 through 8.

**Result.** The target becomes l≥3k, while the older bound gives l≥2k+1. The interval between them contains 28 pairs in this finite table; k=1 has no gap.

**Evidence.** b2=16k+2l, σ=−16k; 11|σ|/8=22k; (10/8)|σ|+2=20k+2.; geometry_calculations.json (item 63)

**Limit.** These are arithmetic gaps in one older bound, not realizable manifolds or a list of currently undecided forms. Stronger known restrictions were deliberately not applied.

**Next decision.** Any realizability investigation must first apply the strongest known form-specific obstructions.

**Background.** [Background source 1](https://arxiv.org/abs/1812.04052)

### 64. Borel rigidity conjecture

**Status:** Restricted statement proved

**Attempt performed.** Proved the torus-to-torus case directly using equivariant lifts and checked an explicit five-dimensional integral automorphism and its inverse by exact matrix multiplication.

**Result.** A homotopy equivalence f:Tn→Tn inducing A∈GL(n,Z) is homotopic to the linear homeomorphism induced by A. The straight-line homotopy of lifts respects every integer translation.

**Evidence.** H_s(x)=(1−s)F(x)+sAx; H_s(x+z)=H_s(x)+Az; saved 5×5 matrices satisfy AA^−1=I.; geometry_calculations.json (item 64)

**Limit.** Both manifolds here are tori. This does not prove rigidity for an arbitrary manifold merely homotopy equivalent to a torus, or for other aspherical manifolds.

**Next decision.** Keep the lift argument as a control; the missing step is geometric identification of a general source manifold.

**Background.** [Background source 1](https://arxiv.org/abs/2507.11337)

### 65. Novikov conjecture

**Status:** Restricted statement proved

**Attempt performed.** Worked out every possible higher signature in dimension two, where positive-degree components of the Hirzebruch L-class cannot contribute.

**Result.** For closed oriented surfaces and an orientation-preserving homotopy equivalence h, naturality of cohomology pairing proves the required equality for every degree-two group-cohomology class; all other degrees contribute zero.

**Evidence.** L(M)=1; ⟨(f∘h)*a,[N]⟩=⟨f*a,h_*[N]⟩=⟨f*a,[M]⟩.; geometry_calculations.json (item 65)

**Limit.** This is the elementary surface case. It does not control positive-degree L-classes in higher dimensions or establish the general conjecture.

**Next decision.** Any extension must address those higher characteristic classes rather than reuse dimension-two vanishing.

**Background.** [Background source 1](https://arxiv.org/abs/2507.11337)

### 66. Farrell–Jones conjecture

**Status:** Restricted statement proved

**Attempt performed.** Specialized the Farrell–Jones assembly map to the infinite dihedral group and checked its explicit semidirect-product relation.

**Result.** The group Z⋊C2 contains Z with index two, so it is virtually cyclic. Consequently a point is a model for E_VCyc(G), and the assembly map is literally the identity.

**Evidence.** (n,ε)(m,δ)=(n+(−1)^εm,ε+δ mod2); rtr=t^−1; E_VCyc(G)=point.; geometry_calculations.json (item 66)

**Limit.** This is an immediate known base case, not a new assembly calculation for a group outside the virtually cyclic family.

**Next decision.** A nontrivial next attempt needs a specified group for which E_VCyc(G) is not already a point.

**Background.** [Background source 1](https://arxiv.org/abs/2507.11337)

### 67. Inverse Galois problem over the rational numbers

**Status:** Restricted statement proved

**Attempt performed.** Constructed an explicit rational polynomial realization of the finite group S3 and checked the two decisive algebraic conditions.

**Result.** The polynomial x³−2 is Eisenstein at 2, hence irreducible. Its discriminant is −108, which is not a rational square; the transitive cubic Galois group is therefore S3.

**Evidence.** disc(x³+ax+b)=−4a³−27b²; a=0,b=−2 gives −108.; geometry_calculations.json (item 67)

**Limit.** This is a standard realization of one already realizable group. It supplies no construction for arbitrary finite groups and no new regular extension.

**Next decision.** Use this example to validate a Galois-group certificate format before choosing a genuinely unresolved group-realization target.

**Background.** [Background source 1](https://arxiv.org/abs/1512.08708)

### 68. Tate conjecture

**Status:** Restricted statement proved

**Attempt performed.** Enumerated the split quadric x0x1−x2x3=0 over F7 and combined its point count with the intersection pairing of its two rational rulings.

**Result.** Exactly 64 of the 400 projective points lie on the quadric. Its two rulings have intersection matrix [[0,1],[1,0]], hence independent classes; the product P1×P1 description shows they span H².

**Evidence.** #Q(F7)=64=(7+1)²; det intersection matrix=−1; both ruling cycles are defined over F7 with Qℓ coefficients, ℓ≠7.; geometry_calculations.json (item 68)

**Limit.** This proves the divisor Tate statement for this split quadric using its known product decomposition, not from point counts alone.

**Next decision.** A non-split surface requires actual Frobenius and cycle calculations instead of this product argument.

**Background.** [Background source 1](https://arxiv.org/abs/2505.07337)

### 69. Lefschetz standard conjecture

**Status:** Restricted statement proved

**Attempt performed.** Computed the Lefschetz operator for the complex abelian surface E×E with product polarization, then supplied algebraic correspondences realizing its inverse.

**Result.** In the saved bases H1→H3 is a permutation matrix squaring to identity. Integration on either elliptic factor, represented by E×E times the other diagonal, gives inverse correspondences whose sum inverts this map.

**Evidence.** h=a1∧b1+a2∧b2; h²=2a1∧b1∧a2∧b2. The H4→H0 inverse has coefficient 1/2.; geometry_restricted_proofs.md, item 69.; geometry_calculations.json (item 69)

**Limit.** This verifies one complex product-polarized surface. Matrix inversion alone would not suffice without the exhibited algebraic cycles.

**Next decision.** Retain the correspondence certificate; extending to other varieties requires analogous algebraic inverse operators.

**Background.** [Background source 1](https://arxiv.org/abs/1002.5011)

### 70. Abundance conjecture

**Status:** Restricted statement proved

**Attempt performed.** Derived the canonical section counts on X=C×C×E×E, with genus-two C given by y²=x⁵−1 and elliptic E by y²=x³−x.

**Result.** K_X pulls back the globally generated canonical bundle on C×C, hence is nef and semiample. Riemann–Roch and Künneth give h0(mK_X)=(2m−1)² for m≥2; m=0..6 yield 1,4,9,25,49,81,121.

**Evidence.** h0(C,mK_C)=2m−1 for m≥2; h0(E,mK_E)=1; numerical dimension ν(K_X)=2.; geometry_restricted_proofs.md, item 70.; geometry_calculations.json (item 70)

**Limit.** This is an explicit product fourfold. Its canonical map at m=1 includes genus-two hyperelliptic maps; it is not an embedding of C×C.

**Next decision.** Use the exact count as a control; a non-product nef canonical divisor needs a different semiampleness argument.

**Background.** [Background source 1](https://arxiv.org/abs/2406.18233)

### 71. Termination of flips conjecture

**Status:** Attempted approach failed

**Attempt performed.** Tested the logical inference that a strictly decreasing nonnegative real progress measure would force every flip sequence to terminate.

**Result.** The exact recurrence x0=1 and x_(n+1)=x_n/(1+x_n) gives x_n=1/(n+1). Eleven values were computed as fractions, and induction proves an infinite strictly decreasing positive sequence.

**Evidence.** x_n−x_(n+1)=1/((n+1)(n+2))>0; inf x_n=0 is never reached.; geometry_calculations.json (item 71)

**Limit.** These numbers are not flips or discrepancies of constructed varieties. The calculation rejects an insufficient termination argument, not the termination conjecture.

**Next decision.** A proposed geometric measure must also have a proved well-founded value set or another finite-descent mechanism.

**Background.** [Background source 1](https://arxiv.org/abs/2305.01752)

### 72. Nagata’s conjecture on plane curves

**Status:** Finite computation verified

**Attempt performed.** Built exact jet-interpolation matrices for ten explicit integer points and equal multiplicities m=1,2,3, taking maximum prohibited degrees d=3,6,9.

**Result.** The matrices have ranks 10/10, 28/28, and 55/55. Independently evaluated square minors modulo 1009 are 6,984,183; their nonvanishing certifies full column rank in characteristic zero.

**Evidence.** Points Pi=(i,(i²+i⁵) mod101), i=0..9; geometry_interpolation_certificates.json records every row, column, and selected minor.; geometry_calculations.json (item 72)

**Limit.** This proves the indicated three multiplicities for very general ten points by openness, including lower degrees by inclusion. It covers neither all multiplicities nor arbitrary point counts.

**Next decision.** Keep the exact minors; future work must introduce an argument controlling unbounded multiplicity.

**Background.** [Background source 1](https://arxiv.org/html/1202.0475v1)

### 73. Segre–Harbourne–Gimigliano–Hirschowitz conjecture

**Status:** Finite computation verified

**Attempt performed.** Executed three mixed-multiplicity interpolation tests on ten points and a two-double-point special-case control, with exact modular minor certificates.

**Result.** For (d;m)=(4;2,1⁹),(4;2²,1⁸),(5;2⁵,1⁵), vector-space dimensions are 3,1,1. The conic control has dimension one, with explicit generator (y−2x)² and rank five.

**Evidence.** geometry_interpolation_certificates.json; in the control E=H−E1−E2, E²=−1, D=2E and D·E=−2.; geometry_calculations.json (item 73)

**Limit.** The first three maximal-rank results hold for very general points. The special control uses eight zero multiplicities and verifies a familiar doubled-line mechanism only.

**Next decision.** Use these positive and negative controls before interpreting a rank defect in a broader mixed system.

**Background.** [Background source 1](https://arxiv.org/html/1202.0475v1)

### 74. Hopf’s positive-curvature Euler-characteristic conjecture

**Status:** Restricted statement proved

**Attempt performed.** Evaluated the six-dimensional Euler form under constant positive sectional curvature, counting its Pfaffian pairings and checking the unit-sphere integral exactly.

**Result.** There are 15 pairings. The Euler density is 15κ³/(8π³) times volume, which is positive when κ>0. Multiplying by Vol(S6)=16π³/15 at κ=1 gives Euler characteristic two.

**Evidence.** (2π)^−3 Pf(Ω)=15κ³/(8π³)dvol; (15/8)(16/15)=2.; geometry_calculations.json (item 74)

**Limit.** This covers constant-curvature six-manifolds via Gauss–Bonnet. Variable positive sectional curvature does not make this substitution legitimate.

**Next decision.** A broader argument must control the full curvature tensor in the Euler polynomial.

**Background.** [Background source 1](https://arxiv.org/abs/2507.16936)

### 75. Hopf’s S2 × S2 problem

**Status:** Restricted statement proved

**Attempt performed.** Applied the exact conformal sectional-curvature formula at a global minimum of an arbitrary smooth conformal factor on the standard product S2×S2.

**Result.** Every metric e^(2f)g_product has a plane with nonpositive curvature: choose a mixed plane at the minimum, where df=0 and Hess f is positive semidefinite. Thus no conformal deformation, of any amplitude, achieves everywhere positive curvature.

**Evidence.** K_new(X∧Y)=e^(−2f)[−Hess f(X,X)−Hess f(Y,Y)]≤0 at the minimum.; geometry_restricted_proofs.md, item 75.; geometry_calculations.json (item 75)

**Limit.** Only the conformal class of the standard product metric is excluded. General nonconformal metrics remain outside the argument.

**Next decision.** Discard this conformal search family as a route to a positively curved counterexample.

**Background.** [Background source 1](https://arxiv.org/abs/math/0411632)

### 76. Chern’s isoparametric conjecture for minimal hypersurfaces

**Status:** Attempted approach failed

**Attempt performed.** Constructed and checked a nonzero formal first-derivative tensor for principal curvatures (−3,−1,1,3), enforcing symmetry, differentiated mean/scalar constraints, and the scalar Simons norm identity.

**Result.** The tensor satisfies those necessary constraints with S=20 and |∇A|²=320, yet ∇K=(48√5,0,0,0). Therefore the proposed shortcut from these pointwise constraints to constant Gauss–Kronecker curvature fails.

**Evidence.** T111=2√5; symmetric T122=−4√5; symmetric T133=2√5; remaining entries zero. |T|²=S(S−4).; geometry_calculations.json (item 76)

**Limit.** This formal jet is not a constructed local immersion or compact hypersurface. Higher-order compatibility and global realization were not proved.

**Next decision.** Any repaired argument must use constraints beyond this verified first-derivative system.

**Background.** [Background source 1](https://arxiv.org/abs/2606.29246)

### 77. Symmetric Mahler conjecture in dimensions four and higher

**Status:** Restricted statement proved

**Attempt performed.** Derived exact primal and polar volumes for K_t=conv(±e1,…,±e4,±t(1,1,1,1)), throughout t≥1/2, using visible pyramids and clipped-cube integration.

**Result.** The volumes are t+1/4 and 32/(3t)−4/(3t³)+1/(4t⁴). Their product exceeds 32/3 because its gap has an explicitly positive polynomial numerator. At t=1 the product is 575/48.

**Evidence.** Product−32/3=(16u³+32u²+14u+1)/(48t⁴), u=2t−1≥0.; geometry_restricted_proofs.md, item 77.; geometry_calculations.json (item 77)

**Limit.** This proves the bound for one stated centrally symmetric polytope family, not all four-dimensional bodies. No novelty claim is made.

**Next decision.** Remove this family from counterexample searches; a wider proof needs control beyond its special diagonal symmetry.

**Background.** [Background source 1](https://video.renyi.hu/video/artem-zvavitch-volume-product-and-mahler-conjecture-for-convex-bodies-407)

### 78. Zariski cancellation problem in characteristic zero

**Status:** Attempted approach failed

**Attempt performed.** Tested whether the kernel of one convenient locally nilpotent derivation can canonically identify a coordinate in the cancellation strategy.

**Result.** On C[x,y,z]/(xy−z²+1), the explicit derivations δ=(0,2z,x) and ε=(2z,0,y) both preserve the relation and are locally nilpotent. Yet x lies in ker δ while ε(x)=2z≠0.

**Evidence.** δ(xy−z²+1)=ε(xy−z²+1)=0; δ³y=ε³x=0; saved generator chains certify local nilpotence.; geometry_calculations.json (item 78)

**Limit.** This surface calculation refutes the single-derivation invariance shortcut. It is not a counterexample to cancellation of complex affine three-space.

**Next decision.** A canonical invariant must account for all relevant derivations or extra justified structure.

**Background.** [Background source 1](https://arxiv.org/abs/2208.14736)

### 79. Bounded negativity conjecture in characteristic zero

**Status:** Restricted statement proved

**Attempt performed.** Specified ten distinct points (i,i²,1) on the smooth projective conic yz−x²=0 and computed the strict transform after blowing up those points.

**Result.** The resulting fixed smooth projective surface contains an irreducible rational curve C with C²=−6. Its canonical intersection is four, and adjunction gives genus zero. Any negativity bound for this surface is at least six.

**Evidence.** C=2H−ΣEi; C²=4−10=−6; K·C=−6+10=4; 2g−2=−2.; geometry_calculations.json (item 79)

**Limit.** One negative curve on one fixed surface does not violate bounded negativity. Allowing the number of blowups to vary changes the surface.

**Next decision.** Further attempts must seek an unbounded sequence on this same fixed surface, not move the ambient surface.

**Background.** [Background source 1](https://arxiv.org/abs/2101.07187)

### 80. Four-dimensional sphere-packing problem

**Status:** Restricted statement proved

**Attempt performed.** Verified D4 covolume two and its 24 shortest vectors, then moved one coset in a two-coset description by s times the first coordinate vector.

**Result.** The original density is π²/16. Two explicit inter-coset vectors give squared minimum distance at most 2−2|s|+s²<2 for 0<|s|<2. At fixed cell volume, rescaling spheres therefore lowers density along this path.

**Evidence.** D4=L∪(b1+L), L=⟨2b1,b2,b3,b4⟩; vectors ±b1+se1 certify the bound.; geometry_calculations.json (item 80)

**Limit.** This is one explicit periodic perturbation control, consistent with known periodic extremality. It neither searches all finite deformations nor proves global packing optimality.

**Next decision.** Exclude this displacement path from improvement searches; different finite deformations require new certificates.

**Background.** [Background source 1](https://arxiv.org/abs/2206.15373); [Background source 2](https://arxiv.org/abs/0808.2013)

### 81. P versus BPP

**Status:** Finite computation verified

**Attempt performed.** The root searched correlated six-bit uniform samplers and checked the complete ordered width-two Boolean-function class; an independent method reconstructed the same class.

**Result.** The exact minimum support is eight. S={0,4,13,14,26,31,33,35} has maximum acceptance error 1/4 over all 18,664 functions. Affine-parity arguments exclude every smaller support.

**Evidence.** sampler_search_8.json; method_candidate_8_verification.json; sampler_optimality_proof.md; sampler_search.py; method_oracle.py.

**Limit.** This proves a finite optimum for the specified six-bit model. It neither constructs samplers at growing lengths nor establishes P=BPP; the reported computation was performed by the root and independent verifier.

**Next decision.** Seek a structural construction explaining the eight-point support and test a precisely stated extension to longer programs.

**Background.** [Background source 1](https://www.math.ias.edu/files/Book-online-Aug0619.pdf)

### 82. NP versus coNP

**Status:** Finite computation verified

**Attempt performed.** Generated the three prescribed odd-charge Tseitin CNFs, exhaustively checked assignments, and compared the identical least-variable Shannon proof with and without sharing canonical residual formulas.

**Result.** All formulas are unsatisfiable. Tree nodes versus distinct shared residuals are 55 versus 23 for K4, 167 versus 51 for K3,3, and 343 versus 99 for the cube.

**Evidence.** computation_batch.py, card82; computation_batch_results.json, item 82; computation_derivations.txt, item 82.

**Limit.** The parity contradiction also has an elementary algebraic proof, but these sharing counts concern one fixed branching representation on three graphs. They provide no general polynomial certificate-size bound.

**Next decision.** Determine which separator restrictions yield a provable sharing bound before extending the input family.

**Background.** [Background source 1](https://www.scottaaronson.com/papers/pnp.pdf)

### 83. L versus NL

**Status:** Restricted statement proved

**Attempt performed.** Implemented the two-bit frontier update, proved its induction for arbitrary chains of two-vertex layers, and compared all 256 two-transition instances with graph traversal.

**Result.** All promised instances agree. Extending the method by discarding nonlayered edges fails on 1,024 of 4,096 four-vertex digraphs; the two-edge path 0→1→3 is an explicit witness.

**Evidence.** m_next(j)=OR_b[m(b) AND E(b,j)]; computation_batch_results.json, item 83; computation_derivations.txt, item 83.

**Limit.** Four frontier bits plus logarithmic indexing suffice for the promised layered class. The adversarial projection failure identifies exactly why this implementation does not decide unrestricted directed reachability.

**Next decision.** Preserve the proven layered algorithm and specify what additional information would represent within-layer and backward reachability.

**Background.** [Background source 1](https://www.math.ias.edu/files/Book-online-Aug0619.pdf)

### 84. L versus BPL

**Status:** Finite computation verified

**Attempt performed.** Ran all fifteen exact rational chain-and-precision combinations for sixteen steps, rounding the first three coordinates downward and assigning the remaining mass to the fourth.

**Result.** Every one of 240 checks satisfies E_next≤(1−ε)E+3·2^(−b). At ε=1/2 the maximum acceptance errors are 3/64, 3/1024, and 3/16384 for b=4,8,12.

**Evidence.** computation_batch_results.json, item 84 stores every step; computation_derivations.txt proves contraction and the rounding bound.

**Limit.** The recurrence concerns this explicit contracting four-state family. Exact rational arithmetic here is not an implementation in logarithmic space, and arbitrary randomized configuration graphs need not contract.

**Next decision.** Account for storage and recomputation costs before turning the error recurrence into a space-bounded algorithm.

**Background.** [Background source 1](https://www.math.ias.edu/files/Book-online-Aug0619.pdf)

### 85. P versus PSPACE

**Status:** Finite computation verified

**Attempt performed.** Executed ordered decision-diagram quantifier elimination on 200 seeded six-variable formulas under the two alternating prefixes, checking each intermediate function against independent truth-table quantification.

**Result.** All 12,600 remaining truth entries agree. The largest reachable diagram contains 25 nodes including terminals across the tested elimination stages.

**Evidence.** computation_batch.py, BDD and card85; computation_batch_results.json records all formulas, outcomes, and stage sizes.

**Limit.** This verifies the prescribed representation and elimination operations on a finite sample. A small maximum on six variables does not control worst-case intermediate growth with variable count or quantifier alternation.

**Next decision.** Construct an explicit adversarial family and derive its diagram-size recurrence before claiming an efficient general QBF method.

**Background.** [Background source 1](https://www.scottaaronson.com/papers/pnp.pdf)

### 86. Existence of one-way functions

**Status:** Finite computation verified

**Attempt performed.** Exhaustively optimized deterministic adaptive strategies of depth at most two in the specified hidden-handle Z/7Z game, then directly replayed each attaining tree on all seven secrets.

**Result.** Optimal inversion success is 3/7 in the baseline, 4/7 with one challenge-parity query, and 3/7 with a redundant copied handle-index bit.

**Evidence.** computation_priority.py; computation_priority_results.json, item 86 includes optimal strategy trees and seven-secret replay outcomes.

**Limit.** The finite oracle exposes only insertion indices; parity is deliberately extra algebraic information. These exact game optima establish neither security of any concrete encoding nor existence of one-way functions.

**Next decision.** Analyze how the optimum changes with group order and query budget while preserving the same explicit oracle semantics.

**Background.** [Background source 1](https://www.math.ias.edu/files/Book-online-Aug0619.pdf); [Background source 2](https://arxiv.org/abs/2307.03065)

### 87. Deterministic polynomial identity testing

**Status:** Finite computation verified

**Attempt performed.** Expanded 100 seeded common-factor sums and 100 exact cancellation controls, applying the prescribed base-seven Kronecker substitution and checking monomial collisions coefficientwise.

**Result.** All 100 sums remain nonzero and all 100 cancellation controls remain zero. No distinct monomials collide; the maximum resulting univariate degree is 1,716.

**Evidence.** computation_batch_results.json, item 87; computation_derivations.txt proves injectivity for exponent digits between zero and six.

**Limit.** This confirms a known substitution under the explicit degree bound. Expansion and the rapidly increasing substituted degree do not give polynomial-time identity testing for unrestricted circuits.

**Next decision.** Require a uniform cost bound for any proposed smaller substitution before counting common-factor examples as an efficiency improvement.

**Background.** [Background source 1](https://www.scottaaronson.com/papers/pnp.pdf)

### 88. VP versus VNP

**Status:** Attempted approach failed

**Attempt performed.** Built the coefficient-flattening matrices for (x1+y1)^k(x2+y2)^k, k=1,…,6, and compared their exact permutation-matrix ranks with sharing-aware circuit gate counts.

**Result.** Ranks are 4,9,16,25,36,49 while circuit sizes are 3,5,7,7,9,9. Already k=1 refutes the candidate inequality rank≤gate count.

**Evidence.** The sole nonzero entry in row(a,b) is column(k−a,k−b); computation_batch_results.json, item 88; computation_derivations.txt.

**Limit.** This rejects the raw rank-to-size inequality for general circuits. The weaker logarithmic inequality survives these six examples, which supplies neither its general proof nor a permanent lower bound.

**Next decision.** Abandon raw flattening rank as an unrestricted circuit-size bound and test any replacement measure against reuse and products first.

**Background.** [Background source 1](https://www.scottaaronson.com/papers/pnp.pdf)

### 89. Efficient classical integer factoring

**Status:** Attempted approach failed

**Attempt performed.** Executed a revealed-prefix enumeration control on fifty balanced eight-bit semiprimes and derived its exact candidate-count formula, explicitly charging for searching unknown prefixes.

**Result.** Revealing 1,2,4,6 leading bits leaves 64,32,8,2 odd candidates. Enumerating all admissible prefixes always returns the original set of 64 odd eight-bit candidates.

**Evidence.** 2^(t−1)·2^(L−t−1)=2^(L−2); computation_batch_results.json, item 89 stores factors, prefixes, and recovered divisors.

**Limit.** The calculation rejects treating the prefix as free in this plain enumeration baseline. It does not analyze a chosen lattice theorem or prove any lower bound for classical factoring.

**Next decision.** Select an explicit partial-information lattice theorem and compare its total cost with this fully charged enumeration control.

**Background.** [Background source 1](https://www.scottaaronson.com/papers/pnp.pdf)

### 90. Polynomial-time graph isomorphism

**Status:** Finite computation verified

**Attempt performed.** Constructed the specified rook and Shrikhande graphs, computed an edge-neighborhood invariant, and verified it under one hundred random relabelings of each graph.

**Result.** Both graphs have degree six and two common neighbors per distinct pair. Those common neighbors are adjacent for every rook edge and nonadjacent for every Shrikhande edge, giving signatures {1:48} and {0:48}.

**Evidence.** computation_batch_results.json, item 90; computation_batch.py, graph90 and signature90.

**Limit.** The invariant rigorously distinguishes this known pair and survives relabeling. Success on two strongly regular graphs is not an algorithm or complexity bound for arbitrary graph isomorphism.

**Next decision.** Find a pair sharing this invariant to identify the next concrete information the proposed method would need.

**Background.** [Background source 1](https://www.scottaaronson.com/papers/pnp.pdf)

### 91. Unique Games Conjecture

**Status:** Finite computation verified

**Attempt performed.** Enumerated all 3^8 assignments on the 24 prescribed unique-game instances and derived the exact optimum criterion for arbitrary permutation constraints around a cycle.

**Result.** Every C8 optimum is 8/8 or 7/8, exactly as predicted by whether the composed permutation has a fixed point. Nonidentity K8 instances attain between 18/28 and 20/28.

**Evidence.** computation_batch_results.json, item 91 records constraints and optimal assignments; computation_derivations.txt gives the cycle proof.

**Limit.** The exhaustive optima provide a correctness baseline, not computational hardness. The proposed SDP comparison was not executed, and no integrality-gap claim follows from these exact values alone.

**Next decision.** Use the saved optima to validate a precisely encoded SDP and distinguish numerical outputs from certified bounds.

**Background.** [Background source 1](https://www.math.ias.edu/files/Book-online-Aug0619.pdf)

### 92. Quantum PCP conjecture

**Status:** Restricted statement proved

**Attempt performed.** Derived operator inequalities for the specified positive-product gadget and exactly evaluated its commuting four-projector control on all sixteen computational basis states.

**Result.** For 0≤hi,hj≤I, hi≤Gij≤I and ker(Gij)=ker(hi)∩ker(hj). Normalized ground energy cannot decrease. In the four-projector control the normalized spectral gap rises from 1/4 to 1/2.

**Evidence.** Gij=2hi−hi²+(I−hi)hj(I−hi); computation_derivations.txt, item 92; computation_batch_results.json, item 92.

**Limit.** The lemma preserves common zeros and gives one-sided energy control. It does not construct an iterated constant-promise-gap reduction preserving QMA-hardness; the control's spectral gap is a different quantity.

**Next decision.** Determine the locality and promise-gap behavior under repeated application before proposing amplification of hard instances.

**Background.** [Background source 1](https://arxiv.org/abs/2510.01333)

### 93. Matrix multiplication exponent

**Status:** Restricted statement proved

**Attempt performed.** Screened all 18,424 three-summand sub-tensors of the fixed Strassen tensor square; the captain independently certified an actual nonzero 3×3 flattening minor for every triple.

**Result.** Every triple has a rank-three flattening. Therefore no exact three-to-two replacement exists over Q or C while the other 46 summands remain fixed, without any coefficient-alphabet restriction.

**Evidence.** computation_priority_results.json, item 93; captain_strassen_minor_certificates.json; captain_priority_audit.py; computation_derivations.txt.

**Limit.** This closes the proposed local move for this decomposition. It neither proves the full tensor has rank 49 nor excludes replacements involving more summands or global decompositions, and says nothing decisive about ω=2.

**Next decision.** Drop the three-to-two search and specify a genuinely larger replacement move with a new necessary-condition screen.

**Background.** [Background source 1](https://arxiv.org/abs/1610.08364)

### 94. Exponential Time Hypothesis

**Status:** Attempted approach failed

**Attempt performed.** Ran both specified DPLL rules on 500 seeded formulas, checked their decisions against exhaustive truth tables, and logged the proposed clause-count potentials after propagation.

**Result.** All 1,000 decisions agree. Total recursive calls are 2,751 versus 2,308. Explicit branches make n+(1/2)m2 rise from 8 to 17/2 and n+(1/4)m2 rise from 8 to 33/4.

**Evidence.** computation_batch_results.json, item 94 contains original/residual clauses and increasing-potential witnesses; computation_derivations.txt.

**Limit.** These witnesses reject monotonicity of both weighted potentials, while the runtime totals describe only this finite sample. Neither a favorable sample average nor a corrected fixed-base recurrence would settle ETH.

**Next decision.** Redesign the potential and prove its change symbolically for all permitted branch types before fitting a recurrence.

**Background.** [Background source 1](https://www.scottaaronson.com/papers/pnp.pdf)

### 95. Planted clique conjecture

**Status:** Finite computation verified

**Attempt performed.** Generated 480 benchmark graphs using separate training and testing seeds, fitted the predefined upper-threshold detectors only on training data, and evaluated held-out confusion counts.

**Result.** Across six settings, edge and signed-triangle detectors classify between 17 and 27 of 40 test graphs correctly. Exact combinatorial identities for both statistics passed eight additional direct small-graph checks.

**Evidence.** computation_batch_results.json, item 95 includes integer statistics, planted sets, thresholds, and confusion counts; computation_derivations.txt derives null moments.

**Limit.** These are small finite detection experiments with mixed outcomes, not clique recovery or asymptotic evidence sufficient to accept or refute the planted-clique conjecture. Test data were not used for threshold selection.

**Next decision.** Use the derived signal-to-noise scaling to decide whether these baseline statistics merit a larger preregistered study.

**Background.** [Background source 1](https://arxiv.org/abs/1806.07508)

### 96. Mandelbrot local-connectivity conjecture

**Status:** Attempted approach failed

**Attempt performed.** Checked the exact bounded-combinatorics hypothesis in the primary MLC theorem, then constructed a concentric-annulus stress test for replacing its uniform bound by pointwise positivity.

**Result.** Choosing moduli m_j=2^(−j−1)>0 gives r_N=r0·exp(−2π(1−2^(−N))) and limiting radius r0·exp(−2π)>0. Positive modulus at every scale alone therefore does not force shrinking.

**Evidence.** computation_batch_results.json, item 96; computation_derivations.txt; Dudko–Lyubich §1.2, Theorems A–B.

**Limit.** The explicit disks are geometric controls, not renormalization domains or counterexamples to MLC. The theorem's constant depends on a fixed combinatorial bound and its parameter conclusion also invokes rigidity.

**Next decision.** Identify a justified nonsummable modulus estimate for the proposed extension and retain a separate parameter-transfer proof obligation.

**Background.** [Background source 1](https://arxiv.org/abs/2512.24171); [Background source 2](https://arxiv.org/html/2309.02107v2#S1.SS2)

### 97. Density of hyperbolicity for complex quadratic polynomials

**Status:** Finite computation verified

**Attempt performed.** Converted the fixed-point and genuine two-cycle multiplier conditions into exact rational inequalities and evaluated every entry of the three specified grids near −3/4.

**Result.** Thirty entries have certified attracting fixed points and thirty have certified attracting two-cycles. Fifteen remain unclassified, including the three repeated parabolic centers; none of those centers was accepted.

**Evidence.** computation_batch_results.json, item 97 stores rational margins; computation_derivations.txt proves the square-root elimination used for fixed points.

**Limit.** There are 75 listed entries, with repeated centers, rather than 75 distinct parameters. Low-period nonacceptance is not a proof of nonhyperbolicity and supplies no density theorem for general complex parameters.

**Next decision.** Preserve these exact certificates as controls when extending the search to higher periods or nearby unclassified parameters.

**Background.** [Background source 1](https://arxiv.org/abs/0805.1658)

### 98. Furstenberg's ×2, ×3 measure conjecture

**Status:** Attempted approach failed

**Attempt performed.** Tried an asymptotic contradiction using invariance along the multiplicative Fourier orbit and the vanishing Cesàro square-coefficient average for nonatomic measures; counted the forced orbit exactly.

**Result.** There are 142 positive frequencies 2^a3^b≤10^6. Their forced contribution is only O(log²N/N), so even a fixed nonzero coefficient on this orbit does not contradict the vanishing average.

**Evidence.** computation_batch_results.json, item 98; computation_derivations.txt gives the orbit bound and a dominated-convergence proof of the nonatomic average.

**Limit.** This is a new failed cross-scale counting argument after the earlier finite-grid obstruction. It constructs no non-Lebesgue invariant nonatomic measure and does not resolve interactions with positive definiteness or ergodicity.

**Next decision.** Seek a mechanism forcing positive-density Fourier information or another stronger constraint, rather than repeating sparse-orbit counting.

**Background.** [Background source 1](https://arxiv.org/abs/2410.22701)

### 99. Brennan's conjecture

**Status:** Finite computation verified

**Attempt performed.** Evaluated the integrability exponent exactly for all sixteen prescribed local corner models and generated their 96 symbolic cutoff-integral expressions, treating the logarithmic case separately.

**Result.** Thirteen models converge, two diverge by a power, and one diverges logarithmically. The classification is determined by the rational sign of β=2+p(1/α−1), without numerical extrapolation.

**Evidence.** I/π=α^(1−p)(1−δ^β)/β for β≠0; computation_batch_results.json, item 99; computation_derivations.txt handles β=0.

**Limit.** These calculations concern the explicit local power maps. They supply neither global distortion estimates nor Brennan's conjecture for arbitrary domains; no numerical quadrature was performed or claimed.

**Next decision.** Identify a concrete multiscale domain where summing the verified local contributions introduces a new controllable difficulty.

**Background.** [Background source 1](https://arxiv.org/abs/2604.12240)

### 100. Hilbert's sixteenth problem, limit-cycle part

**Status:** Restricted statement proved

**Attempt performed.** Derived the first Melnikov integral, computed both endpoint controls symbolically, and used continuity to test the actual rational perturbation pair (a,b)=(−1/10,1).

**Result.** At the separatrix I0→6/5 and I1→6/35; their ratio tends 1/7 and tends 0 at the center. Thus M=I1−I0/10 has at least one interior zero, with positive separatrix limit 9/175.

**Evidence.** computation_priority_results.json, item 100; computation_derivations.txt; captain_priority_audit.py and captain_priority_audit.json independently check the integrals.

**Limit.** The argument establishes an interior first-Melnikov zero, without simplicity, uniqueness, or a limit-cycle count. It provides no uniform bound for polynomial vector fields and does not solve Hilbert's sixteenth problem.

**Next decision.** Test and then prove simplicity or controlled multiplicity of the interior zero before interpreting it as a cycle bifurcation.

**Background.** [Background source 1](https://arxiv.org/abs/2411.09594)

## Appendix: complete statement and proof for #81

## Exact minimum support in the six-bit, width-two benchmark

**Result.** The minimum size of a nonempty uniform sampling support with worst-case absolute acceptance error at most **1/4** is **8**, for the precise finite model below. The lower bound is elementary; the upper bound is verified by exhaustive exact computation over a completely characterized class. No novelty claim is made.

### Model and claim

A program reads six bits exactly once in the order x1, x2, x3, x4, x5, x6. Each layer has two states, labeled 0 and 1. The initial state is 0. Each layer has an arbitrary deterministic transition from the current state and input bit to the next state. Any subset of the final two states may accept.

Let C be the resulting class of Boolean functions on {0,1}^6. A support S contains distinct six-bit strings, sampled uniformly. Its error is

\[
 E(S)=\max_{f\in C}\left|\frac{1}{|S|}\sum_{x\in S}f(x)-\frac{1}{64}\sum_{x\in\{0,1\}^6}f(x)\right|.
\]

The assertion is that the minimum of |S| over nonempty supports satisfying E(S) <= 1/4 equals 8.

### Lower bound: seven points cannot suffice

Every affine parity f(x)=a dot x + b, computed modulo two, belongs to C. A program stores the running parity in its two states; the constant b can be incorporated into the first transition or final acceptance. Every nonconstant affine parity is balanced on the full domain, so its uniform acceptance probability is 1/2.

If S has at most six points, its affine span over F2 has dimension at most five. There is therefore a nonconstant affine parity that is constant on S. Its error is 1/2, exceeding 1/4.

Now suppose S has seven points. If they are affinely dependent, their affine span again has dimension at most five, giving the same obstruction. Otherwise they are affinely independent. Evaluation at these seven points is then an invertible linear map from the seven-dimensional space of affine functions on F2^6 to F2^7. Consequently, an affine parity exists that equals 1 at one selected point and 0 at the other six. It is nonconstant because those values differ. Its error is

\[
 \left|\frac17-\frac12\right|=\frac5{14}>\frac14.
\]

Thus every qualifying uniform support has at least eight points. This argument excludes all smaller supports, not just supports visited by the numerical solver.

### Upper bound: an exactly verified eight-point support

Take

| Integer | Six-bit string |
|---:|:---|
| 0 | 000000 |
| 4 | 000100 |
| 13 | 001101 |
| 14 | 001110 |
| 26 | 011010 |
| 31 | 011111 |
| 33 | 100001 |
| 35 | 100011 |

Exact enumeration and rational arithmetic give E(S)=1/4. For example, the function that accepts precisely when x1=x2=x5=0 accepts three of these eight strings and eight of all 64 strings. Its error is 3/8 - 8/64 = 1/4, so the stated maximum is attained.

The upper-bound verification covers every function in C, using the following complete enumeration rather than trusting the optimization solver.

1. At each prefix cut, a width-two program has at most two distinct suffix residual functions. Conversely, if a function satisfies that property at every cut, use the residual functions as states, their restrictions as transitions, and the constant residual 1 as the accepting terminal state. This constructs a program in the stated model.
2. For efficient enumeration, retain unordered pairs (a,b) of truth tables jointly realizable from the two possible states of a shared suffix program. At suffix length zero these pairs are (0,0), (0,1), (1,1). State relabeling makes ordering unnecessary.
3. Given a realizable pair on r suffix bits, a new preceding state can select either residual for input 0 and either residual for input 1. Its truth table is lo + 2^(2^r) hi, where lo and hi each belong to {a,b}. Any pair, allowing repetition, among the four resulting tables is jointly realizable. Conversely every preceding transition layer has this form, establishing completeness by induction.
4. Continue through five suffix bits, then select one resulting function from the fixed initial state for the sixth bit. The intermediate pair counts are 10, 52, 304, 1,816 and 10,888. The resulting six-bit class has exactly **18,664 distinct functions**.
5. For each of those functions, evaluate both means in E(S) with exact integers and rational numbers. Their maximum is **1/4**. Every enumerated function also passes the per-cut residual-width test. An independently constructed transition-block enumeration produced exactly the same class.

This upper bound and the preceding lower bound prove that the finite optimum is 8, with the upper bound depending on the documented exhaustive computation.

### Reproduction and limits

`method_oracle.py` implements the backward recurrence and exact support verifier. `method_oracle_functions.json` contains the complete function list; `method_candidate_8_verification.json` records this support, its strings, complete-class check, exact maximum, and a witnessing function. Truth-table bit x is the value at integer x, with x1 the most significant input bit.

To repeat the check in Python, import `enumerate_functions` and `verify_support` from `method_oracle`, regenerate the six-bit class, and pass the eight integers above to `verify_support`.

The solver supplied a candidate; solver status is not used to prove optimality. The proof concerns uniform sampling on distinct strings in this six-bit ordered width-two model. It does not establish a general pseudorandom generator, any asymptotic derandomization result, or a resolution of P versus BPP. Verification occurred within an AI-assisted workflow, not through external human peer review or a formal proof assistant.
