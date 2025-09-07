def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            # Mark multiples of p as not prime
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    primes = [i for i, prime_status in enumerate(is_prime) if prime_status]
    return primes
