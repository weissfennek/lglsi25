import pytest
from string_operations import reverse_string

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_reverse_string_invalid_input():
    with pytest.raises(TypeError):
        reverse_string(123)
    with pytest.raises(TypeError):
        reverse_string(None)
