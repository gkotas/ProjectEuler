"""
Lattice paths
Problem 15

Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""
from Combinatorics import nCr

def answer():
    return nCr(40, 20)

if __name__ == "__main__":
    print answer()