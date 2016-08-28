"""
Longest Collatz sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def answer():
    max_c = max_i = 0
    for i in xrange(2, 1000000):
        c = collatz(i)
        if c > max_c:
            max_i = i
            max_c = c
    return max_i

collatz_cache = {}
def collatz(n):
    if n == 1:
        return 1

    if n not in collatz_cache:
        if n & 1 == 1:
            collatz_cache[n] = 1 + collatz(3*n + 1)
        else:
            collatz_cache[n] = 1 + collatz(n/2)

    return collatz_cache[n]

if __name__ == '__main__':
    print answer()
