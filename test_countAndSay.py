from countAndSay import count_and_say
import pytest

def test_count_and_say_spositive():
    assert count_and_say(1) == "1"
    assert count_and_say(4) == "1211"


def test_count_and_say_negative():
    with pytest.raises(ValueError):
        count_and_say(0)
    with pytest.raises(ValueError):
        count_and_say(-3)

def test_count_and_say_large_value():
    assert count_and_say(8) == "1113213211"


def test_count_and_say_multi_type():
    with pytest.raises(TypeError):
        count_and_say("testing")
    with pytest.raises(TypeError):
        count_and_say(3.14)
    with pytest.raises(TypeError):
        count_and_say([1, 2, 3])
