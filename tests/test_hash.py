from algo import hash


def test_containsDuplicate():
    assert hash.containsDuplicate([1, 2, 3, 1]) is True


def test_singleNumber():
    assert hash.singleNumber([2, 2, 1]) == 1


def test_intersection():
    assert hash.intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]


def test_isHappy():
    assert hash.isHappy(19) is True


def test_twoSum():
    assert hash.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert hash.twoSum([3, 2, 4], 6) == [1, 2]
    assert hash.twoSum([3, 3], 6) == [0, 1]

    assert hash.twoSum_2([2, 7, 11, 15], 9) == [0, 1]
    assert hash.twoSum_2([3, 2, 4], 6) == [1, 2]
    assert hash.twoSum_2([3, 3], 6) == [0, 1]
