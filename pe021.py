"""
Amicable numbers
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


d_memo = {}


def d(n):
    """
    Returns the sum of the divisors of n.
    """
    if n not in d_memo:
        # Start with 1 so n isn't counted
        total = 1
        # Loop from 2 to sqrt(n)
        for i in xrange(2, int(n**0.5) + 1):
            if n % i == 0:
                total += i
                # Only add the other divisor if it isn't a square
                if i * i != n:
                    total += n/i

        d_memo[n] = total

    return d_memo[n]


def answer():
    # Use dictionary to store which numbers are amicable
    amicable = {}
    for i in xrange(4, 10000):
        if i not in amicable:
            # Make sure d(i) is different from i
            if i == d(d(i)) and i != d(i):
                amicable[i] = True
                amicable[d(i)] = True
    return sum(amicable.keys())


if __name__ == '__main__':
    print answer()
