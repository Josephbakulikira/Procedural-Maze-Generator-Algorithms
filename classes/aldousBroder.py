import pygame
import random
from classes.grid import Grid, Update
from ui.colors import *

class AldousBroder:
    def __init__(self, grid, path_color="YELLOW"):
        self.grid = grid
        self.rows = grid.rows
        self.cols = grid.cols
        self.starting_node = grid.cells[0][0]
        self.starting_node.isStartingNode = True
        self.end_node = grid.cells[self.cols-1][self.rows-1]
        self.end_node.isgoalNode = True
        self.isDone = False
        self.shortest_path = None
        self.path_color = path_color
        if path_color == "HSV":
            self.grid.path_color = white

    def Generate(self, screen, show_heuristic, show_color_map, show_path):
        if not self.isDone:
            randomX = random.randint(0, self.cols-1)
            randomY = random.randint(0, self.rows-1)
            current = self.grid.cells[randomX][randomY]
            temp_color = current.color
            unvisited = self.rows * self.cols - 1

            while unvisited > 0:

                neighbour = random.choice(current.neighbours)
                if len(neighbour.connections) == 0:
                    Grid.JoinAndDestroyWalls(current, neighbour)
                    unvisited -= 1

                current.color = navy_blue
                self.grid.Show(screen, show_heuristic, show_color_map)
                pygame.display.flip()
                current.color = temp_color
                current = neighbour
            self.isDone = True
            Update(self, screen, show_heuristic, show_color_map, show_path)

        if show_path:
            self.grid.Show(screen, show_heuristic, show_color_map,self.shortest_path)
        else:
            self.grid.Show(screen, show_heuristic, show_color_map, None)
        
