import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from geometry import ORIGIN, Drawing, Circle, Line, Label, UP, RIGHT, Group

mpl.rcParams["font.size"] = 14

A = np.array((np.cos(np.pi/3), np.sin(np.pi/3)))

d = Drawing()
circle = Circle(ORIGIN, 1)
line = Line(ORIGIN, A, ls="--", color="grey")
yaxis = Line(-UP*1.5, UP*1.5, ls="-", color="black")
xaxis = Line(-RIGHT*1.5, RIGHT*1.5, ls="-", color="black")
label_phi = Label(r"$\varphi_A$", ORIGIN+0.1*UP+0.1*RIGHT)
label_xaxis = Label("x", RIGHT*1.5+0.1*UP)
label_yaxis = Label("y", UP*1.5+0.1*RIGHT)
coord_axes = Group(xaxis, yaxis, label_yaxis, label_xaxis)
d.add(circle, line, label_phi, coord_axes)
plt.show()
