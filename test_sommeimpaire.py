import pytest
from sommeimpaire import sum_odd

def test_sum_odd():
    assert sum_odd([1, 2, 3, 4, 5]) == 9
    assert sum_odd([10, 12, 14]) == 0
    assert sum_odd([1, 3, 5, 7, 9]) == 25
    assert sum_odd([-1, -2, -3, -4]) == -4
    assert sum_odd([0]) == 0