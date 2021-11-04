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

cell_size = 40
rows = height//cell_size
cols = width//cell_size

binary_tree = BinaryTree(Grid(rows, cols, cell_size))
side_winder = SideWinder(Grid(rows, cols, cell_size))

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

    # binary_tree.Generate(screen)
    side_winder.Generate(screen)

pygame.quit()
