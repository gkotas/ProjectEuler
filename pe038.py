"""
Pandigital multiples
Problem 38
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def answer():
    most = 918273645
    # The number must be 4 digits which will produce 5 digits when n = 2
    # i must be greater than first four digits of most and must be less than
    # 9876 which is the biggest pandigital prefix
    for i in xrange(9183, 9876):
        digits = set()
        for digit in str(i):
            digits.add(digit)

        # There should be 4 digits in the set now, not including 0
        if len(digits) != 4 or "0" in digits:
            continue

        # Add the digits of i*2
        for digit in str(i*2):
            digits.add(digit)

        # There should be 9 digits not including 0
        if len(digits) != 9 or "0" in digits:
            continue

        # Got a pandigital multiple, check if greater than most
        if int(str(i) + str(i*2)) > most:
            most = int(str(i) + str(i*2))

    return most

if __name__ == "__main__":
    print answer()