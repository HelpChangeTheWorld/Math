# Exact four-term replacement audit: standard Strassen tensor square

## Outcome and interpretation

All 211,876 four-term subsets of the explicit standard 49-term Strassen tensor-square decomposition have tensor rank exactly four over the rational and complex numbers. Therefore no such subset can be replaced by three rank-one terms while the other 45 complete summands remain fixed. The computation includes every subset and uses exact integer arithmetic. A separate implementation verified every saved determinant certificate.

This is a useful reproduction and method-elimination result. It is **not claimed as new mathematics**. A current literature search found an existing stronger result for the same standard Kronecker-square construction: the introduction of Agarwal’s September 2026 preprint reports border radius at least eight. Thus a successful shortening must change at least nine complete original summands under that reported theorem. The present four-term audit is weaker and should be used as a calibration check.

## Exact model

Write the two 2×2 matrices as `[[a,b],[c,d]]` and `[[e,f],[g,h]]`. The seven input products are:

1. `(a+d)(e+h)`
2. `(c+d)e`
3. `a(f-h)`
4. `d(g-e)`
5. `(a+b)h`
6. `(c-a)(e+f)`
7. `(b-d)(g+h)`

Their output coefficient vectors, in row-major order, are `(1,0,0,1)`, `(0,0,1,-1)`, `(0,1,0,1)`, `(1,0,1,0)`, `(-1,1,0,0)`, `(0,0,0,1)`, and `(1,0,0,0)` respectively. Direct coefficient comparison verifies the matrix-multiplication identity. Taking the tensor square gives 49 rank-one tensors in a 16×16×16 tensor space, with the paired-coordinate convention defined by the code. The tensor-square identity was also checked exactly.

The missing historical coefficient archive was not available. Consequently, the present result is stated for the decomposition defined explicitly above and in the supplied code; byte-for-byte identity with the historical archive is not assumed. The earlier all-triples count is reproduced by this construction.

## Why the certificates prove the claim

For a selected subset of four terms, write its sum as

`T = Σ[r=1..4] a_r ⊗ b_r ⊗ c_r`.

Choose one of the three tensor modes. In the first mode, put the four vectors `a_r` into the columns of a matrix `A`, and the four paired vectors `b_r ⊗ c_r` into the columns of a matrix `K`. The corresponding flattening of `T` is `A K^T`.

If both `A` and `K` have column rank four, this flattening has rank four: a left inverse of `A` recovers `K^T`, giving a rank lower bound of four, and the factorization gives the upper bound of four. Nonzero determinants of `A^T A` and `K^T K` certify those column ranks. All entries are integers, and the checked determinants are positive integers, so their nonvanishing is valid over both the rationals and the complex numbers.

Every sum of three rank-one tensors has every matrix flattening of rank at most three. A rank-four flattening therefore prohibits a three-term replacement. Four displayed terms supply the matching tensor-rank upper bound, so the subtensor rank is exactly four.

The paired Gram matrix can be calculated without forming all 256 coordinates: its `(r,s)` entry is the product of the `(r,s)` entries of the individual `b` and `c` Gram matrices. This identity follows by expanding the dot product of the two tensor products.

## Executed results

| Audit | Number of subsets | Rank certified for every subset | Survivors |
|---|---:|---:|---:|
| Three-term control | 18,424 | 3 | 0 |
| Four-term extension | 211,876 | 4 | 0 |

For the quartets, the first successful certificate used mode 1 for 209,821 subsets, mode 2 for 1,971, and mode 3 for 84. These counts sum to 211,876.

The generator calculates determinants by the integer Leibniz formula. The largest individual Gram entries are at most four and paired-Gram entries at most sixteen. Even the conservative bound `24 × 16^4 = 1,572,864` for determinant accumulation is far below the signed 64-bit limit. No floating-point rounding or numerical-rank threshold is used.

The separate verifier parses the seven formulas independently and recomputes 423,752 determinants using Python arbitrary-precision integers with fraction-free Bareiss elimination. It also verifies that the saved subset array exactly equals all four-element subsets of `{0,...,48}` in lexicographic order. All certificates and the completeness check passed.

## Reproduction files

- `strassen_four_audit.py`: explicit decomposition, exact identities, exhaustive triple and quartet generation, and certificates.
- `verify_strassen_four.py`: separate coefficient parser and determinant algorithm.
- `strassen_four_results.json`: numerical summary and precise scope.
- `strassen_3_certificates.npz` and `strassen_4_certificates.npz`: complete per-subset certificate arrays.
- `strassen_four_verification.json`: the second implementation’s result.

Run with Python 3 and NumPy:

```bash
python strassen_four_audit.py
python verify_strassen_four.py
```

This is a finite computational proof with explicit linear-algebra justification and independently implemented checking. It is not a proof-assistant formalization or human external peer review.

## Literature comparison and next decision

The problem’s current baseline must include rational 48-multiplication algorithms for 4×4 matrices. Dumas, Pernet and Sedoglavic provide such a construction, so the local four-term obstruction cannot imply that the original 49-term decomposition is globally optimal.

Agarwal’s preprint studies complete-summand replacement barriers and explicitly reports a stronger result for the 49-term Strassen square: border radius at least eight. Its scope includes the output factors, as does this audit. We inspected the theorem statement and its model description; we have not independently replayed the external paper’s full proof or supplement.

The productive next step is to review that stronger result and the known 48-term constructions, then specify an experiment beyond the eight-term barrier, or a different structural move. Repeating five-through-eight-term exclusions would provide reproduction evidence but would not establish new progress under the reported result. The matrix-multiplication exponent problem remains untouched by the present finite obstruction.

Sources accessed 20 October 2026:

- Dumas, Pernet and Sedoglavic, [A non-commutative algorithm for multiplying 4×4 matrices using 48 non-complex multiplications](https://arxiv.org/abs/2506.13242).
- Agarwal, [Certified local rank and uniqueness barriers for a 48-term matrix-multiplication decomposition](https://arxiv.org/html/2609.13596v1), Introduction, paragraph on the 49-term Strassen Kronecker square.

