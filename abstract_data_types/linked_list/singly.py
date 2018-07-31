from abstract_data_types.linked_list.node import Node


class SinglyLinkedList(object):
    def __init__(self, iterable=[]):
        self.head = None
        self.size = 0
        for item in iterable:
            self.append_left(item)

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __len__(self):
        "returns the number of list items"
        return self.size

    def __str__(self):
        return str(list(self))

    def get(self, index):
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.

        :type index: int
        :rtype: int
        """
        for idx, val in enumerate(self):
            if index == idx:
                return val

        return -1

    def append(self, val):
        """inserts a new node at the end of the list"""
        newNode = Node()
        newNode.set_data(val)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(newNode)

        self.size += 1

    def append_left(self, val):
        """inserts a new node at the beginning of the list"""
        newNode = Node()
        newNode.set_data(val)

        if self.head is None:
            self.head = newNode
        else:
            newNode.set_next(self.head)
            self.head = newNode

        self.size += 1

    def append_index(self, index, val):
        """inserts a new node at the index of the list"""
        if index > len(self):
            raise IndexError("Index out of bound exception")
        elif index == 0:
            self.append_left(val)
        elif index == len(self):
            self.append(val)
        else:
            prev = self.head
            while index > 1 and prev is not None:
                prev = prev.get_next()
                index -= 1

            newNode = Node()
            newNode.set_data(val)

            current = prev.get_next()
            newNode.set_next(current)
            prev.set_next(newNode)

            self.size += 1

    def delete_first(self):
        """delete the first node of the linked list"""
        if self.head is None:
            raise IndexError("The list is empty")
        else:
            self.head = self.head.get_next()
            self.size -= 1

    def delete_index(self, index):
        """delete the index node of the linked list"""
        if index >= len(self):
            raise IndexError("Index out of bound exception")
        elif index == 0:
            self.delete_first()
        else:
            prev = self.head
            while index > 1 and prev is not None:
                prev = prev.get_next()
                index -= 1

            prev.set_next(prev.get_next().get_next())
            self.size -= 1

    def clear(self):
        self.head = None

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

    def hasCycle(self):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = self.head
            fast = self.head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except Exception:
            return False
