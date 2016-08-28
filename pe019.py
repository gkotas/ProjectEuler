"""
Counting Sundays
Problem 19

You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""

def answer():
    total = 0
    # Starting days in the year 1899
    # Saturday = 0, Friday = 6
    months = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]

    # Start in the year 1901
    for year in xrange(1, 100):
        for month in xrange(12):
            # (Day + Day in 1899 + Year + Leap Years) % 7 = Day of Week
            if (1 + months[month] + year + year/4) % 7 == 1:
                total += 1
    return total

if __name__ == '__main__':
    print answer()
