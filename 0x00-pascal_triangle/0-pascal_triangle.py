#!/usr/bin/python3
"""
Displays Pascal's triangle
"""
def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # Start each row with 1
        previous_row = triangle[-1]  # Get the last row from the triangle

        # Compute the values in between the 1s
        for j in range(1, i):
            row.append(previous_row[j - 1] + previous_row[j])

        row.append(1)  # End each row with 1
        triangle.append(row)  # Add the row to the triangle

    return triangle
