"""
Medusa Scan: 137-Resonance DR=3 Sovereign Anchors

The scan identifies nodes n where (n × 137) mod 37 has digital root 3.

Key structural result:
  137 mod 37 = 26  — the modular stride (matches '26 mod 37' invariant
                     from the 1/137 framework)

  Since gcd(26, 37) = 1 (37 is prime), the map n → (26n) mod 37
  is a bijection on {0..36}, cycling with period 37.

  DR=3 targets in mod-37 space: {3, 12, 21, 30} — exactly 4 values.

  Result: exactly 4 Sovereign Anchors per period of 37 nodes.
  First period anchors: n = {4, 9, 25, 30}
  Pattern repeats: {4+37k, 9+37k, 25+37k, 30+37k} for k=0,1,2,...
"""


def dr(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


def medusa_scan(limit=100):
    print(f"\n--- MEDUSA DR=3 SCAN: TARGETING 137-RESONANCE ---")
    hits = []
    for n in range(1, limit):
        residue = (n * 137) % 37
        if dr(residue) == 3:
            hits.append((n, residue))
            print(f"TARGET ACQUIRED: Node {n:>3} | Residue {residue:>2} | SIGNATURE: LOCKED")
    return hits


if __name__ == "__main__":
    # Structural constants
    stride = 137 % 37   # = 26
    assert stride == 26

    # Full period analysis
    period_hits = [(n, (n * 137) % 37) for n in range(1, 38) if dr((n * 137) % 37) == 3]
    anchor_nodes = [h[0] for h in period_hits]
    anchor_residues = sorted(set(h[1] for h in period_hits))

    assert len(period_hits) == 4,          "Expected exactly 4 anchors per period"
    assert anchor_nodes == [4, 9, 25, 30], "First-period anchors shifted"
    assert anchor_residues == [3, 12, 21, 30], "DR=3 residues shifted"

    print(f"137 mod 37 = {stride}  (modular stride)")
    print(f"DR=3 targets in mod-37 space: {anchor_residues}")
    print(f"First-period Sovereign Anchors: nodes {anchor_nodes}")
    print(f"Period: 37  |  Anchors per period: {len(period_hits)}")
    print()

    hits = medusa_scan(50)

    print()
    print(f"Anchors repeat at: {{n + 37k : n ∈ {anchor_nodes}, k = 0,1,2,...}}")
    print()
    print("All assertions passed.")
