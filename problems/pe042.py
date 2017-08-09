"""
Coded triangle numbers
Problem 42

The nth term of the sequence of triangle numbers is given by, tn = 0.5*n*(n+1);
so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
"""
from common.MiscMath import isTriangular


def wordValue(word):
    """
    Returns the value of a word based on the sum of the alphabetical positions
    of its letters.
    """
    value = 0

    for letter in word:
        value += ord(letter) - ord("A") + 1

    return value


def answer():
    # Read the file and make a list of words
    with open("textfiles/p042_words.txt", "r") as f:
        # Read the line, remove quotes, split at ","
        words = f.readlines()[0].replace("\"", "").split(",")

    count = 0

    for word in words:
        if isTriangular(wordValue(word)):
            count += 1

    return count


if __name__ == "__main__":
    print answer()
