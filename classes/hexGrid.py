import pygame
import math
from ui.colors import *
from classes.grid import Grid
from classes.hexCell import HexCell
from constants import *

class HexGrid(Grid):
    def __init__(self, rows, cols, cell_size):
        super().__init__(rows, cols, cell_size)

    def PrepareGrid(self):
        for x in range(self.cols):
            for y in range(self.rows):
                self.cells[x][y] = HexCell(x, y, self.cell_size)

    def ConfigureCells(self):
        for x in range(self.cols):
            for y in range(self.rows):
                north_diagonal, south_diagonal = 0, 0
                if y%2 == 0:
                    north_diagonal = x - 1
                    south_diagonal = x
                else:
                    north_diagonal = x
                    south_diagonal = x + 1
                current = self.cells[x][y]

                if x-1 >= 0:
                    current.North = self.cells[x - 1][y]
                if y+1 < self.rows and (south_diagonal < self.cols and south_diagonal >= 0):
                    current.SouthEast = self.cells[south_diagonal][y+1]
                if y+1 < self.rows and (north_diagonal >= 0 and north_diagonal < self.cols):
                    current.NorthEast = self.cells[north_diagonal][y+1]

                if y-1 >= 0 and (north_diagonal >= 0 and north_diagonal < self.cols):
                    current.NorthWest = self.cells[north_diagonal][y-1]
                if y-1 < self.rows and (south_diagonal < self.cols and south_diagonal >= 0):
                    current.SouthWest = self.cells[south_diagonal][y-1]
                if x+1 < self.cols:
                    current.South = self.cells[x+1][y]


    def Show(self, screen, show_heuristic, show_color_map, shortest_path = None):
        a_size = self.cell_size /2
        b_size = self.cell_size * math.sqrt(3)/2

        w = self.cell_size * 2
        h = b_size * 2

        for x in range(self.cols):
            for y in range(self.rows):
                self.cells[x][y].Draw(screen, show_color_map, a_size, b_size, w, h, self.rows, self.cols)
