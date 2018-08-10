def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    d = {"[": "]", "(": ")", "{": "}"}
    stack = []
    for char in s:
        if char in d:
            stack.append(char)
        elif not stack or char != d[stack.pop()]:
            return False

    return not stack


def evalReversePolishNotation(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: int(x / y),
    }
    stack = []
    for token in tokens:
        if token in operators:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(operators[token](num2, num1))
        else:
            stack.append(int(token))

    return stack.pop()
