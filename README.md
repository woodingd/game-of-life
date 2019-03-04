# Game of Life
A simple implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) in Python using [Pygame](https://www.pygame.org/news).

# Rules
* Any live cell with fewer than two live neighbours dies, as if by underpopulation.
* Any live cell with two or three live neighbours lives on to the next generation.
* Any live cell with more than three live neighbours dies, as if by overpopulation.
* Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# Controls
The grid starts with two known patterns, a 'Glider' and a 'Blinker'.
Click a cell to mark it as live, click again to mark it as dead.
Clear the screen with the 'C' key.
Stop and start the simulation with the 'Space' key.
