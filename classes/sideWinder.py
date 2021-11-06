import pygame
from classes.grid import Grid
from ui.colors import *
import random
import time

class SideWinder:
    def __init__(self, grid):
        self.grid = grid
        self.starting_node = grid.cells[0][0]
        self.starting_node.isStartingNode = True
        self.end_node = grid.cells[self.grid.cols-1][self.grid.rows-1]
        self.end_node.isgoalNode = True
        self.isDone = False
        self.speed = 1
        self.max_speed = 1
        self.show_path = True

    def Generate(self, screen, show_heuristic, show_path):
        if not self.isDone:
            for y in range(self.grid.rows):
                history = []
                for x in range(self.grid.cols):
                    current = self.grid.cells[x][y]
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

                    self.grid.Show(screen, show_heuristic, show_path)
                    pygame.display.flip()
                    if self.speed < 1:
                        time.sleep(self.max_speed - min(self.speed, self.max_speed))
            self.isDone = True
            # Calculate the step of each cell from the starting node
            # it's gonna initialize a grid that store the cost of each cell
            # from the starting node
            h_distances = self.starting_node.CalculateHeuristic(self.grid.rows, self.grid.cols)

            self.grid.heuristics = h_distances
            for x in range(self.grid.cols):
                for y in range(self.grid.rows):
                    self.grid.cells[x][y].cost = 0 if self.grid.heuristics.cells_record[x][y] == None else self.grid.heuristics.cells_record[x][y]
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
