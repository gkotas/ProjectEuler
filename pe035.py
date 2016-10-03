"""
Circular primes
Problem 35
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
"""
from Primes import xprime, isPrime

def answer():
    circulars = set()

    for prime in xprime(1000000):
        is_circular = True
        rotations = []
        for i in xrange(len(str(prime))):
            rotation = int(str(prime)[i:] + str(prime)[:i])
            if isPrime(rotation):
                rotations.append(rotation)
            else:
                is_circular = False
                break

        if is_circular:
            for circular in rotations:
                circulars.add(circular)

    return len(circulars)

if __name__ == "__main__":
    print answer()