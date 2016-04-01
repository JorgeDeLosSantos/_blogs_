# -*- coding: utf8 -*- 
import matplotlib.pyplot as plt	
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

#~ def f(X,Y):
	#~ return (-4*X)/(X**2 + Y**2 + 1)

x = y = np.linspace(-5, 5, 100)
X,Y = np.meshgrid(x,y)
Z = (-4*X)/(X**2 + Y**2 + 1)

cs = ax.contour(X, Y, Z, 15)
ax.clabel(cs, fontsize=8)

fig.savefig('img/img_03.png')
plt.show()
