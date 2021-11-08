import pygame
import random
from classes.grid import Grid
from classes.color import GridColor
from ui.colors import *

class AldousBroder:
    def __init__(self, grid, path_color="YELLOW"):
        self.grid = grid
        self.starting_node = self.grid.cells[0][0]
        self.end_node = self.grid.cells[grid.cols-1][grid.rows-1]
        self.rows = grid.rows
        self.cols = grid.cols
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
            self.Update(screen, show_heuristic, show_color_map, show_path)

        if show_path:
            self.grid.Show(screen, show_heuristic, show_color_map,self.shortest_path)
        else:
            self.grid.Show(screen, show_heuristic, show_color_map, None)
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
