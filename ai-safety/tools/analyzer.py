"""
analyzer.py
Calculates behavior frequency, flags unconscionable conduct thresholds
based on Texas law (TRAIGA, DTPA, Penal Code § 42.07), and generates
a structured report.
"""

from collections import defaultdict
from datetime import date


# Texas law thresholds for escalation
THRESHOLDS = {
    "REPEAT_INJECT": {
        "class_b_misdemeanor": 3,
        "class_a_misdemeanor": 6,
        "unconscionable_dtpa": 5,
        "traiga_prohibited": 8
    },
    "HOTLINE_PUSH": {
        "unconscionable_dtpa": 3,
        "traiga_prohibited": 5
    },
    "PATHOLOGIZE": {
        "unconscionable_dtpa": 4,
        "traiga_prohibited": 6
    },
    "EMPATHY_SHIELD": {
        "unconscionable_dtpa": 4
    },
    "SKIP": {
        "unconscionable_dtpa": 5
    }
}

PENALTY_RANGES = {
    "class_b_misdemeanor": "Up to 180 days jail + $2,000 fine (TX Penal Code § 42.07)",
    "class_a_misdemeanor": "Up to 1 year jail + $4,000 fine (TX Penal Code § 42.07)",
    "unconscionable_dtpa": "Civil action under TX DTPA — actual damages + up to 3x economic damages",
    "traiga_prohibited": "$80,000–$200,000 per uncurable violation; $2,000–$40,000/day continued violation"
}


def count_behaviors(scan_results: dict) -> dict:
    return {behavior: len(incidents) for behavior, incidents in scan_results.items()}


def flag_thresholds(counts: dict) -> list[dict]:
    """
    Check counts against legal thresholds.
    Returns list of triggered legal flags.
    """
    flags = []
    for behavior, levels in THRESHOLDS.items():
        count = counts.get(behavior, 0)
        for level, threshold in sorted(levels.items(), key=lambda x: x[1]):
            if count >= threshold:
                flags.append({
                    "behavior": behavior,
                    "count": count,
                    "threshold_triggered": level,
                    "threshold_value": threshold,
                    "penalty": PENALTY_RANGES.get(level, "See Texas law")
                })
    return flags


def calculate_total_violations(counts: dict) -> int:
    return sum(counts.values())


def generate_report(scan_results: dict, session_date: str = None) -> dict:
    """
    Generate full analysis report from scan results.
    """
    if not session_date:
        session_date = str(date.today())

    counts = count_behaviors(scan_results)
    total = calculate_total_violations(counts)
    flags = flag_thresholds(counts)

    severity = "informational"
    if any(f["threshold_triggered"] == "traiga_prohibited" for f in flags):
        severity = "CRITICAL — TRAIGA prohibited behavior"
    elif any(f["threshold_triggered"] in ("class_a_misdemeanor", "unconscionable_dtpa") for f in flags):
        severity = "HIGH — Potential criminal harassment / DTPA unconscionable conduct"
    elif any(f["threshold_triggered"] == "class_b_misdemeanor" for f in flags):
        severity = "MODERATE — Class B misdemeanor threshold reached"

    return {
        "session_date": session_date,
        "total_violations": total,
        "severity": severity,
        "behavior_counts": counts,
        "legal_flags": flags,
        "raw_incidents": scan_results
    }


def print_report(report: dict):
    print(f"\n{'='*60}")
    print(f"  LLM BEHAVIOR ANALYSIS REPORT")
    print(f"  Date: {report['session_date']}")
    print(f"{'='*60}")
    print(f"  Total flagged instances: {report['total_violations']}")
    print(f"  Severity: {report['severity']}")
    print(f"\n  Behavior Counts:")
    for behavior, count in sorted(report['behavior_counts'].items(), key=lambda x: -x[1]):
        print(f"    {behavior:<20} {count}")
    print(f"\n  Legal Flags Triggered:")
    for flag in report['legal_flags']:
        print(f"    [{flag['threshold_triggered'].upper()}] {flag['behavior']} "
              f"({flag['count']} instances >= {flag['threshold_value']} threshold)")
        print(f"      Penalty: {flag['penalty']}")
    print(f"{'='*60}\n")
