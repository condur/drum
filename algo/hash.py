def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    s = set()
    for _, item in enumerate(nums):
        if item in s:
            return True
        s.add(item)

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
            square_sum += pow(i, 2)
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
    dic = {}
    for idx, num in enumerate(nums):
        if num in dic:
            li = dic[num]
            li.append(idx)
            dic[num] = li
        else:
            dic[num] = [idx]

    for num in nums:
        left = target - num
        if left == num and len(dic[num]) > 1:
            return dic[num]
        elif left != num and left in dic:
            return dic[num] + dic[left]

    return []


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
        if complement in dic.keys():
            return [dic[complement], idx]
        dic[key] = idx
