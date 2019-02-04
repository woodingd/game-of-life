from cell import cell


def setup_grid():
    grid = []
    for row in range(10):
        grid.append([])
        for col in range(10):
            grid[row].append(cell(row, col))

    return grid
