# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sympy as sp

# Calculando puntos de intersección
#~ x = sp.Symbol('x')
#~ x = sp.solve(x**2 - x - 2) 


x = np.linspace(-1,2)
y1 = x + 3
y2 = x**2 + 1

#~ plt.plot(x,y1)
#~ plt.plot(x,y2)
    
#~ plt.show()

step = 0.04
maxval = 1.0

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# create supporting points in polar coordinates
r = np.linspace(-1, 2, 20)
p = np.linspace(0, 2*np.pi, 20)
R, P = np.meshgrid(r, p)

# transform them to cartesian system
X, Y = R*np.cos(P), R*np.sin(P)

Z = R**2
ax.plot_surface(X, Y, Z, rstride=1, cstride=1)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
