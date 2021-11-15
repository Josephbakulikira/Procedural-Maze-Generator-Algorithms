import pygame
from constants import *
from ui.colors import *
from classes.binaryTree import BinaryTree
from classes.sideWinder import SideWinder
from classes.aldousBroder import AldousBroder
from classes.huntandkill import HuntAndKill
from classes.recursiveBacktracker import RecursiveBacktracker
from classes.kruskal import Kruskals
from classes.wilson import Wilson
from classes.prims import SimplePrims, Prims
from classes.grid import Grid
from classes.growingTree import GrowingTree
from classes.ellers import Ellers
from ui.setup import *
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
kruskal = Kruskals(Kruskals.State(Grid(rows, cols, cell_size)))
simplePrims = SimplePrims(Grid(rows, cols, cell_size), "CYAN")
prims = Prims(Grid(rows, cols, cell_size))
growingTree = GrowingTree(Grid(rows, cols, cell_size), "GREEN")
ellers = Ellers(Grid(rows, cols, cell_size), 0, "RED")

show_text = False
color_mode = False
show_path = False
start = False
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
            if event.key == pygame.K_RETURN:
                start = not start
            elif event.key == pygame.K_h:
                show_text = not show_text
            elif event.key == pygame.K_SPACE:
                color_mode = not color_mode
            elif event.key == pygame.K_s:
                show_path = not show_path
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                rightMouseClicked = True

    if start:
        # wilson.Generate(screen, show_text, color_mode, show_path)
        # binary_tree.Generate(screen, show_text, color_mode, show_path)
        # kruskal.Generate(screen, show_text, color_mode, show_path)
        # side_winder.Generate(screen, show_text, color_mode, show_path)
        # hunt_and_kill.Generate(screen, show_text, color_mode, show_path)
        # aldous_broder.Generate(screen, show_text, color_mode, show_path)
        # recursive_backtracker.Generate(screen, show_text, color_mode, show_path)
        # simplePrims.Generate(screen, show_text, color_mode, show_path)
        # prims.Generate(screen, show_text, color_mode, show_path)
        # growingTree.Generate(screen, show_text, color_mode, show_path)
        ellers.Generate(screen, show_text, color_mode, show_path)
    else:
        PressEnter.Render(screen)

    pygame.display.flip()

pygame.quit()
