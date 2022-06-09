#!/usr/bin/python3
"""Bottom-up dynamic programming"""


def makeChange(coins, total):
    """
    Returns minimum amount of coins needed
    to complete the total.
    If total can't be made from coins, return
    -1.
    """
    count = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            count += total // coin
            total = total % coin

    return count if total == 0 else -1
