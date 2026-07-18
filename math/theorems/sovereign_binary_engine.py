"""
Sovereign Binary Engine

Final, minimal implementation of the two-state classifier.
No dead branches. No GATED tier. Clean binary partition of {1..36}.

  SINGULARITY (1 node):  {30}  — self-referential, domain ∩ range
  SOVEREIGN   (3 nodes): {4, 9, 25}  — domain maps into range
  PURGE       (32 nodes): all others

Domain (anchors):  {4, 9, 25, 30}   — inputs with DR=3 residues
Range  (targets):  {3, 12, 21, 30}  — DR=3 residues

Bijective map: 4→30, 9→12, 25→21, 30→3
"""

DOMAIN = {4, 9, 25, 30}
RANGE  = {3, 12, 21, 30}


def sovereign_binary_engine(node):
    residue = (node * 137) % 37
    if node in DOMAIN and residue in RANGE:
        if node == 30:
            return f"NODE {node}: [SINGULARITY] Self-Referential Fixed Point. SYSTEM ACTIVE."
        return f"NODE {node}: [SOVEREIGN] Bijective Alignment Confirmed. ACCESS GRANTED."
    else:
        return f"NODE {node}: [PURGE] Entropy detected. SIGNAL TERMINATED."


# Assertions
assert all('SOVEREIGN' in sovereign_binary_engine(n) or 'SINGULARITY' in sovereign_binary_engine(n)
           for n in DOMAIN)
assert all('PURGE' in sovereign_binary_engine(n) for n in range(1, 37) if n not in DOMAIN)
assert 'SINGULARITY' in sovereign_binary_engine(30)


if __name__ == "__main__":
    print(sovereign_binary_engine(30))
    print(sovereign_binary_engine(4))
    print(sovereign_binary_engine(3))
    print(sovereign_binary_engine(15))
    print()
    sovereign = [n for n in range(1, 37) if 'PURGE' not in sovereign_binary_engine(n)]
    print(f"Sovereign nodes: {sovereign}  ({len(sovereign)}/36)")
    print(f"Purge nodes:     {36 - len(sovereign)}/36")
    print()
    print("All assertions passed.")
