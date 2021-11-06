import pygame
from classes.grid import Grid
import random

class BinaryTree:
    def __init__(self, grid):
        self.grid = grid
        self.isDone = False
        self.starting_node = grid.cells[0][0]
        self.end_node = grid.cells[self.grid.cols-1][self.grid.rows-1]
        self.show_path = True

    def Generate(self, screen, show_heuristic, show_path):
        if not self.isDone:
            for x in range(self.grid.cols):
                for y in range(self.grid.rows):
                    neighbours = []
                    # Check two neighbours
                    # check  for north and south Neighbours
                    if self.grid.cells[x][y].North != None:
                        neighbours.append(self.grid.cells[x][y].North)
                    if self.grid.cells[x][y].East != None:
                        neighbours.append(self.grid.cells[x][y].East)

                    # pick a random neighbour
                    # if any in the neighbours list
                    choice = None
                    if len(neighbours) > 0:
                        choice = random.choice(neighbours)

                    if choice != None:
                        Grid.JoinAndDestroyWalls(self.grid.cells[x][y], choice)

                    self.grid.Show(screen, show_heuristic, show_path)
                    pygame.display.flip()

            self.isDone = True
            # Calculate the step of each cell from the starting node
            # it's gonna initialize a grid that store the cost of each cell
            # from the starting node
            h_distances = self.starting_node.CalculateHeuristic(self.grid.rows, self.grid.cols)
            self.grid.heuristics = h_distances

            # get the path from the goad node to the starting node
            shortest_path = h_distances.BacktrackPath(self.end_node, self.starting_node)
            for x in range(self.grid.cols):
                for y in range(self.grid.rows):
                    # check if the cell is in the path grid
                    # If it is then set it as path
                    if shortest_path.GetRecord(self.grid.cells[x][y]):
                        self.grid.cells[x][y].isPath = True

        self.grid.Show(screen, show_heuristic, show_path)
        pygame.display.flip()
