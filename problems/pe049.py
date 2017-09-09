"""
Prime permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""
from common.Primes import xprime


def answer():
    # Get all 4 digit primes
    primes = [x for x in xprime(1000, 10000)]

    # Dictionary of sorted digits of all primes
    d = {}
    for p in primes:
        key = tuple(sorted(str(p)))
        # Permutation exists, add this prime if its 3330 more than the previous
        if key in d and d[key][-1] + 3330 == p:
                d[key].append(p)
        else:
            # New perm, start the list
            d[key] = [p]

        # Check if the list has 3 primes and isn't the example
        if len(d[key]) == 3 and d[key][0] != 1487:
            return int("{}{}{}".format(*d[key]))


if __name__ == '__main__':
    print answer()
