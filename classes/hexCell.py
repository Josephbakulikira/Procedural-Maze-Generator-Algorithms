import pygame
from ui.colors import *
from classes.cell import Cell
from constants import *

pygame.font.init()
text_font = pygame.font.SysFont("Arial", cell_size//3)

class HexCell(Cell):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.NorthEast = None
        self.NorthWest = None
        self.SouthEast = None
        self.SouthWest = None
        self.centerX = 0
        self.centerY = 0

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

    def GetCenter(self):
        return (self.centerX, self.centerY)

    def Draw(self, screen, show_color_map, a_size, b_size, w, h, r, c):
        cx = self.size + 3 * self.y * a_size
        cy = b_size + self.x * h
        cy += b_size if (self.y%2)!= 0 else 0

        x_farWest = (cx -self.size)
        x_nearWest = (cx-a_size)
        x_nearEast = (cx+a_size)
        x_farEast = (cx+self.size)

        y_north = (cy-b_size)
        y_middle = cy
        y_south = (cy+b_size)

        self.centerY = cy
        self.centerX = cx

        color = self.color
        if self.isStartingNode:
            color = yellow
        if self.isCurrent:
            color = navy_blue
        elif self.isgoalNode:
            color = blue


        if self.show_highlight and self.visited:
            points = [(x_farWest, y_middle), (x_nearWest, y_north),
                      (x_nearEast, y_north), (x_farEast, y_middle),
                      (x_nearEast, y_south), (x_nearWest, y_south)]
            pygame.draw.polygon(screen, self.highlight, points)
        elif self.visited:
            points = [(x_farWest, y_middle), (x_nearWest, y_north),
                      (x_nearEast, y_north), (x_farEast, y_middle),
                      (x_nearEast, y_south), (x_nearWest, y_south)]
            pygame.draw.polygon(screen, color, points)
        else:
            points = [(x_farWest, y_middle), (x_nearWest, y_north),
                      (x_nearEast, y_north), (x_farEast, y_middle),
                      (x_nearEast, y_south), (x_nearWest, y_south)]
            pygame.draw.polygon(screen, black, points)

        if self.SouthWest or self.y == 0 or (self.x == c-1 and self.y % 2 != 0):
            pygame.draw.line(screen, black, (x_farWest, y_middle), (x_nearWest, y_south), 4)
        if self.NorthWest or self.y == 0 or (self.x == 0 and self.y % 2 == 0):
            pygame.draw.line(screen, black, (x_farWest, y_middle), (x_nearWest, y_north), 4)
        if self.North or self.x == 0:
            pygame.draw.line(screen, black, (x_nearWest, y_north), (x_nearEast, y_north), 4)

        if self.NorthEast or self.y == r-1 or (self.x == 0 and self.y%2==0):
            pygame.draw.line(screen, black, (x_nearEast, y_north), (x_farEast, y_middle), 4)
        if self.SouthEast or self.y == r-1 or (self.x == c-1 and self.y%2!=0):
            pygame.draw.line(screen, black, (x_farEast, y_middle), (x_nearEast, y_south), 4)
        if self.South or self.x == c-1:
            pygame.draw.line(screen, black, (x_nearEast, y_south), (x_nearWest, y_south), 4)

        if self.show_text:
            text_surface = text_font.render(str(int(self.cost)), True, self.textColor)
            text_rect = text_surface.get_rect(center=(self.centerX , self.centerY))
            screen.blit(text_surface, text_rect)
