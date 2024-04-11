#!/usr/bin/python3
"""
function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal's triangle of n
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle of size n.

    Parameters:
    n (int): The number of rows in the triangle.

    Returns:
    list of lists: The Pascal's triangle.
    """
    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row
    triangle = [[1]]

    # Generate subsequent rows
    for i in range(1, n):
        # Create a new row
        row = [1]

        # Fill in the middle elements of the row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # Add the last element of the row
        row.append(1)

        # Append the row to the triangle
        triangle.append(row)

    return triangle
