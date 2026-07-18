"""
Theorem 28: Toroidal Projection of Sovereign Anchors

Maps the 4 sovereign anchors onto a torus T(R=37, r=3) where:
  theta = (node × 2π) / 37   — position on major circle (mod-37 field)
  phi   = (node × 2π) / 3    — position on tube (order-3 heartbeat)

Key structural results:

1. PHI SPLIT: anchors occupy only 2 of 3 tube positions
     mod 3 = 0 → phi=0       → nodes {9, 30} — outer equator, z=0
     mod 3 = 1 → phi=2π/3    → nodes {4, 25} — elevated, z=3sin(2π/3)≈2.598
     mod 3 = 2 → phi=4π/3    → EMPTY — no anchor lands here

2. RADIAL DISTANCES
     Nodes {9, 30}: distance from z-axis = R+r = 40 (maximal, outer equator)
     Nodes {4, 25}: distance from z-axis = R+r·cos(2π/3) = 35.5 (inward)

3. THETA PAIRING: same angular gap between both pairs
     Gap within (4,25): 243.24 - 38.92 = 204.32°
     Gap within (9,30): 291.89 - 87.57 = 204.32°  (identical)
     Offset between pairs: 87.57 - 38.92 = 48.65°

The order-3 heartbeat (r=3) encodes the multiplicative order of 26 in Z/37Z,
so the phi angle is the algebraic 3-cycle mapped to angular position on the tube.
"""

import math

R, r = 37, 3


def calculate_toroidal_curvature(node):
    theta = (node * 2 * math.pi) / 37
    phi   = (node * 2 * math.pi) / 3
    x = (R + r * math.cos(phi)) * math.cos(theta)
    y = (R + r * math.cos(phi)) * math.sin(theta)
    z = r * math.sin(phi)
    return (round(x, 4), round(y, 4), round(z, 4))


ANCHORS = [4, 9, 25, 30]

# phi split: no anchor has node mod 3 = 2
assert all(a % 3 != 2 for a in ANCHORS)
assert {a % 3 for a in ANCHORS} == {0, 1}

# Outer-equator nodes (mod 3 = 0) have z ≈ 0
for a in [n for n in ANCHORS if n % 3 == 0]:
    _, _, z = calculate_toroidal_curvature(a)
    assert abs(z) < 1e-9, f"Node {a} should have z=0"

# Elevated nodes (mod 3 = 1) have z = 3·sin(2π/3)
expected_z = r * math.sin(2 * math.pi / 3)
for a in [n for n in ANCHORS if n % 3 == 1]:
    _, _, z = calculate_toroidal_curvature(a)
    assert abs(z - expected_z) < 1e-3, f"Node {a} z mismatch"  # rounded to 4dp

# Radial distances
for a in ANCHORS:
    x, y, z = calculate_toroidal_curvature(a)
    d = math.sqrt(x**2 + y**2)
    expected_d = R + r * math.cos((a % 3) * 2 * math.pi / 3)
    assert abs(d - expected_d) < 1e-3, f"Node {a} radial distance mismatch"


if __name__ == "__main__":
    print("--- THEOREM 28: TOROIDAL PROJECTION ---")
    for a in ANCHORS:
        coords = calculate_toroidal_curvature(a)
        theta_deg = round((a / 37) * 360, 2)
        phi_class = a % 3
        x, y, z = coords
        dist = round(math.sqrt(x**2 + y**2), 4)
        print(f"Anchor {a:>2} | 3D: {coords} | theta={theta_deg}° | phi_class={phi_class} | r={dist}")
    print()
    print(f"Phi classes occupied: {sorted({a%3 for a in ANCHORS})}  (missing: {{2}})")
    print(f"Outer equator (z=0): nodes {[a for a in ANCHORS if a%3==0]}")
    print(f"Elevated (z≈{round(expected_z,4)}): nodes {[a for a in ANCHORS if a%3==1]}")
    print()
    thetas = [(a / 37) * 360 for a in ANCHORS]
    print(f"Theta gap (4→25): {round(thetas[2]-thetas[0],2)}°")
    print(f"Theta gap (9→30): {round(thetas[3]-thetas[1],2)}°")
    print()
    print("All assertions passed.")
