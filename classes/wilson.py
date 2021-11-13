import pygame
from classes.grid import Grid, Update

from ui.colors import *
import random

class Wilson:
    def __init__(self, grid, path_color="BLUE_E"):
        self.grid = grid
        self.rows = grid.rows
        self.cols =grid.cols
        self.path_color = path_color
        self.isDone = False
        self.starting_node = grid.cells[0][0]
        self.starting_node.isStartingNode = True
        self.end_node = grid.cells[self.cols-1][self.rows-1]
        self.end_node.isgoalNode = True
        self.shortest_path = None
        if path_color == "HSV":
            self.grid.path_color = white

    def Generate(self, screen, show_heuristic, show_color_map, show_path):
        if not self.isDone:
            unvisited = self.grid.Flatten()
            random_cell = random.choice(unvisited)
            unvisited.remove(random_cell)
            while len(unvisited) > 0:
                current = random.choice(unvisited)
                path = [current]

                while current in unvisited:
                    current = random.choice(current.neighbours)
                    if current in path:
                        _index = path.index(current)
                        path = path[:_index+1]
                    else:
                        path.append(current)

                if len(path) > 1:
                    for i in range(len(path)-1):
                        path[i+1].isCurrent = True

                        Grid.JoinAndDestroyWalls(path[i], path[i+1], "Normal")
                        unvisited.remove(path[i])

                        self.grid.Show(screen, show_heuristic, show_color_map)
                        path[i+1].isCurrent = False
                        pygame.display.flip()
            self.isDone = True
            Update(self, screen, show_heuristic, show_color_map, show_path)

        if show_path:
            self.grid.Show(screen, show_heuristic, show_color_map, self.shortest_path)
        else:
            self.grid.Show(screen, show_heuristic, show_color_map)
        pygame.display.flip()
