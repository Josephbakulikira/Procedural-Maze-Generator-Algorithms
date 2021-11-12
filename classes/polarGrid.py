import pygame
import random
from classes.grid import Grid
from classes.polarCell import PolarCell
from ui.colors import *
from constants import width ,height
import math

class PolarGrid(Grid):
	def __init__(self, rows, cols, cell_size):
		super().__init__(rows, cols, cell_size)

	def PrepareGrid(self):
		rows = [None for i in range(self.rows)]
		row_height = 1/self.rows

		rows[0] = [PolarCell(0, 0, self.cell_size)]

		for i in range(self.rows):
			if i > 0:
				radius = i / self.rows
				circumference = (2 * math.pi) * radius

				previous_count = len(rows[i-1])
				estimated_cell_width = circumference / previous_count
				ratio = int(estimated_cell_width / row_height)

				cells = previous_count * ratio
				rows[i] = [PolarCell(i, j, self.cell_size) for j in range(cells)]

		return rows

	def ConfigureCells(self):
		for i in range(len(self.cells)):
			for j in range(len(self.cells[i])):
				current = self.cells[i][j]
				x, y = current.x, current.y
				if x > 0:
					_index = y+1
					if _index < len(self.cells[x]):
						current.clockwise = self.cells[x][_index]
					_index = y-1
					if _index >= 0:
						current.c_clockwise = self.cells[x][_index]

					ratio = len(self.cells[x]) / len(self.cells[x-1])
					parent = self.cells[x-1][int(y/ratio)]

					parent.outward.append(current)
					current.inward = parent

	def GetRandomCell(self):
		x = random.randint(0, len(self.cells)-1)
		y = 0
		if len(self.cells[x]) > 0:
			y = random.randint(0, len(self.cells[x])-1)

		return self.cells[x][y]

	def Show(self, screen, show_heuristic=None, show_color_map=None, shortest_path = None):
		centerX = width//2
		centerY = height//2
		for x in range(len(self.cells)):
			for y in range(len(self.cells[x])):
				cell = self.cells[x][y]
				if x > 0:
					theta = (2 * math.pi) / len(self.cells[cell.x])

					inner_radius = cell.x * self.cell_size
					outer_radius = (cell.x + 1) * self.cell_size

					theta_counter_clockwise = cell.y * theta
					theta_clockwise = (cell.y + 1) * theta

					ax = centerX + (inner_radius * math.cos(theta_counter_clockwise))
					ay = centerY + (inner_radius * math.sin(theta_counter_clockwise))

					bx = centerX + (outer_radius * math.cos(theta_counter_clockwise))
					by = centerY + (outer_radius * math.sin(theta_counter_clockwise))

					cx = centerX + (inner_radius * math.cos(theta_clockwise))
					cy = centerY + (inner_radius * math.sin(theta_clockwise))

					dx = centerX + (outer_radius * math.cos(theta_clockwise))
					dy = centerY + (outer_radius * math.sin(theta_clockwise))
					# pygame.draw.line(screen, black, (ax, ay), (cx, cy), 2)
					# pygame.draw.line(screen, black, (cx, cy), (dx, dy), 2)
					if cell.inward :
						pygame.draw.line(screen, black, (ax, ay), (cx, cy), 3)
					if cell.clockwise :
						pygame.draw.line(screen, black, (cx, cy), (dx, dy), 3)
					# if x == len(self.cells)-1 and len(cell.outward) == 0:
					# 	pygame.draw.line(screen, black, (bx, by), (dx, dy), 3)
			pygame.draw.circle(screen, black, (centerX, centerY), self.rows * self.cell_size, 3)
