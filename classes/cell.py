import pygame
from ui.colors import *
from classes.heuristic import Heuristic
from constants import *

pygame.font.init()
text_font = pygame.font.SysFont("Arial", cell_size//3)
offset = 0

class Cell:
    def __init__(self, x, y, size=40):
        self.x = x
        self.y = y

        self.cost = 0
        self.isgoalNode = False
        self.isStartingNode = False
        self.isCurrent = False
        self.isPath = False
        self.show_path = False
        self.highlight = white

        self.show_highlight = False
        self.size = size
        self.color= white
        self.wall_color= black
        self.wall_thickness = 4
        self.visited = False
        self.connections = []
        self.neighbours = []
        self.isAvailable = True
        # Walls -- neighbours
        self.North = None
        self.South = None
        self.East = None
        self.West = None

        self.textColor = (0, 0, 0)
        self.show_text = True

    def CalculateHeuristic(self, rows, cols):
        h_distances = Heuristic(rows, cols)
        frontier = [self]
        while len(frontier) > 0:
            new_frontier = []
            for c in frontier:
                for cell in c.connections:
                    if h_distances.GetRecord(cell):
                        continue
                    val = 0 if h_distances.GetRecord(c) == None else h_distances.GetRecord(c)
                    h_distances.SetRecord(cell, val+1)
                    new_frontier.append(cell)

            frontier = new_frontier
        h_distances.SetRecord(self, 0)
        return h_distances

    def IsConneted(self, cell):
        if cell != None:
            if cell in self.connections and self in cell.connections:
                return True
            else:
                return False

    def Draw(self, screen, rows, cols):
        x = self.x * self.size
        y = self.y * self.size

        if not self.visited or not self.isAvailable:
            pygame.draw.rect(screen, black, [x, y, self.size-offset, self.size-offset])
        else:
            color = self.color
            if self.isStartingNode:
                color = yellow
            if self.isCurrent:
                color = navy_blue
            elif self.isgoalNode:
                color = blue
            pygame.draw.rect(screen, color, [x, y, self.size-offset, self.size-offset])

            if self.show_highlight:
                pygame.draw.rect(screen, self.highlight, [x, y, self.size-offset, self.size-offset])

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

        if self.show_text:
            text_surface = text_font.render(str(int(self.cost)), True, self.textColor)
            text_rect = text_surface.get_rect(center=(x + self.size//2, y + self.size/2))
            screen.blit(text_surface, text_rect)

    def __repr__(self):
        # DEBUG
        return f"({self.x}, {self.y}, {id(self)})"
