import numpy as np
from IPython.core.display_functions import display
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

    def show(self):
        return display(self.figure)

    def remove(self, *shapes):
        for shape in shapes:
            shape.remove()

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def add(self, ax):
        self.mpl_patch = mpatch.Circle(self.center, radius=self.radius, fill=False)
        ax.add_patch(self.mpl_patch)
    def remove(self):
        self.mpl_patch.remove()

class Point(Circle):
    radius = 0.025
    def __init__(self, center):
        super(Point, self).__init__(center, Point.radius)
    def add(self, ax):
        self.mpl_patch = mpatch.Circle(self.center, radius=Point.radius, fill=True, color='k')
        ax.add_patch(self.mpl_patch)
    def remove(self):
        self.mpl_patch.remove()


class Line:
    def __init__(self, start_point, end_point, **kwargs):
        self.start_point = start_point
        self.end_point = end_point
        self.kwargs = kwargs

    def add(self, ax):
        ax.plot((self.start_point[0], self.end_point[0]), (self.start_point[1], self.end_point[1]), **self.kwargs)


class Label:
    def __init__(self, label_name, position):
        self.name = label_name
        self.position = position

    def add(self, ax):
        ax.annotate(self.name, self.position)


class Group:
    def __init__(self, *shapes):
        self.shapes = shapes

    def add(self, ax):
        for shape in self.shapes:
            shape.add(ax)

