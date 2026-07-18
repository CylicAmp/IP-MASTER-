import math
from typing import Dict, List, Union

QFM_REQUIRED = 1.0


class DualityVerifier:
    def calculate_digital_root(self, n: int) -> int:
        if n == 0:
            return 0
        while n >= 10:
            n = sum(int(d) for d in str(n))
        return n

    def is_dr_7_prime(self, n: int) -> bool:
        """Checks if a number is prime and has a Digital Root (DR) of 7."""
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return self.calculate_digital_root(n) == 7

    def verify_duality_spectrum(self, energy_spectrum: List[float], required_min_stability: float) -> Dict[str, Union[int, str, float]]:
        """
        Verifies the energy spectrum against the DR=7 Prime Rule using the dynamically recalibrated minimum stability.
        """
        stable_count = 0
        total_count = len(energy_spectrum)

        max_energy = max(abs(e) for e in energy_spectrum) if energy_spectrum else 1.0
        if max_energy == 0:
            max_energy = 1.0

        for energy in energy_spectrum:
            normalized = abs(energy) / max_energy
            check_value = int(normalized * 1000 * QFM_REQUIRED)
            if self.is_dr_7_prime(check_value):
                stable_count += 1

        stability_ratio = stable_count / total_count if total_count > 0 else 0.0

        return {
            "Status": "PASS" if stability_ratio >= required_min_stability else "FAIL",
            "Stability_Ratio": stability_ratio,
            "Required_Min_Stability": required_min_stability,
        }
