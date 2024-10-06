#!/usr/bin/python3
"""Module to generate Pascal's triangle."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Create a new row with `i + 1` elements initialized to 1
        row = [1] * (i + 1)
        if i > 1:
            # Update the inner elements of the row
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
