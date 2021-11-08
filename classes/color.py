from ui.colors import *
import pygame
import colorsys

def hsv_to_rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

class GridColor:
    heuristics = None
    farthest = None
    max_distance = None

    def __init__(self, color_str = "RED"):
        self.color = color_str
        # print(self.color)
    def distances(self, heuristics, goal, start, grid):
        self.heuristics = heuristics
        self.farthest, self.max_distance = self.heuristics.GetFarthest(goal, start, grid)

    def UpdateColor(self, cell):
        if  self.color != "HSV":
            val = self.heuristics.GetRecord(cell)
            distance = 0 if val == None else val
            intensity = (self.max_distance - distance)/self.max_distance
            dark = min(int(255 * intensity), 255)
            bright = min( int(128 + (127 * intensity)),255)

            colors = {
                "RED":    (bright, dark, dark),
                "BLUE":   (dark, dark, bright),
                "GREEN":  (dark, bright, dark),
                "YELLOW": (bright, bright, dark),
                "CYAN":   (dark, bright, bright),
                "PURPLE":   (bright, dark, bright),
                "PURPLE_E": (bright, dark, bright),
                "GREEN_E":(0, bright, 0),
                "BLUE_E": (0, 0, bright),
                "RED_E":  (bright, 0, 0)
            }

            return tuple(colors[self.color])
        else:
            val = self.heuristics.GetRecord(cell)
            hue = 0 if val == None else val
            _color = hsv_to_rgb((hue/360), 1, 1)
            # print(_color)
            return _color
