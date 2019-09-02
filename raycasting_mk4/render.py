import numpy as np

def render_xy(canvas, array_xy, theta, centre, tilt):
    scale = 5
    for a, b, c, d, e in array_xy:
        coords = ((((a - centre[0]) * np.cos(theta)) - ((b - centre[1]) * np.sin(theta)) + centre[0]) / scale + 300,
            (((a - centre[0]) * np.sin(theta)) + ((b - centre[1]) * np.cos(theta)) + centre[1]) / scale + 300,
            (((c - centre[0]) * np.cos(theta)) - ((d - centre[1]) * np.sin(theta)) + centre[0]) / scale + 300,
            (((c - centre[0]) * np.sin(theta)) + ((d - centre[1]) * np.cos(theta)) + centre[1]) / scale + 300)
        canvas.create_line(coords, tag=e)


