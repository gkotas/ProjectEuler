"""
Riffle Shuffles
Problem 622

A riffle shuffle is executed as follows: a deck of cards is split into two equal
halves, with the top half taken in the left hand and the bottom half taken in
the right hand. Next, the cards are interleaved exactly, with the top card in
the right half inserted just after the top card in the left half, the 2nd card
in the right half just after the 2nd card in the left half, etc. (Note that this
process preserves the location of the top and bottom card of the deck)

Let s(n) be the minimum number of consecutive riffle shuffles needed to restore
a deck of size n to its original configuration, where n is a positive even
number.

Amazingly, a standard deck of 52 cards will first return to its original
configuration after only 8 perfect shuffles, so s(52)=8. It can be verified that
a deck of 86 cards will also return to its original configuration after exactly
8 shuffles, and the sum of all values of n that satisfy s(n)=8 is 412.

Find the sum of all values of n that satisfy s(n)=60.
"""
from common.Primes import factorize


def multiplicativeOrder(b, n):
    """
    Computes the lowest k such that b**k == 1 (mod n). This is limited to return
    0 if k > 60
    """
    k = 1
    result = 1
    while k < n:
        result = (result * b) % n

        if result == 1:
            return k

        k += 1

        # Don't care if it's over 60
        if k > 60:
            return 0


def answer():
    # Get a list of all prime factors, with duplicates
    primes = []
    for base, exp in factorize(2**60 - 1):
        for i in xrange(exp):
            primes.append(base)

    # Get a set of all factors
    factors = set()
    for i in xrange(2**len(primes)):
        b = bin(i)[2:]
        b = "0"*(len(primes) - len(b)) + b

        size = 1
        for j in xrange(len(b)):
            if b[j] == '1':
                size *= primes[j]
        factors.add(size)

    # Check each factor for its multiplicative order
    total = 0
    for factor in factors:
        if multiplicativeOrder(2, factor) == 60:
            total += factor + 1

    return total


if __name__ == '__main__':
    print answer()
