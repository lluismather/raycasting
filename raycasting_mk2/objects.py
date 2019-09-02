import tkinter as tk
import random
import numpy as np
import ray_calc as ray


class objects:
    def __init__(self, canvas, width, height, n):
        self.CANVAS = canvas
        self.WIDTH = width
        self.HEIGHT = height
        self.lines = [(0, 0, self.WIDTH, 0), (0, 0, 0, self.HEIGHT), 
                    (0, self.HEIGHT, self.WIDTH, self.HEIGHT), (self.WIDTH, 0, self.WIDTH, self.HEIGHT)]
        self.initialise(n)
        self.raycast = ray.raycast(self.CANVAS)

    def initialise(self, n):
        for i in range(n):
            x1, x2 = tuple([random.randint(0, self.WIDTH) for i in range(2)])
            y1, y2 = tuple([random.randint(0, self.HEIGHT) for i in range(2)])
            self.CANVAS.create_line((x1, y1, x2, y2), tag="wall_" + str(i), width=2, fill="white")
            self.lines.append((x1, y1, x2, y2))

    def ray_source(self, coords, lim_a, lim_b):
        x, y = coords
        x1, x2 = x - 1, x + 1
        y1, y2 = y - 1, y + 1
        self.CANVAS.delete(self.CANVAS.find_withtag("raycaster"))
        self.CANVAS.create_oval((x1, y1, x2, y2), tag="raycaster", width=3, fill="white")
        self.raycast.cast_rays(x, y, self.lines, lim_a, lim_b)
