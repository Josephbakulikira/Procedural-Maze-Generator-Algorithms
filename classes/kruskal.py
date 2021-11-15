import pygame
from classes.grid import Grid, Update
import random

class Kruskals:
    def __init__(self, state, path_color='BLUE'):
        self.state = state
        self.grid = state.grid
        self.isDone = False
        self.cols = self.grid.cols
        self.rows = self.grid.rows
        self.starting_node = self.grid.cells[0][0]
        self.starting_node.isStartingNode = True
        self.end_node = self.grid.cells[self.grid.cols-1][self.grid.rows-1]
        self.end_node.isgoalNode = True
        self.show_path = True
        self.path_color = path_color
        self.shortest_path = None
        if self.path_color == "HSV":
            self.grid.path_color = white
    class State:
        def __init__(self, grid):
            self.grid = grid
            self.cols = grid.cols
            self.rows = grid.rows
            self.neighbours = []
            self.cells_set = {}
            self.cells_in_set = {}
            for x in range(self.cols):
                for y in range(self.rows):
                    set = len(self.cells_set)
                    self.cells_set[self.grid.cells[x][y]] = set
                    self.cells_in_set[set] = [self.grid.cells[x][y]]

                    if self.grid.cells[x][y].South:
                        self.neighbours.append([self.grid.cells[x][y], self.grid.cells[x][y].South])
                    if self.grid.cells[x][y].East:
                        self.neighbours.append([self.grid.cells[x][y], self.grid.cells[x][y].East])
        def CanMerge(self, left, right):
            return (self.cells_set[left] != self.cells_set[right])

        def Merge(self, left, right):
            Grid.JoinAndDestroyWalls(left ,right)
            winner = self.cells_set[left]
            loser = self.cells_set[right]
            losers = None
            if loser in self.cells_in_set:
                losers = self.cells_in_set[loser]
            else:
                losers = [right]

            for l in losers:
                self.cells_in_set[winner].append(l)
                self.cells_set[l] = winner
            del self.cells_in_set[loser]

        def AddCrossing(self, cell):
            if (len(cell.connections) > 0 or
                not self.CanMerge(cell.East, cell.West) or
                not self.CanMerge(cell.North, cell.South)):
                return False

            for c in self.neighbours:
                left, right = c[0], c[1]
                if left == cell or right == cell:
                    self.neighbours.remove(c)

            if random.randint(0, 1) == 0:
                if cell.West != None:
                    self.Merge(cell.West, cell)
                if cell.East != None:
                    self.Merge(cell, cell.East)

                if cell.North and cell.North.East:
                    self.Merge(cell.North, cell.North.East)
                if cell.South and cell.South.North:
                    self.Merge(cell.South, cell.South.North)
            else:
                if cell.North:
                    self.Merge(cell.North, cell)
                if cell.South:
                    self.Merge(cell, cell.South)

                if cell.West and cell.West.East:
                    self.Merge(cell.West, cell.West.East)
                    self.Merge(cell.East, cell.East.West)

    def Generate(self, screen, show_heuristic, show_color_map,show_path):
        if not self.isDone:
            neighbours = self.state.neighbours
            random.shuffle(neighbours)
            while len(neighbours) > 0:
                poped = neighbours.pop()
                left, right = poped[0], poped[1]

                if self.state.CanMerge(left, right):
                    self.state.Merge(left, right)
                    self.grid.Show(screen, show_heuristic, show_color_map)
                    pygame.display.flip()
            self.isDone = True
            Update(self, screen, show_heuristic, show_color_map, show_path)

        if show_path:
            self.grid.Show(screen, show_heuristic, show_color_map, self.shortest_path)
        else:
            self.grid.Show(screen, show_heuristic, show_color_map)
        
