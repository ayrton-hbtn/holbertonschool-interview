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
    prev_line = []
    prev_index = 0

    while n >= 2:
        prev_line = triangle[prev_index]
        row = [1]
        for i in range(len(prev_line)):
            try:
                row.append(prev_line[i] + prev_line[i + 1])
            except IndexError:
                row.append(1)
        triangle.append(row)
        prev_index += 1
        n -= 1

    return triangle
