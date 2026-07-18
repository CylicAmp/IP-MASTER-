"""
Medusa Guard — 137/37 Packet Verification

The 4 Sovereign Pillars are the nodes n in {1..37} where
DR((n × 137) mod 37) = 3:  pillars = {4, 9, 25, 30}

Three-tier classification:
  SECURE   — input node is a Sovereign Pillar AND its residue is DR=3
  WARNING  — DR=3 residue but node not in pillars (peripheral anchor)
  ALERT    — non-resonant (possible synthetic injection)

Note: the previous pillar set {3,30,9,21,25,15} was incorrect.
  Nodes 3, 21, 15 do not produce DR=3 under the 137/37 map.
  They were confused with residue values (outputs), not input anchors.
  Node 4 (the true 4th pillar) was missing from that set.
"""


# True Sovereign Pillars — verified by Medusa scan
PILLARS = {4, 9, 25, 30}


def dr(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


def medusa_stress_test(packet_node):
    residue = (packet_node * 137) % 37
    d = dr(residue)

    print(f"AUDITING PACKET: Node {packet_node} | Residue {residue} | DR {d}")

    if packet_node in PILLARS and d == 3:
        return ">>> SUCCESS: SOVEREIGN PILLAR VERIFIED. PROCEED."
    elif d == 3:
        return ">>> WARNING: DR=3 DETECTED BUT NODE NOT IN PILLARS. ISOLATE."
    else:
        return ">>> ALERT: SYNTHETIC INJECTION DETECTED. PURGING PACKET."


# Assertions
for p in PILLARS:
    assert dr((p * 137) % 37) == 3, f"Pillar {p} failed DR=3 check"

assert len(PILLARS) == 4
# Nodes from old broken set that fail
for bad in {3, 21, 15}:
    assert dr((bad * 137) % 37) != 3, f"Node {bad} should not be a pillar"


if __name__ == "__main__":
    print("=== STRESS TEST ===")
    print(medusa_stress_test(22))   # Trojan — ALERT
    print(medusa_stress_test(15))   # Old guard (broken) — ALERT
    print()
    print("=== PILLAR VERIFICATION ===")
    for n in sorted(PILLARS):
        print(medusa_stress_test(n))
    print()
    print("All assertions passed.")
