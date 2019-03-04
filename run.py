import setup
import pygame


width = 7
height = 7
margin = 1
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
grey = (200, 200, 200)

grid = setup.setup_grid()
grid[1][5].set_next_state(1)
grid[1][5].set_state()
grid[2][6].set_next_state(1)
grid[2][6].set_state()
grid[2][7].set_next_state(1)
grid[2][7].set_state()
grid[1][7].set_next_state(1)
grid[1][7].set_state()
grid[0][7].set_next_state(1)
grid[0][7].set_state()

grid[33][33].set_next_state(1)
grid[33][33].set_state()
grid[33][34].set_next_state(1)
grid[33][34].set_state()
grid[33][35].set_next_state(1)
grid[33][35].set_state()

pygame.init()
screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption("Grid")
done = False
active = False
clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            cell = grid[row][column]
            if cell.is_alive():
                cell.set_next_state(0)
            else:
                cell.set_next_state(1)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                active = not active
            if event.key == pygame.K_c:
                active = False
                setup.clear_grid(grid)

    screen.fill(black)

    for row in range(100):
        for column in range(100):
            cell = grid[row][column]
            if active:
                cell.check_neighbours(grid)
            colour = white
            if cell.is_alive():
                colour = green
            elif cell.is_visited():
                colour = grey
            pygame.draw.rect(screen, colour, [(margin + width) * column + margin,
                                              (margin + height) * row + margin,
                                              width,
                                              height])
    for row in range(100):
        for column in range(100):
            grid[row][column].set_state()

    clock.tick(30)
    pygame.display.flip()

pygame.quit()
