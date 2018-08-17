from algo import dynamic_programming as dp


def test_rob():
    assert dp.rob_top_down([1, 2, 3, 1]) == 4
    assert dp.rob_bottom_up([1, 2, 3, 1]) == 4


def test_climbStairs():
    assert dp.climbStairs_top_down(2) == 2
    assert dp.climbStairs_top_down(3) == 3
    assert dp.climbStairs_bottom_up(1) == 1
    assert dp.climbStairs_bottom_up(2) == 2
    assert dp.climbStairs_bottom_up(3) == 3
    assert dp.climbStairs_bottom_up(5) == 8
    assert dp.climbStairs_bottom_up_fib(1) == 1
    assert dp.climbStairs_bottom_up_fib(2) == 2
    assert dp.climbStairs_bottom_up_fib(3) == 3
    assert dp.climbStairs_bottom_up_fib(5) == 8
