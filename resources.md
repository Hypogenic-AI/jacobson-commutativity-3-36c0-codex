# Resources Catalog

## Summary

This catalog records the mathematical resources gathered for the project
"Equational Proofs of Jacobson's Commutativity Theorem when `k=3`."

- Papers downloaded: 10
- Priority user-specified paper handled: arXiv:2310.05301
- Computational support created: lightweight SymPy helper plus documented
  SageMath/Prover9 recommendations
- Main mathematical takeaway: Brandenburg already proves the `p^3` case for
  `p=2`, `p=3`, and primes `p == 2 mod 3`; primes `p == 1 mod 3` remain the
  main proof-construction target.

## Papers

| Title | Authors | Year | File | Key Results |
|---|---|---:|---|---|
| Equational proofs of Jacobson's theorem | Martin Brandenburg | 2023 | `papers/2310.05301_brandenburg_equational_proofs_jacobson.pdf` | Prime-power reduction, `k=1`, `k=2`, constructive Wedderburn, period criterion |
| Elementary Proofs of Ring Commutativity Theorems | Michael K. Kinyon, Des MacHale | 2026 | `papers/2601.12599_kinyon_machale_elementary_proofs_ring_commutativity.pdf` | Odd-exponent central-power lemma, Prover9-assisted proofs |
| Equational proofs for a theorem by Jacobson for a significant density of even exponents | M. A. Daas | n.d. | `papers/daas_equational_proofs_density_even_exponents.pdf` | Equational proofs for many even exponents |
| Term Rewrite Rules for Finite Fields | Stanley N. Burris, John Lawrence | 1991 | `papers/burris_lawrence_1991_term_rewrite_rules_finite_fields.pdf` | Rewrite systems for finite fields and `x^m=x` identities |
| Commutativity Theorems: Examples in Search of Algorithms | John Wavrik | 1999 | `papers/wavrik_1999_commutativity_theorems_algorithms.pdf` | Algorithmic noncommutative polynomial reduction |
| A proof of Jacobson's theorem | J. M. Dolan | 1976 | `papers/dolan_1976_proof_of_jacobsons_theorem.pdf` | Choice-free constructive proof of Jacobson's theorem |
| On the commutativity of J-rings | Jiang Luh | 1967 | `papers/luh_1967_commutativity_of_j_rings.pdf` | Classical structure theory for fixed-exponent `J`-rings |
| Wedderburn's Theorem and a Theorem of Jacobson | I. N. Herstein | 1961 | `papers/herstein_1961_wedderburn_and_jacobson.pdf` | Elementary Wedderburn/Jacobson proof background |
| Variations on a theme: Rings satisfying `x^3=x` are commutative | Stephen M. Buckley, Des MacHale | 2013 | `papers/buckley_machale_2013_variations_x3_equals_x.pdf` | Low-exponent commutativity and centrality methods |
| A note on a theorem of Jacobson related to periodic rings | D. D. Anderson, Peter Danchev | 2020 | `papers/anderson_danchev_2020_periodic_rings_jacobson.pdf` | Periodic-ring extension of Jacobson-type commutativity |

See `papers/README.md` for source URLs and descriptions.

## Prior Results Catalog

| Result | Source | Statement Summary | Used For |
|---|---|---|---|
| Jacobson theorem | Jacobson; Dolan; Herstein | Potent rings are commutative | Semantic foundation |
| Equational existence for fixed `n` | Brandenburg via equational completeness | If all `n`-rings are commutative, then `xy=yx` has a formal equational proof | Justifies search for explicit derivations |
| Idempotents central in reduced rings | Standard; Brandenburg; Luh | If `e^2=e` in a reduced ring, then `e` commutes with every element | Basic equational reduction |
| Exponent congruence | Luh; Brandenburg | In an `n`-ring, congruent exponents modulo `n-1` give equal powers | Power simplification |
| Prime-power reduction | Brandenburg | Fixed `n` reduces to characteristic `p` and then to `p^k` identities | Narrows the proof target |
| `p`-ring proof | Brandenburg | Characteristic-`p` rings with `x^p=x` are commutative equationally | Base case |
| `p^2`-ring proof | Brandenburg | Characteristic-`p` rings with `x^{p^2}=x` are commutative equationally | Previous case before `k=3` |
| Constructive Wedderburn reduction | Brandenburg | It suffices to prove suitable `W_{p,k,f}` identities | Main route for `k=3` |
| Monomial sufficiency | Brandenburg | It suffices to prove `W_{p,k,T^{p^i}}` for `1 <= i < k` | Reduces `k=3` to two monomials |
| Period criterion | Brandenburg | If `gcd(k,p^k-1)=1`, the monomial Wedderburn statements follow | Solves most `k=3` primes |
| Odd central-power lemma | Kinyon-MacHale | In a `(2m+1)`-potent ring, `x^m` is central | Extra identity for odd `p^3` |
| Automated centrality proofs | Kinyon-MacHale; Wavrik | Prover9 and polynomial-reduction methods can discover finite derivations | Search support |

## Computational Tools

| Tool | Purpose | Location | Notes |
|---|---|---|---|
| SymPy | Lightweight finite-field polynomial checks | Installed in `.venv`; helper at `code/finite_field_reductions.py` | Good for small gcd and congruence tests |
| SageMath | Finite fields, quotient rings, polynomial composition monoids | External recommendation | Best match for Brandenburg's appendix code |
| Prover9/Mace4 | Equational proof and model search | External recommendation | Used in related commutativity work |

The helper script supports checks such as:

```bash
source .venv/bin/activate
python code/finite_field_reductions.py --p 7 --k 3
python code/finite_field_reductions.py --n 7 --p 2 --max-degree 3
```

## Search Strategy

The first search used the required paper-finder service with the query
"Jacobson commutativity theorem x^n = x p^3 characteristic p equational proof
rings" in diligent mode. The service timed out and returned its fallback file
under `paper_search_results/`, so manual search was used afterward.

Manual search focused on:

- the user-specified arXiv paper `2310.05301`;
- references inside Brandenburg's bibliography;
- arXiv searches for recent fixed-exponent commutativity papers;
- open publisher PDFs and author-hosted PDFs;
- computational algebra papers on equational theories and rewrite systems.

## Selection Criteria

Priority went to papers that either:

- prove Jacobson commutativity or fixed-exponent variants;
- construct equational proofs rather than only semantic ring-theoretic proofs;
- provide algorithms for noncommutative polynomial/equational search;
- contain centrality lemmas usable in the `p^3` case.

## Challenges Encountered

- Paper-finder timed out, so manual search and reference chasing were required.
- Some older papers were behind paywalls or blocked direct PDF access:
  Forsythe-McCoy (1946), Zhang (1990), Hansen-Luh-Ye (1994), Morita (1978),
  Wamsley (1971), Nagahara-Tominaga (1974), Herstein (1954), and Jacobson
  (1945).
- Several publisher PDFs required alternate mirrors or direct service URLs.

## Recommendations for Proof Construction

1. Treat `p=2`, `p=3`, and `p == 2 mod 3` as covered by Brandenburg's
   `gcd(k,p^k-1)=1` criterion for `k=3`.
2. For primes `p == 1 mod 3`, prove `W_{p,3,T^p}` and `W_{p,3,T^{p^2}}`.
3. Begin with `p=7` as the smallest open prime and search for a uniform
   constructive Wedderburn sequence.
4. Add the Kinyon-MacHale centrality identity
   `x^{(p^3-1)/2} in Z(R)` as a candidate auxiliary equation for odd `p`.
5. Use SageMath to enumerate polynomial functions on `F_{p^3}` and Prover9 or
   noncommutative polynomial reduction to turn candidate identities into
   equational certificates.
