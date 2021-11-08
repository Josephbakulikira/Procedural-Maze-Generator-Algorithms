import pygame
from classes.grid import Grid, Update
from ui.colors import *
import random

class BinaryTree:
    def __init__(self, grid, path_color="BLUE"):
        self.grid = grid
        self.isDone = False
        self.starting_node = grid.cells[0][0]
        self.starting_node.isStartingNode = True
        self.end_node = grid.cells[self.grid.cols-1][self.grid.rows-1]
        self.end_node.isgoalNode = True
        self.show_path = True
        self.path_color = path_color
        self.shortest_path = None
        if path_color == "HSV":
            self.grid.path_color = white

    def Generate(self, screen, show_heuristic, show_color_map,show_path):
        if not self.isDone:
            for x in range(self.grid.cols):
                for y in range(self.grid.rows):
                    neighbours = []
                    self.grid.cells[x][y].isCurrent = True
                    # Check two neighbours
                    # check  for north and south Neighbours
                    if self.grid.cells[x][y].North != None:
                        neighbours.append(self.grid.cells[x][y].North)
                    if self.grid.cells[x][y].East != None:
                        neighbours.append(self.grid.cells[x][y].East)

                    # pick a random neighbour
                    # if any in the neighbours list
                    choice = None
                    if len(neighbours) > 0:
                        choice = random.choice(neighbours)

                    if choice != None:
                        Grid.JoinAndDestroyWalls(self.grid.cells[x][y], choice)

                    self.grid.Show(screen, show_heuristic, show_color_map)
                    self.grid.cells[x][y].isCurrent = False
                    pygame.display.flip()

            self.isDone = True
            Update(self, screen, show_heuristic, show_color_map, show_path)

        if show_path:
            self.grid.Show(screen, show_heuristic, show_color_map, self.shortest_path)
        else:
            self.grid.Show(screen, show_heuristic, show_color_map)
        pygame.display.flip()
