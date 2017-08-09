"""
Pandigital prime
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""
from common.Primes import xprime


def isPandigital(x):
    """
    Determines if x is an n-digit pandigital number.
    """
    n_digits = len(str(x))

    digits = set(str(x))
    # Can't have a 0 or have duplicated digits
    if "0" in digits or len(digits) != n_digits:
        return False

    pandigital_digits = set(map(str, range(1, n_digits + 1)))
    return digits == pandigital_digits


def answer():
    most = 0
    # Prime has to be less than 8 digits, since all 8 and 9 pandigitals are
    # divisible by 3
    for prime in xprime(7654321):
        if isPandigital(prime):
            most = prime

    return most


if __name__ == "__main__":
    print answer()
