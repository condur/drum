from algo import remove_duplicates as rm


def test_remove_duplicates():
    assert rm.remove_duplicates([7, 6, 4, 3, 1, 1]) == 5
