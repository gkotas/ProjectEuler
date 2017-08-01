"""
Powerful digit sum
Problem 56

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the
maximum digital sum?
"""


def digitSum(x):
    """
    Returns the sum of all the digits in x.
    """
    return sum(map(int, str(x)))


def answer():
    most = 0

    for a in xrange(1, 100):
        for b in xrange(1, 100):
            ds = digitSum(a**b)
            most = max(most, ds)

    return most

if __name__ == "__main__":
    print answer()