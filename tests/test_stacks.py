from algo import stacks


def test_isValid():
    assert stacks.isValid("()") is True
    assert stacks.isValid("()[]{}") is True
    assert stacks.isValid("(]") is False
    assert stacks.isValid("([)]") is False
    assert stacks.isValid("{[]}") is True
    assert stacks.isValid("]") is False
    assert stacks.isValid("[") is False


def test_evalReversePolishNotation():
    assert stacks.evalReversePolishNotation(["2", "1", "+", "3", "*"]) == 9
