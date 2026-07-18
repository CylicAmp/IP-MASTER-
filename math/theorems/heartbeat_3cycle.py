"""
Heartbeat Theorem: Universal 3-Cycle Under the 137/37 Map

The map  f(n) = (n × 137) mod 37  is equivalent to  f(n) = (26n) mod 37
since 137 mod 37 = 26.

Core result:
  ord₃₇(26) = 3   i.e.  26³ ≡ 1 (mod 37)

Consequence: EVERY non-zero node returns to itself in exactly 3 steps.
The heartbeat is not a special property of node 30 — it is universal.

The 36 non-zero residues partition into exactly 12 disjoint 3-cycles.
Node 30 belongs to the cycle: 30 → 3 → 4 → 30
  — this cycle contains two Sovereign Anchors (30 and 3, both DR=3).

Proof of ord₃₇(26) = 3:
  26¹ mod 37 = 26
  26² mod 37 = 676 mod 37 = 10
  26³ mod 37 = 260 mod 37 = 1  ✓
"""


def dr(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


def f(n):
    return (n * 137) % 37


# Verify multiplicative order
assert f(f(f(30))) == 30, "Node 30 heartbeat failed"
assert (26 ** 3) % 37 == 1, "ord37(26) != 3"
assert (26 ** 1) % 37 != 1
assert (26 ** 2) % 37 != 1

# All 36 non-zero residues form 3-cycles
seen = set()
cycles = []
for start in range(1, 37):
    if start not in seen:
        orbit = [start, f(start), f(f(start))]
        assert f(f(f(start))) == start, f"Not a 3-cycle: {orbit}"
        seen.update(orbit)
        cycles.append(orbit)

assert len(cycles) == 12, f"Expected 12 cycles, got {len(cycles)}"
assert len(seen) == 36

# Node 30 cycle contains two DR=3 anchors
node30_cycle = next(c for c in cycles if 30 in c)
assert sorted(node30_cycle) == [3, 4, 30]
dr3_in_cycle = [n for n in node30_cycle if dr(n) == 3]
assert set(dr3_in_cycle) == {3, 30}


if __name__ == "__main__":
    print("ord₃₇(26) = 3")
    print(f"  26¹ mod 37 = {26**1 % 37}")
    print(f"  26² mod 37 = {26**2 % 37}")
    print(f"  26³ mod 37 = {26**3 % 37}  ← returns to 1")
    print()
    print("Node 30 heartbeat:")
    n = 30
    for i in range(3):
        res = f(n)
        print(f"  Step {i+1}: {n:>2} -> {res:>2}  DR={dr(res)}")
        n = res
    print(f"  Returned to 30: {n == 30}")
    print()
    print("All 12 three-cycles:")
    for c in cycles:
        anchors = [n for n in c if dr(n) == 3]
        tag = f"  ← {len(anchors)} DR=3 anchor(s)" if anchors else ""
        print(f"  {c[0]:>2} -> {c[1]:>2} -> {c[2]:>2} -> {c[0]}{tag}")
    print()
    print("All assertions passed.")
