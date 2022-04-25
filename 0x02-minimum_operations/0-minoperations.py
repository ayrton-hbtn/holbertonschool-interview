#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    """
    Given n, calculate the fewest number of operations
    needed to result in exactly n H characters in the file
    using only copy and paste operations
    """
    h = 'H'
    copy = h
    num_operations = 0
    print(f'h: {h} - operations: {num_operations} - copy: {copy}')
    while len(h) < n:
        if len(h + copy) >= n:
            print(f'h: {h + copy} - operations: {num_operations + 1} - copy: {copy}')
            return num_operations + 1
        if n % 2 == 1 and n % 3 == 0 and len(h) == 2:
            h += copy
            num_operations += 1
            continue
        elif len(h + copy) >= n - len(copy):
            h += copy
            num_operations += 1
            continue
        copy = h
        h += copy
        num_operations += 2
        print(f'h: {h} - operations: {num_operations} - copy: {copy}')
    return num_operations
