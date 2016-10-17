"""
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""
# Constants
ONE = 3
TWO = 3
THREE = 5
FOUR = 4
FIVE = 4
SIX = 3
SEVEN = 5
EIGHT = 5
NINE = 4
TEN = 3
ELEVEN = 6
TWELVE = 6
THIRTEEN = 8
FOURTEEN = 8
FIFTEEN = 7
SIXTEEN = 7
SEVENTEEN = 9
EIGHTEEN = 8
NINETEEN = 8
TWENTY = 6
THIRTY = 6
FORTY = 5
FIFTY = 5
SIXTY = 5
SEVENTY = 7
EIGHTY = 6
NINETY = 6
HUNDRED = 7
AND = 3
THOUSAND = 8


def answer():
    total = 0
    # Numbers 1-9 occur 9 times every hundred + 100 every hundred
    total += ONE*(9*10 + 100 + 1)  # + One thousand
    total += TWO*(9*10 + 100)
    total += THREE*(9*10 + 100)
    total += FOUR*(9*10 + 100)
    total += FIVE*(9*10 + 100)
    total += SIX*(9*10 + 100)
    total += SEVEN*(9*10 + 100)
    total += EIGHT*(9*10 + 100)
    total += NINE*(9*10 + 100)

    # Numbers 10-19 occur once every hundred
    total += TEN*(10)
    total += ELEVEN*(10)
    total += TWELVE*(10)
    total += THIRTEEN*(10)
    total += FOURTEEN*(10)
    total += FIFTEEN*(10)
    total += SIXTEEN*(10)
    total += SEVENTEEN*(10)
    total += EIGHTEEN*(10)
    total += NINETEEN*(10)

    # Tens occur ten times every hundred
    total += TWENTY*(10*10)
    total += THIRTY*(10*10)
    total += FORTY*(10*10)
    total += FIFTY*(10*10)
    total += SIXTY*(10*10)
    total += SEVENTY*(10*10)
    total += EIGHTY*(10*10)
    total += NINETY*(10*10)

    # Hundred occurs 100 times for every hundred except the first hundred
    total += HUNDRED*(9*100)

    # And occurs 99 times ever hundred except the first hundres
    total += AND*(99*9)

    # Thousand occurs once
    total += THOUSAND
    return total


if __name__ == '__main__':
    print answer()
