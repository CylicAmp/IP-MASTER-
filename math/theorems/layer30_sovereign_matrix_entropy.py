"""
1/137 Framework — Layer 30: 9×9 Sovereign Matrix and DR Orbit Entropy

9×9 SOVEREIGN MATRIX
  Two forms:
  (A) Raw form: spine column = 11r (not DR-reduced)
  (B) DR form:  spine column = DR(11r) = DR(2r)  [since 11 ≡ 2 mod 9]
  Outer columns (both forms): M[r,c] = DR(r×c) for c in {1,2,3,4,6,7,8,9}
  Mirror symmetry: M[r,c] = M[r,10-c] for c in {1,2,3,4}

DR ORBIT ENTROPY (uses DR form, all 81 values)
  Frequencies:
    DR in {1,2,4,5,7,8}: 7/81 each  (6 values × 7 = 42 outer + 6 spine)
    DR in {3,6,9}:       13/81 each (3 values × 13 = 36 outer + 3 spine)
    Total: 42+39 = 81 ✓
  Shannon entropy H ≈ 3.102 bits

Layer 30 protocol: syntax audit (ast.parse) + full execution + output comparison.
"""

import ast
import numpy as np
from scipy.stats import entropy


def _dr(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


def build_sovereign_matrix_raw():
    """Raw form: spine = 11r (not reduced)."""
    M = np.zeros((9, 9), dtype=int)
    for r in range(1, 10):
        M[r - 1, 4] = 11 * r
        for c in range(1, 5):
            prod = r * c
            dr_val = prod % 9 if prod % 9 != 0 else 9
            M[r - 1, c - 1] = dr_val
            M[r - 1, 9 - c] = dr_val
    return M


def build_sovereign_matrix_dr():
    """DR form: spine = DR(11r) = DR(2r), used for entropy."""
    M = np.zeros((9, 9), dtype=int)
    for r in range(1, 10):
        M[r - 1, 4] = _dr(11 * r)
        for c in range(1, 5):
            prod = r * c
            dr_val = prod % 9 if prod % 9 != 0 else 9
            M[r - 1, c - 1] = dr_val
            M[r - 1, 9 - c] = dr_val
    return M


def dr_orbit_entropy(M_dr):
    flat = M_dr.flatten()
    counts = np.bincount(flat)[1:]
    probs = counts / 81.0
    return entropy(probs, base=2), counts


# --- Syntax audit (Layer 30 protocol) ---
_code = """
M = np.zeros((9,9), dtype=int)
for r in range(1,10):
    M[r-1,4] = 11 * r
    for c in range(1,5):
        prod = r * c
        dr = prod % 9 if prod % 9 != 0 else 9
        M[r-1,c-1] = dr
        M[r-1,9-c] = dr
"""
ast.parse(_code)

# --- Assertions ---
M_raw = build_sovereign_matrix_raw()
M_dr  = build_sovereign_matrix_dr()

# Raw spine
assert list(M_raw[:, 4]) == [11 * r for r in range(1, 10)]

# DR spine: DR(11r) = DR(2r) since 11 ≡ 2 mod 9
for r in range(1, 10):
    assert M_dr[r - 1, 4] == _dr(2 * r), f"DR spine wrong at r={r}"

# Mirror symmetry (both forms)
for M in (M_raw, M_dr):
    for c in range(4):
        assert np.all(M[:, c] == M[:, 8 - c])

# Outer columns identical in both forms
assert np.all(M_raw[:, [0,1,2,3,5,6,7,8]] == M_dr[:, [0,1,2,3,5,6,7,8]])

# Entropy from DR form (all 81 values)
H, counts = dr_orbit_entropy(M_dr)
assert abs(H - 3.102) < 0.001, f"H={H:.3f}"
for d in [1, 2, 4, 5, 7, 8]:
    assert counts[d - 1] == 7,  f"DR={d}: {counts[d-1]}"
for d in [3, 6, 9]:
    assert counts[d - 1] == 13, f"DR={d}: {counts[d-1]}"

# DR spine adds exactly 1 of each of {1,2,3,4,5,6,7,8,9} — no bias
spine_dr = [M_dr[r, 4] for r in range(9)]
assert sorted(spine_dr) == list(range(1, 10))


if __name__ == "__main__":
    print("1/137 Layer 30 — 9×9 Sovereign Matrix + DR Orbit Entropy")
    print()
    print("Raw form (spine = 11r):")
    print(M_raw)
    print()
    print("DR form (spine = DR(11r), used for entropy):")
    print(M_dr)
    print()
    H, counts = dr_orbit_entropy(M_dr)
    print(f"Frequency counts DR 1..9: {list(counts)}")
    print(f"  {{1,2,4,5,7,8}} → 7/81 each")
    print(f"  {{3,6,9}}       → 13/81 each")
    print(f"Shannon entropy H = {H:.3f} bits")
    print()
    print(f"Note: DR(11r) = DR(2r) because 11 ≡ 2 (mod 9)")
    print(f"Spine DR values: {spine_dr}  (one of each 1-9, no bias)")
    print()
    print("Audit: ast.parse ✓  execution ✓  output match ✓")
    print("All assertions passed.")
