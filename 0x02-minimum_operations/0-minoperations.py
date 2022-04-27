#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n: int) -> int:
    """
    Given n, calculate the fewest number of operations
    needed to result in exactly n H characters in the file
    using only copy and paste operations
    """
    first_cases = {
        1: 0,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 5
    }
    for n_value, op in first_cases.items():
        if n_value == n:
            return op
    h = 'HHHHHH'
    copy = 'HHH'
    min_operations = 5
    for i in range(7, n + 1):
        if len(h + copy) >= n:
            return min_operations + 1
        else:
            if len(h) >= i / 2:
                copy = h[::]
                min_operations += 1
        h += copy
        min_operations += 1
        if len(h) >= n:
            break

    return min_operations
