"""
The 3-6-9 Trinity Trap

The 3-6-9 trinity is a dynamical trap — once entered, never escaped.
But the reverse is also true: starting outside trinity, you can never
reach pure {3, 6, 9} residency.

The 24-cycle contains all 9 digits but visits 3-6-9 only transiently.

Key insight:
- Numbers whose digital root is in {3, 6, 9} stay in {3, 6, 9} under
  repeated doubling (mod 9).
- Numbers outside {3, 6, 9} cycle through the other 6 digits but
  only pass through 3-6-9 as transient visitors — never settling.
"""

from typing import List, Set


TRINITY = {3, 6, 9}
CYCLE_LENGTH = 24


def digital_root(n: int) -> int:
    """Reduce a number to its digital root."""
    if n == 0:
        return 0
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n


def doubling_sequence(start: int, steps: int = 24) -> List[int]:
    """
    Generate a sequence by repeatedly doubling, taking the digital root each step.
    This reveals the 24-cycle structure of the digital root system.
    """
    seq = []
    n = start
    for _ in range(steps):
        dr = digital_root(n)
        seq.append(dr)
        n *= 2
    return seq


def is_trinity(n: int) -> bool:
    """Returns True if n's digital root is in the 3-6-9 trinity."""
    return digital_root(n) in TRINITY


def classify_residency(start: int, steps: int = 24) -> dict:
    """
    Classifies how a starting number behaves across the 24-cycle.

    Returns:
    - whether it starts in trinity
    - how many steps it spends in trinity
    - whether it ever escapes (if it started in trinity)
    - whether it ever enters (if it started outside)
    """
    seq = doubling_sequence(start, steps)
    in_trinity = [dr in TRINITY for dr in seq]
    starts_in = in_trinity[0]
    trinity_count = sum(in_trinity)

    if starts_in:
        ever_escapes = any(not t for t in in_trinity)
        ever_enters = None
    else:
        ever_escapes = None
        ever_enters = any(t for t in in_trinity)

    return {
        "start": start,
        "digital_root": seq[0],
        "starts_in_trinity": starts_in,
        "trinity_visits": trinity_count,
        "total_steps": steps,
        "ever_escapes_trinity": ever_escapes,
        "ever_enters_trinity": ever_enters,
        "sequence": seq,
    }


def demonstrate_trap(steps: int = 24) -> None:
    """
    Demonstrates the 3-6-9 trinity trap across all 9 digital roots.
    Shows which numbers are trapped inside and which are locked outside.
    """
    print("\n=== The 3-6-9 Trinity Trap ===\n")
    print("TRINITY = {3, 6, 9}\n")

    print("--- Starting INSIDE the trinity (trapped in) ---\n")
    for seed in [3, 6, 9]:
        result = classify_residency(seed, steps)
        print(f"  Start DR={result['digital_root']} | "
              f"Trinity visits: {result['trinity_visits']}/{steps} | "
              f"Ever escapes: {result['ever_escapes_trinity']}")
        print(f"  Sequence: {result['sequence']}\n")

    print("--- Starting OUTSIDE the trinity (locked out) ---\n")
    for seed in [1, 2, 4, 5, 7, 8]:
        result = classify_residency(seed, steps)
        print(f"  Start DR={result['digital_root']} | "
              f"Trinity visits: {result['trinity_visits']}/{steps} | "
              f"Ever enters: {result['ever_enters_trinity']}")
        print(f"  Sequence: {result['sequence']}\n")

    print("--- The 24-cycle contains all 9 digits ---")
    full_cycle = doubling_sequence(1, CYCLE_LENGTH)
    unique = sorted(set(full_cycle))
    print(f"  Starting from 1, digits visited: {unique}")
    trinity_in_cycle = [d for d in full_cycle if d in TRINITY]
    print(f"  Trinity digits in cycle: {trinity_in_cycle} (transient only)\n")


if __name__ == "__main__":
    demonstrate_trap()
