# test_factorial.py
import pytest
from factorial import factorial


def test_factorial_positive():
    assert factorial(5) == 120
    assert factorial(3) == 6
    assert factorial(1) == 1
    assert factorial(0) == 1


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)


def test_factorial_large_number():
    assert factorial(10) == 3628800


def test_factorial_non_int():
    with pytest.raises(TypeError):
        factorial(3.5)
    with pytest.raises(TypeError):
        factorial("string")
    with pytest.raises(TypeError):
        factorial([1, 2, 3])
