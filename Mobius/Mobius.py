import numpy as np
from numpy import pi,cos,sin
from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

R,W=10,10
a,b=24,20

def x(u,v):
    return (R+v*cos(u/2))*cos(u)
def y(u,v):
    return (R+v*cos(u/2))*sin(u)
def z(u,v):
    return v*sin(u/2)

u_range = np.linspace(0,2*pi,a)
v_range = np.linspace(-W/2,W/2,b)

uv_meshgrid = np.meshgrid(u_range,v_range)

X,Y,Z = map(lambda f: f(*uv_meshgrid),(x,y,z))

fig = plt.figure() 
ax = fig.gca(projection='3d') 

ax.plot_wireframe(X,Y,Z)

# plt.axis('off')
ax.set_zlim(-.8*W,.8*W)
plt.show()

