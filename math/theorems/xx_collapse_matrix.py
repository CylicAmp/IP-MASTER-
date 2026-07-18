"""
Theorem 29: XX Collapse — 119/911 Matrix Audit

Matrix of 1s and 9s encoding the sovereign/shield duality.
"119" = bridge node (137-18=119, exhaust phi class).
"911" = mirror/reversal of 119.

Key results:

1. DIGIT SUM INVARIANT (Rows 1-3)
   Rows 1,2,3 all have: 8 ones, 4 nines, digit sum=44, DR=8
   Row 4 breaks pattern: 4 ones, 7 nines, sum=67, DR=4, length=11 (not 12)
   → Row 4 is the entropy/exhaust row — different structure, shorter

2. 119/911 SUBSTRING PATTERN
   Row 1: "119" at [3,9]  "911" at [0,6]   — 2 each, offset by 3
   Row 2: "119" at [0,6]  "911" at [3,9]   — 2 each, offset by 3 (inverted row 1)
   Row 3: "119" at [2,5,8]  "911" at [1,4,7] — 3 EACH, spacing=3 (order-3 heartbeat)
   Row 4: no "119" or "911" substrings

3. ROW 3 IS THE RESONANCE ROW
   "191191191191" — pure alternating 1-9-1 period-3 pattern
   Contains exactly 3 occurrences of "119" AND 3 of "911"
   The order-3 heartbeat appears directly in the substring count

4. DR=8 INVARIANT
   All three structured rows have digit sum 44, DR(44)=8
   44 connects to the palindrome sequence 44-26-31-31-62-44 (AHL=8, RH-E position)

5. ROW PAIR INVERSION
   Row 1 and Row 2 are exact inversions of 119/911 positions:
     Row 1: "119" at [3,9], "911" at [0,6]
     Row 2: "119" at [0,6], "911" at [3,9]
"""

matrix = [
    "911119911119",
    "119911119911",
    "191191191191",
    "91991991919"
]


def dr(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


def find_pattern(row, pat):
    return [i for i in range(len(row) - len(pat) + 1) if row[i:i+len(pat)] == pat]


# Assertions
for row in matrix[:3]:
    assert row.count('1') == 8
    assert row.count('9') == 4
    assert sum(int(c) for c in row) == 44
    assert dr(44) == 8

# Row 4 is different
assert matrix[3].count('1') == 4
assert matrix[3].count('9') == 7
assert len(matrix[3]) == 11

# Row 3 has order-3 heartbeat in substring count
assert len(find_pattern(matrix[2], "119")) == 3
assert len(find_pattern(matrix[2], "911")) == 3

# Row 1 and Row 2 are 119/911 inversions of each other
assert find_pattern(matrix[0], "119") == find_pattern(matrix[1], "911")
assert find_pattern(matrix[0], "911") == find_pattern(matrix[1], "119")


if __name__ == "__main__":
    print("--- THEOREM 29: XX COLLAPSE AUDIT ---")
    for i, row in enumerate(matrix):
        ones  = row.count('1')
        nines = row.count('9')
        dsum  = sum(int(c) for c in row)
        p119  = find_pattern(row, "119")
        p911  = find_pattern(row, "911")
        print(f"Phase {i+1}: \"{row}\"")
        print(f"  1s={ones}  9s={nines}  digit_sum={dsum}  DR={dr(dsum)}")
        print(f"  '119' at {p119}  '911' at {p911}")
    print()
    print("Row 3 order-3 heartbeat: 3× '119' and 3× '911'  ✓")
    print("Rows 1-3 digit sum invariant: 44 (DR=8)  ✓")
    print("Row 4 entropy: different structure, length 11, no 119/911  ✓")
    print()
    print("All assertions passed.")
