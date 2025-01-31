import pytest
from bubbleSort_hiba import bubble_sort1

def test_bubble_sort():
    assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert bubble_sort([3, 0, -1, 10]) == [-1, 0, 3, 10]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([2, 1]) == [1, 2]

if __name__ == "__main__":
    pytest.main()
