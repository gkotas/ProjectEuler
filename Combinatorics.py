"""
Flie that holds all functionality dealing with combinatorics.

Functions:
    nCr(n, r)   - Memoized binomial coefficient function.
    f(n)        - Memoized factorial function.

Private Functions:

"""

##### Private Functions ########################################################


##### Public Functions #########################################################
nCr_memo = {}
def nCr(n, r):
    """
    Memoized binomial coefficient function.
    """
    if (n, r) not in nCr_memo:
        c = n - r
        if c < r:
            c, r = r, c

        num = den = 1

        for i in range(r, n):
            num *= (i + 1)

        for i in range(2, c + 1):
            den *= i

        nCr_memo[(n, r)] = num // den

    return nCr_memo[(n, r)]

f_memo = {}
def f(n):
    """
    Memoized factorial function.
    """
    if n < 2:
        return 1

    if n not in f_memo:
        f_memo[n] = n*f(n-1)

    return f_memo[n]
