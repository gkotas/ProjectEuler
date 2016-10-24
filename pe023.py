"""
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""
from MiscMath import divisorSum as d


def answer():
    # Make a list of all the abundants less than 28123
    abundants = []
    for n in xrange(2, 28124):
        if d(n) > n:
            abundants.append(n)

    sum_of_abundants = {}
    for i in xrange(len(abundants)):
        for j in xrange(i, len(abundants)):
            if abundants[i] + abundants[j] > 28123:
                break

            sum_of_abundants[abundants[i] + abundants[j]] = True

    # Return the difference of all the numbers less than 28123 and the sum of
    # all the abundant number.
    return 28123*(28123 + 1)/2 - sum(sum_of_abundants.keys())


if __name__ == '__main__':
    print answer()
