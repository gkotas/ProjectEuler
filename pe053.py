"""
Combinatoric selections
Problem 53

There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = n!/(r!(n-r)!), where r <= n, n! = n*(n-1)*...*3*2*1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are
greater than one-million?
"""
from Combinatorics import nCr


def answer():
    count = 0

    for n in xrange(23, 101):
        for r in xrange(1, n//2 + 1):
            # Find first r when nCr > 10^6
            # Know that nCr == nC(n-r)
            # All numbers between r and n-r > 10^6
            if nCr(n, r) > 10**6:
                count += n - 2*r + 1
                break
    return count


if __name__ == "__main__":
    print answer()