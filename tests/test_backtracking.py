from algo import backtracking as bt


def test_coinChangeTotal():
    assert bt.coinChangeTotalStack([1, 2], 4) == 2
    assert bt.coinChangeTotalStack([1, 2, 5], 11) == 3


def test_generateParenthesis():
    assert bt.generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]


# def test_permute():
#     assert bt.permute([1, 2, 3]) == [
#         [1, 2, 3],
#         [1, 3, 2],
#         [2, 1, 3],
#         [2, 3, 1],
#         [3, 1, 2],
#         [3, 2, 1],
#     ]
