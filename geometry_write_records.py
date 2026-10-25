"""Package executed calculations and explicit restricted arguments; no experiments invented."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
original=json.loads((ROOT.parent/'math_revision2/all_100_proposals.json').read_text())
original={x['id']:x for x in original}
records=[]
def add(i,attempt,result,evidence,status,scope,next_decision,extra=()):
    records.append(dict(id=i,title=original[i]['title'],attempt=attempt,result=result,
        evidence=evidence+[f'geometry_calculations.json (item {i})'],status=status,
        scope_limit=scope,next_decision=next_decision,
        source_urls=list(dict.fromkeys([original[i]['source_url']]+list(extra)))))

add(56,
"Computed the critical points and pole-chart Hessians of the height function on the standard unit sphere S4 in R5, making the simplest handle certificate explicit.",
"There are exactly two critical points. Their Hessians are I4 and −I4, so the Morse indices are 0 and 4 and the associated handle description has one handle of each index.",
["h±(x)=±sqrt(1−|x|²); Hess h±(0)=∓I4."],
"proved_restricted_statement",
"This verifies the standard sphere only; it extracts no certificate for an arbitrary homotopy sphere or a published four-dimensional candidate.",
"Retain this calibration; a candidate-specific proof needs an actual handle description and justified simplifications.")

add(57,
"Constructed explicit parametrizations of both closed hemispheres bounded by the standard equatorial S3 in S4, and checked the sphere equation and inverses algebraically.",
"Each hemisphere is smoothly diffeomorphic to the closed four-ball. The denominator in the inverse is at least one on its matching hemisphere, including the boundary.",
["Φ±(y)=(2y/(1+r),±(1−r)/(1+r)), r=|y|²≤1.","4r+(1−r)²=(1+r)²; inverse y=x/(1±t)."],
"proved_restricted_statement",
"The embedding is the standard equator. This gives no straightening map for a general smooth embedded three-sphere.",
"Use these maps to validate boundary conventions before attempting a nonstandard embedding.")

add(58,
"Built a balanced two-generator presentation using eight elementary Andrews–Curtis moves from the trivial presentation, then executed and logged every inverse move with exact free reduction.",
"The resulting presentation reduces back to the ordered relators x and y. The saved certificate contains the starting words, all eight reducing moves, and every intermediate state.",
["geometry_calculations.py: apply_move, inverse_move, reduce_word; item 58 contains the replayable word certificate."],
"finite_verified",
"This deliberately generated example is known trivial by construction. No hard published candidate or stabilization question was resolved.",
"The move checker is ready; the next substantive input must be an independently specified candidate presentation.")

add(59,
"Examined the explicit disk (u,v,0,0) inside the unit four-ball and computed the radial Morse function to certify the ribbon condition for its boundary unknot.",
"The restricted squared radius is u²+v². Its only interior critical point is a nondegenerate minimum; there are no interior maxima. Thus the disk is an explicit ribbon disk.",
["∇r²=(2u,2v), Hess(r²)=2I2; boundary u²+v²=1."],
"proved_restricted_statement",
"This solves only the unknot calibration and says nothing about a nontrivial slice candidate. No failed search is being interpreted as non-ribbonness.",
"Move to a specified slice knot only after its slicing certificate and diagram are available.")

add(60,
"Multiplied the trefoil Jones polynomial by itself using exact integer convolution, then compared its breadth with the six-crossing connected-sum diagram.",
"The product has lowest exponent 2 and highest exponent 8. Jones breadth gives a lower bound of six crossings, matching the diagram upper bound, so two trefoils have additive crossing number.",
["(t+t³−t⁴)²=t²+2t⁴−2t⁵+t⁶−2t⁷+t⁸; 6≤c(T#T)≤6."],
"proved_restricted_statement",
"This is a familiar alternating example. The polynomial breadth need not attain crossing number for general knots.",
"Retain this exact control; a wider proof needs a lower bound effective when Jones breadth is deficient.",
["https://arxiv.org/abs/0907.5374"])

add(61,
"Derived the first homology of Dehn filling and applied it to every reduced slope p/q with −4≤p≤4 and 1≤q≤4.",
"There are 23 slopes and 253 unordered pairs. Different absolute numerators eliminate 198 pairs for every knot; 55 pairs survive this necessary homological filter.",
["H1(S3_{p/q}(K);Z)=Z/pZ because the longitude vanishes in exterior homology and filling kills pμ; p=0 gives Z."],
"finite_verified",
"Equal homology does not imply homeomorphism, and the surviving pairs are not verified cosmetic surgeries. The filter ignores orientation-sensitive invariants.",
"Apply stronger surgery invariants only to surviving pairs for a specified knot.")

add(62,
"Evaluated the figure-eight colored Jones root-of-unity product formula at N=20,40,80 using independently repeated 70-digit and 130-digit Decimal calculations.",
"The scaled logarithms are approximately 3.36473742636, 2.85816821563, and 2.52511086864. Both precision runs agree within 10^−65; these finite values remain above the known volume 2.02988321282.",
["J_N=Σ(k=0..N−1) Π(j=1..k)4sin²(πj/N); output is (2π/N)log J_N."],
"unresolved_attempt",
"Precision agreement is numerical validation, not a rigorous interval enclosure. Three terms do not prove convergence, and the figure-eight case is already known.",
"Use this normalization control before evaluating a new knot; do not extrapolate a proof from the trend.")

add(63,
"Translated the 11/8 inequality and the older Furuta 10/8+2 inequality into exact integer conditions for forms 2k(−E8)⊕lH, then tabulated k=1 through 8.",
"The target becomes l≥3k, while the older bound gives l≥2k+1. The interval between them contains 28 pairs in this finite table; k=1 has no gap.",
["b2=16k+2l, σ=−16k; 11|σ|/8=22k; (10/8)|σ|+2=20k+2."],
"proved_restricted_statement",
"These are arithmetic gaps in one older bound, not realizable manifolds or a list of currently undecided forms. Stronger known restrictions were deliberately not applied.",
"Any realizability investigation must first apply the strongest known form-specific obstructions.")

add(64,
"Proved the torus-to-torus case directly using equivariant lifts and checked an explicit five-dimensional integral automorphism and its inverse by exact matrix multiplication.",
"A homotopy equivalence f:Tn→Tn inducing A∈GL(n,Z) is homotopic to the linear homeomorphism induced by A. The straight-line homotopy of lifts respects every integer translation.",
["H_s(x)=(1−s)F(x)+sAx; H_s(x+z)=H_s(x)+Az; saved 5×5 matrices satisfy AA^−1=I."],
"proved_restricted_statement",
"Both manifolds here are tori. This does not prove rigidity for an arbitrary manifold merely homotopy equivalent to a torus, or for other aspherical manifolds.",
"Keep the lift argument as a control; the missing step is geometric identification of a general source manifold.")

add(65,
"Worked out every possible higher signature in dimension two, where positive-degree components of the Hirzebruch L-class cannot contribute.",
"For closed oriented surfaces and an orientation-preserving homotopy equivalence h, naturality of cohomology pairing proves the required equality for every degree-two group-cohomology class; all other degrees contribute zero.",
["L(M)=1; ⟨(f∘h)*a,[N]⟩=⟨f*a,h_*[N]⟩=⟨f*a,[M]⟩."],
"proved_restricted_statement",
"This is the elementary surface case. It does not control positive-degree L-classes in higher dimensions or establish the general conjecture.",
"Any extension must address those higher characteristic classes rather than reuse dimension-two vanishing.")

add(66,
"Specialized the Farrell–Jones assembly map to the infinite dihedral group and checked its explicit semidirect-product relation.",
"The group Z⋊C2 contains Z with index two, so it is virtually cyclic. Consequently a point is a model for E_VCyc(G), and the assembly map is literally the identity.",
["(n,ε)(m,δ)=(n+(−1)^εm,ε+δ mod2); rtr=t^−1; E_VCyc(G)=point."],
"proved_restricted_statement",
"This is an immediate known base case, not a new assembly calculation for a group outside the virtually cyclic family.",
"A nontrivial next attempt needs a specified group for which E_VCyc(G) is not already a point.")

add(67,
"Constructed an explicit rational polynomial realization of the finite group S3 and checked the two decisive algebraic conditions.",
"The polynomial x³−2 is Eisenstein at 2, hence irreducible. Its discriminant is −108, which is not a rational square; the transitive cubic Galois group is therefore S3.",
["disc(x³+ax+b)=−4a³−27b²; a=0,b=−2 gives −108."],
"proved_restricted_statement",
"This is a standard realization of one already realizable group. It supplies no construction for arbitrary finite groups and no new regular extension.",
"Use this example to validate a Galois-group certificate format before choosing a genuinely unresolved group-realization target.")

add(68,
"Enumerated the split quadric x0x1−x2x3=0 over F7 and combined its point count with the intersection pairing of its two rational rulings.",
"Exactly 64 of the 400 projective points lie on the quadric. Its two rulings have intersection matrix [[0,1],[1,0]], hence independent classes; the product P1×P1 description shows they span H².",
["#Q(F7)=64=(7+1)²; det intersection matrix=−1; both ruling cycles are defined over F7 with Qℓ coefficients, ℓ≠7."],
"proved_restricted_statement",
"This proves the divisor Tate statement for this split quadric using its known product decomposition, not from point counts alone.",
"A non-split surface requires actual Frobenius and cycle calculations instead of this product argument.")

add(69,
"Computed the Lefschetz operator for the complex abelian surface E×E with product polarization, then supplied algebraic correspondences realizing its inverse.",
"In the saved bases H1→H3 is a permutation matrix squaring to identity. Integration on either elliptic factor, represented by E×E times the other diagonal, gives inverse correspondences whose sum inverts this map.",
["h=a1∧b1+a2∧b2; h²=2a1∧b1∧a2∧b2. The H4→H0 inverse has coefficient 1/2.","geometry_restricted_proofs.md, item 69."],
"proved_restricted_statement",
"This verifies one complex product-polarized surface. Matrix inversion alone would not suffice without the exhibited algebraic cycles.",
"Retain the correspondence certificate; extending to other varieties requires analogous algebraic inverse operators.")

add(70,
"Derived the canonical section counts on X=C×C×E×E, with genus-two C given by y²=x⁵−1 and elliptic E by y²=x³−x.",
"K_X pulls back the globally generated canonical bundle on C×C, hence is nef and semiample. Riemann–Roch and Künneth give h0(mK_X)=(2m−1)² for m≥2; m=0..6 yield 1,4,9,25,49,81,121.",
["h0(C,mK_C)=2m−1 for m≥2; h0(E,mK_E)=1; numerical dimension ν(K_X)=2.","geometry_restricted_proofs.md, item 70."],
"proved_restricted_statement",
"This is an explicit product fourfold. Its canonical map at m=1 includes genus-two hyperelliptic maps; it is not an embedding of C×C.",
"Use the exact count as a control; a non-product nef canonical divisor needs a different semiampleness argument.")

add(71,
"Tested the logical inference that a strictly decreasing nonnegative real progress measure would force every flip sequence to terminate.",
"The exact recurrence x0=1 and x_(n+1)=x_n/(1+x_n) gives x_n=1/(n+1). Eleven values were computed as fractions, and induction proves an infinite strictly decreasing positive sequence.",
["x_n−x_(n+1)=1/((n+1)(n+2))>0; inf x_n=0 is never reached."],
"failed_approach",
"These numbers are not flips or discrepancies of constructed varieties. The calculation rejects an insufficient termination argument, not the termination conjecture.",
"A proposed geometric measure must also have a proved well-founded value set or another finite-descent mechanism.")

add(72,
"Built exact jet-interpolation matrices for ten explicit integer points and equal multiplicities m=1,2,3, taking maximum prohibited degrees d=3,6,9.",
"The matrices have ranks 10/10, 28/28, and 55/55. Independently evaluated square minors modulo 1009 are 6,984,183; their nonvanishing certifies full column rank in characteristic zero.",
["Points Pi=(i,(i²+i⁵) mod101), i=0..9; geometry_interpolation_certificates.json records every row, column, and selected minor."],
"finite_verified",
"This proves the indicated three multiplicities for very general ten points by openness, including lower degrees by inclusion. It covers neither all multiplicities nor arbitrary point counts.",
"Keep the exact minors; future work must introduce an argument controlling unbounded multiplicity.")

add(73,
"Executed three mixed-multiplicity interpolation tests on ten points and a two-double-point special-case control, with exact modular minor certificates.",
"For (d;m)=(4;2,1⁹),(4;2²,1⁸),(5;2⁵,1⁵), vector-space dimensions are 3,1,1. The conic control has dimension one, with explicit generator (y−2x)² and rank five.",
["geometry_interpolation_certificates.json; in the control E=H−E1−E2, E²=−1, D=2E and D·E=−2."],
"finite_verified",
"The first three maximal-rank results hold for very general points. The special control uses eight zero multiplicities and verifies a familiar doubled-line mechanism only.",
"Use these positive and negative controls before interpreting a rank defect in a broader mixed system.")

add(74,
"Evaluated the six-dimensional Euler form under constant positive sectional curvature, counting its Pfaffian pairings and checking the unit-sphere integral exactly.",
"There are 15 pairings. The Euler density is 15κ³/(8π³) times volume, which is positive when κ>0. Multiplying by Vol(S6)=16π³/15 at κ=1 gives Euler characteristic two.",
["(2π)^−3 Pf(Ω)=15κ³/(8π³)dvol; (15/8)(16/15)=2."],
"proved_restricted_statement",
"This covers constant-curvature six-manifolds via Gauss–Bonnet. Variable positive sectional curvature does not make this substitution legitimate.",
"A broader argument must control the full curvature tensor in the Euler polynomial.")

add(75,
"Applied the exact conformal sectional-curvature formula at a global minimum of an arbitrary smooth conformal factor on the standard product S2×S2.",
"Every metric e^(2f)g_product has a plane with nonpositive curvature: choose a mixed plane at the minimum, where df=0 and Hess f is positive semidefinite. Thus no conformal deformation, of any amplitude, achieves everywhere positive curvature.",
["K_new(X∧Y)=e^(−2f)[−Hess f(X,X)−Hess f(Y,Y)]≤0 at the minimum.","geometry_restricted_proofs.md, item 75."],
"proved_restricted_statement",
"Only the conformal class of the standard product metric is excluded. General nonconformal metrics remain outside the argument.",
"Discard this conformal search family as a route to a positively curved counterexample.")

add(76,
"Constructed and checked a nonzero formal first-derivative tensor for principal curvatures (−3,−1,1,3), enforcing symmetry, differentiated mean/scalar constraints, and the scalar Simons norm identity.",
"The tensor satisfies those necessary constraints with S=20 and |∇A|²=320, yet ∇K=(48√5,0,0,0). Therefore the proposed shortcut from these pointwise constraints to constant Gauss–Kronecker curvature fails.",
["T111=2√5; symmetric T122=−4√5; symmetric T133=2√5; remaining entries zero. |T|²=S(S−4)."],
"failed_approach",
"This formal jet is not a constructed local immersion or compact hypersurface. Higher-order compatibility and global realization were not proved.",
"Any repaired argument must use constraints beyond this verified first-derivative system.")

add(77,
"Derived exact primal and polar volumes for K_t=conv(±e1,…,±e4,±t(1,1,1,1)), throughout t≥1/2, using visible pyramids and clipped-cube integration.",
"The volumes are t+1/4 and 32/(3t)−4/(3t³)+1/(4t⁴). Their product exceeds 32/3 because its gap has an explicitly positive polynomial numerator. At t=1 the product is 575/48.",
["Product−32/3=(16u³+32u²+14u+1)/(48t⁴), u=2t−1≥0.","geometry_restricted_proofs.md, item 77."],
"proved_restricted_statement",
"This proves the bound for one stated centrally symmetric polytope family, not all four-dimensional bodies. No novelty claim is made.",
"Remove this family from counterexample searches; a wider proof needs control beyond its special diagonal symmetry.")

add(78,
"Tested whether the kernel of one convenient locally nilpotent derivation can canonically identify a coordinate in the cancellation strategy.",
"On C[x,y,z]/(xy−z²+1), the explicit derivations δ=(0,2z,x) and ε=(2z,0,y) both preserve the relation and are locally nilpotent. Yet x lies in ker δ while ε(x)=2z≠0.",
["δ(xy−z²+1)=ε(xy−z²+1)=0; δ³y=ε³x=0; saved generator chains certify local nilpotence."],
"failed_approach",
"This surface calculation refutes the single-derivation invariance shortcut. It is not a counterexample to cancellation of complex affine three-space.",
"A canonical invariant must account for all relevant derivations or extra justified structure.")

add(79,
"Specified ten distinct points (i,i²,1) on the smooth projective conic yz−x²=0 and computed the strict transform after blowing up those points.",
"The resulting fixed smooth projective surface contains an irreducible rational curve C with C²=−6. Its canonical intersection is four, and adjunction gives genus zero. Any negativity bound for this surface is at least six.",
["C=2H−ΣEi; C²=4−10=−6; K·C=−6+10=4; 2g−2=−2."],
"proved_restricted_statement",
"One negative curve on one fixed surface does not violate bounded negativity. Allowing the number of blowups to vary changes the surface.",
"Further attempts must seek an unbounded sequence on this same fixed surface, not move the ambient surface.")

add(80,
"Verified D4 covolume two and its 24 shortest vectors, then moved one coset in a two-coset description by s times the first coordinate vector.",
"The original density is π²/16. Two explicit inter-coset vectors give squared minimum distance at most 2−2|s|+s²<2 for 0<|s|<2. At fixed cell volume, rescaling spheres therefore lowers density along this path.",
["D4=L∪(b1+L), L=⟨2b1,b2,b3,b4⟩; vectors ±b1+se1 certify the bound."],
"proved_restricted_statement",
"This is one explicit periodic perturbation control, consistent with known periodic extremality. It neither searches all finite deformations nor proves global packing optimality.",
"Exclude this displacement path from improvement searches; different finite deformations require new certificates.",
["https://arxiv.org/abs/0808.2013"])

assert [r['id'] for r in records]==list(range(56,81))
required={'id','title','attempt','result','evidence','status','scope_limit','next_decision','source_urls'}
for row in records:
    assert set(row)==required
    words=sum(len(row[key].split()) for key in ['attempt','result','scope_limit','next_decision'])+sum(len(v.split()) for v in row['evidence'])
    if not 70<=words<=140: print('Word-count review',row['id'],words)
(ROOT/'geometry_work.json').write_text(json.dumps(records,indent=2,ensure_ascii=False),encoding='utf-8')
print(f'Wrote {len(records)} records to {ROOT / "geometry_work.json"}')
