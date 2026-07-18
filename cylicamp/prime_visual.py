"""
Prime Visual Generator — DR=7 Prime Simulation.

Scans a range of numbers, finds all primes whose digital root is 7,
and displays them visually as a grid map.

DR=7 primes: 7, 43, 61, 97, 151, 223, ...
"""


def digital_root(n: int) -> int:
    if n == 0:
        return 0
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_dr7_prime(n: int) -> bool:
    return is_prime(n) and digital_root(n) == 7


def find_dr7_primes(limit: int = 500) -> list:
    """Find all DR=7 primes up to limit."""
    return [n for n in range(2, limit + 1) if is_dr7_prime(n)]


def grid_display(limit: int = 500, width: int = 10) -> None:
    """
    Display numbers 1..limit as a grid.
    DR=7 primes marked with [P], other primes with  p , others with  .
    """
    dr7_primes = set(find_dr7_primes(limit))
    primes = set(n for n in range(2, limit + 1) if is_prime(n))

    print(f"\n=== DR=7 Prime Grid (1 to {limit}) ===")
    print(f"[P] = DR=7 prime   p = other prime   . = composite\n")

    for row_start in range(1, limit + 1, width):
        row = []
        for n in range(row_start, min(row_start + width, limit + 1)):
            if n in dr7_primes:
                row.append(f"[{n:3d}]")
            elif n in primes:
                row.append(f" {n:3d} ")
            else:
                row.append(f"  .  ")
        print(" ".join(row))


def run_simulation(limit: int = 200) -> None:
    dr7 = find_dr7_primes(limit)

    print("=" * 56)
    print("  DR=7 PRIME SIMULATION")
    print("=" * 56)
    print(f"\nScanning 1 to {limit}...")
    print(f"DR=7 primes found: {len(dr7)}")
    print(f"\nList: {dr7}")

    print(f"\nSpacing between consecutive DR=7 primes:")
    for i in range(1, min(10, len(dr7))):
        gap = dr7[i] - dr7[i-1]
        print(f"  {dr7[i-1]} → {dr7[i]} : gap = {gap}  (DR of gap = {digital_root(gap)})")

    print()
    grid_display(limit=100, width=10)


if __name__ == "__main__":
    run_simulation(200)
