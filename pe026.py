"""
Reciprocal cycles
Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.
"""
from Primes import xprime

def isCyclic(prime):
    """
    Determines if the reciprocal of the given prime is a cyclic number of length
    prime - 1
    """
    length = 0
    remainder = 1

    while True:
        length += 1
        # Once the length reaches over half of the prime, it's cyclic
        if length > prime//2:
            return True

        # Calculate the next digit by multiplying remainder by 10 and dividing
        remainder = remainder*10 % prime
        # Once there's only 1 remainder, the cycle ends and thus isn't cyclic
        if remainder == 1:
            return False

def answer():
    ans = 0
    for p in xprime(7, 1000):
        if isCyclic(p):
            ans = p
    return ans

if __name__ == '__main__':
    print answer()
