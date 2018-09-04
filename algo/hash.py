import collections
import itertools
import heapq
from algo.util import partition


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    seen = set()
    for item in nums:
        if item in seen:
            seen.remove(item)
        else:
            seen.add(item)

    return list(seen)[0]


def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    set1, set2 = set(nums1), set()
    for item in nums2:
        if item in set1:
            set2.add(item)

    result = list(set2)
    result.sort()
    return result


def intersect(nums1, nums2):
    """
    Given two arrays, write a function to compute their intersection.

    Note:
        1. Each element in the result should appear as many times as
            it shows in both arrays.
        2. The result can be in any order.

    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    dic1 = collections.defaultdict(list)  # defaults to list
    for num in nums1:
        dic1[num].append(num)

    dic2 = collections.defaultdict(list)  # defaults to list
    for num in nums2:
        if num in dic1:
            dic2[num] += dic1[num]

    return list(itertools.chain(*dic2.values()))


def isHappy(n):
    """
    Write an algorithm to determine if a number is "happy".

    A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the
    sum of the squares of its digits, and repeat the process until
    the number equals 1 (where it will stay), or it loops endlessly
    in a cycle which does not include 1. Those numbers for which
    this process ends in 1 are happy numbers.

    :type n: int
    :rtype: bool
    """

    def get_square_sum(num):
        square_sum = 0
        for i in map(int, str(n)):
            square_sum += i ** 2
        return square_sum

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_square_sum(n)

    return n == 1


def twoSum(nums, target):
    """
    Given an array of integers, return indices of the two numbers
    such that they add up to a specific target.

    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dic = collections.defaultdict(list)  # defaults to list
    for idx, num in enumerate(nums):
        dic[num].append(idx)

    for num in nums:
        left = target - num
        if left == num and len(dic[num]) > 1:
            return dic[num]
        elif left != num and left in dic:
            return dic[num] + dic[left]


def twoSum_2(nums, target):
    """
    Given an array of integers, return indices of the two numbers
    such that they add up to a specific target.

    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dic = {}
    for idx, key in enumerate(nums):
        complement = target - key
        if complement in dic:
            return [dic[complement], idx]
        dic[key] = idx


def isIsomorphic(s, t):
    """
    Given two strings s and t, determine if they are isomorphic.

    Two strings are isomorphic if the characters in s can be replaced
    to get t.

    All occurrences of a character must be replaced with another
    character while preserving the order of characters.
    No two characters may map to the same character but a character
    may map to itself.

    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False

    dic1, dic2 = {}, {}
    for item1, item2 in zip(s, t):
        if item1 in dic1:
            if dic1[item1] != item2:
                return False
        else:
            dic1[item1] = item2

        if item2 in dic2:
            if dic2[item2] != item1:
                return False
        else:
            dic2[item2] = item1

    return True


def findRestaurant(list1, list2):
    """
     Suppose Andy and Doris want to choose a restaurant for dinner,
     and they both have a list of favorite restaurants represented
     by strings.

    You need to help them find out their common interest with the
    least list index sum. If there is a choice tie between answers,
    output all of them with no order requirement.

    You could assume there always exists an answer.

    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    dic1, dic2 = {}, {}

    for idx, item in enumerate(list1):
        dic1[item] = idx

    for idx, item in enumerate(list2):
        if item in dic1:
            dic2[item] = idx + dic1[item]

    minValue = min(dic2.values())
    return [key for key in dic2 if dic2[key] == minValue]


def firstUniqChar(s):
    """
    Given a string, find the first non-repeating character in it and
    return it's index. If it doesn't exist, return -1.

    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return -1

    dic = collections.defaultdict(list)
    for idx, char in enumerate(s):
        dic[char].append(idx)

    # v1
    # res = list(filter(lambda x: len(dic[x]) == 1, dic.keys()))
    # if len(res) > 0:
    #     min_key = min(res, key=lambda x: dic[x][0])
    #     return dic[min_key][0]

    # v2
    for idx, char in enumerate(s):
        if len(dic[char]) == 1:
            return idx

    return -1


def containsNearbyDuplicate(nums, k):
    """
    Given an array of integers and an integer k, find out whether
    there are two distinct indices i and j in the array such that
    nums[i] = nums[j] and the absolute difference between i and j
    is at most k.

    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    dic = collections.defaultdict(list)
    for idx, char in enumerate(nums):
        dic[char].append(idx)

    for val in filter(lambda x: len(x) > 1, dic.values()):
        for idxs in partition(val, 2, 1):
            if abs(idxs[0] - idxs[1]) <= k:
                return True

    return False


def numJewelsInStones(J, S):
    """
    You're given strings J representing the types of stones that
    are jewels, and S representing the stones you have.
    Each character in S is a type of stone you have.
    You want to know how many of the stones you have are also jewels.

    The letters in J are guaranteed distinct, and all characters
    in J and S are letters. Letters are case sensitive, so "a" is
    considered a different type of stone from "A".

    :type J: str
    :type S: str
    :rtype: int
    """
    count = 0
    counter = collections.Counter(J)
    for s in S:
        if counter[s] > 0:
            count += 1

    return count


def lengthOfLongestSubstring(s):
    """
    Given a string, find the length of the longest substring without
    repeating characters.

    Examples:
        Given "abcabcbb", the answer is "abc", which the length is 3.
        Given "bbbbb", the answer is "b", with the length of 1.
        Given "pwwkew", the answer is "wke", with the length of 3.
            Note that the answer must be a substring, "pwke" is a
            subsequence and not a substring.

    :type s: str
    :rtype: int
    """
    dic = {}
    counter = 0
    left = 0
    for right, char in enumerate(s):
        if char in dic:
            left = max(left, dic[char] + 1)
        counter = max(counter, right - left + 1)
        dic[char] = right

    return counter


def topKFrequent(nums, k):
    """
    Given a non-empty array of integers, return the k most frequent elements.

    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    heap = []
    dic = collections.defaultdict(lambda: 0)
    for num in nums:
        dic[num] += 1

    for key, val in dic.items():
        heapq.heappush(heap, (val, key))

    return [j for _, j in heapq.nlargest(k, heap)]
