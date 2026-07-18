"""
Workshop Overview - Moonshot Goal 1
Robotic Avatar Agency and Trust Framework

In the context of Moonshot Goal 1, robotic avatars are envisioned as tools
for enhanced autonomy, accessibility, and superhuman action. However, user
acceptance and control efficiency depend not only on performance, but on the
felt experience of control and on the user trust of the system. Loss of sense
of agency leads to loss of sense of trust, disengagement, and system rejection.

This workshop addresses a pressing gap: how to design, evaluate, and prototype
avatar control systems that support a robust sense of agency, especially under
constraints of latency, AI assistance, or limited embodiment; from a
multidisciplinary and transdisciplinary perspective.

Constraints addressed:
- Latency: delay between user intent and avatar action
- AI assistance: when the system acts on behalf of the user
- Limited embodiment: reduced physical feedback or presence

Disciplines involved:
- Robotics
- Human-computer interaction
- Cognitive science
- Ethics
- Accessibility design
"""

from dataclasses import dataclass
from typing import Optional


CONSTRAINTS = ["latency", "ai_assistance", "limited_embodiment"]

DISCIPLINES = [
    "Robotics",
    "Human-Computer Interaction",
    "Cognitive Science",
    "Ethics",
    "Accessibility Design",
]


@dataclass
class AgencyMetrics:
    """Measures the felt experience of control for a user operating a robotic avatar."""
    control_efficiency: float       # 0.0 to 1.0
    felt_experience_score: float    # 0.0 to 1.0
    trust_level: float              # 0.0 to 1.0
    engagement: float               # 0.0 to 1.0

    def sense_of_agency(self) -> float:
        """
        Overall sense of agency is the average of all metrics.
        When this drops, trust drops, disengagement follows, system gets rejected.
        """
        return (
            self.control_efficiency +
            self.felt_experience_score +
            self.trust_level +
            self.engagement
        ) / 4.0

    def status(self) -> str:
        soa = self.sense_of_agency()
        if soa >= 0.75:
            return "STABLE — user is engaged and in control"
        elif soa >= 0.5:
            return "WARNING — user trust degrading"
        else:
            return "CRITICAL — loss of agency, system rejection risk"


class RoboticAvatarController:
    """
    Moonshot Goal 1: Robotic avatar control system.
    Tracks user agency and adjusts system behavior to maintain trust.
    """

    def __init__(self, user_id: str):
        self.user_id = user_id
        self.metrics: Optional[AgencyMetrics] = None

    def update_metrics(
        self,
        control_efficiency: float,
        felt_experience_score: float,
        trust_level: float,
        engagement: float,
    ) -> None:
        self.metrics = AgencyMetrics(
            control_efficiency=control_efficiency,
            felt_experience_score=felt_experience_score,
            trust_level=trust_level,
            engagement=engagement,
        )

    def evaluate_constraint(self, constraint: str, severity: float) -> str:
        """
        Evaluates how a specific constraint (latency, AI assistance, limited embodiment)
        impacts sense of agency. Severity is 0.0 (none) to 1.0 (maximum).
        """
        if constraint not in CONSTRAINTS:
            return f"Unknown constraint: {constraint}"
        if severity >= 0.75:
            return f"{constraint}: HIGH impact — agency at serious risk"
        elif severity >= 0.4:
            return f"{constraint}: MODERATE impact — monitor closely"
        else:
            return f"{constraint}: LOW impact — within acceptable range"

    def report(self) -> None:
        if not self.metrics:
            print("No metrics recorded yet.")
            return
        soa = self.metrics.sense_of_agency()
        print(f"\n=== Avatar Control Report: {self.user_id} ===")
        print(f"  Control Efficiency:    {self.metrics.control_efficiency:.2f}")
        print(f"  Felt Experience Score: {self.metrics.felt_experience_score:.2f}")
        print(f"  Trust Level:           {self.metrics.trust_level:.2f}")
        print(f"  Engagement:            {self.metrics.engagement:.2f}")
        print(f"  Sense of Agency:       {soa:.2f}")
        print(f"  Status: {self.metrics.status()}\n")


if __name__ == "__main__":
    controller = RoboticAvatarController(user_id="CylicAmp-001")
    controller.update_metrics(
        control_efficiency=0.85,
        felt_experience_score=0.90,
        trust_level=0.80,
        engagement=0.95,
    )
    controller.report()
