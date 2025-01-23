# test_bubbleSort.py
from bubbleSort import bubble_sort

def test_sorted_list():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]

def test_unsorted_list():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]

def test_empty_list():
    assert bubble_sort([]) == []
