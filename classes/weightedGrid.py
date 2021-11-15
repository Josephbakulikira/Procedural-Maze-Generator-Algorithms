from classes.grid import Grid
from classes.weightedCell import WeightedCell

class WeightedGrid(Grid):
    def __init__(self, rows, cols, cell_size):
        super().__init__(rows, cols, cell_size)
        self.farthest = None
        self.maximum = None

    def Distances(self, start, goal, distance):
        self.heuristics = distance
        self.farthest, self.maximum = self.heuristics.GetFarthest(goal, start, self)

    def PrepareGrid(self):
        self.cells = [[None for i in range(self.rows)] for j in range(self.cols)]
        for x in range(self.cols):
            for y in range(self.rows):
                self.cells[x][y] = WeightedCell(x, y, self.cell_size)

    def ConfigureCells(self):
        for x in range(self.cols):
            for y in range(self.rows):
                if self.cells[x][y]:
                    self.cells[x][y].neighbours = []
                    # East neighbour cell
                    if x+1 < self.cols and self.cells[x+1][y]:
                        self.cells[x][y].East = self.cells[x+1][y]
                        self.cells[x][y].neighbours.append(self.cells[x+1][y])
                    # West neightbour cell
                    if x-1 >= 0 and self.cells[x-1][y]:
                        self.cells[x][y].West = self.cells[x-1][y]
                        self.cells[x][y].neighbours.append(self.cells[x-1][y])

                    # North neighbour cell
                    if y-1 >= 0 and self.cells[x][y-1]:
                        self.cells[x][y].North = self.cells[x][y-1]
                        self.cells[x][y].neighbours.append(self.cells[x][y-1])
                    # South neighbour cell
                    if y+1 < self.rows and self.cells[x][y+1]:
                        self.cells[x][y].South = self.cells[x][y+1]
                        self.cells[x][y].neighbours.append(self.cells[x][y+1])
