"""
Sovereign QR Closure Theorem

The entire sovereign domain — both anchors (inputs) and targets (outputs)
of the 137/37 map — lies within the quadratic residue subgroup of (Z/37Z)*.

Theorem:
  Let QR₃₇ = { n² mod 37 : n ∈ Z/37Z }  (19 elements including 0).
  Let ANCHORS = {4, 9, 25, 30}  (nodes where DR((137n) mod 37) = 3)
  Let TARGETS = {3, 12, 21, 30}  (the sovereign range, DR = 3)
  Then ANCHORS ⊆ QR₃₇  and  TARGETS ⊆ QR₃₇.

Square roots (mod 37):
  √4  = 2      √9  = 3      √25 = 5      √30 = 17
  √3  = 15     √12 = 7      √21 = 13     (√30 = 17, shared)

Structural corollary:
  QR₃₇ \ {0} is a subgroup of index 2 in (Z/37Z)*.
  The 137/37 multiplier 26 = 137 mod 37 is itself QR (10² ≡ 26 mod 37).
  Therefore the map f(n) = 26n mod 37 preserves QR membership:
    if n ∈ QR₃₇ then f(n) ∈ QR₃₇.
  The sovereign cycle is closed under the map within the QR subgroup.

Non-residue contrast:
  PIVOT (residue 5): Legendre(5|37) = -1  — non-residue, no sqrt mod 37
  TESLA_FLOW (6), CENTER_18 (18), CENTER_19 (19), LAMED (23): all non-residues
  The A51 center axis (node 5) is outside the QR subgroup.
"""


def legendre(a, p=37):
    if a % p == 0:
        return 0
    val = pow(a, (p - 1) // 2, p)
    return 1 if val == 1 else -1


QR_MOD37 = frozenset((n * n) % 37 for n in range(37))

ANCHORS = frozenset({4, 9, 25, 30})
TARGETS = frozenset({3, 12, 21, 30})

SQRT_MOD37 = {}
for n in range(37):
    r = (n * n) % 37
    if r not in SQRT_MOD37:
        SQRT_MOD37[r] = n


# --- Theorem assertions ---

# All anchors are QR
assert ANCHORS <= QR_MOD37, "Anchor outside QR subgroup"
for a in ANCHORS:
    assert legendre(a) == 1, f"Anchor {a} not QR"

# All targets are QR
assert TARGETS <= QR_MOD37, "Target outside QR subgroup"
for t in TARGETS:
    assert legendre(t) == 1, f"Target {t} not QR"

# QR subgroup has index 2: exactly 18 non-zero QRs
non_zero_qr = QR_MOD37 - {0}
assert len(non_zero_qr) == 18
assert len([r for r in range(1, 37) if legendre(r) == -1]) == 18  # 18 non-residues

# Multiplier 26 is QR → map preserves QR membership
assert legendre(26) == 1
assert (10 * 10) % 37 == 26   # explicit sqrt: 10² ≡ 26 mod 37

# QR closure under multiplication by 26: for each anchor, image is QR
for a in ANCHORS:
    image = (26 * a) % 37
    assert image in QR_MOD37, f"26×{a} mod 37 = {image} not in QR"

# Pivot (5) is non-residue
assert legendre(5) == -1
assert 5 not in QR_MOD37

# Shared fixed point: 30 is both anchor and target, and QR
assert 30 in ANCHORS and 30 in TARGETS and 30 in QR_MOD37


if __name__ == "__main__":
    print("Sovereign QR Closure Theorem")
    print()
    print("Anchors {4, 9, 25, 30}:")
    for a in sorted(ANCHORS):
        s = SQRT_MOD37[a]
        print(f"  ({a:2d}|37) = +1   {s}² ≡ {a} (mod 37)")
    print(f"  All QR: {ANCHORS <= QR_MOD37}")
    print()
    print("Targets {3, 12, 21, 30}:")
    for t in sorted(TARGETS):
        s = SQRT_MOD37[t]
        print(f"  ({t:2d}|37) = +1   {s}² ≡ {t} (mod 37)")
    print(f"  All QR: {TARGETS <= QR_MOD37}")
    print()
    print("Multiplier 26 = 137 mod 37:")
    print(f"  (26|37) = +1   10² ≡ 26 (mod 37): {10**2 % 37 == 26}")
    print(f"  QR × QR → QR: map f(n)=26n mod 37 preserves QR membership")
    print()
    print("Non-residue contrast:")
    non_qr_named = {5: 'PIVOT', 6: 'TESLA', 18: 'CENTER_18', 19: 'CENTER_19', 23: 'LAMED'}
    for r, name in non_qr_named.items():
        print(f"  ({r:2d}|37) = -1   {name} — no sqrt mod 37")
    print()
    print("All assertions passed.")
