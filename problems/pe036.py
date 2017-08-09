"""
Double-base palindromes
Problem 36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""


def isPalindrome(string):
    """
    Determines if the string is palindromic.
    """
    return string == string[::-1]


def answer():
    total = 0
    # Loop through first half of palindrome, then just mirror and append
    for i in xrange(1, 1000):
        # Even length: abccba
        p = int(str(i) + str(i)[::-1])
        # bin() returns a string with the prefix "0b"
        if isPalindrome(bin(p)[2:]):
            total += p

        # Odd length: abcba
        p = int(str(i)[:-1] + str(i)[::-1])
        if isPalindrome(bin(p)[2:]):
            total += p

    return total


if __name__ == "__main__":
    print answer()
