"""
Integer right triangles
Problem 39

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""
from common.Primes import isCoprime


def answer():
    # Dictionary to hold counts of multiples of triples
    counts = {}

    # Use Euclid's Formula to generate Pythagoreon Triples
    for m in xrange(2, 22):
        # If m is even, then n needs to be odd or vise versa
        n_start = m % 2 + 1
        for n in xrange(n_start, m, 2):
            # m and n need to be coprime
            if not isCoprime(m, n):
                continue

            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            perimeter = a + b + c
            if perimeter > 1000:
                # Too big and only going to get bigger, move on to next m value
                break

            # Got a new triple, add its multiples to the dictionary
            for multiple in xrange(perimeter, 1000, perimeter):
                if multiple in counts:
                    counts[multiple] += 1
                else:
                    counts[multiple] = 1

    # Find which perimeter has the greatest count
    greatest = 0
    perimeter = 0
    for key in counts:
        if counts[key] > greatest:
            greatest = counts[key]
            perimeter = key

    return perimeter


if __name__ == "__main__":
    print answer()
