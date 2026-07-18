from typing import List

MODULAR_CONSTANT = 37
SCHLÄFLI_CONSTANT = 8.0        # Schlafli symbol for {8} regular octagon
STABILITY_TRAJECTORY_STEPS = 50


class InsightEngine:
    def __init__(self, multiplier: float = 1.0):
        self.multiplier = multiplier

    def apply_modular_filter(self, raw_data_set: List[int]) -> List[int]:
        """Only keeps indices congruent to {0, 1} mod 37."""
        processed_data = []
        for index, datum in enumerate(raw_data_set):
            if index % MODULAR_CONSTANT in [0, 1]:
                processed_data.append(datum)
        return processed_data

    def calculate_weighted_insights(self, filtered_data: List[int]) -> float:
        """Calculates the weighted insight score, normalized by the modular compression."""
        if not filtered_data:
            return 0.0
        data_sum = sum(filtered_data)
        divisor = (len(filtered_data) / MODULAR_CONSTANT) if len(filtered_data) >= MODULAR_CONSTANT else 1.0

        # V12.0 Enhancement: Apply Schläfli Constant modulation to Insight
        insight_modulator = SCHLÄFLI_CONSTANT * (STABILITY_TRAJECTORY_STEPS / 50.0)

        return (data_sum * self.multiplier * insight_modulator) / divisor
