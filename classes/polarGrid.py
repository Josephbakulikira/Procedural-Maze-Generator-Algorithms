import pygame
from ui.colors import *
from constants import *
from classes.polarCell import PolarCell 
from classes.grid import Grid
import math

def PolarGrid(Grid):
	def __init__(self, rows, cols=1, cellSize=cell_size):
		super().__init__(self, rows, cols, cellSize)
		self.cells = [[PolarCell(x, y, cell_size) for y in range(rows)] for x in range(cols)]
		self.row_cells = []

	def PrepareGrid(self):
		row_cells = [None for i in range(self.rows)]
		r_height = 1.0/self.rows
		initial_cell = PolarCell(0, 0)
		row_cells[0] = [initial_cell]
		
		for i in range(1, self.rows):
			radius = i / self.rows
			circumference = 2 * math.pi * radius

			previous_count = len(row_cells[i - 1])
			estimated_cell_width = circumference / previous_count
			ratio = (estimated_cell_width / r_height).round

			cells = previous_count * ratio
			row_cells[i] = [ PolarCell(i, j) for j in range(cells)]


		return row_cells

	def ConfigureCells(self):
		if len(self.row_cells):
			for x in range(len(self.row_cells)):
				for y in range(len(self.row_cells[x])):
					current = self.row_cells[x][y]
					r, c = current.x, current.y
					if r > 0:
						current.clockWise = self.row_cells[r][c+1]
						current.counterClockWise = self.row_cells[r][c-1]

						ratio = len(self.row_cells[r]) / len(self.row_cells[r-1])
						parent = self.row_cells[r-1][c/ratio]
						parent.outward.append(current)
						current.inward = parent

	






