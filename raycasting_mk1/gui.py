import tkinter as tk
import objects
import time


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
        self.create_menu()
        self.draw = objects.objects(self.CANVAS, self.WIDTH, self.HEIGHT, 5)
        self.lim_a, self.lim_b = 0, 720

    def left_key(self, event):
        self.lim_a -= 3
        self.lim_b -= 3

    def right_key(self, event):
        self.lim_a += 3
        self.lim_b += 3

    def create_menu(self):
        pass

    def motion(self):
        x = self.ROOT.winfo_pointerx() - self.ROOT.winfo_rootx()
        y = self.ROOT.winfo_pointery() - self.ROOT.winfo_rooty()
        return x, y

    def update_frames(self):
        while True:
            time.sleep(self.FRAMERATE)
            self.draw.ray_source(self.motion(), self.lim_a, self.lim_b)
            self.CANVAS.update()
