#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """
    returns a Pascal's Triangle
    of size 'n'
    """

    if n <= 0:
        return []

    triangle = [[1]]
    prev = []
    row = [1]
    current = 0

    while n >= 2:
        prev = triangle[current]
        for i in range(len(prev)):
            try:
                row.append(prev[i] + prev[i + 1])
            except IndexError:
                row.append(1)
        triangle.append(row)
        row = [1]
        current += 1
        n -= 1

    return triangle
