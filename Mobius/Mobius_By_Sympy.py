from sympy import *
from sympy.abc import r, theta, beta, omega
from math import pi
from sympy.plotting import plot3d_parametric_surface

x = (r+omega*cos(beta))*cos(theta)
y = (r+omega*cos(beta))*sin(theta)
z = omega*sin(beta)

R, W = 10, 10

x, y, z = map(lambda expr: expr.subs(
    [(beta, theta/2), (r, R)]), (x, y, z))

plot3d_parametric_surface(x, y, z,
                          (theta, 0, 2*pi), (omega, -W/2, W/2))
