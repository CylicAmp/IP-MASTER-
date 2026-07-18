"""
Euler's Totient Function φ(n).

φ(n) counts the positive integers up to n that are relatively prime to n.
i.e. the count of k in [1..n] where gcd(k, n) = 1.

Key properties:
  - Prime p:          φ(p) = p − 1
  - Prime power p^k:  φ(p^k) = p^k − p^(k−1)
  - Multiplicative:   φ(mn) = φ(m)φ(n)  when gcd(m,n) = 1
  - General formula:  φ(n) = n ∏_{p|n} (1 − 1/p)

φ(37) = 36  — the 37-field has 36 non-zero residues (37 is prime).
"""

import sympy


def totient_table(start: int = 1, end: int = 40) -> list:
    """Return list of (n, φ(n)) for n in [start, end]."""
    return [(n, sympy.totient(n)) for n in range(start, end + 1)]


def totient_values(start: int = 1, end: int = 40) -> list:
    """Return φ(n) values only, for n in [start, end]."""
    return [sympy.totient(n) for n in range(start, end + 1)]


def demonstrate() -> None:
    table = totient_table(1, 40)
    values = [phi for _, phi in table]

    print("=" * 56)
    print("  EULER'S TOTIENT FUNCTION φ(n) — n = 1 to 40")
    print("=" * 56)

    # Per-line output
    for n, phi in table:
        marker = ""
        if sympy.isprime(n):
            marker = f"  (prime: φ = n−1 = {n-1})"
        print(f"  φ({n:2d}) = {int(phi):2d}{marker}")

    print()
    print(f"Values list: {values}")

    # Key structural notes
    print()
    print("Key values:")
    print(f"  φ(37) = {sympy.totient(37)}  — 37 is prime; 36 non-zero residues in the 37-field")
    print(f"  sum φ(1..36) = {sum(sympy.totient(n) for n in range(1, 37))}")
    print(f"  φ(36) = {sympy.totient(36)}   — 12 coprimes to 36")

    # Verify multiplicativity example
    print()
    print("Multiplicativity checks (gcd(m,n)=1 → φ(mn)=φ(m)φ(n)):")
    for m, n in [(3, 5), (4, 9), (7, 8)]:
        lhs = int(sympy.totient(m * n))
        rhs = int(sympy.totient(m)) * int(sympy.totient(n))
        print(f"  φ({m}×{n}) = φ({m*n}) = {lhs}  |  φ({m})×φ({n}) = {rhs}  {'✓' if lhs == rhs else '✗'}")


if __name__ == "__main__":
    demonstrate()
