"""
CylicAmp Master Runner — One entry point, everything connected.

Execution order:
  1. G5 Solver       — trajectory + insight + duality (the core engine)
  2. Law of 12       — cycle completion and Tesla frequencies
  3. Fibonacci DR    — digital root collapse of Fibonacci
  4. Tribonacci DR   — period-39 cycle
  5. Trinity Trap    — 3-6-9 doubling dynamics
  6. Euler Totient   — φ(37)=36, the 37-field
  7. Prime Visual    — DR=7 prime simulation
  8. 120-Cell Entropy — black hole entropy from geometry
"""

from cylicamp.g5_solver import run_g5, print_report
from cylicamp.law_of_12 import demonstrate as law12_demo
from cylicamp.fib_dr import demonstrate as fib_demo
from cylicamp.tribonacci_dr import run_analysis as trib_demo
from cylicamp.trinity import demonstrate_trap
from cylicamp.euler_totient import demonstrate as totient_demo
from cylicamp.prime_visual import run_simulation
from cylicamp.entropy_120cell import demonstrate as entropy_demo


DIVIDER = "\n" + "█" * 60 + "\n"


def run_all(steps: int = 50, multiplier: float = 1.0) -> None:

    print(DIVIDER)
    print("  CYLICAMP MASTER SYSTEM — UNIFIED MATHEMATICAL FRAMEWORK")
    print(DIVIDER)

    # 1. G5 — the core engine everything flows through
    print("\n[1/8] G5 SOLVER — Core Engine\n")
    report = run_g5(steps=steps, multiplier=multiplier)
    print_report(report)

    # 2. Law of 12 — cycle completion
    print(DIVIDER)
    print("[2/8] LAW OF 12 — Universal Cycle Completion\n")
    law12_demo()

    # 3. Fibonacci DR
    print(DIVIDER)
    print("[3/8] FIBONACCI DIGITAL ROOT OPERATOR\n")
    fib_demo()

    # 4. Tribonacci DR — period 39
    print(DIVIDER)
    print("[4/8] TRIBONACCI DIGITAL ROOT — Period 39\n")
    trib_demo()

    # 5. Trinity Trap — 3-6-9 doubling dynamics
    print(DIVIDER)
    print("[5/8] TRINITY TRAP — 3-6-9 Doubling Dynamics\n")
    demonstrate_trap()

    # 6. Euler Totient — the 37-field
    print(DIVIDER)
    print("[6/8] EULER TOTIENT — φ(37)=36, the 37-Field\n")
    totient_demo()

    # 7. DR=7 Prime Simulation
    print(DIVIDER)
    print("[7/8] DR=7 PRIME SIMULATION\n")
    run_simulation(200)

    # 8. 120-Cell Entropy — geometry → black hole entropy
    print(DIVIDER)
    print("[8/8] 120-CELL ENTROPY — Black Hole Geometry\n")
    entropy_demo()

    # Final summary
    print(DIVIDER)
    print("  SYSTEM COMPLETE")
    print(f"\n  G5 Structural Status : {report['structural_status']}")
    print(f"  G5 Insight Score     : {report['insight_score']:,.2f}")
    print(f"  G5 Stability Ratio   : {report['stability_ratio']:.4f}")
    print(f"  Halt Check           : {report['halt_check']}")
    print(f"  DAC                  : {report['dac_check_status']}")
    print(f"  Cosmic Harmony       : {report['harmony_check_status']}")
    print(DIVIDER)


if __name__ == "__main__":
    run_all()
