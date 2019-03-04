class cell:

    def __init__(self, row, col):
        self.alive = 0
        self.next_state = 0
        self.row = row
        self.col = col
        self.visited = 0

    def is_alive(self):
        return self.alive

    def visit(self):
        self.visited = 1

    def is_visited(self):
        return self.visited

    def set_next_state(self, state):
        self.next_state = state

    def set_state(self):
        self.alive = self.next_state

    def clear(self):
        self.next_state = 0;
        self.alive = 0
        self.visited = 0

    def check_neighbours(self, grid):
        check_north = self.row > 0
        check_east = self.col < 99
        check_south = self.row < 99
        check_west = self.col > 0
        count = 0

        if check_north:
            north = grid[self.row - 1][self.col]
            if north.is_alive():
                count += 1
            if check_west:
                n_west = grid[self.row - 1][self.col - 1]
                if n_west.is_alive():
                    count += 1
            if check_east:
                n_east = grid[self.row - 1][self.col + 1]
                if n_east.is_alive():
                    count += 1
        if check_west:
            west = grid[self.row][self.col - 1]
            if west.is_alive():
                count += 1
        if check_east:
            east = grid[self.row][self.col + 1]
            if east.is_alive():
                count += 1
        if check_south:
            south = grid[self.row + 1][self.col]
            if south.is_alive():
                count += 1
            if check_west:
                s_west = grid[self.row + 1][self.col - 1]
                if s_west.is_alive():
                    count += 1
            if check_east:
                s_east = grid[self.row + 1][self.col + 1]
                if s_east.is_alive():
                    count += 1

        if self.is_alive():
            if count < 2 or count > 3:
                self.set_next_state(0)
            else:
                self.set_next_state(1)
                self.visit()
        else:
            if count == 3:
                self.set_next_state(1)
                self.visit()
