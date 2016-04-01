# -*- coding: utf8 -*-
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0,2*np.pi,1000)
r = 5*np.cos(5*theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection="polar")
ax.plot(theta,r,color="#ffb6c1",linewidth=3)

plt.savefig('img/rosa_polar.png')
plt.show()
