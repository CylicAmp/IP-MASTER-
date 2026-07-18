"""
FPS-37 Scanner — LoB 23 / 23b

37-Field forensic feature vector. Audited 2026-04-26.

Bug fixed: has_sqrt previously used perfect squares {0,1,4,9,16,25,36}.
Correct quadratic residues mod 37 = 19 values:
  {0,1,3,4,7,9,10,11,12,16,21,25,26,27,28,30,33,34,36}
Residue 26 (SCALAR_137) is a QR: 10^2 = 100 ≡ 26 (mod 37). Confirmed True.
"""

import math

# True quadratic residues mod 37 (19 values including 0)
QR_MOD37 = frozenset((n * n) % 37 for n in range(37))

# Perfect squares ≤ 36 (7 values — distinct from QR)
PERFECT_SQUARES = frozenset(n * n for n in range(7))  # {0,1,4,9,16,25,36}

SIGNIFICANCE = {
    0:  "NULL_ELEMENT",
    1:  "UNITY",
    3:  "TRINITY",
    5:  "PIVOT_PRIME",
    6:  "TESLA_FLOW",
    9:  "TRINITY_SQUARED",
    10: "DECADE_ANCHOR",
    18: "CENTER_18",
    19: "CENTER_19",
    23: "LAMED_SEAL",
    25: "INV_3",
    26: "SCALAR_137",
    31: "PRIME_MIRROR",
    33: "DICHORAL_144",
    36: "INVERSE_UNITY",
}

PRIMES_0_36 = frozenset({2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31})
TIER_1 = frozenset({3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36})
PROXIMITY_TARGETS = {'null': 0, 'unity': 1, 'trinity': 3,
                     'pivot': 5, '18': 18, '19': 19, 'inv_unity': 36}


def field_scan_37(value, label="input"):
    integer_part = int(math.floor(value))
    fractional_part = value - integer_part
    residue = integer_part % 37
    is_exact = abs(fractional_part) < 1e-12

    flags = {
        'is_null':        residue == 0,
        'is_unity':       residue == 1,
        'is_trinity':     residue == 3,
        'is_pivot':       residue == 5,
        'is_tesla':       residue == 6,
        'is_trinity_sq':  residue == 9,
        'is_decade':      residue == 10,
        'is_center_18':   residue == 18,
        'is_center_19':   residue == 19,
        'is_lamed':       residue == 23,
        'is_inv_3':       residue == 25,
        'is_scalar_137':  residue == 26,
        'is_prime_mirror': residue == 31,
        'is_dichoral':    residue == 33,
        'is_inv_unity':   residue == 36,
    }

    proximities = {}
    for name, t in PROXIMITY_TARGETS.items():
        d = min(abs(residue - t), 37 - abs(residue - t))
        proximities[f'dist_to_{name}'] = d

    structural = {
        'is_prime':       residue in PRIMES_0_36,
        'is_square':      residue in PERFECT_SQUARES,
        'is_self_inverse': (residue * residue) % 37 == 1,
        'has_sqrt':       residue in QR_MOD37,  # fixed: true QR mod 37, not perfect squares
    }

    tier = {
        'tier_1_compatible': residue in TIER_1,
        'tier_2_compatible': residue not in TIER_1,
    }

    return {
        'input':            value,
        'label':            label,
        'integer_part':     integer_part,
        'fractional_part':  fractional_part,
        'residue':          residue,
        'is_exact':         is_exact,
        'significance':     SIGNIFICANCE.get(residue, "FIELD_ELEMENT"),
        **flags,
        **proximities,
        **structural,
        **tier,
    }


# --- Assertions ---

# QR count
assert len(QR_MOD37) == 19
assert 26 in QR_MOD37          # SCALAR_137 has a square root mod 37
assert 10**2 % 37 == 26        # 10 is the sqrt: 100 ≡ 26 (mod 37)

# is_square != has_sqrt (now distinct)
assert PERFECT_SQUARES != QR_MOD37
assert 12 not in PERFECT_SQUARES and 12 in QR_MOD37  # 12 is QR but not perfect square

# Self-inverse: only 1 and 36
assert [r for r in range(37) if (r*r) % 37 == 1] == [1, 36]

# Tier split
assert len(TIER_1) == 12
assert 37 - len(TIER_1) == 25

# psi(232) ground truth
def _chebyshev_psi(x):
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True
    total = 0.0
    for p in range(2, int(x) + 1):
        if is_prime(p):
            k, pk = 1, p
            while pk <= x:
                total += math.log(p)
                k += 1; pk *= p
    return total

psi_232 = _chebyshev_psi(232)
assert abs(psi_232 - 227.763) < 0.001
assert int(math.floor(psi_232)) % 37 == 5   # Pivot

# Batch scan spot checks
assert field_scan_37(227)['residue'] == 5
assert field_scan_37(232)['residue'] == 10
assert field_scan_37(191)['significance'] == "TESLA_FLOW"
assert field_scan_37(137)['significance'] == "SCALAR_137"
assert field_scan_37(137)['has_sqrt'] == True
assert field_scan_37(142857)['significance'] == "NULL_ELEMENT"


if __name__ == "__main__":
    print("FPS-37 Scanner v2 — LoB 23b")
    print()
    cases = [
        (227.763559, "psi(232)"),
        (232,        "psi_arg"),
        (191,        "seed_191"),
        (137,        "scalar_137"),
        (142857,     "null_element"),
        (120,        "120cell"),
        (144,        "dichoral"),
        (36,         "delta5_defect"),
    ]
    for val, lbl in cases:
        r = field_scan_37(val, lbl)
        sqrt_flag = "QR" if r['has_sqrt'] else "non-QR"
        print(f"  {lbl:20s}  residue={r['residue']:2d}  {r['significance']:16s}  {sqrt_flag}")
    print()
    print(f"QR mod 37 ({len(QR_MOD37)} values): {sorted(QR_MOD37)}")
    print()
    print("All assertions passed.")
