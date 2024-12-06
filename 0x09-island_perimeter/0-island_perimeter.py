#!/usr/bin/python3
"""Calculate Island Perimeter"""


def island_perimeter(grid):
    """
    Computes perimeter of an island with no water.
    iterate through the grid
    find all the squares without water
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    x = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                i == x - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
