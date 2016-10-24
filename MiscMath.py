"""
Flie that holds miscellaneous mathematics functionality.

Functions:
    divisorSum(n)       - Returns the sum of divisors of n.
    triangleNumber(n)   - Returns the nth triangle number.
    isTriangular(x)     - Determines if x is a triangle number.
    pentagonNumber(n)   - Returns the nth pentagon number.
    isPentagonal(x)     - Determines if x is a pentagon number


Private Functions:

"""
##### Private Functions #######################################################
dS_memo = {}


##### Public Functions ########################################################
def divisorSum(n):
    """
    Returns the sum of the divisors of n.
    """
    if n not in dS_memo:
        # Start with 1 so n isn't counted
        total = 1
        # Loop from 2 to sqrt(n)
        for i in xrange(2, int(n**0.5) + 1):
            if n % i == 0:
                total += i
                # Only add the other divisor if it isn't a square
                if i * i != n:
                    total += n/i

        dS_memo[n] = total

    return dS_memo[n]


def triangleNumber(n):
    """
    Returns the nth triangle number
    """
    return n*(n + 1)/2


def isTriangular(x):
    """
    Determines if x is a triangle number
    """
    return (8*x + 1)**0.5 % 2 == 1


def pentagonNumber(n):
    """
    Returns the nth pentagon number
    """
    return n*(3*n - 1)/2


def isPentagonal(x):
    """
    Determines if x is a pentagon number
    """
    return (24*x + 1)**0.5 % 6 == 5

