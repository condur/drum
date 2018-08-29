from algo import backtracking as bt


# def test_permute():
#     assert len(list(bt.permute([1, 2, 3]))) == 6


def test_coinChangeTotal():
    assert bt.coinChangeTotalStack([1, 2], 4) == 2
    assert bt.coinChangeTotalStack([1, 2, 5], 11) == 3
