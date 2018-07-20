from abstract_data_types.linked_list.singly import SinglyLinkedList


def test_linked_list():
    list = SinglyLinkedList([1, 2, 3, 4])
    assert list.get_size() == 4
    assert list.calculate_size() == 4


def test_iter():
    data = [1, 2, 3, 4]
    list = SinglyLinkedList(data)
    coll = []
    coll.extend(list)
    coll.reverse()
    assert coll == data
