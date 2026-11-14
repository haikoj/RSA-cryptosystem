from time import perf_counter

from sieve_of_eratosthenes import sieve
from generator import keygen
from rsa import encrypt, decrypt

def main():
    message = str(input("Your message to Bob, which Eve cannot read: "))

    start_time = perf_counter()

    small_primes = sieve(10000)
    public_key, private_key = keygen(small_primes)
    ciphertext = encrypt(message, public_key)
    decrypted_message = decrypt(ciphertext, private_key)

    end_time = perf_counter()

    print(ciphertext)
    print(decrypted_message)

    print(f"run time {end_time - start_time:.2f}")


if __name__ == "__main__":
    main()