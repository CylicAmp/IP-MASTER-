"""
Layer 38 (cont.): Computational Verification of Local Confluence
Unified 1/137 Lattice — diamond property exhaustive check.

State space: (AB parity, grid position, deviation index)
  AB:   2 states  {0, 1}
  Grid: 9 states  {0..8}
  Dev:  8 states  {0..7}
  Total: 144 states

Transitions:
  AB parity flip:      (ab, g, d) → (1-ab, g, d)
  Grid shift:          (ab, g, d) → (ab, (g+1)%9, d)
  Deviation advance:   (ab, g, d) → (ab, g, (d+1)%8)

Diamond property: for every state s and all pairs t1≠t2 reachable in one step,
  ∃ u reachable from both t1 and t2 within bounded depth.

Output (verified):
  States checked: 144
  Local confluence (diamond property) holds: True
  Counterexamples found: 0
"""

from itertools import product

NUM_AB   = 2
NUM_GRID = 9
NUM_DEV  = 8

STATES = list(product(range(NUM_AB), range(NUM_GRID), range(NUM_DEV)))


def next_states(state):
    ab, g, d = state
    return [
        (1 - ab, g, d),
        (ab, (g + 1) % NUM_GRID, d),
        (ab, g, (d + 1) % NUM_DEV),
    ]


def check_diamond(depth=3):
    diamond_holds = True
    counterexamples = 0

    for s in STATES:
        succ = next_states(s)
        for i in range(len(succ)):
            for j in range(i + 1, len(succ)):
                t1, t2 = succ[i], succ[j]
                rt1, rt2 = {t1}, {t2}
                common_found = False
                for _ in range(depth):
                    rt1.update(x for t in list(rt1) for x in next_states(t))
                    rt2.update(x for t in list(rt2) for x in next_states(t))
                    if rt1 & rt2:
                        common_found = True
                        break
                if not common_found:
                    diamond_holds = False
                    counterexamples += 1

    return diamond_holds, counterexamples


if __name__ == "__main__":
    holds, count = check_diamond()
    print("States checked:", len(STATES))
    print("Local confluence (diamond property) holds:", holds)
    print("Counterexamples found:", count)

    assert holds, "Diamond property failed"
    assert count == 0, f"Unexpected counterexamples: {count}"
    print("\nAll assertions passed.")
