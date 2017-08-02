"""
Cyclical figurate numbers
Problem 61

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are
all figurate (polygonal) numbers and are generated by the following formulae:

Triangle        P3,n=n(n+1)/2       1, 3, 6, 10, 15, ...
Square          P4,n=n2             1, 4, 9, 16, 25, ...
Pentagonal      P5,n=n(3n-1)/2      1, 5, 12, 22, 35, ...
Hexagonal       P6,n=n(2n-1)        1, 6, 15, 28, 45, ...
Heptagonal      P7,n=n(5n-3)/2      1, 7, 18, 34, 55, ...
Octagonal       P8,n=n(3n-2)        1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three
interesting properties.

    1. The set is cyclic, in that the last two digits of each number is the
       first two digits of the next number (including the last number with the
       first).
    2. Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and
       pentagonal (P5,44=2882), is represented by a different number in the set.
    3. This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which
each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and
octagonal, is represented by a different number in the set.
"""
from MiscMath import ngonNumber, ngonRoot
from math import ceil


def recurse(chain, ngons):
    """
    Recursive function to try each permutation of orders to find the cycle that
    works.
    """
    # Base Case:
    if len(ngons) == 0:
        # Chain complete, check last 2 digits of last to the first 2 digits of
        # first
        last2 = chain[-1] % 100
        first2 = chain[0]//100
        if last2 == first2:
            return chain

        # Nope
        return

    starting_digits = chain[-1] % 100
    if starting_digits < 10:
        return
    x = (starting_digits) * 100

    # Try each remaining ngons
    for i, ngon in enumerate(ngons):
        n = ceil(ngonRoot(ngon, x))
        next_chain = ngonNumber(ngon, n)

        # Loop through all ngon numbers that start with the the same 2 digits
        while next_chain//100 == starting_digits:
            ret = recurse(chain + [next_chain], ngons[:i] + ngons[i + 1:])
            if ret:
                return ret

            # Didnt work, try next ngon number
            n += 1
            next_chain = ngonNumber(ngon, n)



def answer():
    # Get the smallest n that produces a 4 digit octagonal number
    oct_n = ceil(ngonRoot(8, 1000))
    octagonal = ngonNumber(8, oct_n)

    while octagonal < 10000:
        ret = recurse([octagonal], range(7, 2, -1))
        if ret:
            return sum(ret)

        oct_n += 1
        octagonal = ngonNumber(8, oct_n)


if __name__ == "__main__":
    print answer()