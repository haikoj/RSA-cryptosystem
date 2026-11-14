from math import isqrt

def sieve(n = 100):
    prime = [False, False] + [True] * (n-1)

    for i in range(2, isqrt(n) + 1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False

    return [i for i, is_prime in enumerate(prime) if is_prime]
