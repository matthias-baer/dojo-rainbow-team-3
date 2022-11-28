import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from geometry import ORIGIN, Drawing, Circle, Line, UP, RIGHT

mpl.rcParams["font.size"] = 14

A = np.array((np.cos(np.pi/3), np.sin(np.pi/3)))

d = Drawing()
circle = Circle(ORIGIN, 1)
line = Line(ORIGIN, A, ls="--", color="grey")
yaxis = Line(-UP*1.5, UP*1.5, ls="-", color="black")
xaxis = Line(-RIGHT*1.5, RIGHT*1.5, ls="-", color="black")
d.add(circle, line, yaxis, xaxis)
plt.show()
