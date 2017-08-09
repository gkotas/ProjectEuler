"""
Poker hands
Problem 54

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand    Player 1             Player 2             Winner
1         5H 5C 6S 7S KD        2C 3S 8S 8D TD        Player 2
        Pair of Fives        Pair of Eights

2         5D 8C 9S JS AC        2C 5C 7D 8S QH        Player 1
        Highest card Ace    Highest card Queen

3         2D 9C AS AH AC        3D 6D 7D TD QD        Player 2
        Three Aces            Flush with Diamonds

4         4D 6S 9H QH QC        3D 6D 7H QD QS        Player 1
        Pair of Queens        Pair of Queens
        Highest card Nine    Highest card Seven

5         2H 2D 4C 4D 4S        3C 3D 3S 9S 9D        Player 1
        Full House            Full House
        With Three Fours    with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each
player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
STRAIGHTS = set([0xedcba, 0xdcba9, 0xcba98, 0xba987, 0xa9876, 0x98765, 0x87654,
                 0x76543, 0x65432])


def getHexDigit(h, n):
    """
    Returns the nth hex digit from the right.
    """
    return (h & (0xf << (4*n))) >> (4*n)


def sortHand(hand):
    """
    Returns 5 digit hex number that correspond to the values of the cards,
    sorted high to low.
    """
    values = []

    # Convert to hex representation
    for value in [c[0] for c in hand]:
        if value == 'A':
            values.append(0xe)
        elif value == 'K':
            values.append(0xd)
        elif value == 'Q':
            values.append(0xc)
        elif value == 'J':
            values.append(0xb)
        elif value == 'T':
            values.append(0xa)
        else:
            values.append(int(value))
    # Sort decending
    values.sort(reverse=True)

    # Concatenate all values together
    concat = 0x0
    for v in values:
        concat = (concat << 4) | v

    return concat



def evalHand(hand):
    """
    Returns a 6 digit hex value corresponding to strength of the hand.
    First digit being type of hand. High Card = 0x0, and Royal Flush = 0x9.
    The next five digits are the card values sorted high to low. 2 = 0x2 and
    Ace = 0xe.
    """
    hex_hand = sortHand(hand)
    suits = [c[1] for c in hand]

    is_flush = (len(set(suits)) == 1)

    # Royal Flush
    if hex_hand == 0xedcba and is_flush:
        return 0x900000 | hex_hand

    # Straight Flush
    elif hex_hand in STRAIGHTS and is_flush:
        return 0x800000 | hex_hand

    # Four of a Kind
    # Hex format: 0xXXXXy or 0xXYYYY
    elif ((getHexDigit(hex_hand, 4) == getHexDigit(hex_hand, 1))
          or (getHexDigit(hex_hand, 3) == getHexDigit(hex_hand, 0))):
        return 0x700000 | hex_hand

    # Full House
    # Hex format: 0xXXXYY or 0xXXYYY
    elif ((getHexDigit(hex_hand, 4) == getHexDigit(hex_hand, 2)
           and getHexDigit(hex_hand, 1) == getHexDigit(hex_hand, 0))
          or (getHexDigit(hex_hand, 4) == getHexDigit(hex_hand, 3)
           and getHexDigit(hex_hand, 2) == getHexDigit(hex_hand, 0))):
        return 0x600000 | hex_hand

    # Flush
    elif is_flush:
        return 0x500000 | hex_hand

    # Straight
    elif hex_hand in STRAIGHTS:
        return 0x400000 | hex_hand

    # Three of a Kind
    # Hex format: 0xXXXYZ or 0xXYYYZ or 0xXYZZZ
    elif (getHexDigit(hex_hand, 4) == getHexDigit(hex_hand, 2)
          or getHexDigit(hex_hand, 3) == getHexDigit(hex_hand, 1)
          or getHexDigit(hex_hand, 2) == getHexDigit(hex_hand, 0)):
        return 0x300000 | hex_hand

    # Two Pair
    # Hex format: 0xXXYYZ or 0xXXYZZ or 0xXYYZZ
    elif ((getHexDigit(hex_hand, 4) == getHexDigit(hex_hand, 3)
           and getHexDigit(hex_hand, 2) == getHexDigit(hex_hand, 1))
          or (getHexDigit(hex_hand, 4) == getHexDigit(hex_hand, 3)
           and getHexDigit(hex_hand, 1) == getHexDigit(hex_hand, 0))
          or (getHexDigit(hex_hand, 3) == getHexDigit(hex_hand, 2)
           and getHexDigit(hex_hand, 1) == getHexDigit(hex_hand, 0))):
        return 0x200000 | hex_hand

    # One Pair
    # Hex format: 0xXXYZW or 0xXYYZW or 0xXYZZW or 0xXYZWW
    elif getHexDigit(hex_hand, 4) == getHexDigit(hex_hand, 3):
        return 0x100000 | hex_hand

    # Move paired number to bits 4 and 3
    elif getHexDigit(hex_hand, 3) == getHexDigit(hex_hand, 2):
        return (0x100000 | getHexDigit(hex_hand, 3) << 16
               | getHexDigit(hex_hand, 2) << 12 | getHexDigit(hex_hand, 4) << 8
               | getHexDigit(hex_hand, 1) << 4 | getHexDigit(hex_hand, 0))

    elif getHexDigit(hex_hand, 2) == getHexDigit(hex_hand, 1):
        return (0x100000 | getHexDigit(hex_hand, 2) << 16
               | getHexDigit(hex_hand, 1) << 12 | getHexDigit(hex_hand, 4) << 8
               | getHexDigit(hex_hand, 3) << 4 | getHexDigit(hex_hand, 0))

    elif getHexDigit(hex_hand, 1) == getHexDigit(hex_hand, 0):
        return (0x100000 | getHexDigit(hex_hand, 1) << 16
               | getHexDigit(hex_hand, 0) << 12 | getHexDigit(hex_hand, 4) << 8
               | getHexDigit(hex_hand, 3) << 4 | getHexDigit(hex_hand, 2))

    return hex_hand


def answer():
    wins = 0
    with open('textfiles/p054_poker.txt') as f:
        for line in f:
            p1 = line.strip()[:14].split()
            p2 = line.strip()[15:].split()

            if evalHand(p1) > evalHand(p2):
                wins += 1

    return wins


if __name__ == "__main__":
    print answer()
