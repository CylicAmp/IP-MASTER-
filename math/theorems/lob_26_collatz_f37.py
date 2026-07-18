"""
LoB 26 — Collatz Map T in F_37

Map definition:
  T(x) = x · 19 (mod 37)   if x is even   [division by 2: 2^-1 ≡ 19 mod 37]
  T(x) = 3x + 1 (mod 37)   if x is odd

Theorem (by exhaustive enumeration):
  T has exactly 3 cycles in F_37:
    Cycle 1 (length 1): {0}           — fixed point
    Cycle 2 (length 3): {1→4→2→1}
    Cycle 3 (length 9): {7→22→11→34→17→15→9→28→14→7}
  Total cycle elements: 13. Remaining 24 residues are basin nodes.

Corollary: (3|37) = +1.
  Odd-branch multiplier 3 is QR; sqrt(3) mod 37 = {15, 22} (= ±15 mod 37).
  Note: "±15" and "±22" name the same pair since 37-15=22.

Structural comparison:
  f(n) = 3n+1 (pure linear): 3 cycles of lengths [1, 18, 18] — different structure.
  g(n) = 2n+19: matches T at exactly one point, x=12. Not a Collatz branch.

Modulus-specificity:
  Cycle structure [1,3,9] is F_37-specific. Other primes yield different patterns.
  QR status of elements has no predictive correlation with cycle membership.
"""

import math


def T(x, p=37):
    return (x * 19) % p if x % 2 == 0 else (3 * x + 1) % p


def find_cycles(fn, p=37):
    visited, cycles = set(), []
    for start in range(p):
        if start in visited:
            continue
        path, seen, x = [], {}, start
        while x not in visited and x not in seen:
            seen[x] = len(path)
            path.append(x)
            x = fn(x)
        if x in seen:
            cycle = path[seen[x]:]
            cycles.append(cycle)
            visited.update(cycle)
        visited.update(path)
    return sorted(cycles, key=len)


# --- Assertions ---

# 2-inverse
assert (2 * 19) % 37 == 1

# Fixed point
assert T(0) == 0

# Cycle decomposition
cycles = find_cycles(T)
assert len(cycles) == 3
assert sorted(len(c) for c in cycles) == [1, 3, 9]
assert sum(len(c) for c in cycles) == 13

# Specific cycles
assert T(1) == 4 and T(4) == 2 and T(2) == 1   # 3-cycle
nine_cycle = [7, 22, 11, 34, 17, 15, 9, 28, 14]
for i, x in enumerate(nine_cycle):
    assert T(x) == nine_cycle[(i + 1) % 9], f"9-cycle broken at {x}"

# sqrt(3): two roots, not four
sqrts_3 = [n for n in range(37) if (n * n) % 37 == 3]
assert sqrts_3 == [15, 22]   # ±15 mod 37; 37-15=22 (same pair, not four values)

# g matches T at exactly x=12
def g(x): return (2 * x + 19) % 37
assert [x for x in range(37) if g(x) == T(x)] == [12]

# f(n)=3n+1 has cycles [1, 18, 18]
def f(x): return (3 * x + 1) % 37
f_cycles = find_cycles(f)
assert sorted(len(c) for c in f_cycles) == [1, 18, 18]


if __name__ == "__main__":
    print("LoB 26 — Collatz Map T in F_37")
    print()
    print("T(x) = 19x mod 37  (x even)  |  T(x) = 3x+1 mod 37  (x odd)")
    print(f"2^-1 ≡ 19 (mod 37): {(2*19)%37 == 1}")
    print()
    cycles = find_cycles(T)
    for c in cycles:
        arrow = " → ".join(map(str, c)) + f" → {T(c[-1])}"
        print(f"  Cycle (len {len(c)}): {arrow}")
    print(f"Total in cycles: {sum(len(c) for c in cycles)} / 37")
    print()
    print(f"sqrt(3) mod 37 = {sqrts_3}  (±15 mod 37 — two roots, not four)")
    print()
    print("Comparison:")
    f_cycles = find_cycles(f)
    print(f"  f(n)=3n+1 cycles: {sorted(len(c) for c in f_cycles)}")
    print(f"  g(n)=2n+19 matches T at: {[x for x in range(37) if g(x)==T(x)]}")
    print()
    print("All assertions passed.")
