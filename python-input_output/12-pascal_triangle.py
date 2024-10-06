#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate. Returns an empty list if n <= 0.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []  # This will hold the rows of Pascal's triangle

    for i in range(n):
        row = [1] * (i + 1)  # Initialize the row with 1s

        # Calculate the values for the inner elements
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)  # Add the completed row to the triangle

    return triangle
