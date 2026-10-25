# Exact minimum support in the six-bit, width-two benchmark

**Result.** The minimum size of a nonempty uniform sampling support with worst-case absolute acceptance error at most **1/4** is **8**, for the precise finite model below. The lower bound is elementary; the upper bound is verified by exhaustive exact computation over a completely characterized class. No novelty claim is made.

## Model and claim

A program reads six bits exactly once in the order x1, x2, x3, x4, x5, x6. Each layer has two states, labeled 0 and 1. The initial state is 0. Each layer has an arbitrary deterministic transition from the current state and input bit to the next state. Any subset of the final two states may accept.

Let C be the resulting class of Boolean functions on {0,1}^6. A support S contains distinct six-bit strings, sampled uniformly. Its error is

\[
 E(S)=\max_{f\in C}\left|\frac{1}{|S|}\sum_{x\in S}f(x)-\frac{1}{64}\sum_{x\in\{0,1\}^6}f(x)\right|.
\]

The assertion is that the minimum of |S| over nonempty supports satisfying E(S) <= 1/4 equals 8.

## Lower bound: seven points cannot suffice

Every affine parity f(x)=a dot x + b, computed modulo two, belongs to C. A program stores the running parity in its two states; the constant b can be incorporated into the first transition or final acceptance. Every nonconstant affine parity is balanced on the full domain, so its uniform acceptance probability is 1/2.

If S has at most six points, its affine span over F2 has dimension at most five. There is therefore a nonconstant affine parity that is constant on S. Its error is 1/2, exceeding 1/4.

Now suppose S has seven points. If they are affinely dependent, their affine span again has dimension at most five, giving the same obstruction. Otherwise they are affinely independent. Evaluation at these seven points is then an invertible linear map from the seven-dimensional space of affine functions on F2^6 to F2^7. Consequently, an affine parity exists that equals 1 at one selected point and 0 at the other six. It is nonconstant because those values differ. Its error is

\[
 \left|\frac17-\frac12\right|=\frac5{14}>\frac14.
\]

Thus every qualifying uniform support has at least eight points. This argument excludes all smaller supports, not just supports visited by the numerical solver.

## Upper bound: an exactly verified eight-point support

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

## Reproduction and limits

`method_oracle.py` implements the backward recurrence and exact support verifier. `method_oracle_functions.json` contains the complete function list; `method_candidate_8_verification.json` records this support, its strings, complete-class check, exact maximum, and a witnessing function. Truth-table bit x is the value at integer x, with x1 the most significant input bit.

To repeat the check in Python, import `enumerate_functions` and `verify_support` from `method_oracle`, regenerate the six-bit class, and pass the eight integers above to `verify_support`.

The solver supplied a candidate; solver status is not used to prove optimality. The proof concerns uniform sampling on distinct strings in this six-bit ordered width-two model. It does not establish a general pseudorandom generator, any asymptotic derandomization result, or a resolution of P versus BPP. Verification occurred within an AI-assisted workflow, not through external human peer review or a formal proof assistant.
