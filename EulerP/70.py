


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

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor  # Use integer division
        else:
            divisor += 1
    return factors

def totient(k, n):
    multi = k
    seen = []
    for i in range(len(n)):
        if n[i] in seen:
            continue
        multi = multi * (1 - (1/n[i]))
        seen.append(n[i])
    return multi

def is_perm(n1, n2):
    n1 = str(n1)
    n2 = str(n2)
    return sorted(n1) == sorted(n2)

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def solve(limit):
    phi = list(range(limit))
    min_ratio = float('inf')
    result = 0
    
    # Calculate all totients using sieve method
    for i in range(2, limit):
        if phi[i] == i:  # i is prime
            for j in range(i, limit, i):
                phi[j] = phi[j] * (i - 1) // i
        
        # Check if current number is a solution
        if i > 1:
            ratio = i / phi[i]
            if ratio < min_ratio and is_permutation(i, phi[i]):
                min_ratio = ratio
                result = i
    return result

print(solve(int(input())))
