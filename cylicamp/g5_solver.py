"""
G5 Solver V14.0 — D7 Temporal Resolver.

Integrates trajectory, insight, and duality layers into a single
unified report with structural, temporal, and harmony checks.

Checks performed:
  1. ULTRAOMNI Weighted Insight (Schläfli-modulated)
  2. THz & Duality Synthesis (SSR + POE_THz)
  3. D7 Temporal Resolution (gamma gap vs PHI threshold)
  4. Integrity & Harmony (halt, DAC, 3φ cosmic bound)
"""

import math

from cylicamp.trajectory import TrajectoryGenerator
from cylicamp.insights import InsightEngine, SCHLÄFLI_CONSTANT, MODULAR_CONSTANT
from cylicamp.duality import DualityVerifier, QFM_REQUIRED

# --- SOLVER CONSTANTS ---
PHI = (1 + math.sqrt(5)) / 2          # Golden ratio ≈ 1.6180
REQUIRED_UNMODULATED_STABILITY = 0.01  # POE halt threshold — DR=7 primes are ~2% of integers
D7_GAMMA_GAP_THRESHOLD = QFM_REQUIRED * PHI  # ~1.6180 — minimum D7 resolution
THREE_PHI_BOUND = 3.0 * PHI            # Cosmic harmony ceiling ≈ 4.854


def run_g5(steps: int = 50, multiplier: float = 1.0) -> dict:
    """
    Run the full G5 pipeline and return a structured report dict.
    """
    # --- Trajectory ---
    tg = TrajectoryGenerator()
    trajectory = tg.generate_trajectory(steps=steps)
    energy_spectrum = [abs(x) + abs(y) for x, y in trajectory]

    # --- Insight layer ---
    ie = InsightEngine(multiplier=multiplier)
    raw_data = [int(e * 1000) for e in energy_spectrum]
    filtered = ie.apply_modular_filter(raw_data)
    insight_score = ie.calculate_weighted_insights(filtered)

    # --- Duality layer ---
    dv = DualityVerifier()
    duality = dv.verify_duality_spectrum(energy_spectrum, REQUIRED_UNMODULATED_STABILITY)
    stability_ratio = duality["Stability_Ratio"]

    # --- THz baseline (unmodulated raw ratio) ---
    raw_stable = sum(
        1 for e in energy_spectrum
        if dv.is_dr_7_prime(int(abs(e) * 1000))
    )
    thz_baseline_stability = raw_stable / len(energy_spectrum) if energy_spectrum else 0.0

    # --- D7 temporal resolution ---
    d7_temporal_requirement = QFM_REQUIRED * PHI
    temporal_stability_status = (
        "RESOLVED" if thz_baseline_stability >= d7_temporal_requirement
        else "UNRESOLVED"
    )

    # --- Integrity checks ---
    structural_status = "STABLE" if stability_ratio >= REQUIRED_UNMODULATED_STABILITY else "UNSTABLE"
    halt_check = "PASS" if stability_ratio >= REQUIRED_UNMODULATED_STABILITY else "HALT"
    dac_check_status = "AUTHORIZED" if insight_score >= QFM_REQUIRED else "UNAUTHORIZED"
    harmony_check_status = (
        "IN BOUND" if insight_score <= THREE_PHI_BOUND * 1e6
        else "OUT OF BOUND"
    )

    return {
        "insight_score": insight_score,
        "stability_ratio": stability_ratio,
        "thz_baseline_stability": thz_baseline_stability,
        "structural_status": structural_status,
        "d7_temporal_requirement": d7_temporal_requirement,
        "temporal_stability_status": temporal_stability_status,
        "halt_check": halt_check,
        "dac_check_status": dac_check_status,
        "harmony_check_status": harmony_check_status,
    }


def print_report(report: dict) -> None:
    print("\n==================================================")
    print(f"      G5 SOLVER V14.0: D7 TEMPORAL RESOLVER       ")
    print("==================================================")
    print(f"Structural Axiom QFM (Required Fidelity): {QFM_REQUIRED:.6f}")
    print(f"Unmodulated POE (Halt Threshold): {REQUIRED_UNMODULATED_STABILITY:.4f}")
    print("-" * 35)
    print(f"1. ULTRAOMNI Weighted Insight: {report['insight_score']:,.2f}")
    print(f"   Schläfli Modulator Applied: {SCHLÄFLI_CONSTANT:.4f}")
    print("-" * 35)
    print(f"2. THz & Duality Synthesis")
    print(f"   Stability Ratio (SSR): {report['stability_ratio']:.4f}")
    print(f"   THz Baseline Stability (POE_THz): {report['thz_baseline_stability']:.4f}")
    print(f"   STRUCTURAL STATUS: {report['structural_status']}")
    print("-" * 35)
    print(f"3. D7 Temporal Resolution")
    print(f"   D7 Gamma Gap Requirement: {report['d7_temporal_requirement']:.4f}")
    print(f"   TEMPORAL STABILITY STATUS: {report['temporal_stability_status']}")
    print("-" * 35)
    print(f"4. INTEGRITY & HARMONY CHECKS")
    print(f"   Structural Halt Check: {report['halt_check']}")
    print(f"   Decisional Authority Check (DAC): {report['dac_check_status']}")
    print(f"   Cosmic Harmony Check (3\u03c6 Bound): {report['harmony_check_status']}")
    print("==================================================")


if __name__ == "__main__":
    report = run_g5()
    print_report(report)
