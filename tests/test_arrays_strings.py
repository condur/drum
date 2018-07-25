from algo import arrays_strings as ars


def test_pivot_index():
    assert ars.pivotIndex([1, 2, 3, 1]) == -1
    assert ars.pivotIndex([1, 7, 3, 6, 5, 6]) == 3


def test_domunant_index():
    assert ars.dominantIndex([2, 6, 3, 0]) == 1
    assert ars.dominantIndex([0, 0, 2, 3]) == -1
    assert ars.dominantIndex([3, 2, 0, 0]) == -1
    assert ars.dominantIndex([6, 2, 0, 0]) == 0
    assert ars.dominantIndex([1]) == 0
    assert ars.dominantIndex([1, 0]) == 0


def test_plus_one():
    assert ars.plusOne([1, 2, 3, 1]) == [1, 2, 3, 2]
    assert ars.plusOne([1, 0, 0]) == [1, 0, 1]
    assert ars.plusOne([1, 0, 9]) == [1, 1, 0]
    assert ars.plusOne([9]) == [1, 0]


def test_partition():
    assert list(ars.partition("hell", 2)) == [["h", "e"], ["l", "l"]]


def test_strstr():
    assert ars.strStr("hello", "") == 0
    assert ars.strStr("hello", "e") == 1
    assert ars.strStr("hello", "ll") == 2
    assert ars.strStr("hello", "lo") == 3
    assert ars.strStr("hello", "o") == 4


def test_longest_common_prefix():
    assert ars.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert ars.longestCommonPrefix(["dog", "racecar", "car"]) == ""


def test_twoSum():
    assert ars.twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_removeElement():
    assert ars.removeElement([3, 2, 2, 3], 2) == 2
    assert ars.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
