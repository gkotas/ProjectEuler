"""
Quadratic primes
Problem 27

Euler discovered the remarkable quadratic formula:

    n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer
values 0 <= n <= 39. However, when n=40,40^2 + 40 + 41 = 40(40+1) + 41 is
divisible by 41, and certainly when n=41, 41^2 + 41 + 41 is clearly divisible by
41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes
for the consecutive values 0 <= n <= 79. The product of the coefficients, -79
and 1601, is -126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| <= 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, aa and bb, for the quadratic expression
that produces the maximum number of primes for consecutive values of n, starting
with n = 0.
"""
from Primes import xprime, isPrime

def primeChainCount(a, b):
    """
    Returns how many consectutive primes the quadratic n^2 + an + b produces
    when starting with n == 0.
    """
    count = 0
    n = 0
    while isPrime(n**2 + a*n + b):
        count += 1
        n += 1

    return count

def answer():
    longest_count = 0
    product = 0
    # When n == 0 -> 0^2 + a*0 + b == b, so b must be prime
    for b in xprime(1000):
        # When n is odd and a is even -> (odd)^2 + (even)*(odd) + (odd)
        #                             -> odd + even + odd
        #                             -> even != prime, so a must be odd
        #
        # Lower limit is when n == 1 -> 1 + a + b >= 3
        #                            -> a = 2 - b
        #
        # From the first couple longest chains, a seems to be always negative
        for a in xrange(2 - b, 0, 2):
            this_count = primeChainCount(a, b)
            if this_count > longest_count:
                longest_count = this_count
                product = a*b

    return product

if __name__ == "__main__":
    print answer()