"""
LoB 691/695 — AHL-8 Vault and Observer Gap Lock

LoB_691: AHL-8 VAULT
  j=8 bridges twin primes 11 and 13 while skipping sovereign 12.
    3+8=11  DR=2  (lower twin prime)
    4+8=12  DR=3  <- sovereign target, never reached in the chains
    5+8=13  DR=4  (upper twin prime)
  11+2=13: the direct step across the twin prime gap = 2 (observer gap).

LoB_695: OBSERVER GAP LOCK
  695 % 37 = 29
  Digits of 29: 2+9 = 11 (first twin prime)
  DR(29) = 2
  The 695-seal digit-sum returns to target 11.
"""


def dr(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


def verify_ahl_vault():
    assert 3 + 8 == 11 and dr(11) == 2
    assert 4 + 8 == 12 and 12 in {3, 12, 21, 30}   # sovereign — skipped
    assert 5 + 8 == 13 and dr(13) == 4
    assert 13 - 11 == 2                              # observer gap = twin prime gap
    return "VAULT_SECURED"


def lock_observer_gap():
    r = 695 % 37
    assert r == 29
    assert (r // 10) + (r % 10) == 11   # digit sum = first twin prime
    return r


assert verify_ahl_vault() == "VAULT_SECURED"
assert lock_observer_gap() == 29


if __name__ == "__main__":
    print(f"AHL-8 vault: {verify_ahl_vault()}")
    print(f"  3+8=11 (DR=2)  4+8=12 (sovereign, skipped)  5+8=13 (DR=4)")
    print(f"  Twin prime gap = observer gap = {13-11}")
    print()
    r = lock_observer_gap()
    print(f"695 % 37 = {r}")
    print(f"Digit sum: {r//10}+{r%10} = {r//10+r%10} (first twin prime)")
    print()
    print("All assertions passed.")
