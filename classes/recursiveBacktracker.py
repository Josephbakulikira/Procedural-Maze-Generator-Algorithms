import pygame
from classes.grid import Grid, Update
from classes.mask import Mask, GridMask
from classes.polarGrid import PolarGrid
from ui.colors import *
import random

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
            stack = []
            initial_cell = None
            if type(self.grid) == Grid:
                randomX = random.randint(0, self.cols-1)
                randomY = random.randint(0, self.rows-1)
                initial_cell = self.grid.cells[randomX][randomY]
            else:
                initial_cell = self.grid.GetRandomCell()

            stack.append(initial_cell)

            while len(stack) > 0:
                current = stack[-1]
                neighbours = []
                if type(self.grid) == PolarGrid:
                    neighbours = [cell for cell in current.GetNeighbours() if len(cell.connections) == 0]
                else:
                    neighbours = [cell for cell in current.neighbours if len(cell.connections) == 0]

                if len(neighbours) == 0:
                    stack.pop()
                else:
                    neighbour = random.choice(neighbours)
                    Grid.JoinAndDestroyWalls(current, neighbour)
                    neighbour.isCurrent = True

                    self.grid.Show(screen, show_heuristic, show_color_map)
                    pygame.display.flip()

                    neighbour.isCurrent = False
                    stack.append(neighbour)

            self.isDone = True
            if type(self.grid) != PolarGrid:
                Update(self, screen, show_heuristic, show_color_map, show_path)

        if show_path and type(self.grid) != PolarGrid:
            self.grid.Show(screen, show_heuristic, show_color_map,self.shortest_path)
        else:
            self.grid.Show(screen, show_heuristic, show_color_map, None)
        pygame.display.flip()
