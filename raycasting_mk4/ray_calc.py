import tkinter as tk
import numpy as np
import math


class raycast:
    def __init__(self, canvas):
        self.CANVAS = canvas

    def cast_rays(self, x, y, lines, lim_a, lim_b, width, centre):
        fov = []
        lines = [(line[0], line[1], line[2], line[3]) for line in lines]
        x1 = x
        y1 = y
        lim_a_deg = (np.pi / 180) * lim_a
        lim_b_deg = (np.pi / 180) * lim_b

        for line in lines:
            for point in [(line[0], line[1]), (line[2], line[3])]:
                try:
                    theta = np.tanh((point[1] - y1) / (point[0] - x1))
                    if theta > lim_a_deg and theta < lim_b_deg:
                        fov.append((x1, y1) + point)

                except:
                    pass

        return fov
