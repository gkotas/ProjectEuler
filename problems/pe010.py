"""
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from common.Primes import xprime


def answer():
    ans = 0
    for prime in xprime(2000000):
        ans += prime

    return ans


if __name__ == "__main__":
    print answer()
