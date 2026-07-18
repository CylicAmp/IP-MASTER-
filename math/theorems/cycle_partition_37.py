"""
37-Cycle Partition Theorem

The 12 three-cycles of the map f(n) = 26n mod 37 partition into
two equal groups of 6, determined by node-sum:

  Group A: node-sum = 37  (DR=1)  — 6 cycles
  Group B: node-sum = 74  (DR=2)  — 6 cycles

PROOF:
  For any cycle {n, 26n mod 37, 10n mod 37}, note that 1+26+10 = 37.
  Writing r₁ = 26n mod 37 and r₂ = 10n mod 37 as integers in {1..36}:

    n + r₁ + r₂
    = n + (26n - 37q₁) + (10n - 37q₂)
    = 37n - 37(q₁ + q₂)
    = 37(n - q₁ - q₂)

  The sum is ALWAYS a multiple of 37.
  Since all elements are in {1..36}, the sum lies in [3, 108].
  The only multiples of 37 in that range are 37 and 74.
  Therefore every cycle sums to exactly 37 or 74.  ∎

The binary DR split (DR=1 / DR=2) is a direct consequence:
  DR(37) = 1,  DR(74) = DR(7+4) = 2

Connection to X+Y=10:
  The 4 cycles with DR-path-sum=10 are exactly the cycles
  whose nodes are smallest (starting nodes 1,2,3,5).
  These are the first 4 cycles in canonical order, all in Group A.
"""


def dr(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


def get_all_cycles(field=37, residue=26):
    elements = set(range(1, field))
    cycles = []
    while elements:
        start = min(elements)
        curr = start
        cycle = []
        for _ in range(3):
            cycle.append(curr)
            elements.discard(curr)
            curr = (curr * residue) % field
        cycles.append(cycle)
    return cycles


all_cycles = get_all_cycles()

# Every cycle sum is a multiple of 37
for c in all_cycles:
    assert sum(c) % 37 == 0, f"Cycle {c} sum {sum(c)} not divisible by 37"

# Sums are only 37 or 74
sums = [sum(c) for c in all_cycles]
assert set(sums) == {37, 74}, f"Unexpected sums: {set(sums)}"

# Exactly 6 in each group
group_a = [c for c in all_cycles if sum(c) == 37]
group_b = [c for c in all_cycles if sum(c) == 74]
assert len(group_a) == 6
assert len(group_b) == 6

# DR of group sums
assert all(dr(sum(c)) == 1 for c in group_a)
assert all(dr(sum(c)) == 2 for c in group_b)


if __name__ == "__main__":
    print("37-CYCLE PARTITION")
    print(f"  1 + 26 + 10 = 37  (orbit generator sum = field prime)")
    print()
    print(f"Group A (sum=37, DR=1): {len(group_a)} cycles")
    for c in group_a:
        print(f"  {c}  dr-path={[dr(n) for n in c]}  path-sum={sum(dr(n) for n in c)}")
    print()
    print(f"Group B (sum=74, DR=2): {len(group_b)} cycles")
    for c in group_b:
        print(f"  {c}  dr-path={[dr(n) for n in c]}  path-sum={sum(dr(n) for n in c)}")
    print()
    print("All assertions passed.")
