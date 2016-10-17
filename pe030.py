"""
Digit fifth powers
Problem 30

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""


def sumOfFifthPowers(n):
    """
    Determines in n can be written as the sum of the fifth powers of its
    digits.
    """
    # Must have multiple digits
    if n < 10:
        return False

    total = 0
    for digit in str(n):
        total += int(digit)**5

    return total == n


def answer():
    total = 0
    # Highest possible sum for 7 digits -> 7*9^5 = 413343 which isn't 7 digits
    # Therefore all values are less than the max of 6 digits
    for i in xrange(10, 6*9**5):
        if sumOfFifthPowers(i):
            total += i

    return total


if __name__ == "__main__":
    print answer()
