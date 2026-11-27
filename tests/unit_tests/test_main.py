from unittest.mock import patch

from main import main


modulus = 43733
public_exponent = 65537
private_exponent = 14273


def test_key_generation(capsys):
    with patch("builtins.input", side_effect=["1", "0"]):
        with patch("main.keygen", return_value=((modulus, public_exponent), (modulus, private_exponent))) as mock:
            main()

            mock.assert_called_once()

    output = capsys.readouterr().out

    assert f"modulus n = {modulus}" in output
    assert f"public exponent e = {public_exponent}" in output
    assert f"private exponent d = {private_exponent}" in output

def test_encrypt_message(capsys):
    with patch("builtins.input", side_effect=["2", "test", str(modulus), str(public_exponent), "0"]):
        with patch("main.encrypt", return_value=100) as mock:
            main()

            mock.assert_called_once_with("test", (modulus, public_exponent))

    output = capsys.readouterr().out
    assert "Ciphertext: \n100" in output

def test_decrypt_message(capsys):
    with patch("builtins.input", side_effect=["3", "100", str(modulus), str(private_exponent), "0"]):
        with patch("main.decrypt", return_value="test") as mock:
            main()

            mock.assert_called_once_with(100, (modulus, private_exponent))

    output = capsys.readouterr().out
    assert "test" in output

def test_invalid_encryption_input(capsys):
    with patch("builtins.input", side_effect=["2", "test", "invalid_input", "0"]):
        main()

    output = capsys.readouterr().out
    assert "Error:" in output


def test_invalid_decryption_input(capsys):
    with patch("builtins.input", side_effect=["3", "invalid_input", "0"]):
        main()

    output = capsys.readouterr().out
    assert "Error:" in output

def test_invalid_option_input(capsys):
    with patch("builtins.input", side_effect=["4", "0"]):
        main()

    output = capsys.readouterr().out
    assert "Choose 0, 1, 2 or 3." in output
