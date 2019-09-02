import tkinter as tk
import objects
import time
import numpy as np


class tk_window:
    def __init__(self, width, height, framerate):
        self.WIDTH = width
        self.HEIGHT = height
        self.FRAMERATE = framerate
        self.ROOT = tk.Tk()
        self.CANVAS = tk.Canvas(self.ROOT, width=self.WIDTH, height=self.HEIGHT)
        self.CANVAS.configure(background="black")
        self.CANVAS.pack()
        self.CANVAS.bind_all('<Left>', self.left_key)
        self.CANVAS.bind_all('<Right>', self.right_key)
        self.CANVAS.bind_all('<Up>', self.up_key)
        self.CANVAS.bind_all('<Down>', self.down_key)
        self.draw = objects.objects(self.CANVAS, self.WIDTH, self.HEIGHT, 10)
        self.lim_a, self.lim_b = 0, 45
        self.pos = (self.WIDTH / 2, self.HEIGHT / 2)

    def left_key(self, event):
        self.lim_a -= 3
        self.lim_b -= 3

    def right_key(self, event):
        self.lim_a += 3
        self.lim_b += 3

    def up_key(self, event):
        theta = (np.pi / 180) * (self.lim_a + 22.5)
        x = 2 * np.cos(theta)
        y = 2 * np.sin(theta)
        self.pos = (self.pos[0] + x, self.pos[1] + y)

    def down_key(self, event):
        theta = (np.pi / 180) * (self.lim_a + 22.5)
        x = 2 * np.cos(theta)
        y = 2 * np.sin(theta)
        self.pos = (self.pos[0] - x, self.pos[1] - y)

    def update_frames(self):
        while True:
            time.sleep(self.FRAMERATE)
            self.draw.ray_source(self.pos, self.lim_a, self.lim_b)
            self.CANVAS.update()
