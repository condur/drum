from algo import dynamic_programming as dp


def test_rob():
    assert dp.rob_top_down([1, 2, 3, 1]) == 4
    assert dp.rob_bottom_up([1, 2, 3, 1]) == 4
