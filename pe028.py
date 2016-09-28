"""
Number spiral diagonals
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
"""

def answer():
    # Expand the spiral one more to find function that leads to next diagonal
    #
    # 43 44 45 46 47 48 49
    # 42 21 22 23 24 25 26
    # 41 20  7  8  9 10 27
    # 40 19  6  1  2 11 28
    # 39 18  5  4  3 12 29
    # 38 17 16 15 14 13 30
    # 37 36 35 34 33 32 31

    def ne(x):
        """
        Northeast diagonal:
            Points are (1, 9), (2, 25), (3, 49)
            Resulting quadratic is 4x^2 + 4x + 1
        """
        return 4*x**2 + 4*x + 1

    def se(x):
        """
        Southeast diagonal:
            Points are (1, 3), (2, 13), (3, 31)
            Resulting quadratic is 4x^2 - 2x + 1
        """
        return 4*x**2 - 2*x + 1

    def nw(x):
        """
        Northwest diagonal:
            Points are (1, 7), (2, 21), (3, 43)
            Resulting quadratic is 4x^2 + 2x + 1
        """
        return 4*x**2 + 2*x + 1

    def sw(x):
        """
        Southwest diagonal:
            Points are (1, 5), (2, 17), (3, 37)
            Resulting quadratic is 4x^2 + 1
        """
        return 4*x**2 + 1

    # Start with 1 because is share between all diagonals
    total = 1

    # For a 1001 by 1001 spiral, there will be 500 numbers in each direction
    for x in xrange(1, 501):
        total += ne(x)
        total += se(x)
        total += nw(x)
        total += sw(x)

    return total

if __name__ == "__main__":
    print answer()