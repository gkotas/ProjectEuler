"""
File that holds all functionality dealing with primes.

Functions:
    xprime(n)   - Generator that wraps the _optimizedSeiveOfEratosthenes()
                  to allow it to terminate once the prime is greater than n.
                  Name coming from xrange.
    nthPrime(n) - Returns the nth prime.

Private Functions:
    _optimizedSeiveOfEratosthenes() - Generator function that yields primes
                                         indefinately.
"""
import itertools

# Global Variable
# Acts as a memoizing cache
primes_list = [2, 3]

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

def xprime(n):
    """
    Generator that yields all primes less than or equal to n.
    """
    for prime in _optimizedSeiveOfEratosthenes():
        if prime > n:
            break
        
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