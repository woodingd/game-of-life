import setup


grid = setup.setup_grid()

grid[0][1].set_next_state(1)
grid[1][1].set_next_state(1)
grid[2][1].set_next_state(1)
grid[0][1].set_state()
grid[1][1].set_state()
grid[2][1].set_state()

iterations = 0

while iterations < 10:
    iterations += 1

    for i in range(10):
        print(grid[i])

    for l in grid:
        for c in l:
            c.check_neighbours(grid)

    for l in grid:
        for c in l:
            c.set_state()

    print("------------------------------")