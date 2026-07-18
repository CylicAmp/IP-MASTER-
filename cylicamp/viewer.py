"""
Viewer - lets you read any CylicAmp file from inside the app.
"""
import os

FILES = [
    "cylicamp/core.py",
    "cylicamp/trajectory.py",
    "cylicamp/insights.py",
    "cylicamp/duality.py",
    "cylicamp/pipeline.py",
    "cylicamp/safety_script.py",
    "cylicamp/cli.py",
]


def show_file(filepath: str) -> None:
    """Prints the contents of a file with line numbers."""
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    print(f"\n=== {filepath} ===\n")
    with open(filepath, "r") as f:
        for i, line in enumerate(f, 1):
            print(f"{i:3}  {line}", end="")
    print("\n")


def show_all() -> None:
    """Prints all files."""
    for f in FILES:
        show_file(f)


def menu() -> None:
    """Interactive menu to pick a file to view."""
    print("\n=== CylicAmp File Viewer ===\n")
    for i, f in enumerate(FILES, 1):
        print(f"  {i}. {f}")
    print("  0. Show all files")
    print()
    choice = input("Pick a number: ").strip()
    if choice == "0":
        show_all()
    elif choice.isdigit() and 1 <= int(choice) <= len(FILES):
        show_file(FILES[int(choice) - 1])
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    menu()
