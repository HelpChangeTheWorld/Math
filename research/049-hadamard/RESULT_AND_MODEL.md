# Length-seven sign repair: an exact finite answer

## Result and status

In the model below, every valid normalized, ordered quadruple of length-seven sign sequences has a valid length-nine extension after at most three changes to old signs. The maximum minimum repair cost is exactly three.

This is an exhaustive finite computational result from 20 October 2026. The general Hadamard conjecture is not proved, no arbitrary-length induction is supplied, and originality is unverified. Another AI agent reviewed coverage and distance logic. A separate direct checker certifies a witness requiring three changes.

## Frozen model

Each of four ordered rows is a sequence of +1 or -1 signs of odd length n. Its first sign is +1. For every nonzero cyclic shift t, compute
C_s(t) = sum over j=0,...,n-1 of s[j] s[(j+t) mod n].
A quadruple is periodically complementary when the four correlations sum to zero at each shift.

An extension appends exactly two independently chosen signs to each row. A repair may flip old signs other than the first sign of each row. Row order and sign positions are fixed. The repaired old prefix does not have to remain complementary; the original parent and the final extended quadruple must be complementary. This distinction is part of the theorem.

Counts below concern ordered normalized quadruples, not equivalence classes of Hadamard matrices.

## Exact enumeration

| Parent length | Valid parents | Need 0 flips | Need 1 flip | Need 2 flips | Need 3 flips |
|---|---:|---:|---:|---:|---:|
| 3 -> 5 | 108 | 108 | 0 | 0 | 0 |
| 5 -> 7 | 7,500 | 7,092 | 408 | 0 | 0 |
| 7 -> 9 | 336,140 | 259,844 | 73,644 | 2,640 | 12 |

There are 19,656,756 valid normalized length-nine quadruples. Their length-seven prefixes cover 7,525,024 of the 16,777,216 possible normalized length-seven quadruples. Hamming-distance expansion from that prefix set, restricted to the 24 allowed old-sign coordinates, supplies the minimum repair counts for valid parents.

The complete inventory of the 12 parents needing three changes is preserved in results.json. No valid length-seven parent remains unclassified.

## One independently certified difficult parent

A = B = C = (+, -, -, -, +, +, -)
D         = (+, +, +, -, +, +, +)

The six nonzero-shift correlation sums are all zero.

An exhaustive direct check considers every 256 appended-sign assignment after:
- no old changes: 256 candidates;
- each of 24 single changes: 6,144 candidates;
- each of C(24,2)=276 two-sign changes: 70,656 candidates.

All 77,056 candidates fail. This checker uses direct arrays and all eight nonzero shifts of the target length; it imports no bucket search or bit encoding.

Change row A positions 2 and 6, and row B position 7 (positions here start at 1), and append the following signs:
A' = (+, +, -, -, +, -, -, +, -)
B' = (+, -, -, -, +, +, +, +, +)
C' = (+, -, -, -, +, +, -, +, -)
D' = (+, +, +, -, +, +, +, -, +)

All eight nonzero-shift sums of this length-nine quadruple are zero. Thus the minimum cost for this parent is exactly three.

## Why the exhaustive algorithm covers the model

For odd n, periodic correlation at shift t equals correlation at n-t. Checking shifts 1 through (n-1)/2 is therefore sufficient. All normalized individual rows are enumerated. Every ordered row pair is placed in a bucket indexed by its summed correlation vector. Combining a bucket with the negative-vector bucket yields exactly all valid ordered quadruples.

For extensions, a valid length-(n+2) quadruple supplies an extendable length-n prefix. Deduplicating equal prefixes within a bucket preserves existence. The resulting Boolean table therefore marks precisely the prefixes with some zero-repair extension.

Each distance round starts from the previous reachability table and includes each one-coordinate flip. After d rounds, the marked prefixes are exactly those within Hamming distance d of an extendable prefix. Counts are taken only for valid original parents and after removing those seen at smaller distances, so the histogram measures minimum changes.

All correlation and set-membership operations are integer or Boolean. No floating-point approximation enters the enumeration.

## What follows, and what does not

The former untested question 'Do three changes suffice at length seven?' has an exact finite answer: yes, in this stated model, and three are sometimes necessary.

A claim for length nine, arbitrary odd length, or repairs that preserve complementarity at every intermediate step would be a different statement. No such claim is made here. The next useful work is to explain the exceptional parents structurally and formulate a longer-length claim before committing to a larger exhaustive computation.

Relevant background: Cati and Pasechnik, Implementing Hadamard Matrices in SageMath, https://arxiv.org/abs/2306.16812. This background source does not establish novelty of the present finite repair classification.

Current-status update: Epoch's solution-update section reports a construction at order 668 and the formerly unknown admissible orders through 2000, while the general Hadamard conjecture remains open. https://epoch.ai/frontiermath/open-problems/hadamard . Its older 'About' paragraph contains a stale smallest-open-order sentence; the newer update controls the research baseline.

