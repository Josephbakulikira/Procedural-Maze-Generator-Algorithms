import pygame
from ui.colors import *

class Cell:
    def __init__(self, x, y, size=40):
        self.x = x
        self.y = y
        self.size = size
        self.color= white
        self.wall_color= black
        self.wall_thickness = 2
        self.visited = False

        # Walls -- neighbours
        self.North = None
        self.South = None
        self.East = None
        self.West = None

    def Draw(self, screen, rows, cols):
        x = self.x * self.size
        y = self.y * self.size
        pygame.draw.rect(screen, self.color, [x, y, self.size, self.size])

        if self.North != None or self.y - 1 < 0:
            A = (x, y)
            B = (x + self.size, y)
            pygame.draw.line(screen, self.wall_color, A, B, self.wall_thickness)
        if self.South != None or self.y + 1 >= rows:
            A = (x, y + self.size)
            B = (x + self.size, y + self.size)
            pygame.draw.line(screen, self.wall_color, A, B, self.wall_thickness)
        if self.East != None or self.x + 1 >= cols:
            A = (x + self.size, y)
            B = (x + self.size, y + self.size)
            pygame.draw.line(screen, self.wall_color, A, B, self.wall_thickness)
        if self.West != None or self.x - 1 < 0:
            A = (x, y)
            B = (x, y + self.size)
            pygame.draw.line(screen, self.wall_color, A, B, self.wall_thickness)

    def __repr__(self):
        # DEBUG
        return f"({self.x}, {self.y})"
