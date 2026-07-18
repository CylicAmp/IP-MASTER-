"""
Sovereign Fixed Point Theorem

The check_sovereign_logic classification has two provably dead branches:

  1. "ANCHOR -> ENTROPY" — unreachable because anchors are defined as the
     nodes whose residues land in targets. By definition, every anchor maps
     to a target. No anchor can miss.

  2. "EXTERNAL SOURCE -> TARGET (GATED)" — unreachable because the map
     f(n) = (137n) mod 37 = (26n) mod 37 is a BIJECTION on {1..36}.
     (37 is prime, gcd(26,37)=1, so 26 is a unit in Z/37Z.)
     Each target value is hit by exactly one input node — its anchor.
     No external node can reach a target.

Consequence: the three-tier classification collapses to two states:
  - FIXED POINT / SOVEREIGN  (node 30 only)
  - ANCHOR -> TARGET          (nodes 4, 9, 25)
  - ENTROPY / PURGE           (all other nodes)

The GATED branch exists in the code as a guard, but the math guarantees
it is never triggered within the {1..36} domain.

Anchor-Target bijection (unique correspondence):
  4  -> 30
  9  -> 12
  25 -> 21
  30 -> 3   (self-referential sovereign)
"""

ANCHORS = {4, 9, 25, 30}
TARGETS = {3, 12, 21, 30}


def check_sovereign_logic(node):
    res = (node * 137) % 37
    status = ""
    if node in ANCHORS and res in TARGETS:
        status = "FIXED POINT / SOVEREIGN" if node == 30 else "ANCHOR -> TARGET (VALID)"
    elif node in ANCHORS:
        status = "ANCHOR -> ENTROPY (INVALID)"   # dead branch — see proof above
    elif res in TARGETS:
        status = "EXTERNAL SOURCE -> TARGET (GATED)"  # dead branch — bijection proof
    else:
        status = "ENTROPY (PURGE)"
    return f"Input {node} | Residue {res} | Status: {status}"


# Proof: dead branch 1 — every anchor maps to a target
dead1 = [n for n in ANCHORS if (n * 137) % 37 not in TARGETS]
assert dead1 == [], f"Anchor misses target: {dead1}"

# Proof: dead branch 2 — bijection means no external source hits a target
# f is a bijection on {1..36} since gcd(26,37)=1
all_residues = {n: (n * 137) % 37 for n in range(1, 37)}
assert len(set(all_residues.values())) == 36, "Map is not a bijection"
gated = [n for n in range(1, 37) if n not in ANCHORS and all_residues[n] in TARGETS]
assert gated == [], f"Unexpected GATED nodes: {gated}"

# Node 30 is the unique fixed point (anchor AND target)
assert 30 in ANCHORS and 30 in TARGETS
assert sum(1 for n in range(1, 37) if n in ANCHORS and n in TARGETS) == 1


if __name__ == "__main__":
    print("Forensic verification:")
    print(check_sovereign_logic(30))
    print(check_sovereign_logic(3))
    print(check_sovereign_logic(4))
    print()
    print(f"Dead branch 1 (ANCHOR->ENTROPY) reachable: {len(dead1) > 0}")
    print(f"Dead branch 2 (GATED) reachable: {len(gated) > 0}")
    print(f"Bijection confirmed: {len(set(all_residues.values()))} distinct residues")
    print(f"Unique self-referential sovereign: node 30")
    print()
    print("All assertions passed.")
