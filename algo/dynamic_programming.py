import functools
import sys


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


def increasingTriplet_bottom_up(nums):
    """
    Given an unsorted array return whether an increasing subsequence
    of length 3 exists or not in the array.

    Formally the function should:

        Return true if there exists i, j, k
        such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1
        else return false.

    Note: Your algorithm should run in O(n) time complexity and O(1)
    space complexity.

    :type nums: List[int]
    :rtype: bool
    """
    tabu = [False] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i - 1, -1, -1):
            if nums[i] > nums[j]:
                if tabu[j] is True:
                    return True
                tabu[i] = True

    return False


def increasingTriplet(nums):
    first = second = sys.maxsize
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False


def canJump_top_down(nums):
    """
    Given an array of non-negative integers, you are initially
    positioned at the first index of the array.

    Each element in the array represents your maximum jump length
    at that position.

    Determine if you are able to reach the last index.

    :type nums: List[int]
    :rtype: bool
    """

    @functools.lru_cache()
    def canJumpIdx(fromIdx, toIdx):
        if toIdx == 0:
            return nums[toIdx] >= fromIdx - toIdx

        if nums[toIdx] >= fromIdx - toIdx:
            return canJumpIdx(toIdx, toIdx - 1)
        else:
            return canJumpIdx(fromIdx, toIdx - 1)

    return canJumpIdx(len(nums) - 1, len(nums) - 2)


def coinChangeTotal(coins, amount):
    """
    You are given coins of different denominations and a total amount
    of money amount. Write a function to compute the total number of
    variations that are valid.

    :type coins: List[int]
    :type amount: int
    :rtype: int
    """

    # @functools.lru_cache()
    def combo(amount, currentCoin):
        if amount == 0:
            return 1
        elif amount < 0:
            return 0
        else:
            nCombos = 0
            coin = currentCoin
            while coin < len(coins):
                nCombos += combo(amount - coins[coin], coin)
                coin += 1
            return nCombos

        return combo(amount, 0)


def change_possibilities_bottom_up(amount, denominations):
    """
    You are given coins of different denominations and a total amount
    of money amount. Write a function to compute the total number of
    variations that are valid.

    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[
                higher_amount_remainder
            ]

    return ways_of_doing_n_cents[amount]
