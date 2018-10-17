from algo import arrays_strings as ars


def test_remove_duplicates():
    assert ars.remove_duplicates([7, 6, 4, 3, 1, 1]) == 5
    assert ars.remove_duplicates([7, 6, 4, 3, 3, 1]) == 5
    assert ars.remove_duplicates([7, 7, 4, 3, 3, 1]) == 4


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


def test_maxSubArray():
    assert ars.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_rotate():
    assert ars.rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert ars.rotate_2([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert ars.rotate_3([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert ars.rotate_4([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert ars.rotate_4([1, 2], 1) == [2, 1]
    assert ars.rotate_4([1, 2], 3) == [2, 1]
    assert ars.rotate_4([1, 2, 3, 4, 5, 6], 2) == [5, 6, 1, 2, 3, 4]
    assert ars.rotate_4([1, 2, 3, 4, 5, 6], 3) == [4, 5, 6, 1, 2, 3]


def test_get_pascal_trialge_row():
    assert ars.getPascalTriangleRow(0) == [1]
    assert ars.getPascalTriangleRow(1) == [1, 1]
    assert ars.getPascalTriangleRow(2) == [1, 2, 1]
    assert ars.getPascalTriangleRow(3) == [1, 3, 3, 1]
    assert ars.generatePascalTriangle(2) == [[1], [1, 1]]


def test_reverse_words():
    assert ars.reverseWords(" the  sky is blue ") == "blue is sky the"
    assert (
        ars.reverseWords_2("Let's take LeetCode contest")
        == "s'teL ekat edoCteeL tsetnoc"
    )


def test_moveZeroes():
    assert ars.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_reverse():
    assert ars.reverse(123) == 321
    assert ars.reverse(-123) == -321
    assert ars.reverse(120) == 21
    assert ars.reverse(-120) == -21
    assert ars.reverse(-1) == -1
    assert ars.reverse(1534236469) == 0


def test_isPalindrome():
    assert ars.isPalindrome("A man, a plan, a canal: Panama") is True


def test_longestPalindrome():
    assert ars.longestPalindrome("babad") == "bab"
    assert ars.longestPalindrome("ac") == "a"
    assert ars.longestPalindrome("ccc") == "ccc"


def test_myAtoi():
    assert ars.myAtoi("42") == 42
    assert ars.myAtoi("      -42") == -42
    assert ars.myAtoi("4193 with words") == 4193
    assert ars.myAtoi("words and 987") == 0
    assert ars.myAtoi("-") == 0
    assert ars.myAtoi("0-1") == 0
    assert ars.myAtoi("+1") == 1
    assert ars.myAtoi("+") == 0


def test_missingNumber():
    assert ars.missingNumber([3, 0, 1]) == 2
    assert ars.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert ars.missingNumber([0]) == 1
    assert ars.missingNumber([1, 2]) == 0
    assert ars.missingNumber([1]) == 0


def test_suffle():
    assert ars.shuffle(0) == [0]
    assert ars.shuffle(1) == [1]
    assert ars.shuffle(5) != [1, 2, 3, 4, 5]
    assert ars.shuffle(10) != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_setZeroes():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    assert ars.setZeroes(matrix) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
