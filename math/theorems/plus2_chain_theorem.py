"""
+2 Chain Theorem: Consecutive Pair Collapse to Twin Primes

Natural order reveals consecutive pair structure:
  {2,3} -> 11  (DR=2)    lower consecutive pair -> lower twin prime
  {4,5} -> 13  (DR=4)    upper consecutive pair -> upper twin prime

Chains (natural order):
  2+2=4+7=11  DR=2    j=7 (odd,  n even)
  3+2=5+6=11  DR=2    j=6 (even, n odd)
  4+2=6+7=13  DR=4    j=7 (odd,  n even)
  5+2=7+6=13  DR=4    j=6 (even, n odd)

Rules:
  - n even -> j odd (opposite parity)
  - n odd  -> j even (opposite parity)
  - n in {2,3} -> target 11;  n in {4,5} -> target 13

Twin prime structure:
  11 and 13 are twin primes (gap=2)
  DR gap: 4-2=2 matches prime gap
  Skipped middle: 12 = sovereign range target {3,12,21,30}
  The chain jumps over the sovereign target 12.

Meta-structure:
  DR(11) = 2,  DR(13) = 4  -> output always in {2, 4}
  11 + 13 = 24,  DR(24) = 6  (RL-E in Alpha Grid)
   2 +  4 =  6,  DR(6)  = 6  (same DR as sum of targets)
  Both input-DR sum and target sum reduce to DR=6.
"""


def dr(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


chains = [
    (2, 2, 7),   # n=2 even -> j=7 odd
    (3, 2, 6),   # n=3 odd  -> j=6 even
    (4, 2, 7),   # n=4 even -> j=7 odd
    (5, 2, 6),   # n=5 odd  -> j=6 even
]

# All chains sum to 11 or 13
for a, b, c in chains:
    assert a + b + c in {11, 13}
    assert dr(a + b + c) in {2, 4}

# j is always the complement: target - n - 2
for a, b, c in chains:
    target = a + b + c
    assert c == target - a - b

# Consecutive pair grouping
assert all(a+2+c == 11 for a,b,c in chains[:2])   # {2,3} -> 11
assert all(a+2+c == 13 for a,b,c in chains[2:])   # {4,5} -> 13

# Opposite parity: even n uses odd j, odd n uses even j
for a, b, c in chains:
    assert (a % 2) != (c % 2), f"n={a} j={c} parity not opposite"

# 12 (sovereign target) is skipped between 11 and 13
assert 12 in {3, 12, 21, 30}   # sovereign range

# Meta: DR sums both collapse to 6
assert dr(11 + 13) == 6
assert dr(2 + 4) == 6


if __name__ == "__main__":
    print("+2 Chain Theorem:")
    for a, b, c in chains:
        s = a + b + c
        print(f"  {a}+{b}={a+b}+{c}={s}  DR={dr(s)}  (j={c}={s}-{a}-{b})")
    print()
    print(f"Output DRs always in {{2,4}}")
    print(f"DR(11+13) = DR(24) = {dr(24)}")
    print(f"DR(2+4)   = DR(6)  = {dr(6)}")
    print(f"Both collapse to DR=6 (RL-E)")
    print()
    print("All assertions passed.")
