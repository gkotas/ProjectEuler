"""
Prime pair sets
Problem 60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""
from Primes import xprime, isPrime


def concatPair(a, b, primes):
    """
    Determines if the primes a and b form concatenated primes
    """
    return (isPrime(int(str(a) + str(b)), primes)
            and isPrime(int(str(b) + str(a)), primes))


def answer():
    primes = [p for p in xprime(10000)]

    # Generator a dict of sets that the key and each value in set is concatPair
    pairs = {}
    for i, p in enumerate(primes):
        pairs[p] = set()
        for j in xrange(i + 1, len(primes)):
            if concatPair(p, primes[j], primes):
                pairs[p].add(primes[j])

    for p4 in primes:
        p4pairs = pairs[p4]

        for p3 in p4pairs:
            p43pairs = p4pairs & pairs[p3]

            for p2 in p43pairs:
                p432pairs = p43pairs & pairs[p2]

                for p1 in p432pairs:
                    p4321pairs = p432pairs & pairs[p1]

                    for p0 in p4321pairs:
                        return p0 + p1 + p2 + p3 + p4


if __name__ == "__main__":
    print answer()