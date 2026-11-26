from rsa import encrypt, decrypt

def test_too_long_msg():
    public_key = (10, 3)
    message = "toolong" * 99

    try:
        encrypt(message, public_key)

    except ValueError:
        return

    assert False, "Expected ValueError"
