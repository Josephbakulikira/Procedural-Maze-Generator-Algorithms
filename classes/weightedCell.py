from classes.cell import Cell
from classes.heuristic import Heuristic

class WeightedCell(Cell):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.weight = 1
        self.neighbours = []
    def CalculateHeuristic(self, rows, cols):
        weights = Heuristic(rows, cols)
        pending = [self]
        while len(pending) > 0:
            pending.sort(key=lambda cell: weights.GetRecord(cell))
            this = pending[0]
            pending.remove(this)

            for cell in this.connections:
                val = 0 if not weights.GetRecord(this) else weights.GetRecord(this)
                total =  val + cell.weight
                if not weights.GetRecord(cell)  or total < weights.GetRecord(cell):
                    pending.append(cell)
                    weights.SetRecord(cell, total)
        weights.SetRecord(self, 0)
        return weights
