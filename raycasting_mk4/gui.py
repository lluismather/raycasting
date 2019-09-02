import tkinter as tk
import time
import objects


class window:
    def __init__(self, width, height, framerate, nodes):
        self.WIDTH = width
        self.HEIGHT = height
        self.FRAMERATE = framerate
        self.ROOT = tk.Tk()
        self.CANVAS = tk.Canvas(self.ROOT, width=self.WIDTH, height=self.HEIGHT)
        self.CANVAS.pack()
        self.build_menus()
        self.lim_a = 0
        self.lim_b = 90
        self.d = objects.object(self.CANVAS, self.WIDTH, self.HEIGHT, nodes, self.lim_a, self.lim_b)
        self.angle = 0
        self.tilt = 0
        self.CANVAS.bind_all('<Left>', self.left_key)
        self.CANVAS.bind_all('<Right>', self.right_key)
        self.CANVAS.bind_all('<a>', self.a_key)
        self.CANVAS.bind_all('<d>', self.d_key)

    def build_menus(self):
        pass

    def left_key(self, event):
        self.angle -= 1

    def right_key(self, event):
        self.angle += 1

    def a_key(self, event):
        self.lim_a -= 5
        self.lim_b -= 5

    def d_key(self, event):
        self.lim_a += 5
        self.lim_b += 5

    def update_frames(self):
        while True:
            time.sleep(self.FRAMERATE)
            self.d.refresh_frame(self.angle, self.lim_a, self.lim_b, self.tilt)
