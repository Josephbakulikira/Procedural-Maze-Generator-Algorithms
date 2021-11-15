from classes.cell import *
from ui.colors import *
from classes.color import GridColor
import random

class Grid:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        # Initialize cells
        self.cells = [[Cell(x, y, cell_size) for y in range(rows)] for x in range(cols)]
        self.PrepareGrid()
        self.heuristics = None
        self.path_color = orange
        self.isSorted = False
        self.path = {}
        self.path_values = []

    def Flatten(self):
        flat_grid = []
        for x in range(self.cols):
            for y in range(self.rows):
                if self.cells[x][y]:
                    flat_grid.append(self.cells[x][y])
        return flat_grid

    def PrepareGrid(self):
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

    def JoinAndDestroyWalls(A, B, gridType="Normal"):
        if A.isAvailable and B.isAvailable:
            A.visited = True
            B.visited = True
            A.connections.append(B)
            B.connections.append(A)
            # ---- Grid & Mask Grid -----
            if gridType == "Normal":
                if A.North == B:
                    A.North, B.South = None, None
                elif A.South == B:
                    A.South, B.North = None, None
                elif A.East == B:
                    A.East, B.West = None, None
                elif A.West == B:
                    A.West, B.East = None, None
            # ---- Polar Grid -------
            elif gridType == "Polar":
                if A.inward == B :
                    A.inward = None
                    B.outward.remove(A)
                elif B.inward == A:
                    B.inward = None
                    A.outward.remove(B)
                elif A.clockwise == B or B.c_clockwise == A:
                    A.clockwise =  None
                    B.c_clockwise = None
                elif A.c_clockwise == B or B.clockwise == A:
                    A.c_clockwise = None
                    B.clockwise = None
            # ----- Hex Grid -------
            elif gridType == "Hex":
                if A.North == B:
                    A.North, B.South = None, None
                elif A.South == B:
                    A.South, B.North = None, None
                elif A.SouthEast == B:
                    A.SouthEast, B.NorthWest = None, None
                elif A.SouthWest == B:
                    A.SouthWest, B.NorthEast = None, None
                elif A.NorthEast == B:
                    A.NorthEast, B.SouthWest = None, None
                elif A.NorthWest == B:
                    A.NorthWest, B.SouthEast = None, None

    def Deadends(self):
        deadends_set = []
        for x in range(len(self.cells)):
            for y in range(len(self.cells[x])):
                if len(self.cells[x][y].connections) == 1:
                    deadends_set.append(self.cells[x][y])
        return deadends_set

    def Braid(self, p=1):
        deadends = self.Deadends()
        random.shuffle(deadends)

        for cell in deadends:
            if len(cell.connections) != 1 or random.uniform(0, 1) > p:
                continue
            neighbours = [c for c in cell.neighbours if c not in cell.connections]
            best = []
            for c in neighbours:
                if len(c.connections ) == 1:
                    best.append(c)
            if len(best) == 0:
                best = neighbours

            neighbour = random.choice(best)
            Grid.JoinAndDestroyWalls(cell, neighbour)


    def Show(self, screen, show_heuristic, show_color_map, shortest_path = None):
        if not self.isSorted and shortest_path:
            for x in range(self.cols):
                for y in range(self.rows):
                    if shortest_path.cells_record[x][y]:
                        val = shortest_path.cells_record[x][y]
                        self.path_values.append(val)
                        self.path[str(val)] = ((x+0.5)*self.cell_size, (y+0.5)*self.cell_size)
            self.path_values = sorted(self.path_values)
            self.isSorted = True

        for x in range(self.cols):
            for y in range(self.rows):
                if self.cells[x][y]:
                    self.cells[x][y].show_text = show_heuristic
                    self.cells[x][y].show_highlight = show_color_map
                    self.cells[x][y].Draw(screen, self.rows, self.cols)

        if shortest_path:
            for i in range(len(self.path_values)-1):
                pygame.draw.line(screen, orange, self.path[str(self.path_values[i])], self.path[str(self.path_values[i+1])], 2)
                pygame.draw.circle(screen, orange, self.path[str(self.path_values[i])], self.cell_size//6)

def Update(self, screen, show_heuristic, show_color_map, show_path):
    # Calculate the step of each cell from the starting node
    # it's gonna initialize a grid that store the cost of each cell
    # from the starting node
    h_distances = self.starting_node.CalculateHeuristic(self.grid.rows, self.grid.cols)
    self.grid.heuristics = h_distances
    for x in range(len(self.grid.cells)):
        for y in range(len(self.grid.cells[x])):
            if self.grid.cells[x][y]:
                self.grid.cells[x][y].cost = 0 if self.grid.heuristics.cells_record[x][y] == None else self.grid.heuristics.cells_record[x][y]

    # get the path from the goad node to the starting node
    shortest_path = h_distances.BacktrackPath(self.end_node, self.starting_node)
    for x in range(self.grid.cols):
        for y in range(self.grid.rows):
            if self.grid.cells[x][y]:
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
            if self.grid.cells[x][y]:
                self.grid.cells[x][y].highlight = colorGridShortestPath.UpdateColor(self.grid.cells[x][y])
                self.grid.cells[x][y].color = colorGridMap.UpdateColor(self.grid.cells[x][y])

                self.grid.Show(screen, show_heuristic, show_color_map)
                pygame.display.flip()
    self.shortest_path = shortest_path
