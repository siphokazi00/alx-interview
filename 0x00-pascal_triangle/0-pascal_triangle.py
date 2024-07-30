#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Get the previous row
        prev_row = triangle[-1]
        # Initialize the new row with 1s on both ends
        row = [1] * (i + 1)

        # Fill in the values in between
        for j in range(1, i):
            row[j] = prev_row[j - 1] + prev_row[j]

        # Append the new row to the triangle
        triangle.append(row)

    return triangle
