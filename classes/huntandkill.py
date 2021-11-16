import pygame
import random
from classes.grid import Grid, Update
from ui.colors import *

"""
STEPS:

1. Choose a starting cell.
2. Perform a random walk, carving passages to unvisited neighbors, 
   until the current cell has no unvisited neighbors.
3. Enter “hunt” mode, where you scan the grid looking for an unvisited cell that is adjacent to a visited cell. 
   If found, carve a passage between the two and let the formerly unvisited cell be the new starting cell.
4. Repeat steps 2 and 3 until the hunt mode scans the entire grid and finds no unvisited cells.
"""

class HuntAndKill:
    def __init__(self, grid, path_color):
        self.grid = grid
        self.rows = grid.rows
        self.cols = grid.cols
        self.path_color = path_color
        self.isDone = False
        self.starting_node = grid.cells[0][0]
        self.starting_node.isStartingNode = True
        self.end_node = grid.cells[self.grid.cols-1][self.grid.rows-1]
        self.end_node.isgoalNode = True
        if path_color == "HSV":
            self.grid.path_color = white
        self.shortest_path = None

    def Generate(self, screen, show_heuristic, show_color_map, show_path):
        if not self.isDone:
            randomX, randomY = random.randint(0, self.cols-1), random.randint(0, self.rows-1)
            current = self.grid.cells[randomX][randomY]
            while current:
                unvisited_neighbours = [cell for cell in current.neighbours if len(cell.connections) == 0]
                if len(unvisited_neighbours) > 0:
                    neighbour = random.choice(unvisited_neighbours)
                    neighbour.isCurrent = True
                    Grid.JoinAndDestroyWalls(current, neighbour)

                    self.grid.Show(screen, show_heuristic, show_color_map)
                    pygame.display.flip()

                    neighbour.isCurrent = False
                    current = neighbour

                else:
                    current = None
                    for x in range(self.cols):
                        for y in range(self.rows):
                            this = self.grid.cells[x][y]
                            visited_neighbours = [cell for cell in this.neighbours if len(cell.connections) > 0]
                            if len(this.connections) == 0 and len(visited_neighbours) > 0:
                                current = this
                                neighbour = random.choice(visited_neighbours)
                                neighbour.isCurrent = True
                                Grid.JoinAndDestroyWalls(current, neighbour)

                                self.grid.Show(screen, show_heuristic, show_color_map)
                                neighbour.isCurrent = False

                                pygame.display.flip()
                                break

            self.isDone = True
            Update(self, screen, show_heuristic, show_color_map, show_path)

        if show_path:
            self.grid.Show(screen, show_heuristic, show_color_map,self.shortest_path)
        else:
            self.grid.Show(screen, show_heuristic, show_color_map, None)
        
