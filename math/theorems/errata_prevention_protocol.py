"""
Errata Prevention Protocol — MWS v37.21+

Three classes of errors found in this framework:
  E1: Geometric incidence claim from memory (120-cell cells/edge: 4 → 3)
  E2: QR membership claimed without computation (5 is QR → false, Legendre=-1)
  E3: Duplicate structural fields (is_square == has_sqrt before LoB 23b fix)

Prevention strategies per error class:

CLASS A — MODULAR ARITHMETIC CLAIMS
  Rule: Never assert QR membership, order, or inverse without computing it.
  Oracle: Legendre symbol via Euler criterion  a^((p-1)/2) mod p
  Oracle: Explicit residue table enumeration
  Standard: mpmath dps ≥ 50 for any float-derived residue

CLASS B — GEOMETRIC / COMBINATORIAL CLAIMS
  Rule: Never state incidence numbers (cells/edge, faces/vertex) from memory.
  Oracle: Compute via (total_cells × edges_per_cell) / total_edges
  Reference table for 120-cell (verified):
    Cells: 120 (dodecahedra)     Faces: 720 (pentagons)
    Edges: 1200                  Vertices: 600
    Cells/edge: 3                Faces/edge: 2
    Edges/cell: 30               Vertices/cell: 20

CLASS C — STRUCTURAL FIELD DUPLICATION
  Rule: Before adding a new field to a feature vector, check all existing fields
        for identical computation. Flag if any two fields share the same formula.
  Audit hook: compute pairwise equality of field values across all 37 residues.

LEGENDRE ORACLE (production-ready)
  Covers all framework-critical checks:
  - Is residue r a QR mod 37?
  - What is its square root?
  - Is the map multiplier (26) QR? (yes, sqrt=10)
  - Are all sovereign anchors/targets QR? (yes — Sovereign QR Closure Theorem)
"""

import math


def legendre_37(a):
    a = a % 37
    if a == 0:
        return 0
    val = pow(a, 18, 37)   # (37-1)/2 = 18
    return 1 if val == 1 else -1


def sqrt_mod37(a):
    a = a % 37
    for n in range(37):
        if (n * n) % 37 == a:
            return n
    return None


def field_vector_duplication_check(field_funcs, residues=range(37)):
    duplicates = []
    names = list(field_funcs.keys())
    vectors = {name: [field_funcs[name](r) for r in residues] for name in names}
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if vectors[names[i]] == vectors[names[j]]:
                duplicates.append((names[i], names[j]))
    return duplicates


def verify_120cell_geometry():
    cells, edges_per_cell, total_edges = 120, 30, 1200
    assert (cells * edges_per_cell) / total_edges == 3.0
    return 3


def qr_oracle_check(claimed_qrs, p=37):
    qr_actual = frozenset((n * n) % p for n in range(p))
    false_positives = [r for r in claimed_qrs if r not in qr_actual]
    false_negatives = [r for r in qr_actual if r not in claimed_qrs]
    return false_positives, false_negatives


# --- Self-test: apply all three prevention strategies ---

# CLASS A: Legendre oracle spot checks
assert legendre_37(4)  == 1   # anchor
assert legendre_37(9)  == 1   # anchor
assert legendre_37(25) == 1   # anchor
assert legendre_37(30) == 1   # anchor
assert legendre_37(3)  == 1   # target
assert legendre_37(5)  == -1  # PIVOT — non-residue
assert legendre_37(26) == 1   # SCALAR_137 — QR
assert sqrt_mod37(26)  == 10  # 10² ≡ 26 mod 37

# CLASS B: Geometric oracle
assert verify_120cell_geometry() == 3

# CLASS C: Duplication check on is_square vs has_sqrt (the E3 bug pattern)
qr_set = frozenset((n * n) % 37 for n in range(37))
perfect_squares = frozenset(n * n for n in range(7))  # {0,1,4,9,16,25,36}
fields = {
    'is_square': lambda r: r in perfect_squares,
    'has_sqrt':  lambda r: r in qr_set,
}
dups = field_vector_duplication_check(fields)
assert dups == [], f"Duplicate fields detected: {dups}"  # should be clean now

# QR oracle cross-check: verify FPS-37 QR set is exact
fps37_qr = {0,1,3,4,7,9,10,11,12,16,21,25,26,27,28,30,33,34,36}
fp, fn = qr_oracle_check(fps37_qr)
assert fp == [], f"False positives in FPS-37 QR set: {fp}"
assert fn == [], f"False negatives in FPS-37 QR set: {fn}"


if __name__ == "__main__":
    print("Errata Prevention Protocol — MWS v37.21+")
    print()
    print("CLASS A — Legendre oracle:")
    for r, name in [(4,'anchor'), (9,'anchor'), (25,'anchor'), (30,'anchor/target'),
                     (5,'PIVOT'), (26,'SCALAR_137')]:
        L = legendre_37(r)
        s = sqrt_mod37(r)
        print(f"  ({r:2d}|37) = {L:+d}   {name}   sqrt={s}")
    print()
    print("CLASS B — 120-cell geometry oracle:")
    cells_per_edge = verify_120cell_geometry()
    print(f"  120×30/1200 = {cells_per_edge} cells per edge")
    print()
    print("CLASS C — Field duplication check:")
    print(f"  is_square vs has_sqrt: duplicates = {dups}  (clean)")
    print()
    print("QR set cross-check:")
    print(f"  False positives: {fp}  False negatives: {fn}")
    print()
    print("All assertions passed.")
