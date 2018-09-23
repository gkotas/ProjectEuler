"""
Matrix Sum
Problem 345

We define the Matrix Sum of a matrix as the maximum sum of matrix elements with
each element being the only one in his row and column. For example, the Matrix
Sum of the matrix below equals 3315 ( = 863 + 383 + 343 + 959 + 767):

                              7  53 183 439 863
                            497 383 563  79 973
                            287  63 343 169 583
                            627 343 773 959 943
                            767 473 103 699 303

Find the Matrix Sum of:

          7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
        627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
        447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
        217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
        960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
        870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
        973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
        322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
        445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
        414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
        184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
        821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
         34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
        815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
        813 883 451 509 615  77 281 613 459 205 380 274 302  35 805
"""
from common.Primes import factorize


def hungarianStep0(m, zs, zp, cr, cc):
    """
    First step in algorithm. For each row of the matrix, find the smallest
    element and subtract it from every element in its row.  Go to Step 1.
    """
    for r in xrange(len(m)):
        # Find min element
        min = 0
        for c in xrange(len(m)):
            if m[r][c] < m[r][min]:
                min = c

        min = m[r][min]
        # Subtract each element
        for c in xrange(len(m)):
            m[r][c] -= min

    return 1


def zeroStarInRowCol(zs, r, c):
    """
    Returns true if the row or column specified contains a starred zero.
    """
    for i in xrange(len(zs)):
        if zs[r][i] or zs[i][c]:
            return True

    return False


def hungarianStep1(m, zs, zp, cr, cc):
    """
    Second step in algorithm. Find a zero (Z) in the resulting matrix. If there
    is no starred zero in its row or column, star Z. Repeat for each element
    in the matrix. Go to Step 2.
    """
    for r in xrange(len(m)):
        for c in xrange(len(m)):
            if m[r][c] == 0:
                if not zeroStarInRowCol(zs, r, c):
                    zs[r][c] = True

    return 2


def hungarianStep2(m, zs, zp, cr, cc):
    """
    Cover each column containing a starred zero.  If all columns are covered,
    the starred zeros describe a complete set of unique assignments.  In this
    case, Go to Step 7, otherwise, Go to Step 3.
    """
    for c in xrange(len(m)):
        for r in xrange(len(m)):
            if zs[r][c]:
                cc[c] = True
                break

    if all(cc):
        return 6
    else:
        return 3


def hungarianStep3(m, zs, zp, cr, cc):
    """
    Find a noncovered zero and prime it.  If there is no starred zero in the
    row containing this primed zero, Go to Step 4.  Otherwise, cover this row
    and uncover the column containing the starred zero. Continue in this manner
    until there are no uncovered zeros left. Go to Step 5.
    """
    foundZero = True
    while foundZero:
        foundZero = False
        for r in xrange(len(m)):
            # Skip covered rows
            if cr[r]:
                continue

            for c in xrange(len(m)):
                # Skip covered columns
                if cc[c]:
                    continue

                # Find zero and prime it
                if m[r][c] == 0:
                    foundZero = True
                    zp[r][c] = True

                    # Check for starred zero in same row
                    zStarInRow = False
                    for i in xrange(len(m)):
                        if zs[r][i]:
                            zStarInRow = True
                            cr[r] = True
                            cc[i] = False
                            break

                    if not zStarInRow:
                        return 4


    return 5


def hungarianStep4(m, zs, zp, cr, cc):
    """
    Construct a series of alternating primed and starred zeros as follows. Let
    Z0 represent the uncovered primed zero found in Step 3. Let Z1 denote the
    starred zero in the column of Z0 (if any). Let Z2 denote the primed zero in
    the row of Z1 (there will always be one). Continue until the series
    terminates at a primed zero that has no starred zero in its column. Unstar
    each starred zero of the series, star each primed zero of the series, erase
    all primes and uncover every line in the matrix.  Return to Step 2.
    """
    alt_series = []
    # Find the uncovered primed zero
    for r in xrange(len(m)):
        if cr[r]:
            continue

        for c in xrange(len(m)):
            if cc[c]:
                continue

            if zp[r][c]:
                alt_series.append((r, c))

    while True:
        # Find starred zero in previous zero's column
        hasStarredZ = False
        for r in xrange(len(m)):
            if zs[r][alt_series[-1][1]]:
                hasStarredZ = True
                alt_series.append((r, alt_series[-1][1]))
                break

        if hasStarredZ:
            # Find prime zero in previous zero's row
            for c in xrange(len(m)):
                if zp[alt_series[-1][0]][c]:
                    alt_series.append((alt_series[-1][0], c))
                    break

        else:
            prime = True
            for z in alt_series:
                zs[z[0]][z[1]] = prime

                # Alternate the series
                prime = not prime

            # Erase all primed and uncover all
            for r in xrange(len(m)):
                cc[r] = False
                cr[r] = False
                for c in xrange(len(m)):
                    zp[r][c] = False

            return 2


def hungarianStep5(m, zs, zp, cr, cc):
    """
    Find the smallest uncovered value. Add it to every element of each covered
    row, and subtract it from every element of each uncovered column. Return to
    Step 3 without altering any stars, primes, or covered lines.
    """
    # Find min uncovered value
    min = 1000
    for r in xrange(len(m)):
        if cr[r]:
            continue

        for c in xrange(len(m)):
            if cc[c]:
                continue

            if m[r][c] < min:
                min = m[r][c]

    # Add to all elements in covered rows
    for r in xrange(len(m)):
        if cr[r]:
            for c in xrange(len(m)):
                m[r][c] += min

    # Subtract to all elements in uncovered columns
    for c in xrange(len(m)):
        if cc[c]:
            continue

        for r in xrange(len(m)):
            m[r][c] -= min

    return 3


def hungarianSolve(mat):
    cc = [False] * len(mat)
    cr = [False] * len(mat)
    zs = []
    zp = []
    m = []
    for r in xrange(len(mat)):
        zs.append([])
        zp.append([])
        m.append([])
        for c in xrange(len(mat)):
            zs[r].append(False)
            zp[r].append(False)
            m[r].append(mat[r][c])

    step = 0
    while True:
        if step == 0:
            step = hungarianStep0(m, zs, zp, cr, cc)
        elif step == 1:
            step = hungarianStep1(m, zs, zp, cr, cc)
        elif step == 2:
            step = hungarianStep2(m, zs, zp, cr, cc)
        elif step == 3:
            step = hungarianStep3(m, zs, zp, cr, cc)
        elif step == 4:
            step = hungarianStep4(m, zs, zp, cr, cc)
        elif step == 5:
            step = hungarianStep5(m, zs, zp, cr, cc)
        elif step == 6:
            total = 0
            for r in xrange(len(m)):
                for c in xrange(len(m)):
                    if zs[r][c]:
                        total += mat[r][c]
            return total



def answer():
    m = [
    [  7,  53, 183, 439, 863, 497, 383, 563,  79, 973, 287,  63, 343, 169, 583],
    [627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
    [447, 283, 463,  29,  23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
    [217, 623,   3, 399, 853, 407, 103, 983,  89, 463, 290, 516, 212, 462, 350],
    [960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
    [870, 456, 192, 162, 593, 473, 915,  45, 989, 873, 823, 965, 425, 329, 803],
    [973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
    [322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601,  95, 973],
    [445, 721,  11, 525, 473,  65, 511, 164, 138, 672,  18, 428, 154, 448, 848],
    [414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
    [184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
    [821, 461, 843, 513,  17, 901, 711, 993, 293, 157, 274,  94, 192, 156, 574],
    [ 34, 124,   4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
    [815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107],
    [813, 883, 451, 509, 615,  77, 281, 613, 459, 205, 380, 274, 302,  35, 805],
    ]

    # Covert to minimun sum problem.
    for r in xrange(len(m)):
        for c in range(len(m)):
            m[r][c] = 1000 - m[r][c]

    return len(m)*1000 - hungarianSolve(m)



if __name__ == '__main__':
    print answer()
