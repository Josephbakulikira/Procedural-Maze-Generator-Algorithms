import pygame
import time
from classes.grid import Grid, Update
from classes.mask import Mask, GridMask
from classes.polarGrid import PolarGrid
from classes.weightedGrid import WeightedGrid
from classes.hexGrid import HexGrid
from ui.colors import *
import random

"""
STEPS:

1. Choose a starting point in the field.
2. Randomly choose a wall at that point and carve a passage through to the adjacent cell, 
but only if the adjacent cell has not been visited yet. This becomes the new current cell.
3. If all adjacent cells have been visited, back up to the last cell that has uncarved walls and repeat.
4. The algorithm ends when the process has backed all the way up to the starting point.
"""

class RecursiveBacktracker:
    def __init__(self, grid, path_color):
        self.grid = grid
        self.rows = grid.rows
        self.cols = grid.cols
        self.path_color = path_color
        self.isDone = False
        self.starting_node = None
        self.end_node = None

        if type(self.grid) == Grid:
            self.starting_node = grid.cells[0][0]
            self.starting_node.isStartingNode = True
            self.end_node = grid.cells[self.cols-1][self.rows-1]
            self.end_node.isgoalNode = True
        if path_color == "HSV":
            self.grid.path_color = white
        self.shortest_path = None

    def Generate(self, screen, show_heuristic, show_color_map, show_path):
        if not self.isDone:
            gridtype = "Normal"
            stack = []
            initial_cell = None
            if type(self.grid) == Grid or type(self.grid) == WeightedGrid:
                randomX = random.randint(0, self.cols-1)
                randomY = random.randint(0, self.rows-1)
                initial_cell = self.grid.cells[randomX][randomY]
            elif type(self.grid) == PolarGrid:
                gridtype = "Polar"
                initial_cell = self.grid.GetRandomCell()
            elif type(self.grid) == GridMask:
                initial_cell = self.grid.GetRandomCell()
            elif type(self.grid) == HexGrid:
                gridtype = "Hex"
                randomX = random.randint(0, self.cols-1)
                randomY = random.randint(0, self.rows-1)
                initial_cell = self.grid.cells[randomX][randomY]

            stack.append(initial_cell)

            while len(stack) > 0:
                current = stack[-1]
                neighbours = []
                if type(self.grid) == PolarGrid or type(self.grid) == HexGrid:
                    current.SetNeighbours()
                    neighbours = [cell for cell in current.neighbours if len(cell.connections) == 0]
                else:
                    neighbours = [cell for cell in current.neighbours if len(cell.connections) == 0]

                if len(neighbours) == 0:
                    stack.pop()
                else:
                    neighbour = random.choice(neighbours)
                    Grid.JoinAndDestroyWalls(current, neighbour, gridtype)
                    neighbour.isCurrent = True
                    self.grid.Show(screen, show_heuristic, show_color_map)
                    pygame.display.flip()
                    neighbour.isCurrent = False

                    stack.append(neighbour)

            self.isDone = True
            if type(self.grid) != PolarGrid:
                Update(self, screen, show_heuristic, show_color_map, show_path)
        if type(self.grid) != PolarGrid:
            if show_path:
                self.grid.Show(screen, show_heuristic, show_color_map,self.shortest_path)
            else:
                self.grid.Show(screen, show_heuristic, show_color_map, None)
        else:
            self.grid.Show(screen, show_heuristic, show_color_map, None)
            pygame.display.flip()
