import secrets
import math

from miller_rabin import miller_rabin


def primegen(small_primes, bits=1024, k=40):
    """Generates a 1024-bit probable prime number"""
    while True:
        prime_candidate = secrets.randbits(bits)
        prime_candidate |= 1 # ensures oddness
        prime_candidate |= 2**(bits - 1) # ensures 1024 bits

        # tests if candidate is divisible by small primes
        if any(prime_candidate % p == 0 for p in small_primes):
            continue

        if miller_rabin(prime_candidate, k):
            return prime_candidate


def keygen(small_primes):
    """Generates a public and private key according to the RSA algorithm"""
    e = 65537

    while True:
        p = primegen(small_primes)
        q = primegen(small_primes)
        if p == q:
            continue

        n = p*q
        if n.bit_length() != 2048:
            continue

        phi = (p-1) * (q-1)

        if math.gcd(e, phi) != 1:
            continue

        d = pow(e, -1, phi)

        pub = (n, e)
        priv = (n, d)

        return pub, priv
