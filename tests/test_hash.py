from algo import hash


def test_containsDuplicate():
    assert hash.containsDuplicate([1, 2, 3, 1]) is True


def test_singleNumber():
    assert hash.singleNumber([2, 2, 1]) == 1


def test_intersection():
    assert hash.intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]


def test_intersect():
    assert hash.intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]
    assert hash.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]


def test_isHappy():
    assert hash.isHappy(19) is True


def test_twoSum():
    assert hash.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert hash.twoSum([3, 2, 4], 6) == [1, 2]
    assert hash.twoSum([3, 3], 6) == [0, 1]

    assert hash.twoSum_2([2, 7, 11, 15], 9) == [0, 1]
    assert hash.twoSum_2([3, 2, 4], 6) == [1, 2]
    assert hash.twoSum_2([3, 3], 6) == [0, 1]


def test_isIsomorphic():
    assert hash.isIsomorphic("egg", "add") is True
    assert hash.isIsomorphic("foo", "bar") is False
    assert hash.isIsomorphic("ab", "aa") is False
    assert hash.isIsomorphic("ab", "ca") is True


def test_findRestaurant():
    assert hash.findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"],
    ) == ["Shogun"]

    assert hash.findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["KFC", "Shogun", "Burger King"],
    ) == ["Shogun"]


def test_firstUniqChar():
    assert hash.firstUniqChar("loveleetcode") == 2


def test_containsNearbyDuplicate():
    assert hash.containsNearbyDuplicate([1, 2, 3, 1], 3) is True
    assert hash.containsNearbyDuplicate([1, 0, 1, 1], 1) is True
    assert hash.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False


def test_numJewelsInStones():
    assert hash.numJewelsInStones("aA", "aAAbbbb") == 3


def test_lengthOfLongestSubstring():
    assert hash.lengthOfLongestSubstring("abcabcbb") == 3
    assert hash.lengthOfLongestSubstring("bbbbb") == 1
    assert hash.lengthOfLongestSubstring("pwwkew") == 3
    assert hash.lengthOfLongestSubstring("au") == 2
    assert hash.lengthOfLongestSubstring(" ") == 1
    assert hash.lengthOfLongestSubstring("abba") == 2


def test_topKFrequent():
    assert hash.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert hash.topKFrequent([5, 3, 1, 1, 1, 3, 73, 1], 2) == [1, 3]
