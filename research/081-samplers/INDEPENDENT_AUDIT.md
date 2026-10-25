# Independent sampler audit — 20 October 2026

## Verified conclusion

The old claim “the optimum is 8” and newer claim “11 points cannot suffice” concern different classes: the former fixes the shared order x1,…,x6 and the latter must fool programs in every possible fixed order. The first claim has been independently reproduced here. The second needs a separate proof; I independently read `proof_review/independent_lower_bound_proof.md` in full and found no logical gap in that reconstruction. This is an independent AI-workflow logical review, not formal proof-assistant certification.

For the fixed common order, the exact minimum is 8 for distinct, equally weighted samples and absolute error at most 1/4. Allowing all variable orders enlarges the function class from 18,664 to 1,156,000. The previously published 8-point support has error 1/2 against this enlarged class.

## Bit convention

External strings list **x1 as the leftmost bit**, and an external integer uses ordinary binary notation. The internal enumeration instead places x1 in bit0, so an external integer is bit-reversed before verification. This conversion is explicit in `original_support_verification.json`.

Original support, in the external convention:

`000000, 000100, 001101, 001110, 011010, 011111, 100001, 100011`

Integers: `0, 4, 13, 14, 26, 31, 33, 35`.

Its verified maximum fixed-order error is 128/512 = 1/4. All functions in the class were tested; this conclusion does not rely on a solver's feasibility tolerance.

## Complete enumeration

Represent a Boolean function by its truth table as an integer. For a prefix function f, the next input bit can produce either of the four state transformations 0, 1, f, or 1−f, independently on each input value. Thus the next truth table is `(g0(f), g1(f))`, with g0,g1 from those four choices. Induction shows both that every constructed function is realizable and that every allowed transition sequence is covered. A final accepting subset can be absorbed into the last transition; constants are included.

| Bits | Fixed common order | Any fixed variable order |
|---:|---:|---:|
| 1 | 4 | 4 |
| 2 | 16 | 16 |
| 3 | 88 | 152 |
| 4 | 520 | 2,368 |
| 5 | 3,112 | 47,688 |
| 6 | 18,664 | 1,156,000 |

For the all-order class, the recurrence is applied to every subset of input variables, choosing each variable of that subset in turn as the final read. This is an exact union over all fixed orders, without requiring a permutation of variables chosen adaptively from the input.

`audit_fixed.py` implements the fixed-order enumeration. `all_orders.py` implements the separate subset recurrence. Both were executed successfully. The truth tables are retained as NumPy uint64 arrays.

## Lower bound for the fixed-order optimum

Every affine parity belongs to the fixed-order width-two class and every nonconstant affine parity has uniform mean1/2.

For a support of at most6 points in F2^6, the affine span has dimension at most5. A nonconstant affine parity therefore vanishes on every sample, giving error1/2.

For7 points, choose a nonconstant affine parity vanishing on the first6 points. Such a parity exists by the same dimension argument. It is1 on at most one of the7 points, so its error is at least1/2−1/7=5/14>1/4.

Hence no support of at most7 points works. The exact check of the displayed8-point support supplies the matching upper bound.

## Explicit demonstration that order matters

A separately found8-point support, with x1 leftmost, is:

`000000, 110100, 110010, 101110, 111001, 111101, 101011, 000111`.

It has fixed-order error1/4. The function

`f(x) = 1 XOR x3 XOR x4 XOR (x2 AND x4) XOR x6`

is1 at all eight points and has uniform mean1/2. It is a width-two program in order x1,x2,x4,x3,x5,x6: ignore x1, remember x2, update to x4 AND(1 XOR x2), XOR x3, ignore x5, and XOR x6 with complemented final acceptance. Thus its all-order discrepancy is1/2. Every numerical statement in this paragraph was checked exactly.

## Scope and evidence limits

This is an independent AI-workflow reproduction with a short mathematical lower bound and an exhaustive finite upper-bound check. It is not external human peer review, proof-assistant certification, an asymptotic pseudorandom-generator construction, or a novelty finding.

The 12-point all-order feasibility search is exploratory. A solver timeout or failure to locate a support does not establish nonexistence. Any candidate reported as successful must pass the full integer verifier over all1,156,000 functions.

Two bounded searches were executed. The first used seed731, a small random objective, fixed-order initial constraints, and30-second subproblem caps. Two candidates failed exact all-order checking; the next subproblem timed out without a candidate. The second used a zero objective, all fixed-order and balanced-quadratic constraints, and a45-second cap; its first subproblem timed out without a candidate. **Whether12 points suffice remains unresolved by these searches.** NumPy2.3.5 and SciPy1.17.0 were used. The second run and its exact options are retained in `search_allorders.py` and `search_allorders_k12.json`.

## Cross-review of the Hadamard extension calculation

I reviewed `hadamard_audit/extend_and_repair.py` and its output. The pair-correlation bucket enumeration is complete for ordered normalized quadruples. Prefix deduplication preserves the existential extension condition. Periodic autocorrelation symmetry justifies checking half the nonzero shifts. The breadth-first expansion uses only the previous layer, so its layers are exact Hamming-distance balls; removing previously reached parents gives exact minimum-distance frequencies.

The model allows repaired length-n prefixes to lose complementarity temporarily: the original parent and final length-(n+2) quadruple must be complementary. Rows and positions remain fixed, first signs stay+1, and only noninitial old signs may flip.

As an independent small control, I directly enumerated every ordered normalized quadruple at lengths3 and5, evaluated **all** nonzero periodic shifts, and obtained108 and7,500 valid quadruples. The length5 quadruples have254 distinct normalized length3 prefixes, including all108 valid length3 parents. These agree with the separate bucket implementation. The check is saved in `hadamard_small_independent.json`.
