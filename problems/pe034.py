"""
Digit factorials
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from common.Combinatorics import f


def answer():
    total = 0
    # Lower bound is 10 since there needs to be sum
    # Upper bound is 9!*7 since 9!*8 is not 8 digits long
    upper = f(9)*7
    # return upper
    for i in xrange(10, upper):
        this_total = 0
        for digit in str(i):
            this_total += f(int(digit))

        if this_total == i:
            total += i

    return total


if __name__ == "__main__":
    print answer()
