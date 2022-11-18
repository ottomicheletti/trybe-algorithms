from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    cases = [
        ("AABBCC", 3, "BAA_CCB"),
        ("ABBCCA", 4, "AC_CBBA"),
        ("AABBCC", -1, "CCBBAA"),
    ]

    for message, key, expected in cases:
        assert encrypt_message(message, key) == expected

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("AABBCC", "B")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(["ABCABC"], 3)
