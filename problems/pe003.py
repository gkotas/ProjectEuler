"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from common.Primes import xprime


def greatestPrime(x):
    for prime in xprime(x):
        while x % prime == 0:
            x /= prime

        if x == 1:
            return prime


def answer():
    return greatestPrime(600851475143)


if __name__ == "__main__":
    print answer()
