"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def isPalindrome(x):
    """
    True if the number is a palindrome, False otherwise.
    """
    x = str(x)
    for i in xrange(len(x)/2):
        if x[i] != x[len(x) - i - 1]:
            return False

    return True


def answer():
    """
    Guessing the answer involves two 900+ numbers
    """
    max = 0
    for i in xrange(999, 900, -1):
        for j in xrange(999, i - 1, -1):
            if isPalindrome(i*j):
                if i*j > max:
                    max = i*j

    return max


if __name__ == "__main__":
    print answer()
