"""
Time conversion and digital root patterns.
21:42 analysis — trinity time discovery.
"""


def digital_root(n: int) -> int:
    """Digital root 1-9 (maps 0 to 9)."""
    if n == 0:
        return 9
    return (n - 1) % 9 + 1


def analyze_time(hour_24: int, minute: int) -> dict:
    """Analyze a time for digital root and trinity patterns."""
    hour_12 = hour_24 % 12 or 12
    h_dr = digital_root(hour_24)
    m_dr = digital_root(minute)
    time_num = hour_24 * 100 + minute
    return {
        "time": f"{hour_24:02d}:{minute:02d}",
        "hour_24": hour_24,
        "minute": minute,
        "hour_12": hour_12,
        "hour_dr": h_dr,
        "minute_dr": m_dr,
        "sum": hour_24 + minute,
        "sum_dr": digital_root(hour_24 + minute),
        "product_dr": digital_root(hour_24 * minute),
        "time_number": time_num,
        "time_number_dr": digital_root(time_num),
        "is_trinity": h_dr in {3, 6, 9} and m_dr in {3, 6, 9},
    }


def find_trinity_times() -> list:
    """Find all times where both hour and minute have DR in {3,6,9}."""
    times = []
    for h in range(24):
        for m in range(60):
            h_dr = digital_root(h)
            m_dr = digital_root(m)
            if h_dr in {3, 6, 9} and m_dr in {3, 6, 9}:
                times.append((h, m, h_dr, m_dr))
    return times


def find_sum_to_9_times() -> list:
    """Find all times where DR(hour) + DR(minute) reduces to 9."""
    times = []
    for h in range(24):
        for m in range(60):
            total = digital_root(h) + digital_root(m)
            if digital_root(total) == 9:
                times.append((h, m, digital_root(h), digital_root(m)))
    return times


def run_analysis():
    print("=" * 60)
    print("21:42 TIME ANALYSIS")
    print("=" * 60)

    result = analyze_time(21, 42)

    print(f"\n24-hour format: {result['hour_24']}:{result['minute']:02d}")
    print(f"12-hour format: {result['hour_12']}:{result['minute']:02d} p.m.")

    print(f"\nDigital root patterns:")
    print(f"  Hour (21):       dr = {result['hour_dr']}")
    print(f"  Minutes (42):    dr = {result['minute_dr']}")

    print(f"\nCombined patterns:")
    print(f"  21 + 42 = {result['sum']}, dr = {result['sum_dr']}")
    print(f"  21 * 42 = {21*42}, dr = {result['product_dr']}")

    print(f"\nTime as number 2142:")
    print(f"  Digit sum: 2+1+4+2 = {2+1+4+2}")
    print(f"  Digital root: {result['time_number_dr']}")

    print(f"\nTrinity connection:")
    print(f"  Hour digits (2,1): 2+1 = 3  (trinity)")
    print(f"  Minute digits (4,2): 4+2 = 6  (trinity)")
    print(f"  Total: 3 + 6 = 9  (trinity)")
    print(f"\n21:42 is a trinity time — all components resolve to 3-6-9.")

    print("\n" + "=" * 60)
    print("OTHER TRINITY TIMES (3-6-9 pattern)")
    print("=" * 60)

    trinity_times = find_trinity_times()
    print(f"\nFound {len(trinity_times)} trinity times in 24 hours:")
    for h, m, h_dr, m_dr in trinity_times[:20]:
        print(f"  {h:02d}:{m:02d} -> hour dr={h_dr}, minute dr={m_dr}")
    if len(trinity_times) > 20:
        print(f"  ... and {len(trinity_times) - 20} more")

    print("\n" + "=" * 60)
    print("TIMES WHERE HOUR + MINUTE DIGITS SUM TO 9")
    print("=" * 60)

    sum_9 = find_sum_to_9_times()
    print(f"\nFound {len(sum_9)} such times")
    for h, m, h_dr, m_dr in sum_9[:15]:
        print(f"  {h:02d}:{m:02d} -> {h_dr} + {m_dr} = {h_dr + m_dr} -> 9")


if __name__ == "__main__":
    run_analysis()
