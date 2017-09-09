"""
Odd period square roots
Problem 64

All square roots are periodic when written as continued fractions and can be
written in the form:

sqrt(N) = a0 +           1
               ----------------------
                a1 +        1
                     ----------------
                      a2 +     1
                           ----------
                            a3 + ...

For example, let us consider sqrt(23):

    sqrt(23) = 4 + sqrt(23) - 4 = 4 +      1     = 4 +         1
                                      ----------       ----------------
                                           1               sqrt(23) - 3
                                      ----------       1 + ------------
                                      sqrt(23)-4                 7

If we continue we would get the following expansion:

    sqrt(23) = 4 +            1
                   ------------------------
                    1 +         1
                        -------------------
                         3 +       1
                             --------------
                              1 +     1
                                  ---------
                                   8 + ...

The process can be summarised as follows:

                 1           sqrt(23) + 4        sqrt(23) - 3
    a0 = 4, ------------ =   ------------  = 1 + ------------
            sqrt(23) - 4          7                   7

                 7         7(sqrt(23) + 3)       sqrt(23) - 3
    a1 = 1, ------------ = --------------- = 3 + ------------
            sqrt(23) - 3         14                   2

                 2         2(sqrt(23) + 3)       sqrt(23) - 7
    a2 = 3, ------------ = --------------- = 1 + ------------
            sqrt(23) - 3         14                   7

                 7         7(sqrt(23) + 4)
    a3 = 1, ------------ = --------------- = 8 + sqrt(23) - 4
            sqrt(23) - 4         7

                 1           sqrt(23) + 4        sqrt(23) - 3
    a4 = 8, ------------ =   ------------  = 1 + ------------
            sqrt(23) - 4          7                   7

                 7         7(sqrt(23) + 3)       sqrt(23) - 3
    a5 = 1, ------------ = --------------- = 3 + ------------
            sqrt(23) - 3         14                   2

                 2         2(sqrt(23) + 3)       sqrt(23) - 7
    a6 = 3, ------------ = --------------- = 1 + ------------
            sqrt(23) - 3         14                   7

                 7         7(sqrt(23) + 4)
    a7 = 1, ------------ = --------------- = 8 + sqrt(23) - 4
            sqrt(23) - 4         7

It can be seen that the sequence is repeating. For conciseness, we use the
notation sqrt(23) = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
indefinitely.

The first ten continued fraction representations of (irrational) square roots
are:

    sqrt(2)=[1;(2)], period=1
    sqrt(3)=[1;(1,2)], period=2
    sqrt(5)=[2;(4)], period=1
    sqrt(6)=[2;(2,4)], period=2
    sqrt(7)=[2;(1,1,1,4)], period=4
    sqrt(8)=[2;(1,4)], period=2
    sqrt(10)=[3;(6)], period=1
    sqrt(11)=[3;(3,6)], period=2
    sqrt(12)= [3;(2,6)], period=2
    sqrt(13)=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N <= 13, have an odd period.

How many continued fractions for N <= 10000 have an odd period?
"""


def continuedFractionPeriodLength(x):
    """
    Given a nonsqaure x, return length of the periodic coefficients.
    """
    m = 0
    d = 1
    a = [int(x**0.5)]

    while True:
        m = d*a[-1] - m
        d = (x - m*m)//d
        a.append((a[0] + m)//d)

        # Terminate when last a == 2*a0
        if a[-1] == 2*a[0]:
            # Period doesn't include the first coefficient
            return len(a) - 1


def answer():
    count = 0
    for i in xrange(2, 10001):
        # Skip squares
        if int(i**0.5) == i**0.5:
            continue

        if continuedFractionPeriodLength(i) & 1:
            count += 1

    return count


if __name__ == "__main__":
    print answer()
