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
