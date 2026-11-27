import miller_rabin

# Selected from Mersenne primes https://www.mersenne.org/primes/
prime_1 = 2**107-1
prime_2 = 2**607-1
prime_3 = 2**4253-1

def test_primes():
    assert miller_rabin.miller_rabin(65537) == True
    assert miller_rabin.miller_rabin(prime_1) == True
    assert miller_rabin.miller_rabin(prime_2) == True
    assert miller_rabin.miller_rabin(prime_3) == True

def test_composite_numbers():
    assert miller_rabin.miller_rabin(2**1500) == False
    assert miller_rabin.miller_rabin(5 * prime_1) == False
    assert miller_rabin.miller_rabin(3 * prime_2) == False
    assert miller_rabin.miller_rabin(2 * prime_3) == False

def test_composite_numbers_without_small_prime_factors():
    assert miller_rabin.miller_rabin(prime_1*prime_2) == False
    assert miller_rabin.miller_rabin(prime_1*prime_3) == False
    assert miller_rabin.miller_rabin(prime_2*prime_3) == False
    assert miller_rabin.miller_rabin(prime_1*prime_2*prime_3) == False

def test_small_primes():
    assert miller_rabin.miller_rabin(-1) == False
    assert miller_rabin.miller_rabin(0) == False
    assert miller_rabin.miller_rabin(1) == False
    assert miller_rabin.miller_rabin(2) == True
    assert miller_rabin.miller_rabin(3) == True
