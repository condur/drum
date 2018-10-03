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


def generateParenthesis(n):
    """
    Given n pairs of parentheses, write a function to generate all
    combinations of well-formed parentheses. 
    
    :type n: int
    :rtype: List[str]
    """

    def _backtrack(stack, n):
        if stack:
            _, last_opened, _, = stack.pop()
            if stack:
                _, next_to_open, next_to_close = stack[-1]
                while stack and last_opened == next_to_open:
                    _, last_opened, _, = stack.pop()
                    if stack:
                        _, next_to_open, next_to_close = stack[-1]

                if next_to_close == n:
                    _backtrack(stack, n)

                if next_to_close == next_to_open:
                    _backtrack(stack, n)

    def _generateParenthesis(n):
        open_par, closed_par = "(", ")"
        stack = [(open_par, 1, 0)]
        while stack:
            # add opened parentheses
            _, opened, closed = stack[-1]
            while opened < n:
                opened += 1
                stack.append((open_par, opened, closed))

            # validate the success leaf
            _, opened, closed = stack[-1]
            if opened == n and closed == n:
                yield "".join([par for par, _, _ in stack])

            # backtrack
            if closed == n:
                _backtrack(stack, n)

            # add closed parenthesis
            if stack:
                _, opened, closed = stack[-1]
                stack.append((closed_par, opened, closed + 1))

    return list(_generateParenthesis(n))


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
