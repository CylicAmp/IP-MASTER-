"""
Symposium on Numerical Methods Adapted to Topology and Geometry

This symposium gathers researchers investigating or being interested in
numerical methods adapted to topology or geometry of the problems, and
stimulates discussions and exchange of ideas among them in order to share
perspectives, knowledge and techniques for future development.
"""

from typing import List, Dict


RESEARCH_AREAS = [
    "Numerical methods adapted to topology",
    "Numerical methods adapted to geometry",
    "Topological data analysis",
    "Geometric discretization",
    "Structure-preserving algorithms",
    "Finite element methods on manifolds",
    "Computational differential geometry",
]

SYMPOSIUM_GOALS = [
    "Gather researchers across numerical and geometric disciplines",
    "Stimulate discussion and exchange of ideas",
    "Share perspectives, knowledge, and techniques",
    "Identify directions for future development",
]


class SymposiumFramework:
    """
    Framework for organizing and evaluating research contributions
    at the intersection of numerical methods, topology, and geometry.
    """

    def __init__(self):
        self.contributions: List[Dict] = []

    def add_contribution(
        self,
        researcher: str,
        topic: str,
        method: str,
        domain: str,
    ) -> None:
        """
        Register a research contribution.

        researcher: name or ID of the researcher
        topic: the specific problem being addressed
        method: the numerical method being used or proposed
        domain: topology or geometry
        """
        self.contributions.append({
            "researcher": researcher,
            "topic": topic,
            "method": method,
            "domain": domain.lower(),
        })

    def get_by_domain(self, domain: str) -> List[Dict]:
        """Returns all contributions in a given domain (topology or geometry)."""
        return [c for c in self.contributions if c["domain"] == domain.lower()]

    def summary(self) -> None:
        """Prints a full summary of all contributions."""
        print("\n=== Symposium on Numerical Methods: Topology & Geometry ===\n")
        print(f"Total contributions: {len(self.contributions)}")

        topology = self.get_by_domain("topology")
        geometry = self.get_by_domain("geometry")

        print(f"  Topology:  {len(topology)} contributions")
        print(f"  Geometry:  {len(geometry)} contributions")
        print()

        for i, c in enumerate(self.contributions, 1):
            print(f"  {i}. [{c['domain'].upper()}] {c['researcher']}")
            print(f"     Topic:  {c['topic']}")
            print(f"     Method: {c['method']}")
            print()

    def research_areas(self) -> None:
        """Lists all active research areas."""
        print("\n=== Active Research Areas ===\n")
        for area in RESEARCH_AREAS:
            print(f"  - {area}")
        print()

    def goals(self) -> None:
        """Lists symposium goals."""
        print("\n=== Symposium Goals ===\n")
        for goal in SYMPOSIUM_GOALS:
            print(f"  - {goal}")
        print()


if __name__ == "__main__":
    s = SymposiumFramework()

    s.add_contribution(
        researcher="CylicAmp-001",
        topic="Digital root lattices as topological invariants",
        method="Lattice-based digital root analysis",
        domain="topology",
    )
    s.add_contribution(
        researcher="CylicAmp-002",
        topic="PHI/PSI spiral trajectories on curved surfaces",
        method="Golden ratio geometric discretization",
        domain="geometry",
    )

    s.goals()
    s.research_areas()
    s.summary()
