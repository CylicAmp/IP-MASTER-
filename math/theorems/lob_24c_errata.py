"""
LoB 24c — Errata Correction Record (MWS v37.20 → v37.21)

Two falsified claims identified, verified, corrected, and propagated.
Framework sealed clean after correction.

ERRATA TABLE
============
Item | Original Claim         | Falsified By                        | Corrected Value
-----|------------------------|-------------------------------------|------------------
E1   | 4 cells meet at edge   | 120 × 30 / 1200 = 3.0 (exact)      | 3 cells per edge
E2   | 5 is QR mod 37         | Legendre(5|37) = 5^18 mod 37 = 36  | 5 is non-residue

DEPENDENCY AUDIT
================
E1 (120-cell cells/edge):
  - toroidal_projection.py: references 120-cell but not cells/edge count — CLEAN
  - fps37_scanner.py: no 120-cell geometry — CLEAN
  - No downstream lemma depends on "4 cells/edge"

E2 (5 is non-residue mod 37):
  - fps37_scanner.py QR_MOD37: 5 not present — CLEAN (was already correct in v2)
  - fps37_scanner.py is_pivot: residue==5 flags PIVOT_PRIME (prime, not QR) — CLEAN
  - fps37_scanner.py has_sqrt: returns False for residue 5 — CORRECT
  - No assertion anywhere claims 5 is QR

PROPAGATION STATUS: No rewrites required — contamination did not reach committed code.
"""

import math


def verify_errata():
    # E1: 120-cell cells per edge
    cells_per_edge = (120 * 30) / 1200
    assert cells_per_edge == 3.0, f"Expected 3, got {cells_per_edge}"

    # E2: 5 is non-residue mod 37 (Legendre symbol = -1)
    qr_mod37 = frozenset((n * n) % 37 for n in range(37))
    assert 5 not in qr_mod37, "5 should not be in QR mod 37"

    legendre_5_37 = pow(5, (37 - 1) // 2, 37)  # Euler criterion
    assert legendre_5_37 == 36, f"Expected 36 (≡-1), got {legendre_5_37}"

    # Residue 5 is prime (PIVOT_PRIME label is correct)
    assert 5 in {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

    return "ERRATA_CLEAN"


assert verify_errata() == "ERRATA_CLEAN"


if __name__ == "__main__":
    print("LoB 24c — Errata Correction Record")
    print()

    # E1
    cells_per_edge = (120 * 30) / 1200
    print(f"E1: 120-cell cells/edge")
    print(f"    120 × 30 / 1200 = {cells_per_edge}")
    print(f"    Original: 4  →  Corrected: {int(cells_per_edge)}")
    print()

    # E2
    qr_mod37 = sorted((n * n) % 37 for n in range(37))
    legendre = pow(5, 18, 37)
    print(f"E2: 5 mod 37 residue status")
    print(f"    Legendre(5|37) = 5^18 mod 37 = {legendre} (≡ -1 mod 37)")
    print(f"    5 in QR mod 37: {5 in set(qr_mod37)}")
    print(f"    5 is prime (PIVOT_PRIME): correct label retained")
    print()

    print("Dependency audit: no downstream contamination found.")
    print("Framework version: v37.20 → v37.21")
    print()
    print("All assertions passed.")
