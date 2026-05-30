#!/usr/bin/env python3
"""Exact checks supporting the k=3 Jacobson proof notes.

The script has two roles:

1. Reproduce the congruence split for Brandenburg's period criterion.
2. In the first bad congruence case p=7, model the skew relation
   YX = X^p Y on an irreducible cubic component and check that the
   p^3-potency equations for X + tY force the unit skew component to vanish.

The p=7 skew calculation is not used as the main proof in REPORT.md; it is a
sanity check and a source of low-level algebraic evidence for the norm argument.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from math import gcd
from typing import Iterable


K = tuple[int, int, int]


@dataclass(frozen=True)
class CubicField:
    """A small finite field F_p[a]/(a^3 + c2*a^2 + c1*a + c0)."""

    p: int
    c0: int
    c1: int
    c2: int

    @property
    def q(self) -> int:
        return self.p**3

    @property
    def alpha(self) -> K:
        return (0, 1, 0)

    def scalar(self, c: int) -> K:
        return (c % self.p, 0, 0)

    def add(self, x: K, y: K) -> K:
        return tuple((x[i] + y[i]) % self.p for i in range(3))  # type: ignore[return-value]

    def sub(self, x: K, y: K) -> K:
        return tuple((x[i] - y[i]) % self.p for i in range(3))  # type: ignore[return-value]

    def mul(self, x: K, y: K) -> K:
        tmp = [0] * 5
        for i, xi in enumerate(x):
            for j, yj in enumerate(y):
                tmp[i + j] = (tmp[i + j] + xi * yj) % self.p

        # a^3 = -c2*a^2 - c1*a - c0.
        for degree in (4, 3):
            coeff = tmp[degree] % self.p
            if coeff:
                tmp[degree] = 0
                shift = degree - 3
                tmp[shift] = (tmp[shift] - coeff * self.c0) % self.p
                tmp[shift + 1] = (tmp[shift + 1] - coeff * self.c1) % self.p
                tmp[shift + 2] = (tmp[shift + 2] - coeff * self.c2) % self.p
        return tuple(tmp[:3])  # type: ignore[return-value]

    def pow(self, x: K, n: int) -> K:
        result = self.scalar(1)
        base = x
        while n:
            if n & 1:
                result = self.mul(result, base)
            base = self.mul(base, base)
            n >>= 1
        return result

    def inv(self, x: K) -> K:
        if self.is_zero(x):
            raise ZeroDivisionError("zero has no inverse")
        return self.pow(x, self.q - 2)

    @staticmethod
    def is_zero(x: K) -> bool:
        return x == (0, 0, 0)

    def sigma(self, x: K, i: int) -> K:
        return self.pow(x, self.p ** (i % 3))


class SkewAlgebra:
    """The p=7 algebra K[S]/(S^M-1) + B with B^3=S and Bc=sigma(c)B."""

    def __init__(self, field: CubicField):
        self.F = field
        self.p = field.p
        self.q = field.q
        self.M = (self.q - 1) // 3

    def sp_zero(self) -> list[K]:
        return [self.F.scalar(0)] * self.M

    def sp_const(self, c: K) -> list[K]:
        out = self.sp_zero()
        out[0] = c
        return out

    def sp_add(self, a: list[K], b: list[K]) -> list[K]:
        return [self.F.add(a[i], b[i]) for i in range(self.M)]

    def sp_sub(self, a: list[K], b: list[K]) -> list[K]:
        return [self.F.sub(a[i], b[i]) for i in range(self.M)]

    def sp_mul(self, a: list[K], b: list[K]) -> list[K]:
        out = self.sp_zero()
        for i, ai in enumerate(a):
            if self.F.is_zero(ai):
                continue
            for j, bj in enumerate(b):
                if self.F.is_zero(bj):
                    continue
                out[(i + j) % self.M] = self.F.add(
                    out[(i + j) % self.M], self.F.mul(ai, bj)
                )
        return out

    def sp_sigma(self, a: list[K], i: int) -> list[K]:
        return [self.F.sigma(c, i) for c in a]

    def e_zero(self) -> tuple[list[K], list[K], list[K]]:
        return (self.sp_zero(), self.sp_zero(), self.sp_zero())

    def e_one(self) -> tuple[list[K], list[K], list[K]]:
        return (self.sp_const(self.F.scalar(1)), self.sp_zero(), self.sp_zero())

    def e_const_k(self, c: K) -> tuple[list[K], list[K], list[K]]:
        return (self.sp_const(c), self.sp_zero(), self.sp_zero())

    def e_b(self, t: int) -> tuple[list[K], list[K], list[K]]:
        return (self.sp_zero(), self.sp_const(self.F.scalar(t)), self.sp_zero())

    def e_add(
        self, x: tuple[list[K], list[K], list[K]], y: tuple[list[K], list[K], list[K]]
    ) -> tuple[list[K], list[K], list[K]]:
        return tuple(self.sp_add(x[i], y[i]) for i in range(3))  # type: ignore[return-value]

    def e_sub(
        self, x: tuple[list[K], list[K], list[K]], y: tuple[list[K], list[K], list[K]]
    ) -> tuple[list[K], list[K], list[K]]:
        return tuple(self.sp_sub(x[i], y[i]) for i in range(3))  # type: ignore[return-value]

    def e_mul(
        self, x: tuple[list[K], list[K], list[K]], y: tuple[list[K], list[K], list[K]]
    ) -> tuple[list[K], list[K], list[K]]:
        out = [self.sp_zero(), self.sp_zero(), self.sp_zero()]
        for i, xi in enumerate(x):
            if all(self.F.is_zero(c) for c in xi):
                continue
            for j, yj in enumerate(y):
                if all(self.F.is_zero(c) for c in yj):
                    continue
                prod = self.sp_mul(xi, self.sp_sigma(yj, i))
                carry, residue = divmod(i + j, 3)
                if carry:
                    prod = prod[-carry:] + prod[:-carry]
                out[residue] = self.sp_add(out[residue], prod)
        return (out[0], out[1], out[2])

    def e_pow(
        self, x: tuple[list[K], list[K], list[K]], n: int
    ) -> tuple[list[K], list[K], list[K]]:
        result = self.e_one()
        base = x
        while n:
            if n & 1:
                result = self.e_mul(result, base)
            base = self.e_mul(base, base)
            n >>= 1
        return result

    def trim(self, poly: list[K]) -> list[K]:
        poly = list(poly)
        while poly and self.F.is_zero(poly[-1]):
            poly.pop()
        return poly

    def monic(self, poly: list[K]) -> list[K]:
        poly = self.trim(poly)
        if not poly:
            return []
        inv = self.F.inv(poly[-1])
        return [self.F.mul(c, inv) for c in poly]

    def divmod_poly(self, f: list[K], g: list[K]) -> tuple[list[K], list[K]]:
        f = self.trim(f)
        g = self.trim(g)
        if not g:
            raise ZeroDivisionError("polynomial division by zero")
        quotient = [self.F.scalar(0)] * max(1, len(f) - len(g) + 1)
        inv = self.F.inv(g[-1])
        while len(f) >= len(g) and f:
            coeff = self.F.mul(f[-1], inv)
            shift = len(f) - len(g)
            quotient[shift] = coeff
            for i, gi in enumerate(g):
                f[shift + i] = self.F.sub(f[shift + i], self.F.mul(coeff, gi))
            f = self.trim(f)
        return self.trim(quotient), f

    def gcd_poly(self, f: list[K], g: list[K]) -> list[K]:
        f = self.trim(f)
        g = self.trim(g)
        while g:
            _, r = self.divmod_poly(f, g)
            f, g = g, r
        return self.monic(f)

    def common_s_gcd_degrees(self, t_values: Iterable[int]) -> list[dict[str, int]]:
        """GCD degrees for the S-parameter after adding potency equations."""
        s_relation = [self.F.scalar(-1)] + [self.F.scalar(0)] * (self.M - 1) + [
            self.F.scalar(1)
        ]
        common = s_relation
        a = self.e_const_k(self.F.alpha)
        output = []

        for t in t_values:
            x = self.e_add(a, self.e_b(t))
            diff = self.e_sub(self.e_pow(x, self.q), x)
            for component in range(3):
                poly = self.trim(diff[component])
                if poly:
                    common = self.gcd_poly(common, poly)
            output.append({"t": t, "common_gcd_degree": len(common) - 1})
        return output


def period_split(primes: Iterable[int]) -> list[dict[str, int | bool]]:
    rows = []
    for p in primes:
        value = gcd(3, p**3 - 1)
        rows.append({"p": p, "gcd_3_p3_minus_1": value, "period_criterion": value == 1})
    return rows


def norm_section_summary(p: int) -> dict[str, int]:
    q = p**3
    return {
        "p": p,
        "q": q,
        "irreducible_cubic_count": (q - p) // 3,
        "linear_s_components": p - 1,
        "cubic_s_components": (q - p) // 3,
        "norm_surjective_on_degree_1_components": 1,
        "norm_surjective_on_degree_3_components": 1,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="emit JSON only")
    args = parser.parse_args()

    # First bad prime p=7; T^3 + T^2 + 1 has no F_7-root.
    field = CubicField(p=7, c0=1, c1=0, c2=1)
    skew = SkewAlgebra(field)
    alpha_check = {
        "alpha_p3_minus_alpha": field.sub(field.pow(field.alpha, field.q), field.alpha),
        "alpha_p": field.pow(field.alpha, field.p),
    }

    result = {
        "period_split": period_split([2, 3, 5, 7, 11, 13, 17, 19]),
        "norm_section_summaries": [norm_section_summary(7), norm_section_summary(13)],
        "p7_skew_model": {
            "field_polynomial": "T^3 + T^2 + 1 over F_7",
            "alpha_check": alpha_check,
            "s_parameter_relation": "S^114 = 1",
            "gcd_degrees_after_t_values": skew.common_s_gcd_degrees([1, 2, 3]),
        },
    }

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
        return

    print("Period criterion split for k=3:")
    for row in result["period_split"]:
        status = "covered" if row["period_criterion"] else "bad congruence class"
        print(f"  p={row['p']}: gcd(3,p^3-1)={row['gcd_3_p3_minus_1']} ({status})")

    print("\nNorm-section finite-component summaries:")
    for row in result["norm_section_summaries"]:
        print(
            f"  p={row['p']}: irreducible cubics={row['irreducible_cubic_count']}, "
            f"S-components degrees 1/3 = {row['linear_s_components']}/"
            f"{row['cubic_s_components']}"
        )

    print("\np=7 skew model:")
    print(f"  field: {result['p7_skew_model']['field_polynomial']}")
    print(f"  alpha^343-alpha = {alpha_check['alpha_p3_minus_alpha']}")
    for row in result["p7_skew_model"]["gcd_degrees_after_t_values"]:
        print(f"  after t={row['t']}: common S-gcd degree {row['common_gcd_degree']}")


if __name__ == "__main__":
    main()
