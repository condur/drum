from algo import arrays_strings as ars


def test_remove_duplicates():
    assert ars.remove_duplicates([7, 6, 4, 3, 1, 1]) == 5


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


def test_two_sum():
    assert ars.twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_remove_element():
    assert ars.removeElement([3, 2, 2, 3], 2) == 2
    assert ars.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5


def test_find_max_consecutive_ones():
    assert ars.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
    assert ars.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
    assert ars.findMaxConsecutiveOnes([1, 1, 0, 1]) == 2


def test_min_sub_array_len():
    assert ars.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert ars.minSubArrayLen(11, [1, 2, 3, 4, 5]) == 3