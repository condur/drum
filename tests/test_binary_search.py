from algo import binary_search


def test_search():
    assert binary_search.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binary_search.search([2, 5], 2) == 0
    assert binary_search.search([5], 5) == 0
    assert binary_search.search([-1, 0, 5], 5) == 2


def test_mySqrt():
    assert binary_search.mySqrt(4) == 2
    assert binary_search.mySqrt(8) == 2


def test_findPeakElement():
    assert binary_search.findPeakElement_template_III([1, 2, 3, 1]) == 2
    assert binary_search.findPeakElement_template_III([1, 2, 1, 3, 5, 6, 4]) == 5
    assert binary_search.findPeakElement_template_III([2, 1]) == 0


def test_searchRange():
    assert binary_search.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert binary_search.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert binary_search.searchRange([1, 1, 2], 1) == [0, 1]


def test_isPerfectSquare():
    assert binary_search.isPerfectSquare(16) is True
    assert binary_search.isPerfectSquare(14) is False


def test_nextGreatestLetter():
    assert binary_search.nextGreatestLetter(["c", "f", "j"], "c") == "f"
    assert binary_search.nextGreatestLetter(["c", "f", "j"], "a") == "c"
    assert binary_search.nextGreatestLetter(["c", "f", "j"], "d") == "f"
    assert binary_search.nextGreatestLetter(["c", "f", "j"], "g") == "j"
    assert binary_search.nextGreatestLetter(["c", "f", "j"], "j") == "c"
    assert binary_search.nextGreatestLetter(["c", "f", "j"], "k") == "c"
    assert (
        binary_search.nextGreatestLetter(
            ["e", "e", "e", "k", "q", "q", "q", "v", "v", "y"], "k"
        )
        == "q"
    )
    assert (
        binary_search.nextGreatestLetter(
            ["e", "e", "e", "k", "q", "q", "q", "v", "v", "y"], "q"
        )
        == "v"
    )
    assert (
        binary_search.nextGreatestLetter(
            ["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], "e"
        )
        == "n"
    )
    assert (
        binary_search.nextGreatestLetter(
            ["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], "n"
        )
        == "e"
    )


def test_findMin():
    assert binary_search.findMin([3, 4, 5, 1, 2]) == 1
    assert binary_search.findMin([2, 2, 2, 0, 1]) == 0
