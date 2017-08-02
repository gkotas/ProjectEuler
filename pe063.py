"""
Powerful digit counts
Problem 63
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""


def nDigitPowers(n):
    """
    Returns
    """
    lower = 10**(n - 1)
    upper = 10**n - 1
    lower = int(lower**(1/float(n))) + 1
    upper = int(upper**(1/float(n)))
    return upper - lower



def answer():
    # Digits 1-9 raised to first power are 1 digit
    count = 9
    n = 2.0
    while True:
        lower = 10**(n - 1)
        # Find amount of numbers less that and including 9 that satisfy
        # 10^n always as n+1 digits
        nDigits = 9 - int(lower**(1/n))

        if not nDigits:
            # This happens when 9^n is less than n digits
            return count

        count += nDigits
        n += 1.0


    return count

if __name__ == "__main__":
    print answer()
