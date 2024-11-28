#!/usr/bin/python3
"""
Determines the fewest number of coins needed to meet given total
"""
def makeChange(coins, total):
    """Det the fewest no. of coins needed to meet a given total."""
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins for each value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Loop through each coin
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
