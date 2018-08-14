

# Template I
def binarySearch_template_I(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1


# Template II
def binarySearch_template_II(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if left != len(nums) and nums[left] == target:
        return left
    return -1


# Template II
def binarySearch_template_III(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1


def search(nums, target):
    """
    Given a sorted (in ascending order) integer array nums of
    n elements and a target value, write a function to search
    target in nums. If target exists, then return its index,
    otherwise return -1.

    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0 or x == 1:
        return x

    precision = 1e-5
    left, right = 0, x
    mid = 0
    while abs(left - right) > precision:
        mid = left + (right - left) / 2
        mid_square = int(mid ** 2)
        if mid_square == x:
            break
        elif mid_square < x:
            left = mid
        else:
            right = mid

    return int(mid)


def findPeakElement_template_III(nums):
    """
    A peak element is an element that is greater than its neighbors.

    Given an input array nums, where nums[i] ≠ nums[i+1],
    find a peak element and return its index.

    The array may contain multiple peaks, in that case return the
    index to any one of the peaks is fine.

    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid - 1] > nums[mid]:
            right = mid
        else:
            left = mid

    return left if nums[left] > nums[right] else right


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    left, right = 0, len(nums) - 1
    idx_target = None
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            idx_target = mid
            break
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if idx_target is not None:
        start, end = idx_target, idx_target
        for i in range(idx_target - 1, -1, -1):
            if nums[i] == target:
                start = i
            else:
                break

        for i in range(idx_target + 1, len(nums)):
            if nums[i] == target:
                end = i
            else:
                break

        return [start, end]

    return [-1, -1]


def isPerfectSquare(num):
    """
    Given a positive integer num, write a function which
    returns True if num is a perfect square else False.

    :type num: int
    :rtype: bool
    """
    left, right = 0, num
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            left = mid + 1
        else:
            right = mid - 1

    return False


def nextGreatestLetter_II(letters, target):
    """
    Given a list of sorted characters letters containing
    only lowercase letters, and given a target letter target,
    find the smallest element in the list that is larger than
    the given target.

    Letters also wrap around. For example, if the target is
    target = 'z' and letters = ['a', 'b'], the answer is 'a'.

    :type letters: List[str]
    :type target: str
    :rtype: str
    """
    if target >= letters[-1]:
        return letters[0]

    left, right = 0, len(letters)
    while left < right:
        mid = left + (right - left) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return letters[left]


def nextGreatestLetter(letters, target):
    """
     Given a list of sorted characters letters containing
     only lowercase letters, and given a target letter target,
     find the smallest element in the list that is larger than
     the given target.

    Letters also wrap around. For example, if the target is
    target = 'z' and letters = ['a', 'b'], the answer is 'a'.

    :type letters: List[str]
    :type target: str
    :rtype: str
    """
    if target >= letters[-1]:
        return letters[0]

    left, right = 0, len(letters) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if letters[mid] <= target:
            left = mid
        else:
            right = mid

    if target < letters[left]:
        return letters[left]

    return letters[right]


def findMin(nums):
    """
    Suppose an array sorted in ascending order is rotated at some
    pivot unknown to you beforehand.

    (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

    Find the minimum element.

    You may assume no duplicate exists in the array.
    :type nums: List[int]
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]
