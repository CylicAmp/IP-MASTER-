import itertools
from collections import defaultdict


def digital_root(n):
    """Reduce a number to its digital root."""
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n


def build_full_lattice(d1, d2, d3, d4):
    """Build a 4x4 lattice from four core digits."""
    main_diag = d1 + d4
    anti_diag = d2 + d3
    row1_sum = d1 + d2
    row2_sum = d3 + d4
    col1_sum = d1 + d3
    col2_sum = d2 + d4

    lattice = [
        [main_diag, row1_sum, row1_sum, anti_diag],
        [col1_sum,  d1,       d2,       col2_sum],
        [col1_sum,  d3,       d4,       col2_sum],
        [anti_diag, row2_sum, row2_sum, main_diag],
    ]

    center_sum = row1_sum + row2_sum
    return lattice, center_sum


def generate_all_lattices(digit_set=(0, 1, 2)):
    """Generate all lattices from the given digit set and group by digital root."""
    groups = defaultdict(list)

    for core in itertools.product(digit_set, repeat=4):
        d1, d2, d3, d4 = core
        lattice, center = build_full_lattice(d1, d2, d3, d4)
        dr = digital_root(center) if center > 0 else 0
        groups[dr].append({
            "core": core,
            "lattice": lattice,
            "center": center,
            "digital_root": dr,
        })

    return groups
