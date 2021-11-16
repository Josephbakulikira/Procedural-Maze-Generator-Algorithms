import pygame
from classes.grid import Grid, Update
import random

"""
STEPS:

1. Choose an arbitrary cell from G (the grid), 
   and add it to some (initially empty) set V.
2. Choose the edge with the smallest weight from G, 
   that connects a vertex in V with another cell not in V.
3. Add that edge to the minimal spanning tree, and the edge’s other cell to V.
4. Repeat steps 2 and 3 until V includes every vertex in G.

"""

class SimplePrims:
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
                cell = random.choice(active)
                available_neighbours = []
                for c in cell.neighbours:
                    if len(c.connections) == 0:
                        available_neighbours.append(c)

                if len(available_neighbours) > 0:
                    neighbour = random.choice(available_neighbours)

                    neighbour.isCurrent = True
                    Grid.JoinAndDestroyWalls(cell, neighbour)
                    self.grid.Show(screen, show_heuristic, show_color_map)
                    pygame.display.flip()
                    neighbour.isCurrent = False
                    active.append(neighbour)
                else:
                    active.remove(cell)
            self.isDone = True
            Update(self, screen, show_heuristic, show_color_map, show_path)

        if show_path:
            self.grid.Show(screen, show_heuristic, show_color_map, self.shortest_path)
        else:
            self.grid.Show(screen, show_heuristic, show_color_map)


class Prims(SimplePrims):
    def __init__(self, grid, path_color="RED"):
        super().__init__(grid, path_color)

    def Generate(self, screen, show_heuristic, show_color_map,show_path):
        if not self.isDone:
            active = []
            rx = random.randint(0, self.cols-1)
            ry = random.randint(0, self.rows-1)
            start_at = self.grid.cells[rx][ry]
            active.append(start_at)

            costs = {}
            for x in range(self.cols):
                for y in range(self.rows):
                    costs[self.grid.cells[x][y]] = random.randint(0, 99)
            while len(active) > 0:
                current = None
                min1 = float("inf")
                for i in range(len(active)):
                    if costs[active[i]] < min1:
                        current = active[i]
                        min1 = costs[active[i]]
                available_neighbours = []
                for c in current.neighbours:
                    if len(c.connections) == 0:
                        available_neighbours.append(c)
                if len(available_neighbours) > 0:
                    neighbour = None
                    min2 = float("inf")
                    for i in range(len(available_neighbours)):
                        if costs[available_neighbours[i]] < min2:
                            neighbour = available_neighbours[i]
                            min2 = costs[available_neighbours[i]]

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
        
