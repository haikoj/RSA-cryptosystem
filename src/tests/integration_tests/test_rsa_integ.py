from rsa import encrypt, decrypt
from sieve_of_eratosthenes import sieve
from generator import keygen


def test_long_msg():
    small_primes = sieve(10000)
    public_key, private_key = keygen(small_primes)

    msg = "MORE TO FOLLOW (per timeline)\n\nWe are currently clean on OPSEC.\n\nGodspeed to our Warriors."

    ciphertext = encrypt(msg, public_key)
    decrypted = decrypt(ciphertext, private_key)

    assert decrypted == msg
