from challenges.challenge_encrypt_message import encrypt_message
import pytest


@pytest.mark.parametrize(
    "message, key, expected",
    [
        ("AABBCC", 3, "BAA_CCB"),
        ("ABBCCA", 4, "AC_CBBA"),
        ("AABBCC", -1, "CCBBAA"),
    ],
)
def test_encrypt_message(message, key, expected):
    assert encrypt_message(message, key) == expected
