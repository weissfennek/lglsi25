import pytest
from perfect import is_perfect  # Replace 'your_module' with the actual filename (without the .py extension)

def test_perfect_number():
    # Test known perfect numbers
    assert is_perfect(6) == True    # 6 is perfect
    assert is_perfect(28) == True   # 28 is perfect
    assert is_perfect(496) == True  # 496 is perfect

def test_non_perfect_number():
    # Test known non-perfect numbers
    assert is_perfect(1) == False   # 1 is not perfect
    assert is_perfect(10) == False  # 10 is not perfect
    assert is_perfect(12) == False  # 12 is not perfect
    assert is_perfect(100) == False # 100 is not perfect

def test_edge_cases():
    # Test edge cases
    assert is_perfect(0) == False   # 0 is not perfect
    assert is_perfect(-6) == False  # Negative numbers are not perfect
