import tkinter as tk
import numpy as np


class raycast:
    def __init__(self, canvas):
        self.CANVAS = canvas
        self.lines = []

    def cast_rays(self, x, y, lines, lim_a, lim_b):
        self.lines = lines
        x1 = x
        y1 = y

        for line in self.CANVAS.find_withtag("ray"):
            self.CANVAS.delete(line)

        for radian in range(lim_a, lim_b):
            theta = (np.pi / 180) * radian
            radius = 1000
            x2 = x1 + (radius * np.cos(1 * theta))
            y2 = y1 + (radius * np.sin(1 * theta))

            min_dist = float('inf')
            min_coords = (0, 0, 0, 0)
            for line in self.lines:
                x3, y3, x4, y4 = line
                den = ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4))
                t = (((x1 - x3) * (y3 - y4)) - ((y1 - y3) * (x3 - x4))) / den
                u = -((((x1 - x2) * (y1 - y3)) - ((y1 - y2) * (x1 - x3))) / den)
                
                if t > 0 and t < 1 and u > 0 and u < 1:
                    px = x1 + t * (x2 - x1)
                    py = y1 + t * (y2 - y1)

                    dist = np.sqrt((x1 - px) ** 2 + (y1 - py) ** 2)
                    if dist < min_dist:
                        min_dist = dist
                        min_coords = (x1, y1, px, py)

            self.CANVAS.create_line(min_coords, tag="ray", width=1, fill="white")
