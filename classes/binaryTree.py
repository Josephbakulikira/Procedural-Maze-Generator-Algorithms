import pygame
from classes.grid import Grid
from classes.color import GridColor
from ui.colors import *
import random

class BinaryTree:
    def __init__(self, grid, path_color="BLUE"):
        self.grid = grid
        self.isDone = False
        self.starting_node = grid.cells[0][0]
        self.end_node = grid.cells[self.grid.cols-1][self.grid.rows-1]
        self.show_path = True
        self.path_color = path_color
        self.shortest_path = None
        if path_color == "HSV":
            self.grid.path_color = white

    def Generate(self, screen, show_heuristic, show_color_map,show_path):
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

                    self.grid.Show(screen, show_heuristic, show_color_map)
                    pygame.display.flip()

            self.isDone = True
            self.Update(screen, show_heuristic, show_color_map,show_path)

        if show_path:
            self.grid.Show(screen, show_heuristic, show_color_map, self.shortest_path)
        else:
            self.grid.Show(screen, show_heuristic, show_color_map)
        pygame.display.flip()

    def Update(self, screen, show_heuristic, show_color_map, show_path):
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

        colorGridShortestPath = GridColor(self.path_color)
        colorGridShortestPath.distances(shortest_path, self.end_node, self.starting_node, self.grid)

        temp_path = h_distances.Merge(shortest_path)

        colorGridMap = GridColor(self.path_color)
        colorGridMap.distances(temp_path, self.end_node, self.starting_node, self.grid)

        for x in range(self.grid.cols):
            for y in range(self.grid.rows):
                self.grid.cells[x][y].highlight = colorGridShortestPath.UpdateColor(self.grid.cells[x][y])
                self.grid.cells[x][y].color = colorGridMap.UpdateColor(self.grid.cells[x][y])

                self.grid.Show(screen, show_heuristic, show_color_map)
                pygame.display.flip()
        self.shortest_path = shortest_path
