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
    for i in range(1, n + 1):
        if len(h) >= n:
            break
        if len(h + copy) >= n:
            return min_operations + 1
        else:
            if len(h) >= ceil(n / 2) or len(h) == 3:
                copy = h[::]
                min_operations += 1
        h += copy
        min_operations += 1

    return min_operations
