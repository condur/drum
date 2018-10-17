from algo import util


def test_partition():
    assert list(util.partition("hell", 2)) == [("h", "e"), ("l", "l")]
    assert list(util.partition("hell", 2, 1)) == [("h", "e"), ("e", "l"), ("l", "l")]


def test_shuffle():
    assert list(util.preudo_random_generator(10, 1))[0] <= 10
