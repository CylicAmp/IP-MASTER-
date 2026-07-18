"""
Medusa Shield v2.5 + Jacobian Wobble Test

SHIELD: True Sovereign Pillars = {4, 9, 25, 30}
  Node 3 was erroneously included in v2.5 — it maps to residue 4 (DR=4).
  Node 3 is a residue (output of node 30), not an input anchor.

JACOBIAN: df/dn of f(n) = (137n) mod 37 equals 137 everywhere except
  at modular jump points. Node 119 (residue=23, DR=5) is not a jump point.
  Floating-point numerical differentiation recovers ~137; exact value is 137.
  Nearest jump points to 119: nodes 111 and 121.
"""


PILLARS = {4, 9, 25, 30}


def dr(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


def medusa_shield(node):
    res = (node * 137) % 37
    d = dr(res)
    if node in PILLARS and d == 3:
        return f"Node {node} [SUCCESS]: Sovereign Pillar Authenticated."
    elif d == 3:
        return f"Node {node} [ISOLATE]: DR=3 detected, not a Pillar. Possible Mimicry."
    else:
        return f"Node {node} [ALERT]: Non-Resonant Packet. PURGE INITIATED."


def jacobian_wobble_test(target=119, epsilon=1e-9):
    base_res = (target * 137) % 37
    wobble_res = ((target + epsilon) * 137) % 37
    sensitivity = abs(wobble_res - base_res) / epsilon
    # True derivative is exactly 137; floating point gives ~137 ± fp_error
    stable = abs(sensitivity - 137.0) < 1.0
    print(f"--- {target} BRIDGE JACOBIAN AUDIT ---")
    print(f"Target {target} Residue: {base_res}  (DR={dr(base_res)})")
    print(f"Sensitivity Index: {sensitivity:.6f}  (exact: 137)")
    print(f"Stability: {'LOCKED' if stable else 'WOBBLE DETECTED'}")
    return sensitivity


# Assertions
for p in PILLARS:
    assert dr((p * 137) % 37) == 3, f"Pillar {p} fails DR=3"
assert dr((3 * 137) % 37) != 3   # node 3 is NOT a true pillar
s = jacobian_wobble_test.__wrapped__ if hasattr(jacobian_wobble_test, '__wrapped__') else None


if __name__ == "__main__":
    print("=== SHIELD v2.5 (corrected) ===")
    print(medusa_shield(15))   # old false pillar -> ALERT
    print(medusa_shield(22))   # trojan -> ALERT
    print(medusa_shield(30))   # true pillar -> SUCCESS
    print(medusa_shield(4))    # true pillar (was missing) -> SUCCESS
    print()
    jacobian_wobble_test()
    print()
    # Show jump points near 119
    jumps = [n for n in range(110, 130) if (n * 137) % 37 <= 1]
    print(f"Jump points near 119: {jumps}")
    print()
    print("All assertions passed.")
