import pygame
from constants import *
from ui.colors import *
from classes.binaryTree import BinaryTree
from classes.sideWinder import SideWinder
from classes.aldousBroder import AldousBroder
from classes.huntandkill import HuntAndKill
from classes.recursiveBacktracker import RecursiveBacktracker
from classes.wilson import Wilson
from classes.grid import Grid

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

binary_tree = BinaryTree(Grid(rows, cols, cell_size), "GREEN")
wilson = Wilson(Grid(rows, cols, cell_size), "PURPLE_E")
side_winder = SideWinder(Grid(rows, cols, cell_size), "BLUE")
hunt_and_kill = HuntAndKill(Grid(rows, cols, cell_size), "RED")
aldous_broder = AldousBroder(Grid(rows, cols, cell_size), "GREEN")
recursive_backtracker = RecursiveBacktracker(Grid(rows, cols, cell_size), "BLUE")

show_text = False
color_mode = False
show_path = False

run = True
while run:
    # screen.fill(white)

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

    # wilson.Generate(screen, show_text, color_mode, show_path)
    binary_tree.Generate(screen, show_text, color_mode, show_path)
    # side_winder.Generate(screen, show_text, color_mode, show_path)
    # hunt_and_kill.Generate(screen, show_text, color_mode, show_path)
    # aldous_broder.Generate(screen, show_text, color_mode, show_path)
    # recursive_backtracker.Generate(screen, show_text, color_mode, show_path)

pygame.quit()
