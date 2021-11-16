import pygame
from classes.grid import Grid, Update
from ui.colors import *
import random
import time
from ui.colors import *

"""
STEPS:

1. Work through the grid row-wise, starting with the cell at 0,0. 
   Initialize the “run” set to be empty.
2. Add the current cell to the “run” set.
3. For the current cell, randomly decide whether to carve east or not.
4. If a passage was carved, make the new cell the current cell and repeat steps 2-4.
5. If a passage was not carved, choose any one of the cells in the run set and carve a passage north. 
   Then empty the run set, set the next cell in the row to be the current cell, and repeat steps 2-5.
6. Continue until all rows have been processed.
"""

class SideWinder:
    def __init__(self, grid, path_color="RED"):
        self.grid = grid
        self.starting_node = grid.cells[0][0]
        self.starting_node.isStartingNode = True
        self.end_node = grid.cells[self.grid.cols-1][self.grid.rows-1]
        self.end_node.isgoalNode = True
        self.isDone = False
        self.speed = 1
        self.max_speed = 1
        self.show_path = True
        self.path_color = path_color
        self.shortest_path = None
        if path_color == "HSV":
            self.grid.path_color = white

    def Generate(self, screen, show_heuristic, show_color_map, show_path):
        if not self.isDone:
            for y in range(self.grid.rows):
                history = []

                for x in range(self.grid.cols):
                    current = self.grid.cells[x][y]

                    current.isCurrent = True
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
                            Grid.JoinAndDestroyWalls(random_cell, random_cell.North)
                        history.clear()
                    else:
                        Grid.JoinAndDestroyWalls(current, current.East)

                    self.grid.Show(screen, show_heuristic, show_color_map)
                    current.isCurrent = False
                    pygame.display.flip()

                    if self.speed < 1:
                        time.sleep(self.max_speed - min(self.speed, self.max_speed))
            self.isDone = True

            Update(self, screen, show_heuristic, show_color_map, show_path)

        if show_path:
            self.grid.Show(screen, show_heuristic, show_color_map,self.shortest_path)
        else:
            self.grid.Show(screen, show_heuristic, show_color_map, None)
        
