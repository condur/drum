from abstract_data_types.linked_list.node import Node


class SinglyLinkedList(object):
    def __init__(self, iterable=[]):
        self.head = None
        self.size = 0
        for item in iterable:
            self.append(item)

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def append(self, data):
        """inserts a new node at the beginning of the list"""
        newNode = Node()
        newNode.set_data(data)

        if self.head is None:
            self.head = newNode
        else:
            newNode.set_next(self.head)
            self.head = newNode
        self.size += 1

    def delete_from_beginning(self):
        """delete the first node of the linked list"""
        if self.head is None:
            raise IndexError("The list is empty")
        else:
            self.head = self.head.get_next()
            self.size -= 1

    def clear(self):
        self.head = None

    def get_size(self):
        "returns the number of list items"
        return self.size

    def calculate_size(self):
        "calculate and returns the number of list items"

        count = 0
        current = self.head

        while current is not None:
            # increase counter by one
            count += 1
            # jump to the next linked node
            current = current.get_next()

        return count
