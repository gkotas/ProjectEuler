"""
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def sumsSquared(x):
    """
    Returns the square of the sum of numbers 1 to x.
    """
    return sum(range(x + 1))**2


def squaredSums(x):
    """
    Returns the sum of the first x squares.
    """
    ans = 0
    for i in xrange(x + 1):
        ans += i*i
    return ans


def answer():
    return sumsSquared(100) - squaredSums(100)


if __name__ == "__main__":
    print answer()
