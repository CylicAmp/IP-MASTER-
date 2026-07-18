"""
LoB 25 — Legendre Symbol Applications in the 37-Field

Four verified results:

LoB_25a: GOLDEN RATIO IRREDUCIBILITY
  φ = (1+√5)/2 satisfies x²-x-1=0. Discriminant Δ=5.
  (5|37) = -1: 5 is non-QR mod 37.
  Therefore x²-x-1 is IRREDUCIBLE over F_37.
  φ ∉ F_37. Requires quadratic extension F_37(√5), which has 37²=1369 elements.
  Verified: no x ∈ {0..36} satisfies x²-x-1 ≡ 0 (mod 37).

LoB_25b: TIER NATIVE/EXTENDED CLASSIFICATION
  Tier n has √Δ = 40n. QR status of (40n mod 37) classifies each tier:
  NATIVE  (QR)    — tier's √Δ has a square root in F_37
  EXTENDED (non-QR) — tier requires field extension F_37(√(40n mod 37))
  Pattern (n=1..12): NATIVE, EXT, NATIVE, NATIVE, EXT, EXT,
                     NATIVE, EXT, NATIVE, NATIVE, NATIVE, NATIVE
  Tier 3 (√Δ=120≡9, QR, sqrt=±3) is NATIVE — 120-cell bridge needs no extension.

LoB_25c: MODAL CROSSING ENGINE EMBEDDABILITY
  Evolve   f(n) = 3n + 1:  mult 3 is QR (sqrt=±15), shift 1 is QR → NATIVE
  Promote  g(n) = 2n + 19: mult 2 is non-QR, shift 19 is non-QR   → EXTENDED
  Evolution stays inside F_37. Promotion crosses into the extension field.

LoB_25d: QUADRATIC RECIPROCITY SCAN OF 37
  37 ≡ 1 (mod 4), so (p|37) = (37|p) for all odd primes p.
  37 is QR mod: {3, 7, 11} (among small primes tested)
  37 is non-QR mod: {5, 13, 17, 19, 23, 29, 31}
  In particular: (37|5) = -1, consistent with (5|37) = -1 by reciprocity.
"""


def legendre(a, p=37):
    a = a % p
    if a == 0:
        return 0
    val = pow(a, (p - 1) // 2, p)
    return 1 if val == 1 else -1


QR_MOD37 = frozenset((n * n) % 37 for n in range(37))


# LoB_25a: phi irreducibility
phi_roots = [x for x in range(37) if (x * x - x - 1) % 37 == 0]
assert phi_roots == [], f"phi unexpectedly has roots in F_37: {phi_roots}"
assert legendre(5) == -1   # discriminant is non-QR
assert 5 not in QR_MOD37

# LoB_25b: tier classification
TIER_STATUS = {}
for n in range(1, 13):
    val = (40 * n) % 37
    TIER_STATUS[n] = 'NATIVE' if legendre(val) == 1 else 'EXTENDED'

assert TIER_STATUS[1]  == 'NATIVE'    # 40 ≡ 3 (QR)
assert TIER_STATUS[2]  == 'EXTENDED'  # 80 ≡ 6 (non-QR)
assert TIER_STATUS[3]  == 'NATIVE'    # 120 ≡ 9 (QR, sqrt=±3, Trinity root)
assert TIER_STATUS[4]  == 'NATIVE'    # 160 ≡ 12 (QR)
assert TIER_STATUS[5]  == 'EXTENDED'  # 200 ≡ 15 (non-QR)
assert TIER_STATUS[6]  == 'EXTENDED'  # 240 ≡ 18 (non-QR)
assert TIER_STATUS[7]  == 'NATIVE'    # 280 ≡ 21 (QR)
assert TIER_STATUS[8]  == 'EXTENDED'  # 320 ≡ 24 (non-QR)
assert TIER_STATUS[9]  == 'NATIVE'    # 360 ≡ 27 (QR)
assert TIER_STATUS[10] == 'NATIVE'    # 400 ≡ 30 (QR, sovereign anchor)
assert TIER_STATUS[11] == 'NATIVE'    # 440 ≡ 33 (QR)
assert TIER_STATUS[12] == 'NATIVE'    # 480 ≡ 36 (QR, inverse unity)

# Tier 3 sqrt: 3² ≡ 9 (Trinity root)
assert (3 * 3) % 37 == 9

# LoB_25c: modal crossing embeddability
assert legendre(3) == 1    # f multiplier QR
assert legendre(1) == 1    # f shift QR  → f NATIVE
assert legendre(2) == -1   # g multiplier non-QR
assert legendre(19) == -1  # g shift non-QR → g EXTENDED

# LoB_25d: quadratic reciprocity — (37|p) for small primes
# 37 ≡ 1 mod 4 so (p|37) = (37|p)
qr_of_37 = [p for p in [3,5,7,11,13,17,19,23,29,31] if legendre(37 % p, p) == 1]
non_qr_of_37 = [p for p in [3,5,7,11,13,17,19,23,29,31] if legendre(37 % p, p) == -1]
assert set(qr_of_37) == {3, 7, 11}
assert 5 in non_qr_of_37   # consistent with (5|37)=-1

# Reciprocity cross-check: (5|37) should equal (37|5) since 37≡1 mod 4
assert legendre(5, 37) == legendre(37 % 5, 5)


if __name__ == "__main__":
    print("LoB 25 — Legendre Symbol Applications in the 37-Field")
    print()

    print("LoB_25a: Golden Ratio Irreducibility")
    print(f"  x²-x-1 roots in F_37: {phi_roots}  (none — irreducible)")
    print(f"  (5|37) = {legendre(5)}  →  φ ∉ F_37, requires F_37(√5), |F| = {37**2}")
    print()

    print("LoB_25b: Tier Native/Extended Classification  (√Δ = 40n)")
    for n in range(1, 13):
        val = (40 * n) % 37
        s = TIER_STATUS[n]
        note = " ← 120-cell (Trinity root ±3)" if n == 3 else ""
        print(f"  Tier {n:2d}: 40×{n}={40*n} ≡ {val:2d} (mod 37)  {s}{note}")
    print()

    print("LoB_25c: Modal Crossing Engine Embeddability")
    print(f"  f(n)=3n+1:   (3|37)={legendre(3):+d}  (1|37)={legendre(1):+d}  → NATIVE")
    print(f"  g(n)=2n+19:  (2|37)={legendre(2):+d}  (19|37)={legendre(19):+d}  → EXTENDED")
    print()

    print("LoB_25d: Quadratic Reciprocity — 37 among small primes")
    print(f"  37 is QR mod:     {sorted(qr_of_37)}")
    print(f"  37 is non-QR mod: {sorted(non_qr_of_37)}")
    print(f"  Reciprocity check (5|37)={(legendre(5,37)):+d} = (37|5)={(legendre(37%5,5)):+d}  ✓")
    print()
    print("All assertions passed.")
