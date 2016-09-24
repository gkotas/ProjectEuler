"""
Names scores
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

def answer():
    # Read the file and make a list of names
    with open("names.txt", "r") as f:
        # Read the line, drop the last character, remove quotes and split at ","
        names = f.readlines()[0][:-1].replace("\"", "").split(",")

    # Sort the names
    sorted_names = sorted(names)

    total = 0
    for i in xrange(len(names)):
        # Get the score of each name
        # ord("A") - 64 = 1
        score = 0
        for letter in sorted_names[i]:
            score += ord(letter) - 64
        total += (i + 1)*score

    return total

if __name__ == '__main__':
    print answer()
