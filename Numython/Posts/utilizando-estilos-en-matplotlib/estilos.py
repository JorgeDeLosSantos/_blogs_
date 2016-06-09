# -*- coding: utf8 -*-
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = np.linspace(0, 4*np.pi, 100)
y1 = x*np.cos(x)
y2 = x*np.sin(x)
y3 = np.sin(x)+np.cos(x)
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x, y1, label="$x\,cos(x)$")
ax.plot(x, y2, label="$x\,sin(x)$")
ax.plot(x, y3, label="$sin(x)+cos(x)$")
ax.legend()
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Amplitud (mm)")

plt.savefig('img/img_02.png')
plt.show()
