import pygame
from constants import *
from ui.colors import *
from classes.recursiveBacktracker import RecursiveBacktracker
from classes.weightedGrid import WeightedGrid

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

grid = WeightedGrid(rows, cols, cell_size)
grid.ConfigureCells()
recursive_backtracker = RecursiveBacktracker(grid, "GREEN")
recursive_backtracker.starting_node = grid.cells[0][0]
recursive_backtracker.end_node = grid.cells[cols-1][rows-1]
recursive_backtracker.starting_node.isStartingNode = True
recursive_backtracker.end_node.isgoalNode = True

show_text = False
color_mode = False
show_path = False

run = True
while run:
    screen.fill(black)
    # Set Caption and fps
    clock.tick(fps)
    frame_rate = int(clock.get_fps())
    pygame.display.set_caption(f"Maze Generator - FPS: {frame_rate}")

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_h:
                show_text = not show_text
            elif event.key == pygame.K_SPACE:
                color_mode = not color_mode
            elif event.key == pygame.K_s:
                show_path = not show_path

    recursive_backtracker.Generate(screen, show_text, color_mode, show_path)
    # hexGrid.Show(screen, show_text, color_mode, show_path)
    # pygame.display.flip()

pygame.quit()
