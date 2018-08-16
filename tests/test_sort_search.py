from algo import sort_search as ss


def test_merge():
    assert ss.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
