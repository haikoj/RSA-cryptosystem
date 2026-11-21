from sieve_of_eratosthenes import sieve
from generator import keygen
from rsa import encrypt, decrypt

def main():
    """Runs the RSA cryptosystem"""

    while True:
        print("\n1: Generate RSA keys")
        print("2: Encrypt your message")
        print("3: Decrypt a message")
        print("0: Quit")
        option = input("Choose an option 1, 2, 3 or 0\n")

        if option == "0":
            break

        if option == "1":
            small_primes = sieve(10000)
            public_key, private_key = keygen(small_primes)

            print("Public key:")
            print(f"modulus n = {public_key[0]}")
            print(f"public exponent e = {public_key[1]}")

            print("Private key:")
            print(f"modulus n = {private_key[0]}")
            print(f"private exponent d = {private_key[1]}")

        elif option == "2":
            try:
                message = input("Your message to Bob, which Eve cannot read: ")
                n = int(input("Enter your modulus: "))
                e = int(input("Enter public exponent e: "))

                ciphertext = encrypt(message, (n, e))

                print(f"Ciphertext: \n{ciphertext}")

            except ValueError as error:
                print(f"Error: {error}")

        elif option == "3":
            try:
                ciphertext = int(input("Enter ciphertext: "))
                n = int(input("Enter your modulus: "))
                d = int(input("Enter your private exponent d: "))

                decrypted_message = decrypt(ciphertext, (n, d))

                print(decrypted_message)

            except (ValueError, UnicodeDecodeError) as error:
                print(f"Error: {error}")

        else: print("Choose 0, 1, 2 or 3.")


if __name__ == "__main__":
    main()
