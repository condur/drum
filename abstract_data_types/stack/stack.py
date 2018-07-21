class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self) - 1]

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        while len(self) > 0:
            yield self.items.pop()
