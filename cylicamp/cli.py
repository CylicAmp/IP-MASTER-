"""
CylicAmp - Command line interface.
Run with: python -m cylicamp.cli
"""
from cylicamp.core import generate_all_lattices
from cylicamp.pipeline import run_pipeline


def main():
    print("=" * 50)
    print("  Welcome to CylicAmp")
    print("=" * 50)
    print()
    print("Running lattice analysis...")
    print()

    groups = generate_all_lattices()
    for dr in sorted(groups.keys()):
        print(f"  Digital Root {dr}: {len(groups[dr])} lattices")

    print()
    print("Running energy pipeline...")
    print()
    run_pipeline()
    print()
    print("Done.")


if __name__ == "__main__":
    main()
