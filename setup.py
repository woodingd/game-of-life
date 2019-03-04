from cell import cell


def setup_grid():
    grid = []
    for row in range(100):
        grid.append([])
        for col in range(100):
            grid[row].append(cell(row, col))
    return grid


def clear_grid(grid):
    for row in range(100):
        for col in range(100):
            grid[row][col].clear()
