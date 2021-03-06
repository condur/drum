import collections
import itertools
import random
from algo.util import partition


def remove_duplicates(nums) -> int:
    """
    Remove Duplicates from Sorted Array

    Given a sorted array nums, remove the duplicates
    in-place such that each element appear only once
    and return the new size.

    Args:
        nums: List[int]

    Returns:
        lindex: int
    """
    if len(nums) == 0:
        return 0

    left = 0
    for right in range(len(nums)):
        if left == right or nums[left] == nums[right]:
            continue
        else:
            left += 1
            nums[left] = nums[right]
    return left + 1


def pivotIndex(nums) -> int:
    """
    Given an array of integers nums, write a
    method that returns the "pivot" index of this array.

    We define the pivot index as the index where the sum of
    the numbers to the left of the index is equal to the sum of
    the numbers to the right of the index.

    If no such index exists, we should return -1.
    If there are multiple pivot indexes, you should return the left-most
    pivot index.

    :type nums: List[int]
    :rtype: int
    """
    sum_so_far, sum_nums = 0, sum(nums)
    for idx, item in enumerate(nums):
        if sum_nums - item - sum_so_far == sum_so_far:
            return idx
        sum_so_far += item
    return -1


def dominantIndex(nums):
    """
    In a given integer array nums, there is always exactly one largest
    element.

    Find whether the largest element in the array is at least twice as
    much as every other number in the array.

    If it is, return the index of the largest element, otherwise return -1.

    Note:

        1. nums will have a length in the range [1, 50].
        2. Every nums[i] will be an integer in the range [0, 99].

    :type nums: List[int]
    :rtype: int
    """
    max_first, max_second, idx_max_first = -1, -1, -1
    for idx, item in enumerate(nums):
        if item > max_first:
            max_second = max_first
            idx_max_first, max_first = idx, item
        elif item > max_second and item != max_first:
            max_second = item

    if max_first >= max_second * 2:
        return idx_max_first

    return -1


def plusOne(digits):
    """
    Given a non-empty array of digits representing a non-negative integer,
    plus one to the integer.

    The digits are stored such that the most significant digit is at the
    head of the list, and each element in the array contain a single digit.

    You may assume the integer does not contain any leading zero,
    except the number 0 itself.

    :type digits: List[int]
    :rtype: List[int]
    """
    increment_by = 1
    for idx in range(len(digits) - 1, -1, -1):
        incremented = digits[idx] + increment_by
        digits[idx] = incremented % 10
        increment_by = incremented // 10
        if increment_by == 0:
            break

    if increment_by > 0:
        digits.insert(0, increment_by)

    return digits


def strStr(haystack, needle) -> int:
    """
    Return the index of the first occurrence of
    needle in haystack, or -1 if needle is not part of haystack.

    For the purpose of this problem, we will return 0 when
    needle is an empty string.

    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(needle) == 0:
        return 0

    for idx, item in enumerate(partition(haystack, len(needle), 1)):
        if "".join(item) == needle:
            return idx
    return -1


def longestCommonPrefix(strs):
    """
    Write a function to find the longest common prefix string amongst
    an array of strings.

    If there is no common prefix, return an empty string "".

    :type strs: List[str]
    :rtype: str
    """
    res = []
    for items in zip(*strs):
        if items.count(items[0]) == len(items):
            res.append(items[0])
        else:
            break
    return "".join(res)


def twoSum(numbers, target):
    """
    Given an array of integers that is already sorted in ascending order,
    find two numbers such that they add up to a specific target number.

    The function twoSum should return indices of the two numbers such that
    they add up to the target, where index1 must be less than index2.

    Note:

        1. Your returned answers (both index1 and index2) are not
            zero-based.
        2. You may assume that each input would have exactly one solution
            and you may not use the same element twice.

    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        two_sum = numbers[left] + numbers[right]
        if two_sum < target:
            left += 1
        elif two_sum > target:
            right -= 1
        elif two_sum == target:
            break

    return [left, right]


def removeElement(nums, val):
    """
    Given an array nums and a value val, remove all instances of that
    value in-place and return the new length.

    Do not allocate extra space for another array, you must do this
    by modifying the input array in-place with O(1) extra memory.

    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    left = 0
    for right in nums:
        if right != val:
            nums[left] = right
            left += 1

    return left


def findMaxConsecutiveOnes(nums):
    """
    Given a binary array, find the maximum number of consecutive 1s
    n this array.

    Note:

        1. The input array will only contain 0 and 1.
        2. The length of input array is a positive integer and will
            not exceed 10,000

    :type nums: List[int]
    :rtype: int
    """
    left, max_1s = -1, 0
    for right in range(len(nums)):
        if nums[right] != 1:
            max_1s = max(max_1s, right - left - 1)
            left = right
        elif right == len(nums) - 1:  # the last item in the list
            max_1s = max(max_1s, right - left)

    return max_1s


def minSubArrayLen(s, nums):
    """
    Given an array of n positive integers and a positive integer s,
    find the minimal length of a contiguous subarray of which the sum ≥ s.
    If there isn't one, return 0 instead.

    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0

    left, curr_sum, min_in = 0, 0, float("inf")
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum >= s:
            min_in = min(min_in, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    min_in = 0 if min_in == float("inf") else min_in
    return min_in


def maxSubArray(nums):
    """
    Given an integer array nums, find the contiguous subarray
    (containing at least one number) which has the largest sum
    and return its sum.

    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    max_ending_here = max_so_far = nums[0]

    for n in nums[1:]:
        max_so_far = max(n, max_so_far + n)
        max_ending_here = max(max_so_far, max_ending_here)

    return max_ending_here


def rotate(nums, k):
    """
    Given an array, rotate the array to the right by k steps,
    where k is non-negative.

    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    d = collections.deque(nums)
    d.rotate(k)
    return list(d)


def rotate_2(nums, k):
    """
    Given an array, rotate the array to the right by k steps,
    where k is non-negative.

    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    for _ in range(k):
        nums.insert(0, nums.pop())
    return nums


def rotate_3(nums, k):
    """
    Given an array, rotate the array to the right by k steps,
    where k is non-negative.

    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    k = -(k % len(nums))
    nums = nums[k:] + nums[:k]
    return nums


def rotate_4(nums, k):
    """
    Given an array, rotate the array to the right by k steps,
    where k is non-negative.

    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    k = k % len(nums)
    if k == 0:
        return

    def calculate_next(curr, k, n):
        next = curr + k
        if next >= n:
            next = next - n
        return next

    curr = 0
    curr_value = nums[curr]
    next = curr + k
    items = {curr}
    for _ in range(len(nums)):
        nums[next], curr_value = curr_value, nums[next]
        curr = next

        if curr in items:
            curr += 1
            curr_value = nums[curr]
        items.add(curr)

        next = calculate_next(curr, k, len(nums))
    return nums


def getPascalTriangleRow(rowIndex):
    """
    Given a non-negative index k where k ≤ 33, return the kth index
    row of the Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers
    directly above it.

    Note that the row index starts from 0.

    :type rowIndex: int
    :rtype: List[int]
    """
    deque = collections.deque([1])
    for _ in range(rowIndex):
        for _ in range(len(deque) - 1):
            deque.appendleft(deque.pop() + deque[-1])
        deque.appendleft(1)
    return list(deque)


def generatePascalTriangle(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    result = []
    if numRows == 0:
        return result

    deque = collections.deque([1])
    result.append(list(deque))
    for _ in range(numRows - 1):
        for _ in range(len(deque) - 1):
            deque.appendleft(deque.pop() + deque[-1])
        deque.appendleft(1)
        result.append(list(deque))

    return result


def reverseWords(s):
    """
    Given an input string, reverse the string word by word.

    Note:

    1.A word is defined as a sequence of non-space characters.
    2.Input string may contain leading or trailing spaces. However,
        your reversed string should not contain leading or trailing spaces.
    3.You need to reduce multiple spaces between two words to a single
        space in the reversed string.

    :type s: str
    :rtype: str
    """
    return " ".join(reversed(s.split()))


def reverseWords_2(s):
    """
    Given a string, you need to reverse the order of characters in each
    word within a sentence while still preserving whitespace and initial
    word order.

    :type s: str
    :rtype: str
    """
    words = s.split()
    for idx, word in enumerate(words):
        words[idx] = word[::-1]

    return " ".join(words)


def moveZeroes(nums):
    """
    Given an array nums, write a function to move all 0's to the end
    of it while maintaining the relative order of the non-zero elements.

    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    left = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            continue
        else:
            nums[left] = nums[right]
            left += 1

    for idx in range(left, len(nums)):
        nums[idx] = 0

    return nums


def reverse(x):
    """
    Given a 32-bit signed integer, reverse digits of an integer.

    :type x: int
    :rtype: int
    """
    s = str(x)
    if len(s) == 1:
        return x

    res = []
    if x < 0:
        res.append("-")
        res.extend(s[::-1])
        res.pop()
    else:
        res = s[::-1]

    reversed = int("".join(res))
    if -2 ** 31 <= reversed <= 2 ** 31 - 1:
        return reversed

    return 0


def isAnagram(s, t):
    """
    Given two strings s and t , write a function to determine
    if t is an anagram of s.

    An anagram is a word or phrase formed by rearranging the
    letters of a different word or phrase, typically using all
    the original letters exactly once.

    :type s: str
    :type t: str
    :rtype: bool
    """
    dic = collections.defaultdict(lambda: 0)
    for i in s:
        dic[i] += 1

    for j in t:
        if j not in dic:
            return False
        else:
            dic[j] -= 1

    return all(val == 0 for val in dic.values())


def isPalindrome(s):
    """
    Given a string, determine if it is a palindrome, considering
    only alphanumeric characters and ignoring cases.

    Note: For the purpose of this problem, we define empty string
    as valid palindrome.

    :type s: str
    :rtype: bool
    """

    str1 = filter(lambda x: x.isalnum(), s)
    str2 = filter(lambda x: x.isalnum(), s[::-1])

    return all(s1.lower() == s2.lower() for s1, s2 in zip(str1, str2))


def longestPalindrome(s):
    """
    Given a string s, find the longest palindromic substring in s.
    You may assume that the maximum length of s is 1000.

    :type s: str
    :rtype: str
    """

    def isPalindrom(s, left, right):
        str1 = s[left : right + 1]
        str2 = s[right : left + 1 : -1]
        return all(s1 == s2 for s1, s2 in zip(str1, str2))

    dic = collections.defaultdict(list)
    for idx, char in enumerate(s):
        dic[char].append(idx)

    max_length, max_start, max_end = 0, 0, 0
    for char, idxs in filter(lambda item: len(item[1]) > 1, dic.items()):
        for start in idxs:
            for end in idxs:
                if start != end and isPalindrom(s, start, end):
                    if end - start > max_length:
                        max_length = end - start
                        max_start = start
                        max_end = end + 1

    return s[0] if max_length == 0 else s[max_start:max_end]


def myAtoi(str):
    """
    Implement atoi which converts a string to an integer.

    The function first discards as many whitespace characters
    as necessary until the first non-whitespace character is found.
    Then, starting from this character, takes an optional initial
    plus or minus sign followed by as many numerical digits as
    possible, and interprets them as a numerical value.

    The string can contain additional characters after those
    that form the integral number, which are ignored and have
    no effect on the behavior of this function.

    If the first sequence of non-whitespace characters in str
    is not a valid integral number, or if no such sequence
    exists because either str is empty or it contains only
    whitespace characters, no conversion is performed.

    If no valid conversion could be performed, a zero value is returned.

    :type str: str
    :rtype: int
    """
    str = str.lstrip()
    if len(str) == 0:
        return 0

    signs = list(itertools.takewhile(lambda x: x == "-" or x == "+", str))
    if len(signs) > 1:
        return 0

    if len(signs) > 0 and (signs[0] == "-" or signs[0] == "+"):  # signed
        digits = list(itertools.takewhile(lambda x: x.isdigit(), str[1:]))
    else:
        digits = list(itertools.takewhile(lambda x: x.isdigit(), str))

    if len(digits) == 0:
        return 0

    num = (
        -1 * int("".join(digits))
        if len(signs) == 1 and signs[0] == "-"  # negative number
        else int("".join(digits))
    )

    if num < -2 ** 31:
        return -2 ** 31
    elif num > 2 ** 31 - 1:
        return 2 ** 31 - 1
    else:
        return num


def missingNumber(nums):
    """
    Given an array containing n distinct numbers taken
    from 0, 1, 2, ..., n, find the one that is missing from the array.

    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    sum_formula = (n * (n + 1)) // 2
    return sum_formula - sum(nums)


def fibonacci():
    """
    Fibonacci Sequence
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def shuffle(n):
    """
    Input a single integer N. Output the integers 1..N in random order.
    """
    # if it's 0 or 1 items
    if n <= 1:
        return [n]

    # generate the list 1..N
    the_list = []
    for i in range(1, n + 1):
        the_list.append(i)

    # loop through list indexes
    for i in range(0, n):
        # choose a random not-yet-placed item to place there
        # (could also be the item currently in that spot)
        # must be an item AFTER the current item, because the numbers
        # before has all already been placed
        random_index = random.randrange(i, n)
        # place the random choice in the spot by swapping
        if random_index != i:
            the_list[i], the_list[random_index] = the_list[random_index], the_list[i]

    return the_list


def setZeroes(matrix):
    """
    Given a m x n matrix, if an element is 0, set its entire
    row and column to 0. Do it in-place.

    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    row_len = len(matrix)
    col_len = len(matrix[0])

    first_row = [None] * row_len
    first_col = [None] * col_len

    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == 0:
                first_row[i] = 0
                first_col[j] = 0

    for i in range(row_len):
        for j in range(col_len):
            if first_row[i] == 0 or first_col[j] == 0:
                matrix[i][j] = 0

    return matrix
