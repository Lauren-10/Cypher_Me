from math import sqrt

def subtractions(a, b, cap=None):
    s = 0
    while b:
        q = a // b
        s += q
        if cap is not None and s > cap:  # strict '>' keeps ties
            return s
        a, b = b, a - q*b
    return s

def smallest_m_with_steps_up(n, TARGET=61, report_every=1_000_000):
    phi = (1 + sqrt(5)) / 2
    c   = int(n / phi)                    # generous upper cap
    # Hard lower bound in the q0=1 region:
    # S >= q0 + 2, so q0 must be 1 for a minimal TARGET in this range.
    # A tight start for q0=1 with tail sum TARGET-1 is near the CF [1, TARGET-1].
    # This puts b well above n/2; we can just start at n//2+1 safely.
    b0 = n//2 + 30000000001

    checked = 0
    for m in range(b0, c + 1):
        checked += 1
        if checked % report_every == 0:
            print(f"...checked {checked:,} (m={m})")
        if subtractions(n, m, cap=TARGET) == TARGET:
            print(f"found at m={m} after {checked:,} candidates")
            return m
    print("no m with exactly", TARGET, "steps in the scanned range")
    return None

if __name__ == "__main__":
    n = 1_000_000_000_039
    print("Smallest m with 61 steps:", smallest_m_with_steps_up(n, 61, 100_000_000))
