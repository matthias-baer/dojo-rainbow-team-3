import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from geometry import*

mpl.rcParams["font.size"] = 14
Point.radius = 0.025

A = np.array((np.cos(np.pi/3), np.sin(np.pi/3)))

d = Drawing()
circle = Circle(ORIGIN, 1)
point_A = Point(A)
line = Line(ORIGIN, A, ls="--", color="grey")
yaxis = Line(-UP*1.5, UP*1.5, ls="-", color="black")
xaxis = Line(-RIGHT*1.5, RIGHT*1.5, ls="-", color="black")
label_phi = Label(r"$\varphi_A$", ORIGIN+0.1*UP+0.1*RIGHT)
label_A = Label('A', A+0.1*UP+0.1*LEFT)
label_xaxis = Label("x", RIGHT*1.5+0.1*UP)
label_yaxis = Label("y", UP*1.5+0.1*RIGHT)
coord_axes = Group(xaxis, yaxis, label_yaxis, label_xaxis)
d.add(circle, line, label_phi, coord_axes, point_A, label_A)

alpha = np.pi/6
S = np.array((np.cos(alpha), np.sin(alpha))) + A
point_S = Point(S)
d.add(point_S)
# d.remove(point_S)
d.show()

d.remove(point_S)
d.show()
