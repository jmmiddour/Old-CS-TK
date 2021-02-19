#!/bin/python

import sys


# Need to find out how many ways to make change based on the given amount
# Use a counting sort method to iterate through the denominations and see how many of each
# Need to count all the ways that change can be made.
# for the amount entered
#   If amount is 0 return 0
#   If amount is > 0:
#     Divide by the highest denomination 1st
#     Divide by the rest of the denomination
#     Need to have a bucket to count up the ways that change can be made.
from pdb import set_trace as st

def making_change(amount, denominations):
    num_dems = len(denominations)
    times = [0]

    for coins in denominations:
        for num in range(amount):
            if amount >= coins:
                print(coins)
                try:
                    if num >= coins:
                        times += times[num - coins]
                        print(times)
                except:
                  st()

    return sum(times)


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")