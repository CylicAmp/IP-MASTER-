"""
Fibonacci Digital Root Operator

f(a, b) = DR(a + b)

Instead of standard Fibonacci where each term is a + b,
this operator takes the digital root of a + b at each step.
This collapses the infinite Fibonacci sequence into a finite
repeating cycle of single digits.
"""

from typing import List, Tuple


def digital_root(n: int) -> int:
    """Reduce a number to its digital root."""
    if n == 0:
        return 0
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n


def f(a: int, b: int) -> int:
    """The Fibonacci Digital Root Operator: f(a, b) = DR(a + b)"""
    return digital_root(a + b)


def fib_dr_sequence(seed_a: int, seed_b: int, steps: int = 24) -> List[int]:
    """
    Generate a sequence using the Fibonacci Digital Root Operator.
    Each term is DR(previous + current).
    """
    seq = [digital_root(seed_a), digital_root(seed_b)]
    for _ in range(steps - 2):
        seq.append(f(seq[-2], seq[-1]))
    return seq


def find_cycle(seed_a: int, seed_b: int, max_steps: int = 100) -> Tuple[List[int], int]:
    """
    Finds the repeating cycle in a Fibonacci DR sequence.
    Returns the cycle and the step at which it begins.
    """
    seq = fib_dr_sequence(seed_a, seed_b, max_steps)
    # Look for a repeated pair (a, b) which marks the cycle start
    seen = {}
    for i in range(len(seq) - 1):
        pair = (seq[i], seq[i + 1])
        if pair in seen:
            cycle_start = seen[pair]
            return seq[cycle_start:i], cycle_start
        seen[pair] = i
    return seq, 0


def demonstrate() -> None:
    print("\n=== Fibonacci Digital Root Operator ===")
    print("f(a, b) = DR(a + b)\n")

    print("--- Standard seeds (1, 1) ---")
    seq = fib_dr_sequence(1, 1, 24)
    print(f"Sequence: {seq}")
    cycle, start = find_cycle(1, 1)
    print(f"Cycle (length {len(cycle)}, starts at step {start}): {cycle}\n")

    print("--- All single-digit seed pairs ---")
    seen_cycles = {}
    for a in range(1, 10):
        for b in range(1, 10):
            cycle, _ = find_cycle(a, b)
            key = tuple(cycle)
            if key not in seen_cycles:
                seen_cycles[key] = (a, b)

    print(f"Unique cycles found: {len(seen_cycles)}\n")
    for i, (cycle, (a, b)) in enumerate(seen_cycles.items(), 1):
        print(f"  {i}. Seeds ({a},{b}) → cycle length {len(cycle)}: {list(cycle)}")

    print()
    print("--- Trinity seeds (3, 6) ---")
    seq = fib_dr_sequence(3, 6, 24)
    print(f"Sequence: {seq}")
    cycle, start = find_cycle(3, 6)
    print(f"Cycle: {cycle}\n")


if __name__ == "__main__":
    demonstrate()
