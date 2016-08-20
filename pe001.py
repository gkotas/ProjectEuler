"""
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multipleSum(multiple, limit):
    """
    Calculates sum of multiples that are strictly less than the limit
    """
    num_of_terms = (limit - 1) // multiple
    max_multiple = num_of_terms * multiple
    
    return num_of_terms*(multiple + max_multiple) / 2

def answer():
    # Sum of Multiples of 3 and 5 == Sum of Multiples of 3
    #    + Sum of Multiples of 5 - Sum of Multiples of 15
    return multipleSum(3, 1000) + multipleSum(5, 1000) - multipleSum(15, 1000)

if __name__ == "__main__":
    print answer()