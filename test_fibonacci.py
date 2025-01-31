import pytest
from fibonacci import fibonacci

def test_fibonacci_positive():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(10) == 55

def test_fibonacci_edge_cases():
    assert fibonacci(1) == 1  # Test for the first number
    assert fibonacci(2) == 1  # Test for the second number
    assert fibonacci(3) == 2  # Test for the third number

def test_fibonacci_invalid_input():
    with pytest.raises(ValueError):
        fibonacci(-1)  # Test for negative input
    with pytest.raises(ValueError):
        fibonacci(-5)  # Test for negative input

def test_fibonacci_large_input():
    assert fibonacci(20) == 6765 # Test for a somewhat larger input, but not excessively large
    assert fibonacci(30) == 832040 # Test for a somewhat larger input, but not excessively large