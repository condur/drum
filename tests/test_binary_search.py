from algo import binary_search as bs


def test_search():
    assert bs.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert bs.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert bs.search([2, 5], 2) == 0
    assert bs.search([5], 5) == 0
    assert bs.search([-1, 0, 5], 5) == 2


def test_mySqrt():
    assert bs.mySqrt(4) == 2
    assert bs.mySqrt(8) == 2


def test_findPeakElement():
    assert bs.findPeakElement_template_III([1, 2, 3, 1]) == 2
    assert bs.findPeakElement_template_III([1, 2, 1, 3, 5, 6, 4]) == 5
    assert bs.findPeakElement_template_III([2, 1]) == 0


def test_searchRange():
    assert bs.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert bs.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert bs.searchRange([1, 1, 2], 1) == [0, 1]


def test_isPerfectSquare():
    assert bs.isPerfectSquare(16) is True
    assert bs.isPerfectSquare(14) is False


def test_nextGreatestLetter():
    assert bs.nextGreatestLetter(["c", "f", "j"], "c") == "f"
    assert bs.nextGreatestLetter(["c", "f", "j"], "a") == "c"
    assert bs.nextGreatestLetter(["c", "f", "j"], "d") == "f"
    assert bs.nextGreatestLetter(["c", "f", "j"], "g") == "j"
    assert bs.nextGreatestLetter(["c", "f", "j"], "j") == "c"
    assert bs.nextGreatestLetter(["c", "f", "j"], "k") == "c"
    assert (
        bs.nextGreatestLetter(["e", "e", "e", "k", "q", "q", "q", "v", "v", "y"], "k")
        == "q"
    )
    assert (
        bs.nextGreatestLetter(["e", "e", "e", "k", "q", "q", "q", "v", "v", "y"], "q")
        == "v"
    )
    assert (
        bs.nextGreatestLetter(["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], "e")
        == "n"
    )
    assert (
        bs.nextGreatestLetter(["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], "n")
        == "e"
    )


def test_findMin():
    assert bs.findMin([3, 4, 5, 1, 2]) == 1
    assert bs.findMin([2, 2, 2, 0, 1]) == 0
