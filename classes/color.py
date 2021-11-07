from ui.colors import *



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
        val = self.heuristics.GetRecord(cell)
        distance = 0 if val == None else val
        intensity = (self.max_distance - distance)/self.max_distance
        dark = min(int(255 * intensity), 255)
        bright = min( int(128 + (127 * intensity)),255)

        rgbColor = (dark, bright, dark)

        colors = {
            "RED": (bright, dark, dark),
            "BLUE": (dark, dark, bright),
            "GREEN": (dark, bright, dark),
            "YELLOW": (bright, bright, dark),
            "CYAN": (dark, bright, bright)
        }

        return tuple(colors[self.color])
