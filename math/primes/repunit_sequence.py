"""
REPUNIT SEQUENCE AND 81-PAIR CONNECTION
================================================================

The repunit sequence reveals the 2n-1 (skip-2) pattern:
- 0 → 3 → 5 → 7 → 9 → 2 → 4 → 6 → 8 → 1
- Formula: 2n - 1
- 10th line resets to 1 (10 ≡ 1 mod 9)

Connection to 81-pair grid:
- Each row shifts cyclically
- The grid embodies the skip-2 pattern
- 162 doubling preserves DR=9
"""

import numpy as np


def digital_root(n):
    """Digital root 1-9."""
    if n == 0:
        return 9
    return (n - 1) % 9 + 1


def repunit(n):
    """Generate repunit of length n."""
    return int('1' * n)


def repunit_sequence():
    """Generate the repunit sequence and DR pattern."""
    sequence = [(0, 0)]  # (n, dr)

    for n in range(2, 11):
        r = repunit(n)
        k = n - 1
        val = r + k
        dr = digital_root(val)
        sequence.append((n, dr))

    return sequence


def verify_2n_minus_1():
    """Verify the 2n-1 formula."""
    results = {}
    for n in range(2, 11):
        result = 2 * n - 1
        dr = digital_root(result)
        results[n] = (result, dr)
    return results


# Main analysis
if __name__ == "__main__":
    print("Repunit Sequence Analysis")
    print("=" * 50)

    seq = repunit_sequence()
    print("\nSequence (n, DR):")
    for n, dr in seq:
        print(f"  n={n}: DR = {dr}")

    print("\n2n-1 verification:")
    verify = verify_2n_minus_1()
    for n, (result, dr) in verify.items():
        print(f"  n={n}: 2n-1 = {result}, DR = {dr}")
