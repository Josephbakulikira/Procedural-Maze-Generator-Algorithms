from classes.cell import *

class Grid:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        # Initialize cells
        self.cells = [[Cell(x, y, cell_size) for y in range(rows)] for x in range(cols)]
        self.UpdateNeighbours()
        self.heuristics = None

    def UpdateNeighbours(self):
        for x in range(self.cols):
            for y in range(self.rows):
                # East neighbour cell
                if x+1 < self.cols:
                    self.cells[x][y].East = self.cells[x+1][y]
                # West neightbour cell
                if x-1 >= 0:
                    self.cells[x][y].West = self.cells[x-1][y]
                # North neighbour cell
                if y-1 >= 0:
                    self.cells[x][y].North = self.cells[x][y-1]
                # South neighbour cell
                if y+1 < self.rows:
                    self.cells[x][y].South = self.cells[x][y+1]

    def JoinAndDestroyWalls(A, B):
        A.connections.append(B)
        B.connections.append(A)
        if A.North == B:
            A.North, B.South = None, None
        elif A.South == B:
            A.South, B.North = None, None
        elif A.East == B:
            A.East, B.West = None, None
        else:
            A.West, B.East = None, None

    def Show(self, screen, show_heuristic, show_path):
        for x in range(self.cols):
            for y in range(self.rows):
                self.cells[x][y].show_text = show_heuristic
                self.cells[x][y].show_path = show_path
                self.cells[x][y].Draw(screen, self.rows, self.cols)
