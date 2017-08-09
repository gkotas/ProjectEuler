"""
Champernowne's constant
Problem 40

An irrational decimal fraction is created by concatenating the positive
integers:

    0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
"""


def answer():
    total = 1
    # Start with the 9 single digit numbers
    total_num_digits = 9
    digits = 2
    # Loop through powers of 10 until 1000000
    for power in xrange(1, 7):
        d = 10**power

        next_set_of_digits = 9 * 10**digits * digits

        # Add the next set of digits if the new total doesn't exceed d
        # By set I mean 2-digit numbers, 3-digit numbers, etc
        while total_num_digits + next_set_of_digits < d:
            total_num_digits += next_set_of_digits
            digits += 1
            next_set_of_digits = 9 * 10**digits

        # We know the dth digit is in this set, found which index it is from d
        digit_needed = d - total_num_digits - 1

        # Digit is in the nth number
        nth_num_needed = digit_needed // digits
        # Digit is in this place of the nth number
        place_needed = digit_needed % digits

        # Multiply it to the total
        total *= int(str(10**digits + nth_num_needed)[place_needed])

    return total


if __name__ == "__main__":
    print answer()
