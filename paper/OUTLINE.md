# Outline: Cyclic Norm Certificates for the \(p^3\)-Case

## Title

Cyclic Norm Certificates for Equational Jacobson Proofs in the \(p^3\)-Case

## Abstract

- Fixed-exponent Jacobson problem for characteristic-\(p\) rings with \(x^{p^3}=x\).
- Brandenburg covers the cases \(\gcd(3,p^3-1)=1\); the remaining primes satisfy \(p\equiv 1 \pmod 3\).
- Main contribution: cyclic norm certificates prove the two monomial Wedderburn statements in the remaining case.
- Exact computations verify the congruence split and finite norm-component structure.

## Introduction

- State motivation: equational proofs make Jacobson commutativity explicit.
- Summarize classical and recent context: Jacobson, Herstein, Luh, Dolan, Brandenburg, Kinyon--MacHale.
- Identify the \(k=3\) gap.
- Preview the cyclic norm normalization \(b \mapsto u^{-1}b\), producing \(c^3=1\).
- List contributions and paper organization.

## Preliminaries

- Ring conventions, \(p^3\)-rings, reducedness, central idempotents.
- Factorization of \(T^{p^3}-T\) into linear and cubic irreducibles.
- Constructive Wedderburn statements \(W_{p,3,f}\).
- Cited Brandenburg reductions: monomial sufficiency and period criterion.
- Define finite equational certificates.

## Main Results

- Prove split-polynomial centrality in reduced rings.
- Prove the finite cyclic norm section lemma.
- Prove monomial Wedderburn certificates for \(p\equiv 1 \pmod 3\).
- Combine with Brandenburg's period criterion for all primes.
- Include examples: \(p=5\) as period case, \(p=7\) as norm case, and a non-split centrality warning.
- Record computational verification from `results/k3_checks.json`.

## Discussion

- Explain why the bad congruence class contains a genuine Frobenius 3-cycle.
- Discuss finite certificate generation and limitations.
- State open questions about explicit certificate emitters, minimization, and higher \(k\).

## Conclusion

- Summarize the completed \(k=3\) proof schema.
- Emphasize finite polynomial identity certificates for fixed primes.
