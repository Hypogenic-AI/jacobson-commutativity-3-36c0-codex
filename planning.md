# Research Plan: Equational Jacobson Proofs for \(k=3\)

## Motivation & Novelty Assessment

### Why This Research Matters
Jacobson's theorem is semantically classical, but fixed-exponent equational proofs expose how much of the theorem is visible inside pure equational logic. The case \(x^{p^3}=x\), \(p=0\), is the first prime-power layer not handled by Brandenburg's explicit \(k=1\) and \(k=2\) arguments.

### Gap in Existing Work
Brandenburg proves all \(p^3\)-cases for which \(\gcd(3,p^3-1)=1\), namely \(p=2\), \(p=3\), and primes \(p \equiv 2 \pmod 3\). The unresolved family is \(p \equiv 1 \pmod 3\), where the period argument only yields a 3-cycle under Frobenius and does not prove the required constructive Wedderburn statements.

### Our Novel Contribution
The session will try to extend Brandenburg's constructive Wedderburn method to \(k=3\) by isolating new identities in the remaining Frobenius 3-cycle case. If a complete proof is not found, the deliverable will identify the precise algebraic obstruction and provide reproducible finite-field/skew-algebra computations to guide subsequent proof search.

### Experiment Justification
- Experiment 1: Verify the congruence split for \(k=3\) and reproduce Brandenburg's coverage. This prevents spending effort on cases already solved by the period criterion.
- Experiment 2: Analyze \(W_{p,3,T^p}\) and \(W_{p,3,T^{p^2}}\) in the first open case \(p=7\). This is the smallest representative of the unresolved congruence class.
- Experiment 3: Compute identities in the skew relation \(YX=X^pY\) under \(X^{p^3}=X\), \(Y^{p^3}=Y\), and \((X+Y)^{p^3}=X+Y\). This tests whether ordinary \(p^3\)-potency of linear combinations visibly kills the Frobenius-twisted component.
- Experiment 4: Search for reusable polynomial identities over \(\mathbb{F}_p\) that hold uniformly for primes \(p \equiv 1 \pmod 3\). This is the route to a human-readable equational proof.

## Research Question
Can one construct an explicit equational proof that every characteristic-\(p\) ring satisfying \(x^{p^3}=x\) is commutative, with particular focus on the missing primes \(p \equiv 1 \pmod 3\)?

## Background and Motivation
For fixed \(n\), Birkhoff completeness guarantees an equational proof of commutativity from \(x^n=x\), but this proof is nonconstructive. Brandenburg's paper makes the problem concrete by reducing fixed exponents to prime-power cases and proving \(k=1\), \(k=2\), plus a broad period-criterion family. The first genuinely unresolved prime-power layer is \(k=3\) with \(p \equiv 1 \pmod 3\).

## Hypothesis Decomposition
1. The \(k=3\) theorem is already proved equationally when \(\gcd(3,p^3-1)=1\).
2. For \(p \equiv 1 \pmod 3\), it suffices by Brandenburg's monomial theorem to prove \(W_{p,3,T^p}\) and \(W_{p,3,T^{p^2}}\).
3. These Wedderburn statements may follow from additional \(p^3\)-potency identities applied to sums such as \(a+b\), where \(ba=a^p b\).
4. If a direct proof is unavailable, finite algebra computations should identify whether low-complexity identities can force \(b=0\) on irreducible cubic components.

## Proposed Methodology

### Approach
Use Brandenburg's reduction as the main proof skeleton. Treat the known congruence classes as solved by Theorem 8.10, then focus all original work on the two monomial Wedderburn statements for \(p \equiv 1 \pmod 3\). Computational work will model the universal skew relation \(YX=X^pY\) over cubic finite-field components and test identities induced by \(p^3\)-potency.

### Experimental Steps
1. Reproduce the \(k=3\) congruence split using the local SymPy helper.
2. Write down precise definitions and theorems needed from Brandenburg.
3. Prove easy supporting lemmas: reducedness, central idempotents, exponent congruence, and centrality of split-polynomial powers such as \(x^{(p^3-1)/3}\) when \(p \equiv 1 \pmod 3\).
4. Attempt a direct proof of \(W_{p,3,T^p}\) and \(W_{p,3,T^{p^2}}\).
5. Implement skew-algebra calculations for \(p=7\) and, if feasible, \(p=13\) to search for low-degree certificates.
6. Refine the proof attempt based on the computational results.

### Baselines
The baseline is Brandenburg's existing period criterion, which proves the theorem for the good \(k=3\) cases and fails exactly when \(p \equiv 1 \pmod 3\). The \(p=2\) and \(p=3\) examples in Brandenburg serve as sanity checks for the computational encoding.

### Evaluation Metrics
- Mathematical: a complete derivation of the missing monomial Wedderburn statements, or a precise reduction showing what remains.
- Computational: reproducible outputs confirming the congruence split and any candidate identities for \(p=7\).
- Expository: all claims stated with explicit hypotheses, no hidden use of non-equational structural arguments in claimed equational steps.

### Statistical Analysis Plan
No statistical inference is appropriate: this is proof construction. Computation is used for exact finite-field algebra and counterexample/certificate search, so outputs are deterministic and validated by repeated runs.

## Expected Outcomes
A positive outcome is a proof of both missing monomial Wedderburn statements for all \(p \equiv 1 \pmod 3\), completing the \(k=3\) case. A partial outcome is a verified proof for all already-covered congruence classes plus a sharpened obstruction and computational evidence for the remaining class.

## Timeline and Milestones
1. Resource review and setup: complete.
2. Planning and notation: short markdown deliverables.
3. Proof construction: main effort, focused on Wedderburn monomials.
4. Computational verification: exact finite-field/skew-algebra scripts in `src/`.
5. Refinement and validation: check for logical gaps and reproducibility.
6. Final documentation: `REPORT.md`, `README.md`, and result files.

## Potential Challenges
- The remaining case may require identities too large for a short human proof.
- Direct skew-algebra computations for \(p=13\) may become large.
- A classical finite-field argument may accidentally use non-equational reasoning; such steps must be reported as proof-search guidance rather than a completed equational proof.

## Success Criteria
The session succeeds if it either supplies a complete \(k=3\) proof or cleanly documents the strongest verified reduction and computational evidence for the unresolved \(p \equiv 1 \pmod 3\) cases. In either case, final documentation must distinguish proved statements from conjectural or computationally observed identities.
