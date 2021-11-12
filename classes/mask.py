import random
from classes.grid import Grid

class Mask:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.boolGrid = [[True for y in range(rows)] for x in range(cols)]
        self.count = 0

    def Count(self):
        count = 0
        for x in range(self.cols):
            for y in range(self.rows):
                if self.boolGrid[x][y]:
                    count += 1
        self.count = count
        return count

    def Random(self):
        while True:
            x = random.randint(0, self.cols-1)
            y = random.randint(0, self.rows-1)
            if self.boolGrid[x][y]:
                return x, y

class GridMask(Grid):
    def __init__(self, rows, cols, cell_size, mask):
        super().__init__(rows, cols, cell_size)
        self.mask = mask

    def UpdateGrid(self):
        for x in range(self.cols):
            for y in range(self.rows):
                if self.mask.boolGrid[x][y] == False:
                    self.cells[x][y] = None

        self.PrepareGrid()

    def GetRandomCell(self):
        x , y = self.mask.Random()
        return self.cells[x][y]

    def GetSize(self):
        return self.mask.Count()
