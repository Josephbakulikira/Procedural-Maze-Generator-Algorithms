import pygame
from ui.colors import *
from classes.binaryTree import BinaryTree
from classes.sideWinder import SideWinder
from classes.grid import Grid

width, height = 1000, 800
size = (width, height)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

cell_size = 50
rows = height//cell_size
cols = width//cell_size

binary_tree = BinaryTree(Grid(rows, cols, cell_size))
side_winder = SideWinder(Grid(rows, cols, cell_size))

show_text = False
show_color_map = True

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
                show_color_map = not show_color_map

    binary_tree.Generate(screen, show_text, show_color_map)
    # side_winder.Generate(screen, show_text, show_color_map)

pygame.quit()
