class Node(object):
    def __init__(self):
        # store data
        self.data = None

        # store reference (next item)
        self.next = None

    def get_data(self):
        """getting the data field of the node"""
        return self.data

    def set_data(self, data) -> None:
        """setting the data field of the node"""
        self.data = data

    def get_next(self):
        """getting the next field of the node"""
        return self.next

    def set_next(self, next) -> None:
        """setting the next field of the node"""
        self.next = next

    def has_next(self) -> bool:
        """returns true if the node points to another node"""
        return self.next is not None

    def has_value(self, value) -> bool:
        "compares the value with the node data"
        if self.data == value:
            return True
        else:
            return False
