#!/usr/bin/python3
"""
Determines the fewest number of coins needed to meet given total
"""


def makeChange(coins, total):
    """Det the fewest no. of coins needed to meet a given total."""
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total == 0:
            break
        # Use as many of the current coin as possible
        if coin <= total:
            count += total // coin
            total %= coin

    return count if total == 0 else -1
