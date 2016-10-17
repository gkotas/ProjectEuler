"""
Lexicographic permutations
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
"""
from Combinatorics import f


def answer():
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    nth_perm = 1000000
    string = ""
    # There are 9! permutation for first digit, 8! for second, etc.
    for i in xrange(9, 0, -1):
        # How many 9! can happen below 1000000, Remainder is for next digit
        next_digit = nth_perm / f(i)
        nth_perm = nth_perm % f(i)
        string += digits.pop(next_digit)

    return int(string)


if __name__ == '__main__':
    print answer()
