# Independent reconstruction: no sampler of size at most 11 for all variable orders

**Status.** This is a direct algebraic proof reconstructed in the present session. It was not copied from or compared line by line with the unrecovered original research pack. Its supporting checks reproduce the two distinctive prior counts: 1,800 balanced quadratics and 20,475 syndrome-counting cases. No novelty claim is made. The scope is a finite sampler problem, not a resolution of a major unsolved problem.

## Exact model

The domain is \(X=\mathbb F_2^6\), with all 64 inputs equally likely. A sampler is a **nonempty set of distinct points**, with the uniform distribution on that set. Allowed tests are deterministic width-two branching programs that read each input coordinate once. Each program uses one fixed variable order, but that order may differ between programs; a single sampler must work for **every order**. The required acceptance-probability discrepancy is at most \(1/4\), inclusive.

We number coordinates \(x_0,\ldots,x_5\); the integer encoding is \(x=\sum_{i=0}^5 2^i x_i\). Arithmetic inside Boolean polynomials is over \(\mathbb F_2\).

## Main theorem

For every set \(S\subseteq X\) with \(|S|=11\), there is an allowed **balanced** Boolean test \(f\), accepting exactly 32 of the 64 full-domain inputs, that accepts at most 2 points of \(S\). Consequently,

\[
\left|\Pr_{x\in S}[f(x)=1]-\Pr_{x\in X}[f(x)=1]\right|
\ge \frac12-\frac2{11}=\frac7{22}>\frac14.
\]

The companion arguments below exclude all sample sizes 1 through 10 as well. Therefore any sampler in this exact model has at least 12 points. This does **not** establish that 12 points suffice.

## The test family

Every nonconstant affine function is balanced and computable by a two-state program using parity updates. We also use

\[
f(x)=x_i x_j+a_i x_i+a_j x_j+\sum_{k\notin\{i,j\}}a_kx_k+c,
\]

where at least one coefficient outside \(\{i,j\}\) is nonzero. There are

\[
\binom62\cdot 4\cdot(2^4-1)\cdot2=1800
\]

such functions. Each is balanced because toggling an outside variable with coefficient 1 toggles the output.

A two-state program reads \(x_i\) and \(x_j\) first. After the first bit, store \(x_i+a_j\). After the second bit, replace the state by

\[
(x_i+a_j)(x_j+a_i)+(c+a_ia_j)
=x_ix_j+a_ix_i+a_jx_j+c.
\]

Read the remaining coordinates, XORing those with coefficient 1 and otherwise preserving the state. This reads every coordinate once. This construction is why the quantifier over **all variable orders** matters.

## Affine evaluation code

Evaluate all affine functions on the ordered list of points of \(S\). The resulting vectors form a binary linear code

\[
C=\{(a_0+\sum_i a_i x_i)_{x\in S}: a_0,a_i\in\mathbb F_2\}\subseteq\mathbb F_2^{|S|}.
\]

If the affine evaluation map has rank less than 7, a nonzero affine function vanishes on \(S\). Since \(S\) is nonempty, this function is not the constant 1; it is nonconstant and balanced on the full domain. It already gives discrepancy \(1/2\). Thus we may assume \(\dim C=7\). The all-one vector belongs to \(C\).

For \(|S|=11\), a codeword of weight 1 or 2 gives the desired balanced affine witness. Therefore suppose every nonzero codeword has weight at least 3. The all-one vector then ensures every nonconstant codeword has weight between 3 and 8.

## Lemma 1: some coordinate product is outside the affine code

For distinct points and \(|S|>7\), at least one evaluation vector

\[
q=(x_ix_j)_{x\in S},\qquad i\ne j,
\]

lies outside \(C\).

Indeed, if every product of two coordinate generators lay in \(C\), then \(C\) would be closed under coordinatewise multiplication: products of arbitrary affine generators expand into constants, coordinates, squares \(x_i^2=x_i\), and the assumed pair products. The coordinate functions separate the distinct points of \(S\). For any \(s\in S\), its singleton indicator on \(S\) is

\[
\prod_{i=0}^5(1+x_i+s_i).
\]

Closure would put all \(|S|\) singleton indicators in \(C\), making \(C=\mathbb F_2^{|S|}\), contradicting \(\dim C=7<|S|\).

## Lemma 2: every nonzero syndrome has at least four low-weight representatives

Let \(H\) be a parity-check matrix for the binary \([11,7,\ge3]\) code \(C\). It has four independent rows. Minimum distance at least 3 implies its 11 columns are distinct nonzero vectors in \(\mathbb F_2^4\).

Fix a nonzero syndrome \(s\in\mathbb F_2^4\). The 16 vectors of this space partition into eight unordered pairs \(\{u,u+s\}\).

* If \(s\) is a column, the 11 occupied vectors fill at least three pairs completely, because eight pairs can accommodate at most eight occupied vectors without a complete pair, and each complete pair provides only one additional occupied vector. These give three distinct weight-two representatives of syndrome \(s\), in addition to the weight-one representative from column \(s\).
* If \(s\) is not a column, the pair \(\{0,s\}\) is empty. The 11 columns occupy the remaining seven pairs, so at least four pairs are complete. These give four distinct weight-two representatives.

Thus each nonzero coset of \(C\) contains at least four vectors of weight at most 2. This lemma can also be checked in exactly \(\binom{15}{11}\cdot15=20,475\) finite cases; the counting proof is sufficient by itself.

## Completing the 11-point proof

Choose \(q=(x_ix_j)_{x\in S}\notin C\) using Lemma 1. By Lemma 2, \(q+C\) contains at least four distinct vectors of weight at most 2.

Let \(W=\operatorname{span}\{1,x_i,x_j\}\) denote the evaluation vectors for affine corrections using just the two selected coordinates. The eight vectors in \(q+W\) are the indicators of the four cells determined by \((x_i,x_j)\), and their complements.

Each cell has at most eight points: it is contained in a coordinate-level set, whose size is at most eight by the affine distance bounds. Thus no cell complement has weight at most 2. At most three of the four cells can have size at most 2, because the four cell sizes sum to 11. Consequently, \(q+W\) contains at most three vectors of weight at most 2.

Select a low-weight vector in \((q+C)\setminus(q+W)\). Its affine correction necessarily uses a coordinate outside \(\{i,j\}\), since the affine evaluation map is injective. Hence it corresponds to one of the 1,800 balanced, allowed quadratics. Its weight is at most 2, proving the theorem.

## Excluding smaller sample sizes

It is not enough merely to exclude size 11: feasible sampler cardinalities need not be monotone. The following separate arguments close that gap.

### Sizes 1 through 7

If affine evaluation has rank below 7, the vanishing affine witness above applies. Full rank is possible only when \(|S|\ge7\). At size 7 it gives \(C=\mathbb F_2^7\), so an affine function can accept exactly one sampled point and has full-domain acceptance \(1/2\). Its discrepancy is \(1/2-1/7=5/14>1/4\).

### Sizes 9 and 10

Assume rank 7 and that all balanced affine functions meet the tolerance. Such a function must accept at least 3 sampled points, so the affine evaluation code has minimum distance at least 3. Its Hamming balls of radius 1 are disjoint, implying

\[
2^7(1+|S|)\le 2^{|S|}.
\]

This fails for size 9 (1,280 > 512) and size 10 (1,408 > 1,024). Thus a balanced affine witness exists at both sizes.

### Size 8

Assume rank 7 and that the affine functions meet the tolerance. The code is a binary \([8,7,\ge2]\) code. Its one-row parity-check matrix must have all columns nonzero, so it is the all-one row and \(C\) is exactly the even-weight code.

Lemma 1 yields \(q=x_ix_j\notin C\). Then \(q+C\) is the odd-weight coset, which contains all eight unit vectors. At most three unit vectors can lie in \(q+W\): each pair cell has size at most 6 (from the affine tolerance), so complements cannot be unit vectors, and all four cells cannot be singletons because their sizes sum to 8. Therefore some unit vector in \(q+C\) uses an affine correction outside the two selected coordinates. This produces an allowed balanced quadratic accepting one sampled point, with discrepancy \(1/2-1/8=3/8>1/4\).

## Executed supporting checks

`verify_lower_bound.py` uses only Python's standard library and exact integer arithmetic. It independently checks:

* All 20,475 syndrome-counting cases. The number of low-weight representatives is 4 in 12,600 cases, 5 in 7,560 cases, and 6 in 315 cases.
* All 126 nonconstant affine functions and all 1,800 distinct quadratics are balanced on the 64-point domain.
* Every quadratic truth table matches the explicit two-state read-once transition construction above.
* Explicit violating witnesses for 5,000 seeded random supports: 100 at each size 1 through 10 and 4,000 at size 11. These random checks are smoke tests, not the justification for the universal theorem.

A separate preliminary MILP probe hit its 40-second time limit without a feasible solution or an infeasibility certificate. It supplies no proof evidence and is not used in the result.

## Literature boundary

The related paper is Andrej Bogdanov, Zeev Dvir, Elad Verbin, and Amir Yehudayoff, **Pseudorandomness for Width-2 Branching Programs**, *Theory of Computing* 9(7), 283–293 (2013), DOI 10.4086/toc.2013.v009a007. Primary source: https://theoryofcomputing.org/articles/v009a007/v009a007.pdf .

The paper explicitly considers general programs that need not be read once and proves a reduction from low-degree polynomial pseudorandomness to width-two programs. It provides background and related techniques, not a direct published verification or novelty certification of this exact six-bit cardinality claim. This session's targeted lookup does not establish whether the finite result is new.
