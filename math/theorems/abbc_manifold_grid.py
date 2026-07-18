"""
ABBC Manifold Grid Structure — Verified

The grid enumerates all integer pairs (a,b) with a,b in {0..9},
organized in blocks by sum value s = a+b, with mirror symmetry.

Descending double sequence (same-pair blocks):
  nn = n+n = 2n = n+n   for n = 9,8,...,1
  Sums: 18,16,14,12,10,8,6,4,2 (even, descending)
  DRs: 9,7,5,3,1,8,6,4,2  (all 9 distinct values, one pass)

13/14 adjacency observation (status: CONJECTURE):
  Sum 13 appears at row (6+7) / (7+6)
  Sum 14 appears at row (7+7)
  First Riemann zero rho_1 = 14.134725 sits at this crossing.
  Decimal trade: 14.13 approximates rho_1 with error 0.0047.
  Status: pattern observation — not yet proved as derivation.

Row-sum triples (verified):
  {1,3,5}: sum=9   DR=9
  {2,4,6}: sum=12  DR=3
  {7,8,9}: sum=24  DR=6

Arithmetic chains (all verified):
  14+13=27  DR=9
  7+11=18   DR=9
  |13-16|=3,  11-7=4,  7-4=3  (interval gaps)
  13+16=29, digit_sum(29)=11
"""


def dr(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


# Descending double sequence
DOUBLE_SEQUENCE = [(n, 2 * n) for n in range(9, 0, -1)]

# DR of sums: 18,16,...,2
DOUBLE_DR_SEQUENCE = [dr(2 * n) for n in range(9, 0, -1)]


# --- Assertions ---

# Descending double DRs cover all 9 distinct values
assert sorted(DOUBLE_DR_SEQUENCE) == list(range(1, 10))

# Row-sum triples
assert dr(1 + 3 + 5) == 9
assert dr(2 + 4 + 6) == 3
assert dr(7 + 8 + 9) == 6

# Arithmetic chains
assert dr(14 + 13) == 9
assert dr(7 + 11) == 9
assert abs(13 - 16) == 3
assert 11 - 7 == 4
assert 7 - 4 == 3
assert (2 + 9) == 11          # digit_sum(29) = 11
assert 9 + 4 == 13
assert 13 + 7 == 20

# 13/14 adjacency: rho_1 sits between sums 13 and 14
rho1_actual = 14.134725
approximation = 14.13
assert 13 < rho1_actual < 14 + 1   # bounded above by 15
assert int(rho1_actual) == 14       # integer part = 14
assert abs(approximation - rho1_actual) < 0.01  # approximation within 1%

# Mirror symmetry: a+b == b+a (trivial but stated)
for a in range(10):
    for b in range(10):
        assert a + b == b + a


if __name__ == "__main__":
    print("ABBC Manifold Grid Structure")
    print()
    print("Descending double sequence:")
    for n, s in DOUBLE_SEQUENCE:
        print(f"  {n}{n}={n}+{n}={s}  DR={dr(s)}")
    print(f"  DR sequence: {DOUBLE_DR_SEQUENCE}  (all 9 distinct values)")
    print()

    print("Row-sum triples:")
    for group, label in [([1,3,5],'odd'), ([2,4,6],'even'), ([7,8,9],'terminal')]:
        s = sum(group)
        print(f"  {group}: sum={s}  DR={dr(s)}")
    print()

    print("13/14 adjacency (rho_1 observation):")
    print(f"  6+7=13  7+7=14  rho_1={rho1_actual}")
    print(f"  Decimal trade: 14.13  error={abs(approximation-rho1_actual):.4f}")
    print(f"  Status: CONJECTURE (approximation, not derivation)")
    print()
    print("All assertions passed.")
