"""
Spiral primes
Problem 58

Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ~= 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?
"""
from common.Primes import isPrime


def ne(n):
    """
    Returns the nth number on the North East diagonal.
    """
    return 4*n*n - 2*n + 1


def nw(n):
    """
    Returns the nth number on the North West diagonal.
    """
    return 4*n*n + 1


def sw(n):
    """
    Returns the nth number on the South West diagonal.
    """
    return 4*n*n + 2*n + 1


def answer():
    num = 0
    den = 1
    iter = 1
    while True:
        # 4 new numbers on the diagonal each iteration
        den += 4

        # Check the 3 non-square diagonals for primes
        if isPrime(ne(iter)):
            num += 1

        if isPrime(nw(iter)):
            num += 1

        if isPrime(sw(iter)):
            num += 1


        if float(num)/den < 0.1:
            return 2*iter + 1

        iter += 1


if __name__ == "__main__":
    print answer()
