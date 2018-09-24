"""
Problem 500!!!
Problem 500

The number of divisors of 120 is 16.
In fact 120 is the smallest number having 16 divisors.

Find the smallest number with 2500500 divisors.
Give your answer modulo 500500507.
"""
from common.Primes import xprime


def answer():
    # Start with factorization of 120
    factors = [[2, 3], [3, 1], [5, 1]]
    total = 120
    divisors = 4
    for np in xprime(7, 1000000000):
        while True:
            # Find the next smallest factor to multiply in
            # Either the next prime (np) or an existing prime with its exponent
            # increased to 1 less than the next power of 2
            min_p = np
            min_e = 1
            for p, e in factors:
                if p ** (e + 1) < min_p ** min_e:
                    min_p = p
                    min_e = e + 1
                if e == 1:
                    break

            total *= (min_p ** min_e) % 500500507
            total = total % 500500507
            divisors += 1
            if divisors == 500500:
                return total

            if min_p != np:
                # Next prime is too large, increment one from factors list instead
                for i in xrange(len(factors)):
                    if factors[i][0] == min_p:
                        factors[i][1] += min_e
            else:
                factors.append([np, 1])
                break


if __name__ == "__main__":
    print answer()
