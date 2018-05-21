def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def isArraylnSortedOrder(A):
    if len(A) == 1:
        return True
    return A[0] <= A[1] and isArraylnSortedOrder(A[1:])


def increment(nums):
    carry = 0
    for item in nums[::-1]:
        item = 1 + item + carry
        yield item
        carry = item - 9


def main():
    for item in increment([1, 0, 0]):
        print(item)


if __name__ == "__main__":
    main()
