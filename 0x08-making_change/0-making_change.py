#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total
    """
    coins.sort(reverse=True)
    count = 0
    change = 0
    for coin in coins:
        try:
            if total % change in coins:
                return count + 1
        except ZeroDivisionError:
            pass
        if change + coin > total:
            continue
        while change + coin <= total:
            change += coin
            count += 1
        if change == total:
            break

    if change != total:
        return -1
    return count
