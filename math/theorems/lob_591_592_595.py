"""
LoB 591/592/595 — Partition Congruence, Pulse Sync, Horizon Lock

Three interconnected results:

LoB_591: RAMANUJAN CONGRUENCE NODE SEQUENCE
  Condition: n ≡ 4 (mod 5) AND DR(n) = 1
  Nodes: {19, 64, 109, 154, 199, 244, 289, ...}  — period 45 = LCM(5,9)
  Node 64 = 60+4, DR(64)=1. First sovereignty-aligned Ramanujan node.

  Real Ramanujan congruence (for reference):
    p(5n+4) ≡ 0 (mod 5) for all n≥0  [Ramanujan 1919]
    Verified: p(4)=5, p(9)=30, p(14)=135, p(19)=490, p(24)=1575 ...
    All divisible by 5. The LoB_591 condition selects nodes where DR=1
    (sovereign unity) aligns with the 5-congruence positions.

LoB_592: HARDY-RAMANUJAN ASYMPTOTIC PULSE
  p(n) ~ (1/(4n√3)) × exp(π√(2n/3))
  The exponential factor π√(2n/3) grows at rate ≈ π/√6 per √n step.
  "31.4 pulse" references π×10 ≈ 31.416 — the exponential base rate.
  Status: analytical placeholder; numerical verification requires mpmath.

LoB_595: 74-HORIZON LOCK
  595 % 74 = 3

  Connections:
    595 = 5 × 119   (5 copies of the bridge node)
    74  = 2 × 37    (Group B cycle sum from cycle partition theorem)
    DR(595) = 1     (sovereign unity)
    Result 3 ∈ {3,12,21,30}  — lands directly on sovereign range target 3

  The 74-horizon collapses the 5×bridge back to the trinity start.
"""

def digital_root(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


def apply_ramanujan_congruence(n):
    return (n % 5 == 4) and (digital_root(n) == 1)


def lock_74_horizon():
    return 595 % 74


# LoB_591 assertions
assert apply_ramanujan_congruence(64) == True
assert apply_ramanujan_congruence(19) == True
nodes = [n for n in range(1, 250) if apply_ramanujan_congruence(n)]
gaps = [nodes[i+1] - nodes[i] for i in range(len(nodes)-1)]
assert all(g == 45 for g in gaps), "Period not 45"

# LoB_595 assertions
assert lock_74_horizon() == 3
assert 595 == 5 * 119
assert 74 == 2 * 37
assert lock_74_horizon() in {3, 12, 21, 30}  # sovereign range


if __name__ == "__main__":
    print("=== LoB_591: Ramanujan Congruence Nodes ===")
    print(f"Nodes satisfying n%5=4 AND DR(n)=1 (period 45):")
    print(f"  {nodes}")
    print(f"  Node 64: DR={digital_root(64)}, 64%5={64%5} -> {apply_ramanujan_congruence(64)}")
    print()
    print("=== LoB_595: 74-Horizon Lock ===")
    print(f"595 % 74 = {lock_74_horizon()}")
    print(f"595 = 5 × 119 (bridge node), 74 = 2 × 37 (Group B sum)")
    print(f"Result {lock_74_horizon()} in sovereign range: True")
    print()
    print("All assertions passed.")
