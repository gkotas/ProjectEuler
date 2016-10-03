"""
Digit cancelling fractions
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.
"""

def cancelledFraction(n, d):
    """
    Returns the cancelled fraction's numerator and denominator if the given is
    cancelable.
    """
    # Get the digits of the num and den
    n0, n1 = list(str(n))
    d0, d1 = list(str(d))

    # Try cancelling the first digit of n with first of d
    if n0 == d0:
        if float(n1)/float(d1) == float(n)/d:
            return (n1, d1)

    # Try cancelling the first digit of n with second of d
    elif n0 == d0:
        if float(n1)/float(d0) == float(n)/d:
            return (n1, d0)

    # Try cancelling the second digit of n with first of d
    elif n1 == d0:
        if float(n0)/float(d1) == float(n)/d:
            return (n0, d1)

    # Try cancelling the second digit of n with second of d
    elif n1 == d1:
        if float(n0)/float(d0) == float(n)/d:
            return (n0, d0)

    # Not cancelable, return None
    return None

def answer():
    den = 1
    nums = []
    # 9 < n < d < 100
    for n in xrange(10, 99):
        for d in xrange(n + 1, 100):
            # Non-trivial cases
            if n % 10 and d % 10:
                is_cancelled = cancelledFraction(n, d)
                # If is cancelled, multiply the denominator and store the
                # numerator
                if is_cancelled:
                    den *= int(is_cancelled[1])
                    nums.append(int(is_cancelled[0]))

    # Found all the cases, now reduce the denominator with the store numerators
    for num in nums:
        if den % num == 0:
            den /= num

    return den

if __name__ == "__main__":
    print answer()