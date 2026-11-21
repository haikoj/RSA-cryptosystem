def encrypt(message, public_key):
    """Encrypt a utf-8 message using the public key"""
    n, e = public_key
    msg = int.from_bytes(message.encode("utf-8"), "big")

    if msg > n:
        raise ValueError("The message was too long")

    return pow(msg, e, n)


def decrypt(ciphertext, private_key):
    """Decrypt the ciphertext using the private key."""
    n, d = private_key
    msg = pow(ciphertext, d, n)
    msg_length = (msg.bit_length()+7) // 8

    return msg.to_bytes(msg_length, "big").decode("utf-8")
