# -*- coding: utf8 -*-
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
# plt.style.use("ggplot")

def normalize(vector):
	return [k/la.norm(vector) for k in vector]
	
x = np.array([1,3,1])

fig = plt.figure()
ax = fig.add_subplot(111)
plt.pie(x)
plt.show()


