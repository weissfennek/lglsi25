from bubble_sort import bubble_sort

def test_bubble_sort():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([5, 3, 8, 6, 2]) == [2, 3, 5, 6, 8]
