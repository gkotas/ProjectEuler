"""
Goldbach's other conjecture
Problem 46

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

    9 = 7 + 2*1^2
    15 = 7 + 2*2^2
    21 = 3 + 2*3^2
    25 = 7 + 2*3^2
    27 = 19 + 2*2^2
    33 = 31 + 2*1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
"""
from common.Primes import primeGen, isPrime


def answer():
    primes = [2, 3, 5, 7]
    i = 9
    while True:
        if isPrime(i, primes):
            primes.append(i)
            i += 1
            continue

        for prime in primes:
            sq = (i - prime)//2
            if sq**0.5 == int(sq**0.5):
                break
        else:
            return i

        i += 1


if __name__ == '__main__':
    print answer()
