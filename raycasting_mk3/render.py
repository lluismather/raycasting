import tkinter as tk
import math


def renderer(array, canvas, width, height):
    v_width = width / len(array)
    clean_canvas(canvas)
    colour_array = [200 if n == math.inf else (1 - (n / width)) * 200 for n in array]
    height_array = [height if n == math.inf else (1 - (n / height)) * height for n in array]
    for i in range(0, len(array)):
        hexadecimal = "#%02x%02x%02x" % (int(colour_array[i]), int(colour_array[i]), int(colour_array[i]))
        bottom_left = (v_width * i, (height / 2) - (height_array[i] / 2))
        top_right = (v_width * (i + 1), (height / 2) + (height_array[i] / 2))
        canvas.create_rectangle(bottom_left + top_right, fill="grey", outline=hexadecimal, tag="shader")

def clean_canvas(canvas):
    for vertex in canvas.find_withtag("shader"):
        canvas.delete(vertex)