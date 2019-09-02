import random
import render
import ray_calc as ray
import numpy as np


class object:

    def __init__(self, canvas, width, height, nodes, lim_a, lim_b):
        self.CANVAS = canvas
        self.WIDTH = width
        self.HEIGHT = height
        self.array_z_vals = []
        self.array_xy_vals = []
        self.nodes = nodes
        self.lim_a = lim_a
        self.lim_b = lim_b
        self.raycast = ray.raycast(self.CANVAS)
        self.initialise(self.nodes)

    def initialise(self, n):
        for y in range(n):
            y_scale = y * (self.WIDTH / n)
            self.array_z_vals.append([])
            for x in range(n):
                x_scale = x * (self.HEIGHT / n)
                self.array_xy_vals.append([y_scale, x_scale, y_scale, x_scale + (self.HEIGHT / n), "x_line"])
                self.array_xy_vals.append([y_scale, x_scale, y_scale + (self.WIDTH / n), x_scale, "y_line"])
                self.array_xy_vals.append([y_scale, x_scale + (self.HEIGHT / n), y_scale + (self.WIDTH / n), x_scale, "diagonal"])
                self.array_z_vals[y].append([y, x, random.randint(-10, 10)])

    def scene_refresh(self, angle, attack):
        theta = (np.pi / 180) * angle
        centre = (self.WIDTH / 2, self.HEIGHT / 2)
        render.render_xy(self.CANVAS, self.array_xy_vals, theta, centre, attack)

    def delete(self, tags):
        for tag in tags:
            for obj in self.CANVAS.find_withtag(tag):
                self.CANVAS.delete(obj)

    def refresh_frame(self, angle, lim_a, lim_b, tilt):
        self.lim_a = lim_a
        self.lim_b = lim_b
        self.delete(["x_line", "y_line", "diagonal", "ray"])
        self.scene_refresh(angle, tilt)
        self.CANVAS.update()


