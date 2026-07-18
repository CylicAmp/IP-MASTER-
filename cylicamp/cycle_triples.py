"""
Cycle Triple Digital Root Analysis

Slides a 3-element window across the master cycle array.
For each consecutive triple (a, b, c), computes their sum
and collapses it to a digital root.

The cycle is the master sequence of digital roots observed
across the system. The triple window reveals the next emergent
DR at each position — showing how the sequence generates itself.
"""


def dr(n: int) -> int:
    """Digital root: maps 0 to 0, all others to 1-9."""
    if n == 0:
        return 0
    return 1 + (n - 1) % 9


CYCLE = [2, 4, 7, 4, 6, 8, 9, 5, 4, 9, 9, 4, 4, 8, 7, 1, 7, 6, 5, 9,
         2, 7, 9, 9, 7, 7, 5, 1, 4, 1, 6, 2, 9, 8, 1, 9, 9, 1, 1]


def analyze_triples(cycle: list, count: int = 8) -> list:
    """
    Slide a 3-element window across the cycle.
    Returns list of (a, b, c, sum, dr) tuples.
    """
    results = []
    for i in range(count):
        a, b, c = cycle[i], cycle[i + 1], cycle[i + 2]
        s = a + b + c
        results.append((a, b, c, s, dr(s)))
    return results


def run_analysis() -> None:
    print("=== Cycle Triple Digital Root Analysis ===\n")
    print(f"Cycle length: {len(CYCLE)}")
    print(f"Cycle: {CYCLE}\n")
    print("--- First 8 consecutive triples ---\n")
    for a, b, c, s, d in analyze_triples(CYCLE, 8):
        print(f"  {a}+{b}+{c} = {s} → DR: {d}")


if __name__ == "__main__":
    run_analysis()
