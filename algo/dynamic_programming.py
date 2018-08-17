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


def climbStairs_top_down(n):
    """
    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct
    ways can you climb to the top?

    Note: Given n will be a positive integer.

    This is like a Fibonacci sequence just is starting with 1, 2
    :type n: int
    :rtype: int
    """

    @functools.lru_cache()
    def climb(n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return climb(n - 1) + climb(n - 2)

    return climb(n)


def climbStairs_bottom_up(n):
    """
    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct
    ways can you climb to the top?

    Note: Given n will be a positive integer.

    This is like a Fibonacci sequence just is starting with 1, 2
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1

    tabu = [0] * (n + 1)
    tabu[1] = 1
    tabu[2] = 2
    for i in range(2, n):
        tabu[i + 1] = tabu[i] + tabu[i - 1]

    return tabu[-1]


def climbStairs_bottom_up_fib(n):
    """
    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct
    ways can you climb to the top?

    Note: Given n will be a positive integer.

    This is like a Fibonacci sequence just is starting with 1, 2
    :type n: int
    :rtype: int
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return b
