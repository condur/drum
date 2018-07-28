from abstract_data_types.linked_list.singly import SinglyLinkedList
import pytest


def test_init_and_len():
    list = SinglyLinkedList([1, 2, 3, 4])
    assert len(list) == 4
    assert list.calculate_size() == 4


def test_iter():
    data = [1, 2, 3, 4]
    list = SinglyLinkedList(data)
    coll = []
    coll.extend(list)
    coll.reverse()
    assert coll == data


def test_get():
    list = SinglyLinkedList([1, 2, 3, 4])
    assert list.get(0) == 4
    assert list.get(1) == 3
    assert list.get(10) == -1


def test_append_index():
    list = SinglyLinkedList([1, 2, 3, 4])

    with pytest.raises(IndexError):
        list.append_index(5, 5)

    list.append_index(0, 0)
    assert list.get(0) == 0
    list.append_index(1, 10)
    assert list.get(1) == 10
    list.append_index(6, 6)
    assert list.get(6) == 6


def test_delete_index():
    list = SinglyLinkedList([1, 2, 3, 4])

    with pytest.raises(IndexError):
        list.delete_index(5)

    list.delete_index(3)
    assert len(list) == 3
    list.delete_index(1)
    assert len(list) == 2
    list.delete_index(0)
    assert len(list) == 1
