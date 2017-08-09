"""
Sub-string divisibility
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

# Shifting the indices of d by 1:
#   d1d2d3=406 is divisible by 2
#   d2d3d4=063 is divisible by 3
#   d3d4d5=635 is divisible by 5
#   d4d5d6=357 is divisible by 7
#   d5d6d7=572 is divisible by 11
#   d6d7d8=728 is divisible by 13
#   d7d8d9=289 is divisible by 17


def answer():
    DIGIT_STRING = "0123456789"
    d = ["x"]*10

    total = 0

    # Loop through all multiples of
    for m17 in xrange(17, 1000, 17):
        s17 = str(m17)
        # Make a string that is 3 digits long
        if len(s17) < 3:
            s17 = "0"*(3 - len(s17)) + s17

        digits = set(s17)
        # Has to have unique digits
        if len(digits) < 3:
            continue
        d[7:] = list(s17)

        # Loop through d6
        for d6 in DIGIT_STRING:
            # Make sure the digit is unique
            if d6 in digits:
                continue

            m13 = int(d6 + "".join(d[7:9]))
            # Make d6d7d8 its a multiple of 13
            if m13 % 13 != 0:
                continue

            # Mark digits as used
            d[6] = d6
            digits.add(d6)

            # Loop through d5, which needs to be 0 or 5
            for d5 in "05":
                # Make sure the digit is unique
                if d5 in digits:
                    continue

                m11 = int(d5 + "".join(d[6:8]))
                # Make d5d6d7 its a multiple of 11
                if m11 % 11 != 0:
                    continue

                # Mark digits as used
                d[5] = d5
                digits.add(d5)

                # Loop through d4
                for d4 in DIGIT_STRING:
                    # Make sure the digit is unique
                    if d4 in digits:
                        continue

                    m7 = int(d4 + "".join(d[5:7]))
                    # Make d4d5d6 its a multiple of 7
                    if m7 % 7 != 0:
                        continue

                    # Mark digits as used
                    d[4] = d4
                    digits.add(d4)

                    # Loop through d3, which needs to be even
                    for d3 in "02468":
                        # Make sure the digit is unique
                        if d3 in digits:
                            continue

                        # We know d3d4d5 is multiple of 5 since d5 is 0 or 5

                        # Mark digits as used
                        d[3] = d3
                        digits.add(d3)

                        # Loop through d2
                        for d2 in DIGIT_STRING:
                            # Make sure the digit is unique
                            if d2 in digits:
                                continue

                            m3 = int(d2 + "".join(d[3:5]))
                            # Make d2d3d4 its a multiple of 3
                            if m3 % 3 != 0:
                                continue

                            # Mark digits as used
                            d[2] = d2
                            digits.add(d2)

                            # Loop through d1
                            for d1 in DIGIT_STRING:
                                # Make sure the digit is unique
                                if d1 in digits:
                                    continue

                                # Mark digits as used
                                d[1] = d1
                                digits.add(d1)

                                # Loop through d0
                                for d0 in DIGIT_STRING:
                                    # Make sure the digit is unique
                                    if d0 in digits:
                                        continue

                                    d[0] = d0
                                    # Got a solution, add it to the total
                                    total += int("".join(d))

                                # Mark digit as unused
                                digits.discard(d1)

                            # Mark digit as unused
                            digits.discard(d2)

                        # Mark digit as unused
                        digits.discard(d3)

                    # Mark digit as unused
                    digits.discard(d4)

                # Mark digit as unused
                digits.discard(d5)

            # Mark digit as unused
            digits.discard(d6)

    return total


if __name__ == "__main__":
    print answer()
