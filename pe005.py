"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

from math import log

from Primes import xprime

def smallestMultiple(x):
    """
    Determines smallest number divisible by all numbers 1 to x.
    """
    ans = 1
    for prime in xprime(x):
        ans *= prime**int(log(x, prime))
    
    return ans

def answer():
    return smallestMultiple(20)

if __name__ == "__main__":
    print answer()