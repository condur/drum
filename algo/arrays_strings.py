import sys
import itertools


def remove_duplicates(nums):
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
    lindex = 0
    for index, _ in enumerate(nums):
        if nums[lindex] == nums[index]:
            continue
        else:
            lindex += 1
            nums[lindex] = nums[index]
    return lindex + 1


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
        increment_by = incremented // 10
        digits[idx] = incremented % 10

    if increment_by > 0:
        digits.insert(0, increment_by)

    return digits


def partition(iterable, step, pad=0):
    """
    Returns a lazy sequence of lists of n items each, at offsets
    step apart. If step is not supplied, defaults to n, i.e.
    the partitions do not overlap. If a pad collection is supplied,
    use its elements as necessary to complete last partition upto
    n items. In case there are not enough padding elements, return
    a partition with less than n items.
    """
    pad = step if pad == 0 else pad
    start, stop = 0, step
    item = list(itertools.islice(iterable, start, stop))
    while item:
        yield item
        start, stop = start + pad, stop + pad
        item = list(itertools.islice(iterable, start, stop))


def strStr(haystack, needle):
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

    index = 0
    for item in partition(haystack, len(needle), 1):
        if "".join(item) == needle:
            return index
        index += 1
    return -1


def longestCommonPrefix(strs):
    """
    Write a function to find the longest common prefix string amongst
    an array of strings.

    If there is no common prefix, return an empty string "".

    :type strs: List[str]
    :rtype: str
    """
    coll = []
    for items in zip(*strs):
        if items.count(items[0]) == len(items):
            coll.append(items[0])
        else:
            break
    return "".join(coll)


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
    index1, index2 = 0, len(numbers) - 1
    while index1 < index2:
        if numbers[index1] + numbers[index2] < target:
            index1 += 1
        elif numbers[index1] + numbers[index2] > target:
            index2 -= 1
        elif numbers[index1] + numbers[index2] == target:
            break

    return [index1, index2]


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
    left_idx = 0
    for item in nums:
        if item != val:
            nums[left_idx] = item
            left_idx += 1

    return left_idx


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
    left_idx, max_1s = -1, 0
    for idx in range(len(nums)):
        if nums[idx] != 1:
            max_1s = max(max_1s, idx - left_idx - 1)
            left_idx = idx
        elif idx == len(nums) - 1:  # the last item in the list
            max_1s = max(max_1s, idx - left_idx)

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

    idx_begin, curr_sum, min_interval = 0, 0, sys.maxsize
    for idx_end, num in enumerate(nums):
        curr_sum += num
        while curr_sum >= s:
            min_interval = min(min_interval, idx_end - idx_begin + 1)
            curr_sum -= nums[idx_begin]
            idx_begin += 1

    min_interval = 0 if min_interval == sys.maxsize else min_interval
    return min_interval
