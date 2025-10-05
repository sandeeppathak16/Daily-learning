from copy import deepcopy

def cherry_pickup(grid):
    rows = len(grid)
    cols = len(grid[0])

    copy_grid = deepcopy(grid)

    # Recursion
    def recursion_for_down(row, col):
        if row == rows - 1 and col == cols - 1:
            if grid[row][col] == -1:
                grid[:] = deepcopy(copy_grid)
                return 0

            return grid[row][col]

        if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 1:
            grid[:] = deepcopy(copy_grid)
            return 0

        grid[row][col] = 0

        return grid[row][col] + max(recursion_for_down(row + 1, col), recursion_for_down(row, col + 1))

    def recursion_for_up(row, col, grid):
        if row == 0 and col == 0:
            return grid[row][col]

        if row < 0 or col < 0 or grid[row][col] == 1:
            grid = copy_grid[:]
            return 0

        if grid[row][col] == 1:
            grid[row][col] = 0

        return grid[row][col] + max(recursion_for_up(row + 1, col, grid), recursion_for_up(row + 1, col + 1, grid))

    down_pick = recursion_for_down(0, 0)
    print(down_pick)
    print(grid)


grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]

print(cherry_pickup(grid))
