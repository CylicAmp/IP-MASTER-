"""
Modal Crossing Orbit Generator — LoB 20
Verified: orbit_p, orbit_v, gate, promotion map g(n)=2n+19, commutation lock g∘f=f∘g
"""

mod = 37
f = lambda n: (3 * n + 1) % mod   # evolve
g = lambda n: (2 * n + 19) % mod  # promote


def get_orbit(start, func, length):
    orbit = []
    curr = start
    for _ in range(length):
        orbit.append(curr)
        curr = func(curr)
    return orbit


orbit_p = get_orbit(0, f, 18)  # [P] — peripheral / potential
orbit_v = get_orbit(2, f, 18)  # [V] — verified / active
gate = 18                       # [G] — sovereign fixed point


def verify_promotion_map():
    """Verify g(n) maps every element of orbit_p into orbit_v."""
    v_set = set(orbit_v)
    results = []
    for n in orbit_p:
        gn = g(n)
        results.append((n, gn, gn in v_set))
    return results


def verify_commutation():
    """Verify g∘f = f∘g for all n in orbit_p."""
    results = []
    for n in orbit_p:
        gof = g(f(n))
        fog = f(g(n))
        results.append((n, gof, fog, gof == fog))
    return results


if __name__ == "__main__":
    print("=== ORBIT GENERATION ===")
    print(f"orbit_p = {orbit_p}")
    print(f"orbit_v = {orbit_v}")
    print(f"gate    = {gate}")
    print(f"len(P)={len(orbit_p)}, len(V)={len(orbit_v)}, total={len(orbit_p)+len(orbit_v)+1}")

    print("\n=== PROMOTION MAP g(n) = 2n+19 ===")
    promo = verify_promotion_map()
    all_valid = all(r[2] for r in promo)
    for n, gn, valid in promo:
        print(f"  g({n:2d}) = {gn:2d}  {'✓' if valid else '✗'}")
    print(f"All 18 promotions valid: {all_valid}")

    print("\n=== COMMUTATION LOCK g∘f = f∘g ===")
    comm = verify_commutation()
    all_locked = all(r[3] for r in comm)
    for n, gof, fog, match in comm:
        print(f"  n={n:2d}  g(f(n))={gof:2d}  f(g(n))={fog:2d}  {'✓' if match else '✗'}")
    print(f"Structural lock confirmed: {all_locked}")
