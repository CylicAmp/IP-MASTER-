"""
Long-Range Persistence Audit — Gate Integrity Monitor.

Checks gate resonance and jitter stability in real time.
"""

import time
import math

# --- AUDIT CONFIGURATION ---
GATE = 1911101
K = 1.062
WINDOW_72H = 72 * 3600  # Seconds


def log_gate_integrity(node: int) -> str:
    """
    Calculate real-time resonance for a gate node.

    Y = cos((2*pi/3) * node) — resonance value.
      At Y = -0.5: gate is in phase (SECURE).
      Otherwise: RE-SYNC REQUIRED.

    T_jitter = (node * K) mod 1.0 — jitter stability measure.
    """
    y = round(math.cos((2 * math.pi / 3) * node), 4)
    t_jitter = (node * K) % 1.0
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    status = "SECURE" if y == -0.5 else "RE-SYNC REQUIRED"
    return f"[{timestamp}] Gate: {node} | Y: {y} | T: {t_jitter:.4f} | Status: {status}"


def audit_range(start: int, count: int = 10) -> None:
    """Audit a range of gate nodes and report their status."""
    secure = 0
    resync = 0
    for node in range(start, start + count):
        result = log_gate_integrity(node)
        print(result)
        if "SECURE" in result:
            secure += 1
        else:
            resync += 1
    print(f"\nSummary: {secure} SECURE, {resync} RE-SYNC REQUIRED")


if __name__ == "__main__":
    print(f"--- Long-Range Persistence Audit: Gate {GATE} ---")
    print(log_gate_integrity(GATE))
    print()
    print(f"--- Scanning nearby nodes ---")
    audit_range(GATE - 2, 5)
