from algo import sort_search as ss


def test_merge():
    assert ss.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]


def test_quicksort():
    assert ss.quicksort([3, 2, 1, 5, 6, 4]) == [1, 2, 3, 4, 5, 6]


def test_findKthLargest():
    assert ss.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert ss.findKthLargest([99, 99], 1) == 99
