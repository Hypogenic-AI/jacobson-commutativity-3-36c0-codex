# Equational Proofs of Jacobson's Theorem for \(k=3\)

## 1. Executive Summary

The research question was whether Brandenburg's equational approach to Jacobson's commutativity theorem can be extended from \(k=1,2\) to rings of characteristic \(p\) satisfying \(x^{p^3}=x\).

The main result of this session is a proof schema for the remaining case \(p\equiv 1\pmod 3\). Brandenburg's period criterion already proves the other congruence classes. For \(p\equiv 1\pmod 3\), the new ingredient is a cyclic norm argument: a Frobenius-skew unit \(b\) with \(ba=a^p b\) or \(ba=a^{p^2}b\) can be normalized to an element \(c\) with \(c^3=1\); because \(T^3-1\) splits over \(\mathbb F_p\), reducedness forces \(c\) to be central, which collapses the Frobenius action.

The result is not an expanded line-by-line equational derivation for every prime. Instead, it identifies finite polynomial certificates which can be computed for each fixed \(p\), matching Brandenburg's style of finite equational proof generation.

## 2. Research Question

Let \(p\) be prime and let \(A\) be a characteristic-\(p\) ring satisfying
\[
x^{p^3}=x
\]
for all \(x\in A\). Can one construct an equational proof that \(A\) is commutative?

By Brandenburg's reduction, it suffices to prove the monomial constructive Wedderburn statements
\[
W_{p,3,T^p},\qquad W_{p,3,T^{p^2}}.
\]

## 3. Definitions and Notation

A \(p^3\)-ring is a ring satisfying \(px=0\) and \(x^{p^3}=x\) for every element \(x\). Such a ring is reduced, because \(x^2=0\) implies \(x=x^{p^3}=0\).

For \(f\in\mathbb F_p[T]\), \(W_{p,3,f}\) is the statement:

> If \(A\) is a \(p^3\)-ring and \(ba=f(a)b\), then \(ba=ab\).

The polynomial \(T^{p^3}-T\) is the product of all monic irreducible polynomials over \(\mathbb F_p\) of degree \(1\) or \(3\). Thus each element \(a\) decomposes equationally into linear and irreducible-cubic components via the standard central idempotents attached to this factorization.

## 4. Statement of Results

**Lemma 1 (split-polynomial centrality).** Let \(A\) be reduced. If \(c\in A\) satisfies a separable polynomial split over \(\mathbb F_p\), then \(c\) is central. In particular, when \(p\equiv 1\pmod 3\), any \(c\) with \(c^3=1\) is central.

**Lemma 2 (finite norm section).** Let \(p\equiv 1\pmod 3\), let \(g\in\mathbb F_p[T]\) be irreducible cubic, and let \(i\in\{1,2\}\). In
\[
B=\mathbb F_p[S,T]/(S^{p^3-1}-1,\ g(T)),
\]
with \(\sigma_i(S)=S\), \(\sigma_i(T)=T^{p^i}\), there is a unit \(U\) such that
\[
U\sigma_i(U)\sigma_i^2(U)=S.
\]

**Proposition 3.** If \(p\equiv 1\pmod 3\), then \(W_{p,3,T^p}\) and \(W_{p,3,T^{p^2}}\) have finite equational certificates.

**Theorem 4.** For every prime \(p\), characteristic-\(p\) rings satisfying \(x^{p^3}=x\) are commutative, with an equational proof for each fixed \(p\).

## 5. Proofs

### Proof of Lemma 1

Let \(m(T)=\prod_{\lambda\in\Lambda}(T-\lambda)\) with distinct \(\lambda\in\mathbb F_p\), and suppose \(m(c)=0\). Lagrange interpolation gives polynomials \(e_\lambda(T)\) with \(e_\lambda(\mu)=\delta_{\lambda,\mu}\). Modulo \(m(T)\), the \(e_\lambda\) are pairwise orthogonal idempotents and \(T=\sum_\lambda \lambda e_\lambda\). Evaluating at \(c\), the \(e_\lambda(c)\) are idempotents. Idempotents are central in reduced rings, hence \(c=\sum_\lambda \lambda e_\lambda(c)\) is central.

### Proof of Lemma 2

Let \(q=p^3\) and \(C=\mathbb F_p[S]/(S^{q-1}-1)\). Since the roots of \(S^{q-1}-1\) are \(\mathbb F_q^\times\), every simple factor of \(C\) has degree \(1\) or \(3\) over \(\mathbb F_p\).

Over a degree-1 factor, \(B\) becomes \(\mathbb F_q\), and the norm \(\mathbb F_q^\times\to\mathbb F_p^\times\) is surjective. Over a degree-3 factor, \(g\) splits and \(B\cong\mathbb F_q^3\); \(\sigma_i\) cyclically permutes the three factors, so \((x_0,x_1,x_2)\mapsto x_0x_1x_2\) is surjective onto \(\mathbb F_q^\times\). Thus \(S\) has a norm preimage on every simple factor. The Chinese remainder theorem combines these preimages into \(U\in B\).

For fixed \(p\) and \(g\), choosing a polynomial representative of \(U\) and verifying the displayed norm identity is a finite polynomial calculation, hence an equational certificate.

### Proof of Proposition 3

It is enough to treat \(W_{p,3,T^{p^i}}\) for \(i=1,2\). Suppose \(A\) is a \(p^3\)-ring and
\[
ba=a^{p^i}b.
\]

By Brandenburg's unit-support reduction, we may work on the central support where \(b\) is a unit. Decompose \(a\) using the central idempotents attached to the irreducible factors of \(T^{p^3}-T\). Frobenius preserves each such idempotent, so the relation respects the decomposition. Linear components are immediate because \(a^{p^i}=a\).

Now work on a component where \(g(a)=0\) for an irreducible cubic \(g\). The element \(a^{p^i}-a\) is a unit there, since \(g\) is coprime to \(T^{p^i}-T\). Let \(\sigma(a)=a^{p^i}\). Then
\[
b^3a=a^{p^{3i}}b^3=ab^3,
\]
so \(s=b^3\) commutes with both \(a\) and \(b\). By Lemma 2, choose \(u\) in the commutative subring generated by \(a\) and \(s\) such that
\[
u\sigma(u)\sigma^2(u)=s.
\]
Since \(bu=\sigma(u)b\), the element \(c=u^{-1}b\) satisfies
\[
c^3=u^{-1}\sigma(u)^{-1}\sigma^2(u)^{-1}b^3=1.
\]
Because \(p\equiv 1\pmod 3\), Lemma 1 makes \(c\) central. But
\[
ca=u^{-1}ba=u^{-1}a^{p^i}b=a^{p^i}c.
\]
As \(c\) is a central unit, \(a=a^{p^i}\), contradicting the fact that \(a^{p^i}-a\) is a unit on a nonzero cubic component. Thus the unit support of \(b\) on every cubic component is zero. Therefore \(ba=ab\) everywhere.

### Proof of Theorem 4

If \(p=2\), \(p=3\), or \(p\equiv 2\pmod 3\), then
\[
\gcd(3,p^3-1)=1,
\]
so Brandenburg's period criterion proves the \(p^3\)-case. If \(p\equiv 1\pmod 3\), Proposition 3 proves the two monomial Wedderburn statements, and Brandenburg's monomial sufficiency theorem gives commutativity.

## 6. Computational Verification

Environment:

- Python: 3.12.8
- SymPy: 1.14.0
- pypdf: 6.12.2
- Hardware: four NVIDIA RTX A6000 GPUs detected, not needed for the symbolic checks

Scripts:

- `code/finite_field_reductions.py`: pre-gathered helper reproducing Brandenburg's gcd criterion.
- `src/k3_wedderburn_checks.py`: new exact checks for this session.

Key output saved in `results/k3_checks.json`:

| Check | Result |
|---|---|
| \(p=2,3,5,11,17\) sample | \(\gcd(3,p^3-1)=1\), period criterion applies |
| \(p=7,13,19\) sample | \(\gcd(3,p^3-1)=3\), bad congruence class |
| \(p=7\) norm summary | \(112\) irreducible cubic factors; norm sections reduce to degree \(1\) and \(3\) components |
| \(p=13\) norm summary | \(728\) irreducible cubic factors; same component structure |
| \(p=7\) skew model | In \(T^3+T^2+1\), the common \(S\)-gcd degree drops from \(13\) to \(0\) after adding \(t=3\), indicating no unit skew parameter survives the tested potency equations |

Validation commands run successfully:

```bash
source .venv/bin/activate
python -m py_compile src/k3_wedderburn_checks.py code/finite_field_reductions.py
diff <(python src/k3_wedderburn_checks.py --json) <(python src/k3_wedderburn_checks.py --json)
```

## 7. Discussion

The proof isolates why \(k=3\), \(p\equiv 1\pmod 3\), is different from the period-criterion cases. The obstruction is a genuine Frobenius 3-cycle. The new observation is that this cycle can be absorbed by a cyclic norm preimage of \(b^3\); after normalization, the skewing element has cube \(1\). Since \(\mathbb F_p\) contains the cube roots of unity in exactly this congruence class, reducedness makes the normalized element central and kills the cycle.

The argument is equational in the same finite-certificate sense used by Brandenburg: for each fixed \(p\), all finite choices reduce to explicit polynomial identities in finite quotient rings.

## 8. Limitations

The report does not print the concrete norm-section polynomial \(U_{g,i}(S,T)\) for every irreducible cubic \(g\) and prime \(p\equiv 1\pmod 3\). Lemma 2 proves such a polynomial exists and is computable by finite algebra/CRT, but a production-grade certificate generator would be needed to emit fully expanded equational derivations.

The computational skew check was performed only for the first open prime \(p=7\) and one irreducible cubic representative. It supports the proof strategy but is not the main proof.

## 9. Open Questions

1. Build a certificate generator that computes \(U_{g,i}(S,T)\) for each irreducible cubic \(g\) and emits a machine-checkable equational derivation.
2. Minimize the resulting certificates using equivalences between irreducible cubics under linear substitution and reciprocals.
3. Investigate whether the cyclic norm idea extends to higher bad prime-power layers \(k>3\).

## 10. Conclusions

The \(k=3\) case can be completed by combining Brandenburg's period criterion with a cyclic norm argument for primes \(p\equiv 1\pmod 3\). The proof reduces the missing monomial Wedderburn statements to finite norm-section certificates and a simple centrality argument for elements satisfying \(c^3=1\).

This gives a credible path from the semantic Jacobson theorem to explicit equational proofs for every fixed \(p^3\)-identity.

## References

- Martin Brandenburg, "Equational proofs of Jacobson's theorem", arXiv:2310.05301, 2023.
- Michael K. Kinyon and Des MacHale, "Elementary Proofs of Ring Commutativity Theorems", arXiv:2601.12599, 2026.
- Jiang Luh, "On the commutativity of J-rings", 1967.
- J. M. Dolan, "A proof of Jacobson's theorem", 1976.
- I. N. Herstein, "Wedderburn's Theorem and a Theorem of Jacobson", 1961.
