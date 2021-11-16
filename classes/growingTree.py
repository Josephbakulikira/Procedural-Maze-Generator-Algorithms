import pygame
import random
from classes.grid import Grid, Update

"""
STEPS:

1. Let C be a list of cells, initially empty. Add one cell to C, at random.
2. Choose a cell from C, and carve a passage to any unvisited neighbor of that cell, 
adding that neighbor to C as well. If there are no unvisited neighbors, remove the cell from C.
3. Repeat #2 until C is empty.
"""

class GrowingTree:
    def __init__(self, grid, path_color="BLUE"):
        self.grid = grid
        self.cols = grid.cols
        self.rows = grid.rows
        self.isDone = False
        self.starting_node = grid.cells[0][0]
        self.starting_node.isStartingNode = True
        self.end_node = grid.cells[self.cols-1][self.rows-1]
        self.end_node.isgoalNode = True
        self.show_path = True
        self.path_color = path_color
        self.shortest_path = None
        if path_color == "HSV":
            self.grid.path_color = white

    def Generate(self, screen, show_heuristic, show_color_map,show_path):
        if not self.isDone:
            active = []
            rx = random.randint(0, self.cols-1)
            ry = random.randint(0, self.rows-1)
            start_at = self.grid.cells[rx][ry]
            active.append(start_at)

            while len(active) > 0:
                current = active[-1]
                available_neighbours = []
                for cell in current.neighbours:
                    if len(cell.connections) == 0:
                        available_neighbours.append(cell)

                if len(available_neighbours) > 0:
                    neighbour = random.choice(available_neighbours)

                    neighbour.isCurrent = True
                    Grid.JoinAndDestroyWalls(current, neighbour)
                    self.grid.Show(screen, show_heuristic, show_color_map)
                    pygame.display.flip()
                    neighbour.isCurrent = False

                    active.append(neighbour)
                else:
                    active.remove(current)
            self.isDone = True
            Update(self, screen, show_heuristic, show_color_map, show_path)

        if show_path:
            self.grid.Show(screen, show_heuristic, show_color_map, self.shortest_path)
        else:
            self.grid.Show(screen, show_heuristic, show_color_map)
        
