"""
Shell Opacity Theorem: 100% INVIOLATE

Of the 32 purge nodes, zero map into the sovereign range {3,12,21,30}.
Shell opacity = 32/32 = 100%.

This is a direct corollary of the Sovereign Fixed Point bijection:
  f(n) = (137n) mod 37 is a bijection on {1..36}.
  The 4 anchors {4,9,25,30} exclusively occupy the pre-images of {3,12,21,30}.
  No purge node can reach a sovereign residue — the shell is mathematically sealed.
"""

DOMAIN = {4, 9, 25, 30}
RANGE  = {3, 12, 21, 30}


def check_shell_opacity():
    purge_nodes = [n for n in range(1, 37) if n not in DOMAIN]
    absorptions = sum(1 for n in purge_nodes if (n * 137) % 37 not in RANGE)
    opacity = (absorptions / 32) * 100
    return f"SHELL OPACITY: {opacity}% | STATUS: INVIOLATE"


purge_nodes = [n for n in range(1, 37) if n not in DOMAIN]
assert len(purge_nodes) == 32
assert all((n * 137) % 37 not in RANGE for n in purge_nodes)
assert check_shell_opacity() == "SHELL OPACITY: 100.0% | STATUS: INVIOLATE"


if __name__ == "__main__":
    print(check_shell_opacity())
    print()
    print("All assertions passed.")
