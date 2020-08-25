import math


def perfect_square(num: int) -> bool:
    """
    Check if a number is perfect square number or not
    :param num: the number to be checked
    :return: True if number is square number, otherwise False

    >>> perfect_square(9)
    True
    >>> perfect_square(16)
    True
    >>> perfect_square(1)
    True
    >>> perfect_square(0)
    True
    >>> perfect_square(10)
    False
    """
    return math.sqrt(num) * math.sqrt(num) == num


def perfect_square_binary_search(n: int) -> bool:
    """
    Check if a number is perfect square using binary search.
    Time complexity : O(Log(n))
    Space complexity: O(1)

    >>> perfect_square(9)
    True
    >>> perfect_square(16)
    True
    >>> perfect_square(1)
    True
    >>> perfect_square(0)
    True
    >>> perfect_square(10)
    False
    """
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if mid ** 2 == n:
            return True
        elif mid ** 2 > n:
            right = mid - 1
        else:
            left = mid + 1
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
