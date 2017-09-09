"""
Consecutive prime sum
Problem 50

The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""
from common.Primes import xprime


def answer():
    # Get list and set of all primes < 1000000
    primes = [x for x in xprime(1000000)]
    sprimes = set(primes)

    max_p = 0
    max_streak = 0

    for start in xrange(len(primes)):
        # Done if the prime at start plus the next max_streak primes is greater
        # than million
        if sum(primes[start:start + max_streak]) > 1000000:
            break
        p = primes[start]
        offset = 1
        while p < 1000000:
            p += primes[start + offset]
            offset += 1
            if offset > max_streak and p in sprimes:
                max_p = p
                max_streak = offset

    return max_p


if __name__ == '__main__':
    print answer()
