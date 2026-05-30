#!/usr/bin/env python3
"""Finite-field checks for fixed-exponent Jacobson reductions.

This is a lightweight SymPy companion to the SageMath routines in
Brandenburg's arXiv:2310.05301 appendix. It is intended for small cases and
for quickly checking which prime-power target appears in the one-variable
reduction step.
"""

from __future__ import annotations

import argparse
from itertools import product
from math import gcd, lcm

from sympy import Poly, Symbol, divisors, isprime


T = Symbol("T")


def n_primes(n: int) -> list[int]:
    """Primes p such that p - 1 divides n - 1."""
    return sorted(d + 1 for d in divisors(n - 1) if isprime(d + 1))


def reduction_exponent(n: int, p: int) -> int:
    """Least common multiple of d with p**d - 1 dividing n - 1."""
    ds = []
    d = 1
    while p**d - 1 <= n - 1:
        if (n - 1) % (p**d - 1) == 0:
            ds.append(d)
        d += 1
    if not ds:
        raise ValueError(f"p={p} is not relevant for n={n}")
    return lcm(*ds)


def monic_polynomials(p: int, max_degree: int):
    """Yield monic polynomials over GF(p), ordered by degree."""
    for degree in range(1, max_degree + 1):
        for coeffs in product(range(p), repeat=degree):
            expr = T**degree + sum(c * T**i for i, c in enumerate(coeffs))
            yield Poly(expr, T, modulus=p)


def reduction_gcd(n: int, p: int, max_degree: int = 3):
    """Compute a partial gcd of f**n - f over GF(p)."""
    k = reduction_exponent(n, p)
    target = Poly(T ** (p**k) - T, T, modulus=p)
    current = None
    used: list[Poly] = []

    for f in monic_polynomials(p, max_degree=max_degree):
        rel = Poly(f.as_expr() ** n - f.as_expr(), T, modulus=p)
        if rel.is_zero:
            continue
        current = rel.monic() if current is None else current.gcd(rel).monic()
        used.append(f)
        if target.rem(current).is_zero:
            return k, target, current, used

    return k, target, current, used


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, help="fixed exponent n in x^n = x")
    parser.add_argument("--p", type=int, required=True, help="prime characteristic")
    parser.add_argument("--max-degree", type=int, default=3)
    parser.add_argument(
        "--k",
        type=int,
        help="check Brandenburg gcd criterion gcd(k, p^k - 1) = 1",
    )
    args = parser.parse_args()

    if args.k is not None:
        value = gcd(args.k, args.p**args.k - 1)
        print(f"gcd({args.k}, {args.p}^{args.k} - 1) = {value}")
        print("gcdmain applies" if value == 1 else "gcdmain does not apply")

    if args.n is not None:
        print(f"n-primes({args.n}) = {n_primes(args.n)}")
        k, target, current, used = reduction_gcd(args.n, args.p, args.max_degree)
        print(f"reduction exponent k = {k}; target = {target.as_expr()}")
        print(f"partial gcd = {None if current is None else current.as_expr()}")
        print("polynomials used:")
        for f in used:
            print(f"  {f.as_expr()}")


if __name__ == "__main__":
    main()
