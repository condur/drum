import random


def merge(nums1, m, nums2, n):
    """
    Given two sorted integer arrays nums1 and nums2, merge nums2
    into nums1 as one sorted array.

    Note:
        1. The number of elements initialized in nums1 and nums2
            are m and n respectively.
        2. You may assume that nums1 has enough space (size that
            is greater or equal to m + n) to hold additional
            elements from nums2.

    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """

    for i in range(n):  # nums2 loop
        for j in range(m + i + 1):  # nums1 loop
            if nums2[i] >= nums1[j] and j < m + i:  # skip except the last
                continue
            else:
                for k in range(m + i, j, -1):
                    nums1[k] = nums1[k - 1]
                nums1[j] = nums2[i]
                break
            nums1[m + i] = nums2[i]

    return nums1


def quicksort(values):
    """Quick sort"""

    def _partition(values, left, right, pivotidx):
        """In place paritioning from left to right using the element at
           pivotidx as the pivot. Returns the new pivot position."""

        pivot = values[pivotidx]
        # swap pivot and the last element
        values[right], values[pivotidx] = values[pivotidx], values[right]

        storeidx = left
        for idx in range(left, right):
            if values[idx] < pivot:
                values[idx], values[storeidx] = values[storeidx], values[idx]
                storeidx += 1

        # move pivot to the proper place
        values[storeidx], values[right] = values[right], values[storeidx]
        return storeidx

    def _doquicksort(values, left, right):
        if left < right:
            pivotidx = random.randint(left, right)  # random pivot
            pivotidx = _partition(values, left, right, pivotidx)
            _doquicksort(values, left, pivotidx)
            _doquicksort(values, pivotidx + 1, right)

        return values

    return _doquicksort(values, 0, len(values) - 1)


def findKthLargest(nums, k):
    """
    Find the kth largest element in an unsorted array.
    Note that it is the kth largest element in the sorted order,
    not the kth distinct element.

    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    def _partition(nums, left, right, pivotidx):
        """In place paritioning from left to right using the element at
           pivotidx as the pivot. Returns the new pivot position."""

        pivot = nums[pivotidx]
        # swap pivot and the last element
        nums[right], nums[pivotidx] = nums[pivotidx], nums[right]

        storeidx = left
        for idx in range(left, right):
            if nums[idx] < pivot:
                nums[idx], nums[storeidx] = nums[storeidx], nums[idx]
                storeidx += 1

        # move pivot to the proper place
        nums[storeidx], nums[right] = nums[right], nums[storeidx]
        return storeidx

    def _findKthSmallest(nums, k, left, right):
        if left < right:
            pivotidx = random.randint(left, right)  # random pivot
            pivotidx = _partition(nums, left, right, pivotidx)
            if pivotidx > k:
                return _findKthSmallest(nums, k, left, pivotidx)
            elif pivotidx < k:
                return _findKthSmallest(nums, k, pivotidx + 1, right)
            else:
                return nums[pivotidx]

    res = _findKthSmallest(nums, len(nums) - k, 0, len(nums) - 1)
    if res is not None:
        return res

    # the list is already sorted
    return nums[len(nums) - k]
