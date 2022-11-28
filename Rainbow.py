import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatch
mpl.rcParams["font.size"] = 14

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


d = Drawing()
circle = Circle(ORIGIN, 1)
d.add(circle)
plt.show()
