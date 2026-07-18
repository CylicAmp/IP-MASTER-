import math
from typing import List, Tuple

PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
PSI = PHI - 1                  # Reciprocal of PHI


class TrajectoryGenerator:
    def __init__(self, start: Tuple[float, float] = (1.0, 0.0)):
        self.current_position = start

    def generate_step(self, angle_multiplier: float = 1.0) -> Tuple[float, float]:
        """Calculates the next position using PHI for angle and PSI for distance."""
        x, y = self.current_position
        current_angle = math.atan2(y, x)
        new_angle = current_angle + (PHI * angle_multiplier)
        current_distance = math.sqrt(x**2 + y**2)
        new_distance = current_distance * PSI
        new_x = new_distance * math.cos(new_angle)
        new_y = new_distance * math.sin(new_angle)
        self.current_position = (new_x, new_y)
        return self.current_position

    # NOTE: Default steps is 50 here, but we override it in the execute_logic function.
    def generate_trajectory(self, steps: int = 50, angle_multiplier: float = 1.0) -> List[Tuple[float, float]]:
        """Generates a list of points representing the trajectory."""
        trajectory = [self.current_position]
        for i in range(steps):
            trajectory.append(self.generate_step(angle_multiplier))
        return trajectory
