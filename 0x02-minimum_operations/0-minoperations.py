#!/usr/bin/python3
"""Minimum operations"""

from math import ceil


def minOperations(n: int) -> int:
    """
    Given n, calculate the fewest number of operations
    needed to result in exactly n H characters in the file
    using only copy and paste operations
    """
    if n == 1:
        return 0
    h = 'H'
    copy = h[::]
    min_operations = 1
    for i in range(2, n + 1):
        if len(h) >= n:
            break
        if len(h + copy) >= n:
            return min_operations + 1
        if len(h) == 3:
            copy = h[::]
            min_operations += 1
        if len(h) == i / 2 and len(copy) < len(h) / 2:
            copy = h[::]
            min_operations += 1
        h += copy
        min_operations += 1

    return min_operations
