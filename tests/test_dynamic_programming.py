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


def test_increasingTriplet():
    assert dp.increasingTriplet_bottom_up([1, 2, 3, 4, 5]) is True
    assert dp.increasingTriplet_bottom_up([5, 4, 3, 2, 1]) is False
    assert dp.increasingTriplet_bottom_up([1, 0, 0, 10, 0, 0, 1000]) is True

    assert dp.increasingTriplet([1, 2, 3, 4, 5]) is True
    assert dp.increasingTriplet([5, 4, 3, 2, 1]) is False
    assert dp.increasingTriplet([1, 0, 0, 10, 0, 0, 1000]) is True
    assert dp.increasingTriplet([2, 1, 5, 0, 3]) is False


def test_canJump():
    assert dp.canJump_top_down([2, 3, 1, 1, 4]) is True
    assert dp.canJump_top_down([3, 2, 1, 0, 4]) is False
    assert dp.canJump_bottom_up([2, 3, 1, 1, 4]) is True
    assert dp.canJump_bottom_up([3, 2, 1, 0, 4]) is False


def test_lengthOFLIS():
    assert dp.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert dp.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
