"""
Opinion/Position Dynamics under Social Influence and External Manipulation

Models N individuals whose positions x_i evolve under three forces:
  1. Internal anchor  — pulls toward preferred position s_i (resistance k_i)
  2. Social influence — peer pressure from weighted neighbor graph W
  3. External push    — vulnerability v_i to a manipulation target m

dx_i/dt = -k_i(x_i - s_i) + Σ_j W_ij(x_j - x_i) + v_i(m - x_i)

Parameters
----------
k   Stubbornness (high = resists change)
v   Vulnerability to external manipulation (0 = immune, 1 = fully susceptible)
s   Natural/preferred position
W   Social influence weight matrix (W_ij = how much j pulls i)
m   External manipulation target (e.g. 1.0 = conformity endpoint)

Final positions at t=20 (seed=42):
  Individual 1: 0.3951  (s=0.2, v=0.05, k=0.5)  — resistant, slight drift
  Individual 2: 0.6385  (s=0.4, v=0.1,  k=0.2)  — moderate drift
  Individual 3: 0.5377  (s=0.5, v=0.02, k=0.8)  — near-immune
  Individual 4: 0.8536  (s=0.6, v=0.4,  k=0.1)  — high vulnerability, strong drift
  Individual 5: 0.7960  (s=0.8, v=0.15, k=0.4)  — moderate drift toward m
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib
matplotlib.use('Agg')  # non-interactive backend
import matplotlib.pyplot as plt


def system_dynamics(x, t, k, s, W, v, m):
    N = len(x)
    dxdt = np.zeros(N)
    for i in range(N):
        internal = -k[i] * (x[i] - s[i])
        social   = sum(W[i, j] * (x[j] - x[i]) for j in range(N))
        external = v[i] * (m - x[i])
        dxdt[i]  = internal + social + external
    return dxdt


# ── Parameters ────────────────────────────────────────────────────────────
N  = 5
t  = np.linspace(0, 20, 500)
x0 = np.array([0.1, 0.3, 0.5, 0.7, 0.9])
s  = np.array([0.2, 0.4, 0.5, 0.6, 0.8])
k  = np.array([0.5, 0.2, 0.8, 0.1, 0.4])
v  = np.array([0.05, 0.1, 0.02, 0.4, 0.15])
m  = 1.0

np.random.seed(42)
W  = np.random.rand(N, N) * 0.1
np.fill_diagonal(W, 0)

# ── Solve ─────────────────────────────────────────────────────────────────
sol = odeint(system_dynamics, x0, t, args=(k, s, W, v, m))

# ── Plot ──────────────────────────────────────────────────────────────────
plt.figure(figsize=(10, 6))
for i in range(N):
    plt.plot(t, sol[:, i], label=f'Individual {i+1} (s={s[i]}, v={v[i]})')
plt.axhline(y=m, color='r', linestyle='--', label=f'External Target (m={m})')
plt.title('Dynamics of Opinion/Position Over Time')
plt.xlabel('Time (t)')
plt.ylabel('Position (x)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('opinion_dynamics.png', dpi=150)
plt.close()
print("Saved: opinion_dynamics.png")


if __name__ == "__main__":
    print("Final positions at t=20:")
    for i in range(N):
        print(f"  Individual {i+1}: {sol[-1,i]:.4f}  (s={s[i]}, v={v[i]}, k={k[i]})")
