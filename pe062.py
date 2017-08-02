"""
Cubic permutations
Problem 62

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.
"""


def answer():
    cube_digits = {}
    x = 100
    while True:
        digits = "".join(sorted(str(x*x*x)))

        # Add x to the list
        if digits in cube_digits:
            cube_digits[digits].append(x)

            # Check if count reached 5
            if len(cube_digits[digits]) == 5:
                return cube_digits[digits][0]

        else:
            # First perm, start list
            cube_digits[digits] = [x]

        x += 1


if __name__ == "__main__":
    print answer()
