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
                current = self.cells[x][y]
                row, col = current.x, current.y
                north_diagonal, south_diagonal = 0, 0

                if (col%2) == 0:
                    north_diagonal = row - 1
                    south_diagonal = row
                else:
                    north_diagonal = row
                    south_diagonal = row + 1

                if row - 1 >= 0:
                    current.North = self.cells[row - 1][col]
                if north_diagonal >= 0 and north_diagonal < self.cols:
                    if col - 1 >= 0 :
                        current.NorthWest = self.cells[north_diagonal][col-1]
                if north_diagonal >= 0 and north_diagonal < self.cols:
                    if col + 1 < self.rows:
                        current.NorthEast = self.cells[north_diagonal][col+1]

                if row + 1 < self.cols:
                    current.South = self.cells[row+1][col]
                if south_diagonal >= 0 and south_diagonal < self.cols:
                    if col + 1 < self.rows :
                        current.SouthEast = self.cells[south_diagonal][col+1]
                if south_diagonal >= 0 and south_diagonal < self.cols:
                    if col - 1 >= 0 :
                        current.SouthWest = self.cells[south_diagonal][col-1]

    def Show(self, screen, show_heuristic, show_color_map, shortest_path = None):
        a_size = self.cell_size /2
        b_size = self.cell_size * math.sqrt(3)/2

        w = self.cell_size * 2
        h = b_size * 2

        if not self.isSorted and shortest_path:
            for x in range(self.cols):
                for y in range(self.rows):
                    if shortest_path.cells_record[x][y]:
                        val = shortest_path.cells_record[x][y]
                        self.path_values.append(val)
                        self.path[str(val)] = self.cells[x][y]
            self.path_values = sorted(self.path_values)
            self.isSorted = True

        for x in range(self.cols):
            for y in range(self.rows):
                self.cells[x][y].show_text = show_heuristic
                self.cells[x][y].show_highlight = show_color_map
                self.cells[x][y].Draw(screen, show_color_map, a_size, b_size, w, h, self.rows, self.cols)

        if shortest_path:
            for i in range(len(self.path_values)-1):
                pygame.draw.line(screen, orange, self.path[str(self.path_values[i])].GetCenter(), self.path[str(self.path_values[i+1])].GetCenter(), 2)
                pygame.draw.circle(screen, orange, self.path[str(self.path_values[i])].GetCenter(), self.cell_size//6)
