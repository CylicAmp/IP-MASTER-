"""
17-Point Resonance Row and 1335 Partition Invariant

Two results:

1. RESONANCE ROW STRUCTURE
   Sequence: pairs (nn, nn+1) for each repeated digit 11..99, plus terminal 99.
   17 elements total.
   DR sequence splits into two bands:
     First 8:  [2,3,4,5,6,7,8,9]  — DR 2-9 (missing 1)
     Final 9:  [1,2,3,4,5,6,7,8,9] — complete DR cycle 1-9
   The 17-point row encodes one full DR cycle (1-9) plus a partial
   leading ramp (2-9), totaling 17 points.

2. 1335 PARTITION INVARIANT
   DR(1335) = 3.
   Any additive partition of the digit string "1335" reduces to DR=3:
     1+33+5  = 39  → DR=3
     13+35   = 48  → DR=3
     133+5   = 138 → DR=3
   This follows from DR algebra: DR(a+b) = DR(DR(a)+DR(b)),
   so any grouping of digits that sums to 1335 inherits DR=3.
"""


def dr(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


# 17-Point Resonance Row
seq = [11, 12, 22, 23, 33, 34, 44, 45, 55, 56, 66, 67, 77, 78, 88, 89, 99]
roots = [dr(x) for x in seq]

assert roots[:8]  == [2, 3, 4, 5, 6, 7, 8, 9], "First band failed"
assert roots[8:]  == [1, 2, 3, 4, 5, 6, 7, 8, 9], "Second band failed"

# 1335 Partition Invariant
partitions = [1 + 33 + 5, 13 + 35, 133 + 5]
partition_roots = [dr(p) for p in partitions]

assert all(r == 3 for r in partition_roots), "1335 invariant failed"
assert dr(1335) == 3, "DR(1335) != 3"


if __name__ == "__main__":
    print("17-Point Resonance Row:")
    print(f"  Sequence: {seq}")
    print(f"  DR values: {roots}")
    print(f"  Band 1 (positions 1-8):  {roots[:8]}")
    print(f"  Band 2 (positions 9-17): {roots[8:]}")
    print()
    print("1335 Partition Invariant:")
    for expr, val, r in zip(["1+33+5", "13+35", "133+5"], partitions, partition_roots):
        print(f"  {expr} = {val}  → DR={r}")
    print(f"  DR(1335) = {dr(1335)}")
    print()
    print("All assertions passed.")
