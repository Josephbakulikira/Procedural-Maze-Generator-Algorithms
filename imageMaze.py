import pygame
from constants import *
from ui.colors import *
from classes.recursiveBacktracker import RecursiveBacktracker
from classes.grid import Grid
from classes.mask import Mask, GridMask
import cv2

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

image = cv2.imread("./images/polygon.png")

show_text = False
color_mode = False
show_path = False

mask = Mask(rows, cols)
for i in range(rows):
    for j in range(cols):

        if image[j*cell_size][i*cell_size][0] == 255:
            mask.boolGrid[i][j] = False

maskGrid = GridMask(rows, cols, cell_size, mask)
maskGrid.PrepareGrid()

recursive_backtracker = RecursiveBacktracker(maskGrid, "PURPLE_E")
recursive_backtracker.starting_node = maskGrid.cells[cols//2][rows//2]
recursive_backtracker.starting_node.isStartingNode = True
recursive_backtracker.end_node = maskGrid.cells[cols//2][0]
recursive_backtracker.end_node.isgoalNode = True

run = True
while run:
    #screen.fill(black)

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
