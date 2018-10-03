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
