from unittest.mock import patch

from generator import primegen
from generator import keygen


small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

# primegen tests:

def test_number_is_odd():
    assert primegen(small_primes) & 1 == 1

def test_number_is_1024_bits():
    assert primegen(small_primes).bit_length() == 1024

def test_number_not_divisible_with_small_primes():
    p = primegen(small_primes)
    assert all(p % n != 0 for n in small_primes)

def test_calls_miller_rabin():
    with patch("generator.secrets.randbits", return_value = 131):
        with patch("generator.miller_rabin", return_value = True) as mocker:
            primegen([2, 3, 5], bits = 8)

            mocker.assert_called_once_with(131, 40)

# keygen tests:

def test_e_is_65537():
    assert keygen(small_primes)[0][1] == 65537

def test_n_is_2048_bits():
    assert keygen(small_primes)[0][0].bit_length() == 2048

def test_encryption_and_decryption():
    pub, priv = keygen(small_primes)

    message = 12345
    encrypted = pow(message, pub[1], pub[0])
    decrypted = pow(encrypted, priv[1], pub[0])
    
    assert decrypted == message
