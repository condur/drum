from algo import sort_search as ss


def test_merge():
    assert ss.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]


def test_quicksort():
    assert ss.quicksort([3, 2, 1, 5, 6, 4]) == [1, 2, 3, 4, 5, 6]


def test_findKthLargest():
    assert ss.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert ss.findKthLargest([99, 99], 1) == 99


def test_merge_intervals():
    assert ss.merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]
    assert ss.merge_intervals([[1, 4], [2, 3]]) == [[1, 4]]


def test_searchMatrix():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert ss.searchMatrix(matrix, 12) is True
    assert ss.searchMatrix(matrix, 20) is False
    assert ss.searchMatrix([[1, 3, 5]], 2) is False
    assert ss.searchMatrix([[-5]], -5) is True
