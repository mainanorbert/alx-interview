#!/usr/bin/python3


def island_perimeter(grid):

    perimeter = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                perimeter += 4
                if x > 1 and grid[x + 1][y] == 1:
                    perimeter = perimeter - 2
                if y > 1 and grid[x][y + 1] == 1:
                    perimeter = perimeter - 2
    return perimeter


grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
print(island_perimeter(grid))