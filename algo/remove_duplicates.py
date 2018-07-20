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
