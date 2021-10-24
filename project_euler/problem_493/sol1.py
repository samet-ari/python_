"""
Project Euler Problem 493: https://projecteuler.net/problem=493

70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours.
What is the expected number of distinct colours in 20 randomly picked balls?
Give your answer with nine digits after the decimal point (a.bcdefghij).

-----

This combinatorial problem can be solved by decomposing the problem into the
following steps:
1. Calculate the total number of possible picking cominations
[combinations := binom_coeff(70, 20)]
2. Calculate the number of combinations with one colour missing
[missing := binom_coeff(60, 20)]
3. Calculate the probability of one colour missing
[missing_prob := missing / combinations]
4. Calculate the probability of no colour missing
[no_missing_prob := 1 - missing_prob]
5. Calculate the expected number of distinct colours
[expected = 7 * no_missing_prob]

References:
- https://en.wikipedia.org/wiki/Binomial_coefficient
"""

import math

BALLS_PER_COLOUR = 10
NUM_COLOURS = 7
NUM_BALLS = BALLS_PER_COLOUR * NUM_COLOURS


def solution(num_picks: int = 20) -> float:
    """
    Calculates the expected number of distinct colours

    >>> f'{solution(10):.9f}'
    '5.669644129'

    >>> f'{solution(30):.9f}'
    '6.985042712'
    """
    total = math.comb(NUM_BALLS, num_picks)
    missing_colour = math.comb(NUM_BALLS - BALLS_PER_COLOUR, num_picks)

    result = NUM_COLOURS * (1 - missing_colour / total)

    return result


if __name__ == "__main__":
    print(f"{solution(20):.9f}")
