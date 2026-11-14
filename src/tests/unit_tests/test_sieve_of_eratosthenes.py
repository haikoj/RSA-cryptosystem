from sieve_of_eratosthenes import sieve


def test_primes_up_to_100():
    assert sieve(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
                          43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,]

def test_prime_count_up_to_1_million():
    assert len(sieve(1000000)) == 78498