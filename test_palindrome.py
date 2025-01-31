#test palindrome
import pytest
from palindrome import palindrome
def rmpty_string  ():
    assert palindrome("") == True
def case_string():
    assert palindrome("RadAr") == True
    assert palindrome("lEVel") == True
def normal_string():
    assert palindrome("radar")
    assert palindrome("reviver")
    assert palindrome("refer")
def test_palindrome_non_string():
    with pytest.raises(TypeError):
        palindrome(10)
    with pytest.raises(TypeError):
        palindrome(5.3)
    with pytest.raises(TypeError):
        palindrome(False)