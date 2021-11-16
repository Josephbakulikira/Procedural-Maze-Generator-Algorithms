import pygame
import random
from classes.grid import Grid, Update

"""
STEPS:
1. Initialize the cells of the first row to each exist in their own set.
2. Randomly join adjacent cells, but only if they are not in the same set. 
   When joining adjacent cells, merge the cells of both sets into a single set, 
   indicating that all cells in both sets are now connected.
3. For each set, randomly create vertical connections downward to the next row. 
   Each remaining set must have at least one vertical connection. 
   The cells in the next row thus connected must share the set of the cell above them.
4. Flesh out the next row by putting any remaining cells into their own sets.
5. Repeat until the last row is reached.
6. For the last row, join all adjacent cells that do not share a set, and omit the vertical connections, and you’re done!
"""

class Ellers:
    def __init__(self, grid,starting_set=0, path_color="BLUE"):
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
        self.starting_set = starting_set

    def Generate(self, screen, show_heuristic, show_color_map,show_path):
        if not self.isDone:
            row_state = State(self.starting_set, self.cols)

            for y in range(self.rows):
                for x in range(self.cols):
                    cell = self.grid.cells[x][y]
                    if not cell.West:
                        continue

                    _set = row_state.SetFor(cell)
                    old_set = row_state.SetFor(cell.West)

                    if _set != old_set:
                        if cell.South == None or random.randint(0, 1) == 0:
                            temp = cell.West
                            temp.isCurrent = True
                            Grid.JoinAndDestroyWalls(cell, temp)
                            self.grid.Show(screen, show_heuristic, show_color_map)
                            pygame.display.flip()
                            temp.isCurrent = False

                            row_state.Merge(old_set, _set)

                if self.grid.cells[0][y].South:
                    next_row = row_state.Next()

                    for set in row_state.cells_in_set:
                        cells = row_state.cells_in_set[set].copy()
                        random.shuffle(cells)
                        for _index, _cell in enumerate(cells):
                            if _index == 0 or random.randint(0,2) == 0:
                                if _cell.South:
                                    temp = _cell.South
                                    temp.isCurrent = True
                                    Grid.JoinAndDestroyWalls(_cell, temp)
                                    self.grid.Show(screen, show_heuristic, show_color_map)
                                    pygame.display.flip()
                                    temp.isCurrent = False

                                    next_row.Record(row_state.SetFor(_cell), temp)
                    row_state = next_row
            self.isDone = True
            Update(self, screen, show_heuristic, show_color_map, show_path)

        if show_path:
            self.grid.Show(screen, show_heuristic, show_color_map, self.shortest_path)
        else:
            self.grid.Show(screen, show_heuristic, show_color_map)
        pygame.display.flip()

class State:
        def __init__(self, starting_set, rows):
            self.cols = rows
            self.cells_in_set = {}
            self.set_for_cell = [None for x in range(self.cols)]
            self.next_set = starting_set

        def Record(self, set, cell):
            self.set_for_cell[cell.x] = set
            if set not in self.cells_in_set:
                self.cells_in_set[set] = []
            self.cells_in_set[set].append(cell)

        def SetFor(self, cell):
            if not self.set_for_cell[cell.x]:
                self.Record(self.next_set, cell)
                self.next_set += 1

            return self.set_for_cell[cell.x]

        def Merge(self, winner, loser):
            for cell in self.cells_in_set[loser]:
                self.set_for_cell[cell.x] = winner
                self.cells_in_set[winner].append(cell)

            del self.cells_in_set[loser]
        def Next(self):
            return State(self.next_set, self.cols)
