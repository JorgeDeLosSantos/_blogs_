# -*- coding: utf8 -*- 
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

x = y = np.linspace(-5, 5, 400)
X,Y = np.meshgrid(x,y)
Z = (-4*X)/(X**2 + Y**2 + 1)

ax.plot_surface(X, Y, Z, cmap=plt.cm.jet, lw=0.0)
ax.set_axis_off()
ax.view_init(45, 60)
#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_zlabel('Z')

fig.savefig("img/surface.png")
plt.show()
