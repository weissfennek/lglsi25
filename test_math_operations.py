# test_math_operations.py
import pytest
from math_operations import add, divide

# Test add function
def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(0, 0) == 0
    assert add(-5, -5) == -10

# Test divide function
def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    assert divide(-6, 2) == -3
    assert divide(-6, -2) == 3

# Edge case: testing divide by zero
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

# Test divide with float values
def test_divide_with_floats():
    assert divide(5.5, 2) == 2.75
    assert divide(9.5, 2) == 4.75
