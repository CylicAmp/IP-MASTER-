# Euler Totient Function — Verified Data Table

## phi(n) for n = 1 to 40

| n | phi(n) | n | phi(n) | n | phi(n) | n | phi(n) |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 11 | 10 | 21 | 12 | 31 | 30 |
| 2 | 1 | 12 | 4 | 22 | 10 | 32 | 16 |
| 3 | 2 | 13 | 12 | 23 | 22 | 33 | 20 |
| 4 | 2 | 14 | 6 | 24 | 8 | 34 | 16 |
| 5 | 4 | 15 | 8 | 25 | 20 | 35 | 24 |
| 6 | 2 | 16 | 8 | 26 | 12 | 36 | 12 |
| 7 | 6 | 17 | 16 | 27 | 18 | 37 | 36 |
| 8 | 4 | 18 | 6 | 28 | 12 | 38 | 18 |
| 9 | 6 | 19 | 18 | 29 | 28 | 39 | 24 |
| 10 | 4 | 20 | 8 | 30 | 8 | 40 | 16 |

## Key Properties

- **Primes:** phi(p) = p - 1
- **Prime powers:** phi(p^k) = p^k - p^(k-1)
- **Multiplicative:** phi(mn) = phi(m) * phi(n) when gcd(m,n) = 1
- **General formula:** phi(n) = n * product(1 - 1/p) over distinct prime factors p of n

## 37-Field Integration

- phi(37) = 36 — active stratum (top layer)
- phi(37) ≡ 0 (mod 36) — anchors the field
- Middle-column descent: 36 → 18 → 24 → 16 (phi(37) to phi(40))
- 432 resonance: all four values sit on exact harmonic nodes
- Registry slots R-37 through R-40: LOCKED AND IMMUTABLE

## Verification

Computed via sympy.totient() — independently verified against standard number theory references.
