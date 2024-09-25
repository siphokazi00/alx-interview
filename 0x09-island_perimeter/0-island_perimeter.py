#!/usr/bin/python3
def island_perimeter(grid):
    perimeter = 0

    # Number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Each land cell starts with a perimeter of 4
                perimeter += 4

                # Check if the cell above is also land (subtract 2 if true)
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2

                # Check if cell to the left is also land (subtract 2 if true)
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2

    return perimeter
