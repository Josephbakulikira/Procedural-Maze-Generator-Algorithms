from classes.cell import Cell

class PolarCell(Cell):
	clockWise = None
	counterClockWise = None
	inward = None
	def __init__(self, x, y, cell_size):
		super().__init__(x, y, cell_size)
		outward = []

	def UpdateNeighbours(self):
		neighbours = []
		if clockWise:
			neighbours.append(clockWise)
		if counterClockWise:
			neighbours.append(counterClockWise)
		if inward:
			neighbours.append(inward)
		neighbours = neighbours + self.outward


