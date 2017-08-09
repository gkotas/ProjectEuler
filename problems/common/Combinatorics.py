"""
Flie that holds all functionality dealing with combinatorics.

Functions:
    nCr(n, r)   - Memoized binomial coefficient function.
    f(n)        - Memoized factorial function.
    fib(n)      - Memoized Fibonacci sequence.

Private Functions:

"""
##### Private Functions #######################################################
nCr_memo = {}
f_memo = {}
fib_memo = {
    1: 1,
    2: 1,
}


##### Public Functions ########################################################
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


def f(n):
    """
    Memoized factorial function.
    """
    if n < 2:
        return 1

    if n not in f_memo:
        f_memo[n] = n*f(n-1)

    return f_memo[n]


def fib(n):
    """
    Returns the nth Fibonacci number.
    """
    if n not in fib_memo:
        fib_memo[n] = fib_memo[n - 1] + fib_memo[n - 2]

    return fib_memo[n]
