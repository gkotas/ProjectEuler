"""
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def answer():
    for a in xrange(1, 1000):
        # B must be greater than or equal to a
        for b in xrange(a, 1000):
            # C has to make the sum equal 1000
            c = 1000 - b - a

            # C has to be the largest value and less than the sum of the others
            if c < b or c > a + b:
                continue
            if a**2 + b**2 == c**2:
                return a*b*c


if __name__ == "__main__":
    print answer()
