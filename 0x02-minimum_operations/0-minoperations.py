#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n: int) -> int:
    """
    Given n, calculate the fewest number of operations
    needed to result in exactly n H characters in the file
    using only copy and paste operations
    """
    operations = 0
    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n = n / i

    return operations
