#!/usr/bin/python3


def increment(nums):
    carry = 1
    for item in nums[::-1]:
        item = item + carry
        if item >= 10:
            item = item - 10
            carry = 1
        else:
            carry = 0
        yield item


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_diff = 0
    for price in prices:
        for second_price in prices:
            if max_diff < (second_price - price):
                max_diff = second_price - price
                print(price, second_price, max_diff)

    return max_diff


def main():
    ss = {"a", "b", "c", "c"}
    print(ss)
    pass


if __name__ == "__main__":
    main()
