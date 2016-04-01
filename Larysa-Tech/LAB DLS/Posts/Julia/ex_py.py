# -*- coding: utf8 -*-
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

x = np.loadtxt("data_performance.txt")
x = np.transpose(x)
names = ["Fortran", "Julia", "Python", "R", "MATLAB", "JavaScript", "Java"]

for cd,lab in zip(x,names):
	plt.plot(cd, label=lab)

plt.ylim(0,100)

plt.legend()
plt.show()
