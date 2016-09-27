"""
File that holds all functionality dealing with primes.
Functions:
    xprime([start,] end)
                 - Generator that wraps the _optimizedSeiveOfEratosthenes()
                   to allow it to terminate once the prime is greater than end.
                   Name coming from xrange.
    nthPrime(n)  - Returns the nth prime number.
    isPrime(n)   - Determines if n is prime or not.
    factorize(n) - Returns list of all prime factors.
    numberOfDivisors(n)
                 - Returns number of divisors of n.

Private Functions:
    _optimizedSeiveOfEratosthenes() - Generator function that yields primes
                                      indefinately.
"""
import itertools
##### Private Functions ########################################################

def _optimizedSeiveOfEratosthenes():
    not_primes = {}
    yield 2

    # Loop through all odd numbers forever
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = not_primes.pop(q, None)
        if p is None:
            # q isn't in not_primes, so it's prime
            # Mark q^2 as not prime, and q as it's first prime factor
            not_primes[q*q] = q
            yield q
        else:
            # q is not ptime
            # Store the next odd, unknown not_prime in the form of N*p + q
            x = p + q
            while x in not_primes or not (x&1):
                x += p
            not_primes[x] = p

##### Public Functions #########################################################

def xprime(start, end=None):
    """
    Generator that yields all primes less than or equal to end, starting with 2
    or start if 2 args are specified.
    """
    # If only one arg is specified, it's the end
    if end == None:
        start, end = 0, start

    for prime in _optimizedSeiveOfEratosthenes():
        if prime > end:
            break

        if prime > start:
            yield prime

def nthPrime(n):
    """
    Counts primes given by _optimizedSeiveOfEratosthenes() and returns the
    nth one.
    """
    for prime in _optimizedSeiveOfEratosthenes():
        n -= 1

        if n == 0:
            return prime

def isPrime(n):
    """
    Determines if n is prime.
    """
    for prime in _optimizedSeiveOfEratosthenes():
        if prime > n:
            return False

        if prime == n:
            return True

def factorize(n):
    """
    Returns a list of all the prime factors and their exponents.
    """
    prime_factors = []

    for p in xprime(n**.5):
        exp = 0
        while n % p == 0:
            exp += 1
            n /= p

        if exp > 0:
            prime_factors.append((p, exp))

    return prime_factors

def numberOfDivisors(n):
    """
    Returns the total number of divisors of n.
    """
    total = 1
    for p in factorize(n):
        total *= p[1] + 1

    return total
