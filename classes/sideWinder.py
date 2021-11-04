import pygame
from classes.grid import Grid
from ui.colors import *
import random
import time

class SideWinder:
    def __init__(self, grid):
        self.grid = grid
        self.isDone = False
        self.speed = 1
        self.max_speed = 1
    def Generate(self, screen):
        if not self.isDone:
            for y in range(self.grid.rows):
                history = []
                for x in range(self.grid.cols):
                    current = self.grid.cells[x][y]
                    current.color = (255, 200, 200)
                    history.append(current)

                    at_eastern_edge = False
                    at_northern_edge = False

                    if current.East == None:
                        at_eastern_edge = True
                    if current.North == None:
                        at_northern_edge = True

                    if at_eastern_edge or (at_northern_edge == False and random.randint(0, 1)==1):
                        random_cell = random.choice(history)
                        if random_cell.North:
                            Grid.Deconnect(random_cell, random_cell.North)
                        history.clear()
                    else:
                        Grid.Deconnect(current, current.East)

                    self.grid.Show(screen)
                    pygame.display.flip()
                    if self.speed < 1:
                        time.sleep(self.max_speed - min(self.speed, self.max_speed))
            self.isDone = True
