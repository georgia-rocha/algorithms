from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(4, "hello")
    with pytest.raises(TypeError):
        encrypt_message(4, 4)
    with pytest.raises(TypeError):
        encrypt_message("hello", "hello")
    assert encrypt_message("hello", 2) == "oll_eh"
    assert encrypt_message("hello", 0) == "olleh"
