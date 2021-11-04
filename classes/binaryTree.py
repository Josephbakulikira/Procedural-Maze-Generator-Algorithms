import pygame
from classes.grid import Grid
import random

class BinaryTree:
    def __init__(self, grid):
        self.grid = grid
        self.isDone = False

    def Generate(self, screen):
        if not self.isDone:
            for x in range(self.grid.cols):
                for y in range(self.grid.rows):
                    neighbours = []
                    # Check two neighbours
                    # for us we gonna check only for north and south
                    if self.grid.cells[x][y].North != None:
                        neighbours.append(self.grid.cells[x][y].North)
                    if self.grid.cells[x][y].East != None:
                        neighbours.append(self.grid.cells[x][y].East)

                    choice = None
                    if len(neighbours) > 0:
                        choice = random.choice(neighbours)

                    if choice != None:
                        Grid.Deconnect(self.grid.cells[x][y], choice)

                    self.grid.Show(screen)
                    pygame.display.flip()
            self.isDone = True
