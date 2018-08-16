import functools


def rob_top_down(nums):
    """
    You are a professional robber planning to rob houses along
    a street. Each house has a certain amount of money stashed,
    the only constraint stopping you from robbing each of them
    is that adjacent houses have security system connected and
    it will automatically contact the police if two adjacent
    houses were broken into on the same night.

    Given a list of non-negative integers representing the amount
    of money of each house, determine the maximum amount of money
    you can rob tonight without alerting the police.

    :type nums: List[int]
    :rtype: int
    """

    @functools.lru_cache()
    def robbing(index):
        if index < 0:
            return 0
        return max(robbing(index - 2) + nums[index], robbing(index - 1))

    return robbing(len(nums) - 1)


def rob_bottom_up(nums):
    """
    You are a professional robber planning to rob houses along
    a street. Each house has a certain amount of money stashed,
    the only constraint stopping you from robbing each of them
    is that adjacent houses have security system connected and
    it will automatically contact the police if two adjacent
    houses were broken into on the same night.

    Given a list of non-negative integers representing the amount
    of money of each house, determine the maximum amount of money
    you can rob tonight without alerting the police.

    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    tabu = [0] * (len(nums) + 1)
    tabu[1] = nums[0]
    for i in range(1, len(nums)):
        tabu[i + 1] = max(tabu[i - 1] + nums[i], tabu[i])

    return tabu[-1]
