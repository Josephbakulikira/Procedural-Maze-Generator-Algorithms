from classes.cell import *
from ui.colors import *
from classes.color import GridColor
class Grid:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        # Initialize cells
        self.cells = [[Cell(x, y, cell_size) for y in range(rows)] for x in range(cols)]
        self.UpdateNeighbours()
        self.heuristics = None
        self.path_color = orange


    def Flatten(self):
        flat_grid = []
        for x in range(self.cols):
            for y in range(self.rows):
                if self.cells[x][y]:
                    flat_grid.append(self.cells[x][y])
        return flat_grid

    def UpdateNeighbours(self):
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

    def JoinAndDestroyWalls(A, B):
        if A.isAvailable and B.isAvailable:
            A.visited = True
            B.visited = True
            A.connections.append(B)
            B.connections.append(A)
            if A.North == B:
                A.North, B.South = None, None
            elif A.South == B:
                A.South, B.North = None, None
            elif A.East == B:
                A.East, B.West = None, None
            elif A.West == B:
                A.West, B.East = None, None
            # ---- Polar Grid -------
            elif A.inward == B:
                A.inward = None
            elif B in A.outward:
                B.inward = None
            elif A.clockwise == B:
                A.clockwise, B.c_clockwise = None, None
            elif A.c_clockwise == B:
                A.c_clockwise = None
                B.clockwise = None



    def Show(self, screen, show_heuristic, show_color_map, shortest_path = None):
        for x in range(self.cols):
            for y in range(self.rows):
                if self.cells[x][y]:
                    self.cells[x][y].show_text = show_heuristic
                    self.cells[x][y].show_highlight = show_color_map
                    self.cells[x][y].Draw(screen, self.rows, self.cols)
                    if shortest_path != None:
                        if shortest_path.cells_record[x][y] != None:
                            A = ((x + 0.5) * self.cell_size, (y+0.5) * self.cell_size)
                            pygame.draw.circle(screen, self.path_color, A, self.cell_size//6)

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
