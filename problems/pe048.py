"""
Self powers
Problem 48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


def answer():
    total = 0
    for i in xrange(1, 1001):
        total += pow(i, i, 10**10)
    return total % 10**10


if __name__ == '__main__':
    print answer()
