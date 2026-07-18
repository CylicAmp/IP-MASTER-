"""
LCM Convergence and Digital Root Cycle
Master Kimchi — Little Wood 37 Framework

Results:
  LCM(1,2,3)   = 6   — 1-2-3 group meets every 6n
  LCM(1,2,3,9) = 18  — 9 joins every 18n (every 3rd step of 6n)
  DR cycle of 6n: {6, 3, 9} repeating, period 3

Key insight: 9 only meets the 1-2-3 group at EVEN multiples of 9
(18, 36, 54...) because 9 is odd and the group requires divisibility by 2.
"""


def digital_root(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


limit = 108  # 6 full cycles of 18

# 1. Convergence of 1, 2, 3
convergence_123 = [i for i in range(1, limit + 1) if i % 6 == 0]

# 2. Convergence of 1, 2, 3, 9
convergence_1239 = [i for i in range(1, limit + 1) if i % 18 == 0]

# 3. Digital roots of 6n — prove {6,3,9} period-3 cycle
dr_6n = [(i, digital_root(i)) for i in convergence_123]
dr_values = [dr for _, dr in dr_6n]

# Verify period-3 cycle
cycle = dr_values[:3]
for i, dr in enumerate(dr_values):
    assert dr == cycle[i % 3], f"Cycle broken at step {i+1}: got {dr}, expected {cycle[i%3]}"

# Verify 9 appears only at n ≡ 0 (mod 3) in 6n sequence
nine_positions = [i+1 for i, (_, dr) in enumerate(dr_6n) if dr == 9]
for pos in nine_positions:
    assert pos % 3 == 0, f"9 appeared at non-multiple-of-3 position: {pos}"


if __name__ == "__main__":
    print("LCM(1,2,3)   =", 6)
    print("LCM(1,2,3,9) =", 18)
    print()
    print("Multiples of 6 (first 9):")
    for val, dr in dr_6n[:9]:
        marker = " ← 9 joins here" if val % 18 == 0 else ""
        print(f"  6×{val//6:>2} = {val:>3}   DR={dr}{marker}")
    print()
    print(f"DR cycle of 6n: {cycle}  (period 3, repeats forever)")
    print(f"9 appears at positions: {nine_positions[:6]}...")
    print(f"All 9-positions are multiples of 3: {all(p % 3 == 0 for p in nine_positions)}")
    print()
    print("All assertions passed.")
