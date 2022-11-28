import numpy as np
from matplotlib import pyplot as plt, patches as mpatch

ORIGIN = np.array((0, 0))
UP = np.array((0, 1))
RIGHT = np.array((1, 0))
LEFT = -RIGHT
DOWN = -UP


class Drawing:
    def __init__(self):
        self.figure, self.ax = plt.subplots(1, 1, figsize=(8, 8))
        self.ax.set_xlim([-2, 2])
        self.ax.set_ylim([-2, 2])
        self.ax.set_aspect("equal")
        self.ax.set_axis_off()

    def add(self, *shapes):
        for shape in shapes:
            shape.add(self.ax)


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def add(self, ax):
        ax.add_patch(mpatch.Circle(self.center, radius=self.radius, fill=False))


class Line:
    def __init__(self, start_point, end_point, **kwargs):
        self.start_point = start_point
        self.end_point = end_point
        self.kwargs = kwargs

    def add(self, ax):
        ax.plot((self.start_point[0], self.end_point[0]), (self.start_point[1], self.end_point[1]), **self.kwargs)