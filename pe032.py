"""
Pandigital products
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

def answer():
    # To ensure the product only gets counted once, use set to store
    # solutions and then sum
    pandigitals = set()
    # a*b = c
    # a <= b <= c
    # if a = b = 100 -> 100*100 = 10000 -> 11 digits minimum
    for a in xrange(2, 100):
        # b can be at most 5000, when a = 2
        for b in xrange(a, 5000):
            # Continue until the length of the multiplicand, multiplier, and
            # product is 9 digits
            if len(str(a)) + len(str(b)) + len(str(a*b)) < 9:
                continue

            # Quit once the length exceeds 9 digits
            if len(str(a)) + len(str(b)) + len(str(a*b)) > 9:
                break

            # Add all digits to set to ensure no duplicates
            digits = set()
            for digit in "%i%i%i" % (a, b, a*b):
                digits.add(digit)

            # There should be 9 digits not including zero
            if len(digits) == 9 and "0" not in digits:
                pandigitals.add(a*b)

    return sum(pandigitals)

if __name__ == "__main__":
    print answer()