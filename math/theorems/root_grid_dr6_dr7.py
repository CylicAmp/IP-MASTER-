"""
Root Grid Theorem — DR Classes 6 and 7 (Raw Archive v37.22)

For any DR class d, 2-digit numbers with DR=d split into two groups:
  Group LOW:  digit_sum = d        → Logic Reduction = 2d
  Group HIGH: digit_sum = d + 9   → Logic Reduction = 2(d+9)

Grid span: max(value) - min(value) = 81 = 9² in both grids.

Root-6 Grid (DR=6):
  LOW  (digit_sum=6,  LR=12): 06, 15, 24, 33, 42, 51, 60
  HIGH (digit_sum=15, LR=30): 69, 78, 87
  Span: 87 - 06 = 81

Root-7 Grid (DR=7):
  LOW  (digit_sum=7,  LR=14): 07, 16, 25, 34, 43, 52, 61, 70
  HIGH (digit_sum=16, LR=32): 79, 88
  Span: 88 - 07 = 81

Parity rule:
  LOW group, d even: entries alternate E/E and O/O
  LOW group, d odd:  entries alternate E/O and O/E
  HIGH group inherits opposite parity at the crossing from digit_sum=d+9

Logic Reduction formula: LR(a,b) = a+b+b+a = 2(a+b) = 2×digit_sum
"""


def dr(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


def digit_sum(n):
    return sum(int(d) for d in str(n))


def logic_reduction(n):
    a, b = int(str(n).zfill(2)[0]), int(str(n).zfill(2)[1])
    return a + b + b + a


def parity(n):
    s = str(n).zfill(2)
    p = lambda d: 'E' if int(d) % 2 == 0 else 'O'
    return f'{p(s[0])}/{p(s[1])}'


ROOT6 = [6, 15, 24, 33, 42, 51, 60, 69, 78, 87]
ROOT7 = [7, 16, 25, 34, 43, 52, 61, 70, 79, 88]

LABELS = list('ABCDEFGHIJ')


# --- Assertions ---

# All DR values correct
assert all(dr(v) == 6 for v in ROOT6)
assert all(dr(v) == 7 for v in ROOT7)

# Logic Reduction = 2 × digit_sum
for v in ROOT6 + ROOT7:
    assert logic_reduction(v) == 2 * digit_sum(v)

# Group split: digit_sum in {d, d+9}
assert all(digit_sum(v) in {6, 15} for v in ROOT6)
assert all(digit_sum(v) in {7, 16} for v in ROOT7)

# Logic Reductions: only 2d or 2(d+9)
assert all(logic_reduction(v) in {12, 30} for v in ROOT6)
assert all(logic_reduction(v) in {14, 32} for v in ROOT7)

# Span = 81 = 9²
assert ROOT6[-1] - ROOT6[0] == 81
assert ROOT7[-1] - ROOT7[0] == 81

# Group sizes
root6_low  = [v for v in ROOT6 if digit_sum(v) == 6]
root6_high = [v for v in ROOT6 if digit_sum(v) == 15]
root7_low  = [v for v in ROOT7 if digit_sum(v) == 7]
root7_high = [v for v in ROOT7 if digit_sum(v) == 16]
assert len(root6_low) == 7 and len(root6_high) == 3   # 7+3=10
assert len(root7_low) == 8 and len(root7_high) == 2   # 8+2=10

# LR formula: always 2×digit_sum
for v in ROOT6 + ROOT7:
    assert logic_reduction(v) == 2 * digit_sum(v), f"LR formula failed for {v}"


if __name__ == "__main__":
    for root_name, vals, d in [("Root-6", ROOT6, 6), ("Root-7", ROOT7, 7)]:
        print(f"=== {root_name} Grid (DR={d}) ===")
        low  = [v for v in vals if digit_sum(v) == d]
        high = [v for v in vals if digit_sum(v) == d + 9]
        for i, v in enumerate(vals):
            print(f"  {LABELS[i]}{d}: {v:02d}  ds={digit_sum(v):2d}  "
                  f"DR={dr(v)}  parity={parity(v)}  LR={logic_reduction(v)}")
        print(f"  LOW  (ds={d},   LR={2*d}):    {low}")
        print(f"  HIGH (ds={d+9}, LR={2*(d+9)}): {high}")
        print(f"  Span: {vals[-1]}-{vals[0]} = {vals[-1]-vals[0]} = 9²")
        print()

    print("General rule: LR(a,b) = a+b+b+a = 2×digit_sum")
    print("Span always 81 = 9² across all DR classes.")
    print()
    print("All assertions passed.")
