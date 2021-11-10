from classes.cell import Cell

class PolarCell(Cell):
	clockwise = None
	c_clockwise = None
	inward = None

	def __init__(self, x, y, size):
		super().__init__(x, y, size)
		self.outward = []
		self.neighbours = []

	def GetNeighbours(self):
		self.neighbours = []
		if self.clockwise:
			self.neighbours.append(self.clockwise)
		if self.c_clockwise:
			self.neighbours.append(self.c_clockwise)
		if self.inward:
			self.neighbours.append(self.inward)
		self.neighbours += self.outward
		return self.neighbours
