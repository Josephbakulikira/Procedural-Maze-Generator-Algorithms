import pygame
from ui.colors import *
from classes.cell import Cell
from constants import *

class HexCell(Cell):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.NorthEast = None
        self.NorthWest = None
        self.SouthEast = None
        self.SouthWest = None

    def SetNeighbours(self):
        self.neighbours = []
        if self.North:
            self.neighbours.append(self.North)
        if self.South:
            self.neighbours.append(self.South)
        if self.NorthEast:
            self.neighbours.append(self.NorthEast)
        if self.NorthWest:
            self.neighbours.append(self.NorthWest)
        if self.SouthEast:
            self.neighbours.append(self.SouthEast)
        if self.SouthWest:
            self.neighbours.append(self.SouthWest)

    def Draw(self, screen, show_color_map, a_size, b_size, w, h, r, c):
        cx = self.size + 3 * self.y * a_size
        cy = b_size + self.x * h
        cy += b_size if (self.y%2)!= 0 else 0

        x_farWest = (cx -self.size) + height/r
        x_nearWest = (cx-a_size) + height/r
        x_nearEast = (cx+a_size) + height/r
        x_farEast = (cx+self.size) + height/r

        y_north = (cy-b_size) + rows
        y_middle = cy + rows
        y_south = (cy+b_size)+ rows

        # if self.SouthWest:
        #     pygame.draw.line(screen, black, (x_farWest, y_middle), (x_nearWest, y_north), 4)
        # if self.NorthWest or self.y == 0:
        #     pygame.draw.line(screen, black, (x_farWest, y_middle), (x_nearWest, y_south), 4)
        # if self.North or self.x == 0:
        #     pygame.draw.line(screen, black, (x_nearWest, y_north), (x_nearEast, y_north), 4)
        # if self.NorthEast or self.y == r-1 or self.x == 0:
        #     pygame.draw.line(screen, black, (x_nearEast, y_north), (x_farEast, y_middle), 4)
        # if self.SouthEast or self.y == r-1 or self.x == c-1:
        #     pygame.draw.line(screen, black, (x_farEast, y_middle), (x_nearEast, y_south), 4)
        # if self.South or self.x == c-1:
        #     pygame.draw.line(screen, black, (x_nearEast, y_south), (x_nearWest, y_south), 4)

        if not self.SouthWest:
            pygame.draw.line(screen, black, (x_farWest, y_middle), (x_nearWest, y_north), 4)
        if not self.NorthWest:
            pygame.draw.line(screen, black, (x_farWest, y_middle), (x_nearWest, y_south), 4)
        if not self.North:
            pygame.draw.line(screen, black, (x_nearWest, y_north), (x_nearEast, y_north), 4)
        if not self.NorthEast:
            pygame.draw.line(screen, black, (x_nearEast, y_north), (x_farEast, y_middle), 4)
        if not self.SouthEast:
            pygame.draw.line(screen, black, (x_farEast, y_middle), (x_nearEast, y_south), 4)
        if not self.South:
            pygame.draw.line(screen, black, (x_nearEast, y_south), (x_nearWest, y_south), 4)
        # if show_color_map:
        #     points = [(x_farWest, y_middle), (x_nearWest, y_north),
        #               (x_nearEast, y_north), (x_farEast, y_middle),
        #               (x_nearEast, y_south), (x_nearWest, y_south)]
        #     pygame.draw.polygon(screen, coffee_brown, points)
