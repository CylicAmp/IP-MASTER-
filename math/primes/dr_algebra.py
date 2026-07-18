"""
CLOSED ALGEBRA ON DIGITAL ROOT CLASSES
================================================================

A complete group-theoretic analysis of digital roots:
- Group structure (DR, +) isomorphic to Z/9Z
- Subgroup lattice
- Cycle decomposition under doubling
- 81 two-digit number mapping
"""

import numpy as np
from itertools import product


def digital_root(n):
    """Digital root 1-9."""
    if n == 0:
        return 9
    return (n - 1) % 9 + 1


class DRAlgebra:
    """Algebraic structure on digital root classes."""

    def __init__(self):
        self.dr_classes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.addition_table = self._build_addition_table()
        self.doubling_map = {x: digital_root(x * 2) for x in self.dr_classes}

    def _build_addition_table(self):
        """Build the DR-addition Cayley table."""
        table = {}
        for a in self.dr_classes:
            for b in self.dr_classes:
                table[(a, b)] = digital_root(a + b)
        return table

    def add(self, a, b):
        """DR-addition: a + b (mod 9)."""
        return self.addition_table[(a, b)]

    def double(self, x):
        """Doubling map: x → DR(2x)."""
        return self.doubling_map[x]

    def find_cycles(self):
        """Find cycles under doubling."""
        visited = set()
        cycles = []

        for start in self.dr_classes:
            if start in visited:
                continue

            path = []
            current = start
            while current not in visited:
                visited.add(current)
                path.append(current)
                current = self.double(current)

                if current == start:
                    cycles.append(path)
                    break

        return cycles

    def generate_subgroup(self, g):
        """Generate cyclic subgroup <g>."""
        subgroup = {9}  # Identity
        current = g
        while current not in subgroup:
            subgroup.add(current)
            current = self.add(current, g)
        return sorted(subgroup)


# Main analysis
if __name__ == "__main__":
    algebra = DRAlgebra()

    print("DR-Algebra Structure")
    print("=" * 50)

    # Addition table
    print("\nAddition Table:")
    print("  " + " ".join(f"{i:>2}" for i in algebra.dr_classes))
    for a in algebra.dr_classes:
        row = [algebra.add(a, b) for b in algebra.dr_classes]
        print(f"{a:>2}|" + " ".join(f"{r:>2}" for r in row))

    # Cycles
    print("\nDoubling Cycles:")
    cycles = algebra.find_cycles()
    for cycle in cycles:
        print(f"  {' → '.join(map(str, cycle))} → {cycle[0]} (length {len(cycle)})")

    # Generators
    print("\nGenerators:")
    generators = [g for g in algebra.dr_classes
                  if len(algebra.generate_subgroup(g)) == 9]
    print(f"  {generators}")
