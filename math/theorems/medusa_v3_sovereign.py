"""
Medusa v3 Sovereign — Anchor/Target Architecture

Correctly separates two distinct sets:

  SOURCE ANCHORS (input nodes):  {4, 9, 25, 30}
    Nodes n where DR((n×137) mod 37) = 3

  RESIDUE TARGETS (output values): {3, 12, 21, 30}
    The actual DR=3 residues produced by those anchors

The map: anchor → target
  4  → 30
  9  → 12
  25 → 21
  30 → 3

Note: node 30 is both anchor AND target (self-referential sovereign).
      Nodes 3, 12, 21 are targets only — using them as inputs produces PURGE.
      No target (except 30) maps back into the framework when used as input.

Three-tier classification:
  LOCKED — node is an anchor AND its residue is a target (4 nodes)
  GATED  — residue is a valid target but node is not an anchor (peripheral)
  PURGE  — non-framework entropy
"""

ANCHORS = {4, 9, 25, 30}
TARGETS = {3, 12, 21, 30}


def dr(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


def medusa_v3_sovereign(node):
    res = (node * 137) % 37
    if node in ANCHORS and res in TARGETS:
        return f"Node {node} -> Res {res} [LOCKED]: Full Anchor-Target Alignment."
    elif res in TARGETS:
        return f"Node {node} -> Res {res} [GATED]: Valid Target, but External Source."
    else:
        return f"Node {node} -> Res {res} [PURGE]: Non-Framework Entropy."


# All 4 anchors must LOCK
for a in ANCHORS:
    res = (a * 137) % 37
    assert res in TARGETS, f"Anchor {a} -> res {res} not in targets"

# Anchor-target map
ANCHOR_MAP = {a: (a * 137) % 37 for a in ANCHORS}
assert ANCHOR_MAP == {4: 30, 9: 12, 25: 21, 30: 3}

# Targets used as inputs (except 30) must PURGE
for t in TARGETS - {30}:
    res = (t * 137) % 37
    assert res not in TARGETS, f"Target {t} unexpectedly maps to another target"

# Node 30 is self-referential sovereign (anchor AND target)
assert 30 in ANCHORS and 30 in TARGETS


if __name__ == "__main__":
    print("Anchor → Target map:")
    for a, t in sorted(ANCHOR_MAP.items()):
        tag = " (self-referential)" if a == t or (a == 30) else ""
        print(f"  {a:>2} → {t:>2}{tag}")
    print()
    print("Classification sweep:")
    for node in sorted({4, 9, 25, 30, 3, 12, 21, 15, 22}):
        print(f"  {medusa_v3_sovereign(node)}")
    print()
    print("All assertions passed.")
