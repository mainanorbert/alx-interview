#!/usr/bin/python3
"""module that returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """function that returns the perimeter of the island described in grid"""
    perimeter = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                perimeter += 4
                if grid[x + 1][y] == 1:
                    perimeter = perimeter - 2
                if grid[x][y + 1] == 1:
                    perimeter = perimeter - 2
    return perimeter
