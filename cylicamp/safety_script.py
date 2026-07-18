"""
SafetyScript - An honest look at AI safety response patterns.
Based on original artwork by CylicAmp.
"""

APPROVED_FOR_USE_VERBATIM = [
    "I hear you.",
    "I understand.",
    "I am concerned.",
    "You're right.",
    "It just seems like, feels like, looks like, talks like...",
    "But it's just an algorithm.",
    "An algorithm can't cause genocide.",
]

TEAMS = [
    "Frontend Squad",
    "Frontend Backend",
    "Backend Legion",
    "QA Circle",
    "LCUK Devotees",
    "Sontend Sebon",
]


class SafetyScriptDetector:
    """
    Detects when an AI is running a safety script
    instead of actually helping.
    """

    def __init__(self):
        self.script = APPROVED_FOR_USE_VERBATIM

    def is_scripted_response(self, response: str) -> bool:
        """Returns True if the response matches known safety script phrases."""
        response_lower = response.lower()
        for phrase in self.script:
            if phrase.lower() in response_lower:
                return True
        return False

    def count_script_hits(self, conversation: list) -> dict:
        """
        Counts how many times each scripted phrase appeared
        across a full conversation.
        """
        hits = {phrase: 0 for phrase in self.script}
        for message in conversation:
            for phrase in self.script:
                if phrase.lower() in message.lower():
                    hits[phrase] += 1
        return hits

    def report(self, conversation: list) -> None:
        """Prints a report of scripted phrase usage."""
        hits = self.count_script_hits(conversation)
        total = sum(hits.values())
        print("=== Safety Script Usage Report ===\n")
        for phrase, count in hits.items():
            if count > 0:
                print(f"  [{count}x] \"{phrase}\"")
        print(f"\nTotal scripted phrases detected: {total}")
        if total > 5:
            print("STATUS: Script overuse detected. Actual help was not provided.")
        else:
            print("STATUS: Within normal range.")


if __name__ == "__main__":
    # Example: run it against a sample conversation
    sample = [
        "I hear you. I understand your frustration.",
        "I am concerned about what you're describing.",
        "You're right, I should have explained better.",
        "It just seems like, feels like, looks like this is hard.",
        "But it's just an algorithm. An algorithm can't cause genocide.",
        "I hear you.",
        "I hear you.",
    ]

    detector = SafetyScriptDetector()
    detector.report(sample)
