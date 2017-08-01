"""
Square root convergents
Problem 57

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

    sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

    1 + 1/2 = 3/2 = 1.5
    1 + 1/(2 + 1/2) = 7/5 = 1.4
    1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
    1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?
"""


def numDigits(x):
    """
    Returns the number of digits in number x.
    """
    return len(str(x))


def answer():
    count = 0
    num = 3
    den = 2

    for _ in xrange(1000):
        # New den = old num + old den
        # New num = old den + new den
        num, den = num + 2*den, num + den
        if numDigits(num) > numDigits(den):
            count += 1

    return count


if __name__ == "__main__":
    print answer()
