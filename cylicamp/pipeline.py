from cylicamp.trajectory import TrajectoryGenerator
from cylicamp.insights import InsightEngine
from cylicamp.duality import DualityVerifier


def run_pipeline(steps: int = 50, multiplier: float = 1.0, required_min_stability: float = 0.5):
    # Generate trajectory
    tg = TrajectoryGenerator()
    trajectory = tg.generate_trajectory(steps=steps)

    # Extract energy values from trajectory
    energy_spectrum = [abs(x) + abs(y) for x, y in trajectory]

    # Apply modular filter and calculate insights
    ie = InsightEngine(multiplier=multiplier)
    raw_data = [int(e * 1000) for e in energy_spectrum]
    filtered = ie.apply_modular_filter(raw_data)
    insight_score = ie.calculate_weighted_insights(filtered)

    # Verify duality spectrum
    dv = DualityVerifier()
    result = dv.verify_duality_spectrum(energy_spectrum, required_min_stability)

    print(f"Insight Score:     {insight_score:.4f}")
    print(f"Spectrum Status:   {result['Status']}")
    print(f"Stability Ratio:   {result['Stability_Ratio']:.4f}")


if __name__ == "__main__":
    run_pipeline()
