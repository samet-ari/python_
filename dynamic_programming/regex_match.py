"""
Regex matching check if a text matches wildcard pattern or not.
Pattern:
    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.
More info:
    https://medium.com/trick-the-interviwer/regular-expression-matching-9972eb74c03
"""


def recursive_match(text: str, pattern: str) -> bool:
    """
    Recursive matching algorithm.

    Time complexity: O(2 ^ (m + n)), where m is the length of text and n is the length of pattern.
    Space complexity: Recursion depth is O(m + n).

    :param text: Text to match.
    :param pattern: Pattern to match.
    :return: True if text matches pattern, False otherwise.

    >>> recursive_match('abc', 'a.c')
    True
    >>> recursive_match('abc', 'af*.c')
    True
    >>> recursive_match('abc', 'a.c*')
    True
    >>> recursive_match('abc', 'a.c*d')
    False
    >>> recursive_match('aa', '.*')
    True
    """
    if not text and not pattern:
        return True

    if text and not pattern:
        return False

    if not text and pattern and pattern[-1] != '*':
        return False

    if not text and pattern and pattern[-1] == '*':
        return recursive_match(text, pattern[:-2])

    if text[-1] == pattern[-1] or pattern[-1] == '.':
        return recursive_match(text[:-1], pattern[:-1])

    if pattern[-1] == '*':
        return recursive_match(text[:-1], pattern) or recursive_match(text, pattern[:-2])

    return False


def dp_match(text: str, pattern: str) -> bool:
    """
    Dynamic programming matching algorithm.

    Time complexity: O(m * n), where m is the length of text and n is the length of pattern.
    Space complexity: O(m * n).

    :param text: Text to match.
    :param pattern: Pattern to match.
    :return: True if text matches pattern, False otherwise.

    >>> dp_match('abc', 'a.c')
    True
    >>> dp_match('abc', 'af*.c')
    True
    >>> dp_match('abc', 'a.c*')
    True
    >>> dp_match('abc', 'a.c*d')
    False
    >>> dp_match('aa', '.*')
    True
    """
    m = len(text)
    n = len(pattern)
    dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        dp[i][0] = False

    for j in range(1, n + 1):
        dp[0][j] = pattern[j - 1] == '*' and dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[j - 1] == '.' or pattern[j - 1] == text[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (pattern[j - 2] == '.' or pattern[j - 2] == text[i - 1]))
            else:
                dp[i][j] = False

    return dp[m][n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
