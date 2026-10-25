# What We Have Found So Far

This file is the short index to the current strongest results in **Help Change The World — Math**.

## Important status statement

We have **not** solved any of the famous parent conjectures in the 100-problem catalog, and we do **not** claim that the finite results below are new to mathematics unless a separate novelty review establishes that.

The project separates:
- ideas,
- numerical or computational experiments,
- exact finite computations,
- mathematical proofs,
- reproduced known results,
- and genuinely new results.

## #81 — Randomness reduction / six-bit samplers

Two different models must be kept separate.

### Fixed common reading order
For deterministic width-two read-once programs on six input bits using one common variable order, the exact minimum uniform support size at error tolerance 1/4 is **8**.

A verified support is:

`{0, 4, 13, 14, 26, 31, 33, 35}`

Seven or fewer are impossible in that model.

### Every allowed reading order
When the sample must work against programs that may choose different fixed reading orders, every support of size **1 through 11** is impossible.

For any 11-point support, an allowed program can have true acceptance probability 1/2 while accepting at most 2 of the 11 sampled inputs. Therefore the error is at least:

`1/2 - 2/11 = 7/22 ≈ 0.31818`

which exceeds the permitted 1/4 error.

**Current frontier:** at least 12 points are necessary. Whether 12 suffice remains unresolved in this project.

See `research/081-samplers/`.

## #49 — Hadamard-related complementary sign-sequence extension

For the precisely defined normalized ordered length-7 to length-9 extension experiment, all **336,140** valid parents were classified by the minimum number of permitted old-sign flips needed before an append-only extension succeeds.

- 0 flips: 259,844
- 1 flip: 73,644
- 2 flips: 2,640
- 3 flips: 12

Thus the maximum minimum repair radius is exactly **3** in this finite model. This does **not** solve the Hadamard matrix conjecture or prove that three flips suffice at arbitrary lengths.

See `research/049-hadamard/`.

## #93 — Matrix multiplication local obstruction

For the specified standard 49-term Strassen square, all **211,876** choices of four complete summands were checked. Each selected four-term subtensor has a certificate obstructing replacement by three terms while the other 45 terms are held fixed.

A later literature comparison found a stronger related reported result, so this is treated as a reproduced finite benchmark rather than a new matrix-multiplication breakthrough.

See `research/093-matrix-multiplication/`.

## The full 100-problem record

`100-PROBLEMS.md` contains the continuation ledger for all 100 original targets: the bounded attempt, historical status, limitation, and next mathematical obligation.

The complete earlier Round 2 report is in `research/100-problem-ledger/Math_Frontiers_Work_Round_2.md`.

## Verification philosophy

Do not trust the headline alone. Each active track includes code, outputs, model definitions, and independent checking artifacts where available. The `verification/` directory records claim scope and environment information. Historical material is preserved under `archive/` rather than silently overwritten.
