import pygame
from constants import *
from ui.colors import *
from classes.recursiveBacktracker import RecursiveBacktracker
from classes.polarGrid import PolarGrid
# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

polarGrid = PolarGrid(8, 1, cell_size)
polarGrid.cells = polarGrid.PrepareGrid()
polarGrid.ConfigureCells()
recursive_backtracker = RecursiveBacktracker(polarGrid, "PURPLE")
recursive_backtracker.starting_node = polarGrid.cells[0][0]
recursive_backtracker.starting_node.isStartingNode = True
recursive_backtracker.end_node = polarGrid.cells[0][0]
recursive_backtracker.end_node.isgoalNode = True

show_text = False
color_mode = False
show_path = False

run = True
while run:
    screen.fill(white)
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


pygame.quit()
