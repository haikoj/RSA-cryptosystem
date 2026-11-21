import miller_rabin


def test_smallest_numbers():
    assert miller_rabin.miller_rabin(0) == False
    assert miller_rabin.miller_rabin(1) == False
    assert miller_rabin.miller_rabin(2) == True
    assert miller_rabin.miller_rabin(3) == True
    assert miller_rabin.miller_rabin(4) == False


def test_primes():
    assert miller_rabin.miller_rabin(7) == True
    assert miller_rabin.miller_rabin(17) == True
    assert miller_rabin.miller_rabin(97) == True
    assert miller_rabin.miller_rabin(8191) == True
    assert miller_rabin.miller_rabin(65537) == True

def test_nonprimes():
    assert miller_rabin.miller_rabin(9) == False
    assert miller_rabin.miller_rabin(25) == False
    assert miller_rabin.miller_rabin(91) == False
    assert miller_rabin.miller_rabin(6601) == False
    assert miller_rabin.miller_rabin(65541) == False
