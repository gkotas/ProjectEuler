"""
Truncatable primes
Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from common.Primes import xprime, isPrime


def answer():
    count = 0
    total = 0
    # Loop through primes until the 11th truncatable prime is found
    for prime in xprime(10, 1 << 30):
        # Truncatable primes must start and end with a prime
        if int(str(prime)[0]) not in (2, 3, 5, 7):
            continue
        if int(str(prime)[-1]) not in (2, 3, 5, 7):
            continue

        is_trunc = True
        # No need to check if a single digit is prime if we know it is
        for i in xrange(1, len(str(prime)) - 1):
            # Truncate from the right
            if not isPrime(int(str(prime)[i:])):
                is_trunc = False
                break
            # Truncate from the left
            if not isPrime(int(str(prime)[:0 - i])):
                is_trunc = False
                break

        if is_trunc:
            count += 1
            total += prime

        if count == 11:
            return total


if __name__ == "__main__":
    print answer()
