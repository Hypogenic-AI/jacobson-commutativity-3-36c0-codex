# Literature Review

## Research Area Overview

Jacobson's commutativity theorem states that a ring in which every element is
potent is commutative. The present project fixes the exponent and asks for an
equational proof in the variety of rings satisfying

```text
x^{p^3} = x,    p x = 0
```

where `p` is prime. The key source is Brandenburg's arXiv:2310.05301, which
turns the classical theorem into an explicit equational-proof problem. For
fixed exponent `n`, Birkhoff completeness gives existence of an equational
proof once the ordinary theorem is known, but Brandenburg's goal is to
construct such proofs.

The literature suggests a sharp split for `k=3`. Brandenburg's period
criterion proves the `p^3` case whenever `gcd(3,p^3-1)=1`, which includes
`p=2`, `p=3`, and primes `p == 2 mod 3`. The remaining primes `p == 1 mod 3`
are the natural target for new proof construction.

## Key Definitions

**Ring/rng.** Several papers allow nonunital associative rings. Brandenburg
uses "rng" for the nonunital case and "ring" for the unital case.

**Potent ring.** A ring is potent if, for every element `x`, there is an
integer `n(x)>1` such that `x^{n(x)}=x`.

**`n`-ring or `J`-ring.** A ring satisfying the fixed identity `x^n=x` for all
`x`. Luh calls these `J`-rings. A `p^k`-ring satisfies `x^{p^k}=x` and has
characteristic `p`.

**Equational proof.** A proof in pure equational logic from the ring axioms and
the fixed identities, using equality rules, congruence, and substitution. The
method excludes arguments through ideals, quotients, subrings, quantifiers, and
ordinary case reasoning unless those steps are represented by equations.

**Reduced ring.** A ring with no nonzero nilpotents. Any fixed-exponent ring
`x^n=x` is reduced, since a nilpotent element eventually has powers zero.

**Simple number.** In Brandenburg's terminology, `n` is simple if every prime
power `q` with `q-1 | n-1` is already prime. Simple exponents reduce to the
`k=1` case.

**Constructive Wedderburn statement `W_{p,k,f}`.** For `f in F_p[T]`,
`W_{p,k,f}` is the assertion that in a `p^k`-ring of characteristic `p`,
`ba=f(a)b` implies `ba=ab`. Brandenburg reduces commutativity of `p^k`-rings
to proving these statements equationally for enough polynomials `f`.

## Key Papers

### Brandenburg: Equational proofs of Jacobson's theorem

- **Author**: Martin Brandenburg
- **Year**: 2023
- **Source**: arXiv:2310.05301
- **Main results**:
  - Reduces fixed-exponent equational commutativity to prime-power cases in
    prime characteristic.
  - Gives explicit equational proofs for `p`-rings and `p^2`-rings.
  - Reduces general `p^k`-rings to constructive Wedderburn statements
    `W_{p,k,f}`.
  - Proves a period criterion: if `gcd(k,p^k-1)=1`, then every `p^k`-ring of
    characteristic `p` has an equational commutativity proof.
  - Gives explicit `8`-ring and `27`-ring computations.
- **Proof techniques**: finite-field polynomial gcds in `F_p[T]`, idempotent
  centrality, unit/idempotent decomposition, Vandermonde separation,
  noncommutative coefficient extraction, and finite polynomial-composition
  monoids.
- **Relevance**: This is the direct template for the project. It proves many
  `k=3` cases but leaves the primes `p == 1 mod 3` outside the period
  criterion.

### Kinyon and MacHale: Elementary Proofs of Ring Commutativity Theorems

- **Authors**: Michael K. Kinyon and Des MacHale
- **Year**: 2026
- **Source**: arXiv:2601.12599
- **Main results**:
  - Provides elementary proofs for small fixed exponents.
  - Shows that in a `(2m+1)`-potent ring, `x^m` is central for every `x`.
  - Uses Prover9 to find or verify several Herstein-type centrality proofs.
- **Proof techniques**: reduced-ring centrality tests, central idempotents,
  polynomial identities, and automated equational search.
- **Relevance**: For odd `p`, the `p^3` identity has odd exponent, so
  `x^{(p^3-1)/2}` is central. This may be useful in the unresolved
  `p == 1 mod 3` cases.

### Daas: Equational proofs for a theorem by Jacobson for a significant density of even exponents

- **Author**: M. A. Daas
- **Main results**: Develops equational proofs for a positive-density family
  of even exponents.
- **Proof techniques**: fixed-exponent manipulation and equational reductions.
- **Relevance**: Useful background for `p=2`, where the target exponent is
  `8`. Brandenburg's paper contains the strongest directly usable `8`-ring
  proof.

### Burris and Lawrence: Term Rewrite Rules for Finite Fields

- **Authors**: Stanley N. Burris and John Lawrence
- **Year**: 1991
- **Main results**: Studies finite equational axiomatizations and finite
  rewrite systems for finite fields and for rings satisfying `x^m=x`.
- **Proof techniques**: term-rewrite systems, finite-field equations, and
  Knuth-Bendix style completion.
- **Relevance**: Gives computational-algebra context for producing equational
  derivations from finite-field identities.

### Wavrik: Commutativity Theorems: Examples in Search of Algorithms

- **Author**: John Wavrik
- **Year**: 1999
- **Main results**: Frames commutativity theorems as algorithmic membership
  problems for noncommutative polynomial identities.
- **Proof techniques**: noncommutative polynomial reduction with integer
  coefficients and substitution closure.
- **Relevance**: Provides an algorithmic path for searching equational proofs
  when hand derivations become large.

### Luh: On the commutativity of J-rings

- **Author**: Jiang Luh
- **Year**: 1967
- **Main results**: Gives structural results for fixed-exponent `J`-rings and
  `p^k`-rings, including finite-field decomposition statements.
- **Proof techniques**: central idempotents, reducedness, finite division
  rings, and direct-sum decompositions.
- **Relevance**: Classical structural background for the prime-power
  decomposition that Brandenburg makes equational.

### Dolan: A proof of Jacobson's theorem

- **Author**: J. M. Dolan
- **Year**: 1976
- **Main results**: Gives a short proof of Jacobson's theorem avoiding the
  axiom of choice.
- **Proof techniques**: finite subrings generated by elements, central
  idempotents, and a constructive Wedderburn-style commutator argument.
- **Relevance**: Historical bridge from classical structural proof to
  constructive/equational proof design.

### Other supporting sources

- Herstein (1961) supplies elementary Wedderburn/Jacobson proof ideas.
- Buckley and MacHale (2013) analyze variants of `x^3=x` and centrality
  arguments for low exponents.
- Anderson and Danchev (2020) place Jacobson's theorem in the broader context
  of periodic rings, though their result is not an equational fixed-`p^3`
  proof.

## Known Results

**Jacobson commutativity theorem.** If every element `x` of a ring satisfies
`x^{n(x)}=x` for some `n(x)>1`, then the ring is commutative.

**Fixed exponent implies equational existence.** For a fixed `n`, the class of
`n`-rings is an equational variety. Since ordinary Jacobson commutativity holds
semantically, equational completeness gives a formal proof of `xy=yx`; this is
nonconstructive and does not identify a practical derivation.

**Central idempotents.** In a reduced ring, idempotents are central. In an
`n`-ring this can be proved equationally because square-zero elements vanish.

**Exponent congruence.** In an `n`-ring, powers with exponents congruent modulo
`n-1` agree. In particular, `x^{n-1}` is idempotent.

**Prime-power reduction.** Brandenburg reduces the fixed `n` problem to
characteristics `p` with `p-1 | n-1`, then to `p^k`-rings. The integer `k` is
determined by the prime powers `p^d` for which `p^d-1 | n-1`.

**`k=1`.** In a `p`-ring of characteristic `p`, each element can be written as
a finite `F_p`-linear combination of central idempotents, giving an equational
proof of commutativity.

**`k=2`.** Brandenburg proves every `p^2`-ring of characteristic `p`
commutative by equational methods. The proof uses power sums, Vandermonde
linear algebra, and noncommutative coefficient extraction.

**Constructive Wedderburn reduction.** To prove a `p^k`-ring commutative, it is
enough to prove the relevant `W_{p,k,f}` statements. Brandenburg further shows
that the monomial cases `f(T)=T^{p^i}` for `1 <= i < k` are sufficient.

**Period criterion.** If the composition class of `f` has period `pi` and
`d=gcd(pi,p^k-1)`, then `f^d(a)=a` in a `p^k`-ring. For monomials
`T^{p^m}`, the period is the order of `m` in `Z/kZ`. Hence if
`gcd(k,p^k-1)=1`, the monomial Wedderburn statements hold equationally.

**Consequence for `k=3`.** Since

```text
gcd(3,p^3-1) = 1  for p = 2, p = 3, or p == 2 mod 3,
gcd(3,p^3-1) = 3  for p == 1 mod 3,
```

Brandenburg's period theorem covers all `p^3`-rings except primes
`p == 1 mod 3`. The first uncovered prime is `p=7`, i.e. exponent `343`.

## Proof Techniques in the Literature

**Finite-field polynomial reductions.** Work in `F_p[T]` with polynomials such
as `T^n-T` and `T^{p^k}-T`, use gcds and extended Euclidean combinations, then
translate the resulting polynomial identities into equational ring proofs.

**Central idempotent decomposition.** Show powers such as `x^{n-1}` are
central idempotents, then decompose elements into idempotent and unit-like
parts. Commuting units then imply full commutativity.

**Vandermonde separation.** In the `p^2` case, evaluate identities over all
field elements and invert a Vandermonde matrix to isolate noncommutative
coefficients.

**Constructive Wedderburn sequences.** Starting from `ba=f(a)b`, build
sequences that combine conjugation-like relations until an equation forces a
commutator to vanish. Brandenburg's `8`- and `27`-ring computations are model
cases.

**Composition monoids over `F_p[T]/(T^{p^k}-T)`.** Analyze the period of
polynomial functions under composition. This is the cleanest route when the
period is coprime to `p^k-1`.

**Automated equational search.** Burris-Lawrence, Wavrik, and
Kinyon-MacHale support the use of rewrite systems, noncommutative polynomial
reduction, and Prover9/Mace4 for discovering finite equational derivations.

## Related Open Problems and Gaps

The practical unresolved target for this project is:

```text
For every prime p == 1 mod 3, construct an equational proof that
every characteristic-p ring satisfying x^{p^3}=x is commutative.
```

By Brandenburg's `weddermonomial` theorem, a focused route is to construct
equational proofs of

```text
W_{p,3,T^p}     and     W_{p,3,T^{p^2}}.
```

The period lemma alone gives only a 3-cycle relation in the uncovered cases,
because `3 | p^3-1`. A new argument must exploit additional identities of
`p^3`-rings, central powers, or a more refined constructive Wedderburn
calculation.

## Recommendations for Proof Strategy

1. Split the `k=3` proof by congruence class of `p mod 3`. Use Brandenburg's
   period criterion directly for `p=2`, `p=3`, and `p == 2 mod 3`.
2. For `p == 1 mod 3`, focus on the two monomial Wedderburn statements
   `W_{p,3,T^p}` and `W_{p,3,T^{p^2}}`.
3. Start computational exploration at `p=7`. It is the first missing case and
   should reveal whether a uniform finite sequence exists.
4. Use the odd-exponent centrality lemma from Kinyon-MacHale as an auxiliary
   identity: in the target rings with odd `p`, `x^{(p^3-1)/2}` is central.
5. Use SageMath for finite-field and composition-monoid calculations. Use
   Prover9 or noncommutative polynomial reduction to search for short
   equational certificates after candidate identities are found.
