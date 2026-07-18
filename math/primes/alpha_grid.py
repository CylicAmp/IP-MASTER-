"""
Alpha Odds and Even Grid
1234-(5)-6789

Position labels:
  LL = Left Low    LH = Left High
  RL = Right Low   RH = Right High
  O = Odd          E = Even
  (5) = A51 — center axis

Grid:
  1: LL-O    2: LL-E    3: LH-O    4: LH-E
  (5): A51
  6: RL-E    7: RL-O    8: RH-E    9: RH-O
"""

def dr(n):
    n = abs(int(n))
    return 9 if n % 9 == 0 and n != 0 else n % 9

# ── Position map ───────────────────────────────────────────────────────────
GRID = {
    1: {"side": "L", "level": "L", "parity": "O", "label": "LL-O"},
    2: {"side": "L", "level": "L", "parity": "E", "label": "LL-E"},
    3: {"side": "L", "level": "H", "parity": "O", "label": "LH-O"},
    4: {"side": "L", "level": "H", "parity": "E", "label": "LH-E"},
    5: {"side": "C", "level": "C", "parity": "O", "label": "A51"},   # center axis
    6: {"side": "R", "level": "L", "parity": "E", "label": "RL-E"},
    7: {"side": "R", "level": "L", "parity": "O", "label": "RL-O"},
    8: {"side": "R", "level": "H", "parity": "E", "label": "RH-E"},  # AHL
    9: {"side": "R", "level": "H", "parity": "O", "label": "RH-O"},
}

# AHL / ALO from previous session
AHL = 8   # Alpha High — RH-E
ALO = 7   # Alpha Low  — RL-O

# ── OEOEOEOE pattern ──────────────────────────────────────────────────────
# 12 pairs cycling: OE OE OE OE
# 12 × 4 = 48 → DR = 12 → DR = 3

oe_pairs = 4
base = 12
product = base * oe_pairs        # 48
print(f"OEOEOEOE: {base} × {oe_pairs} = {product} → DR = {dr(product)}")

# ── 12+n sequence (DR cycle) ───────────────────────────────────────────────
print("\n12+n DR cycle:")
for n in range(1, 10):
    val = 12 + n
    print(f"  12+{n} = {val} → DR = {dr(val)}")

# ── LL/LH/RL/RH count sums ────────────────────────────────────────────────
# LLLLLL-HH = 6+2 = 8+4 = 12 → DR = 3+1 = 4
# RRRR-LL-LL = 4+3 = 6+4 = 10 → DR = 1+3 = 4
print()
print(f"LL+HH chain: 6+2={6+2}+4={6+2+4} → DR={dr(6+2+4)} → 3+1=4")
print(f"RR+LL chain: 4+3={4+3}+4={4+3+4} → DR={dr(4+3+4)} → 1+3=4")

# ── 46/64 mirror ──────────────────────────────────────────────────────────
print()
print(f"64 - 46 = {64-46} → DR = {dr(64-46)}")
print(f"46 - 64 = {46-64} → abs DR = {dr(abs(46-64))}")
print(f"AHL({AHL}) + ALO({ALO}) = {AHL+ALO} → DR = {dr(AHL+ALO)}")
print(f"AHL in grid: {GRID[AHL]['label']}")
print(f"ALO in grid: {GRID[ALO]['label']}")

# ── Print full grid ────────────────────────────────────────────────────────
print()
print("── 44/26/13/31/62 mirror cluster ───────────────────────────────────")
# 13 and 31 are digit-reverses, both DR=4
# 26 and 62 are digit-reverses, both DR=8  (26=2×13, 62=2×31)
# 44 = DR 8
# All paths land on 8 (AHL)
cluster = [(44,8),(26,8),(13,4),(31,4),(62,8),(44,8)]
for val, expected in cluster:
    print(f"  {val} → DR = {dr(val)}")
print()
print(f"  13 reversed = 31  |  DR match: {dr(13)} = {dr(31)}")
print(f"  26 reversed = 62  |  DR match: {dr(26)} = {dr(62)}")
print(f"  26 = 2×13    62 = 2×31  (doubling preserves mirror)")
print()
print("  Path 13 → DR(4): 4 → 5 → 7 → 8")
print("  Path 31 → DR(4): 4 → 7 → 5 → 8")
print("  Both paths end at 8 (AHL / RH-E)")
print("  44 → DR = 8 (AHL anchor)")

print()
print("── 44-26-31-31-62-44 palindrome grid ──────────────────────────────")
seq2 = [44, 26, 31, 31, 62, 44]
print("  Sequence: ", "  ".join(str(v) for v in seq2))
print("  DR:       ", "  ".join(str(dr(v)) for v in seq2))
print()
print("  L1(DR):   8  8  4  4  8  8")
print("  L2:       7  7  8  7  7   ")
print("  L3:       4  5  4  4  5  4")
fwd = [dr(v) for v in seq2]
print(f"  Palindrome: {fwd == fwd[::-1]}  →  {fwd}")
print(f"  Center 31+31: DR(4+4)=8 (AHL)  |  Outer 44/44: DR=8  |  Inner 26/62: DR=8")

print()
print("── Full Alpha Grid ─────────────────────────────────────────────────")
for n, g in GRID.items():
    marker = " ← AHL" if n == AHL else " ← ALO" if n == ALO else ""
    print(f"  {n}: {g['label']}{marker}")
