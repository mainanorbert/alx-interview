#!/usr/bin/python3
"""Module that calculates perimeter of the island described in grid"""


def island_perimeter(grid):
    """function that  calculates perimeter of the island described in grid"""
    perimeter = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                if grid[x - 1][y] == 0:
                    perimeter += 1
                if grid[x + 1][y] == 0:
                    perimeter += 1
                if grid[x][y-1] == 0:
                    perimeter += 1
                if grid[x][y + 1] == 0:
                    perimeter += 1
    return perimeter
