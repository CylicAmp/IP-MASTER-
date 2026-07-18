import pytest
from cylicamp.core import digital_root, build_full_lattice, generate_all_lattices


def test_digital_root_single_digit():
    assert digital_root(5) == 5


def test_digital_root_two_digits():
    assert digital_root(19) == 1  # 1+9=10 -> 1+0=1


def test_digital_root_zero():
    assert digital_root(0) == 0


def test_build_lattice_all_zeros():
    lattice, center = build_full_lattice(0, 0, 0, 0)
    assert center == 0
    assert all(v == 0 for row in lattice for v in row)


def test_build_lattice_all_twos():
    lattice, center = build_full_lattice(2, 2, 2, 2)
    assert center == 8
    assert all(v == 4 for row in lattice for v in row)


def test_generate_all_lattices_count():
    groups = generate_all_lattices((0, 1, 2))
    total = sum(len(v) for v in groups.values())
    assert total == 81  # 3^4


def test_generate_all_lattices_dr4_peak():
    groups = generate_all_lattices((0, 1, 2))
    assert len(groups[4]) == 19
