from abstract_data_types.stack.stack import Stack


def test_stack_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert len(stack) == 2


def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert len(stack) == 1


def test_stack_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    assert len(stack) == 2


def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty() is True


def test_stack_is_not_empty():
    stack = Stack()
    stack.push(1)
    assert stack.is_empty() is False


def test_stack_iter():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    coll = []
    for value in stack:
        coll.append(value)
    assert coll == [3, 2, 1]
