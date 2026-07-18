from cylicamp.core import generate_all_lattices


def print_summary(groups):
    print("=== SUMMARY: Lattices by Center Digital Root ===\n")
    for dr in sorted(groups.keys()):
        print(f"Digital Root {dr}: {len(groups[dr])} lattices")
    print()


def print_groups(groups):
    sep = "=" * 70
    print(sep)
    for dr in sorted(groups.keys()):
        entries = groups[dr]
        print(f"\n=== DIGITAL ROOT {dr} ({len(entries)} lattices) ===\n")
        for i, entry in enumerate(entries, 1):
            d1, d2, d3, d4 = entry["core"]
            center = entry["center"]
            print(f"{i}. Core: {d1}{d2} / {d3}{d4}   |   Center sum: {center} -> DR={dr}")
            for row in entry["lattice"]:
                print("   " + " ".join(f"{v:2d}" for v in row))
            print()
    print(sep)
    print("DONE")
    print(sep)


def run(digit_set=(0, 1, 2)):
    groups = generate_all_lattices(digit_set)
    print_summary(groups)
    print_groups(groups)
