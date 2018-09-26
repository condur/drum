def coinChangeTotalStack(coins, amount):
    """
    You are given coins of different denominations and a total amount
    of money amount. Write a function to compute the total number of
    variations that are valid.

    :type coins: List[int]
    :type amount: int
    :rtype: int
    """

    # def combo(currentAmount, currentCoin, solutions):
    #     if currentAmount == 0:
    #         return 1
    #     elif currentAmount < 0:
    #         return 0
    #     else:
    #         nCombos = 0
    #         coin = currentCoin
    #         while coin < len(coins):
    #             # solutions.append(coins[coin])
    #             solution = combo(currentAmount - coins[coin], coin, solutions)
    #             # if currentAmount - coins[coin] == 0:
    #                # print(solutions)
    #                 # solutions.pop()
    #             nCombos += solution
    #             coin += 1
    #         return nCombos

    def combo(amount):
        stack = [(amount, 0)]  # amount, coin index
        while stack:
            current_amount, coin = stack[-1]
            while current_amount > 0:
                current_amount = current_amount - coins[coin]
                stack.append((current_amount, coin))

            if current_amount == 0:  # success leaf
                yield [coin + 1 for _, coin in stack[1:]]  # return the result

            _, coin = stack.pop()
            coin += 1

            while stack and coin >= len(coins):  # backtrack
                _, coin = stack.pop()
                coin += 1

            if stack:  # get the next
                current_amount, _ = stack[-1]
                stack.append((current_amount - coins[coin], coin))

    return min([len(x) for x in combo(amount)])


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
