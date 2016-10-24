"""
Power digit sum
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""


def answer():
    total = 0
    for digit in str(2**1000):
        total += int(digit)
    return total


if __name__ == "__main__":
    print answer()
