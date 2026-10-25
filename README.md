# Help Change The World — Math

## 100 difficult math problems. Let's get after them.

This is an open, AI-assisted research project exploring 100 difficult problems in mathematics.

The goal is not to ask an AI to “solve” famous unsolved problems and publish whatever it says. The goal is to build a research process:

- Understand what mathematicians already know.
- Break large problems into smaller, testable questions.
- Run exact computations where possible.
- Search aggressively for counterexamples.
- Try to destroy our own arguments.
- Preserve the code, calculations, proofs, and failures.
- Publish everything so other people can check our work.

## Don't trust us. Check us.

Large language models can make mistakes, rediscover known mathematics, and produce arguments that sound convincing but are wrong.

That is why we want the evidence public.

For every meaningful result, we will try to distinguish between:

**Idea** — something worth investigating.

**Experiment** — something observed computationally.

**Finite result** — something exhaustively verified inside a precisely defined model.

**Proof** — a mathematical argument establishing the stated claim.

**New result** — something that has also survived a serious search of the existing mathematical literature.

Those are not the same thing.

## What we've found so far

### #81 — Randomness Reduction / Samplers

We studied a six-bit model with 64 possible inputs.

For programs that all read the six inputs in the same order, we found that **8 sample inputs are sufficient and 7 are not**.

Under the stronger requirement that the sample must work regardless of the order in which an allowed program reads the inputs, we proved that **11 inputs cannot be sufficient**.

Therefore at least **12** are necessary.

Whether 12 are sufficient remains unresolved in our research.

### #49 — Hadamard-Related Sign Sequences

In a precisely defined finite extension problem, we classified **336,140 valid normalized length-seven starting configurations**.

Most could be extended immediately or after one permitted change.

A small number required two changes.

Exactly **12 required three changes**.

None required more than three under the stated rules.

This answers that finite question. It does **not** solve the general Hadamard Matrix Conjecture.

### #93 — Matrix Multiplication

We tested **211,876 four-term selections** in a specified Strassen-based construction.

None of those four terms could simply be replaced by three while leaving the rest of the construction fixed.

A literature review found stronger related existing results, so we treat this as a reproduced finite obstruction rather than a claim of a new breakthrough.

## The 100 Problems

The research program includes problems connected to:

Riemann Hypothesis · P vs NP · Birch and Swinnerton-Dyer · Hodge Conjecture · Yang-Mills · Collatz · Goldbach · Twin Primes · Hadamard Matrices · P vs BPP · Matrix Multiplication · Hilbert's Sixteenth Problem · and many others.

A complete 100-problem research ledger will be published in this repository.

## How this repository will work

Each research problem will eventually contain:

**Overview**  
Why the problem matters and what we are trying to learn.

**Current Status**  
What has actually been established.

**Full Mathematics**  
Definitions, assumptions, derivations, and proofs.

**Experiments**  
Computer searches and exact finite calculations.

**Verification**  
Independent checking scripts and reproducible outputs.

**Literature**  
Relevant existing mathematical research.

**Failures**  
Approaches that did not work and why.

**Next Question**  
The next precise thing worth attacking.

## Found an error?

Good.

Please tell us.

The purpose of making this public is not to defend every result. It is to make the work easier to inspect, criticize, reproduce, correct, and improve.

If something is wrong, we want to know.

If something is already known, we want to know that too.

If something survives, we keep pushing.

## Why?

This is part of a larger experiment documented at **FredEsser.com**:

Can increasingly capable AI tools reduce the cost of helping with serious research?

We don't know.

Let's find out.
