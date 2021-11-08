class Heuristic:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells_record = [[None for y in range(rows)] for x in range(cols)]

    def SetRecord(self, cell, distance):
        self.cells_record[cell.x][cell.y] = distance

    def GetFarthest(self, goal, start, grid):
        max_distance = 0
        farthest= start
        for x in range(self.cols):
            for y in range(self.rows):
                dist = self.cells_record[x][y] if self.cells_record[x][y] else 0
                cell = grid.cells[x][y]
                if dist > max_distance:
                    farthest = cell
                    max_distance = dist

        return farthest, max_distance

    def Merge(self, other):
        new_distances = Heuristic(self.rows, self.cols)
        for x in range(self.cols):
            for y in range(self.rows):
                if other.cells_record[x][y] != None:
                    new_distances.cells_record[x][y] = other.cells_record[x][y]
                else:
                    new_distances.cells_record[x][y] = self.cells_record[x][y]

        return new_distances

    def BacktrackPath(self, goal, start):
        current = goal
        path_track = Heuristic(self.rows, self.cols)
        path_track.SetRecord(current, self.GetRecord(current))
        max_counter = self.rows * self.cols
        counter = 0
        while current != start:
            for cell in current.connections:
                if self.GetRecord(cell) < self.GetRecord(current):
                    path_track.SetRecord(cell, self.GetRecord(cell))
                    current = cell
            counter += 1
            if counter > max_counter:
                break
        return path_track

    def GetRecord(self, cell):
        return self.cells_record[cell.x][cell.y]
