class Heuristic:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells_record = [[None for y in range(rows)] for x in range(cols)]

    def SetRecord(self, cell, distance):
        self.cells_record[cell.x][cell.y] = distance

    def BacktrackPath(self, goal, start):
        current = goal
        path_track = Heuristic(self.rows, self.cols)
        path_track.SetRecord(current, self.GetRecord(current))
        while current != start:
            for cell in current.connections:
                if self.GetRecord(cell) < self.GetRecord(current):
                    path_track.SetRecord(cell, self.GetRecord(cell))
                    current = cell
        return path_track

    def GetRecord(self, cell):
        return self.cells_record[cell.x][cell.y]
