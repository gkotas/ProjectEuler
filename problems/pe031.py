"""
Coin sums
Problem 31

In England the currency is made up of pound, and pence, p, and there are
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, 100p and 200p.

It is possible to make 200p in the following way:

    1*100p + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p

How many different ways can 200p be made using any number of coins?
"""


def answer():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    return recurse(200, coins)


def recurse(money, coins):
    # IF we get to 0p, that means its a valid partition
    if money == 0:
        return 1

    # If there are no coins left to add or the money is negative, that means
    # not a valid partition
    if len(coins) == 0 or money < 0:
        return 0

    # Either we can add the coin and deduct the money left or we can skip this
    # coin. Add these two possiblities.
    return recurse(money - coins[0], coins) + recurse(money, coins[1:])


if __name__ == "__main__":
    print answer()
