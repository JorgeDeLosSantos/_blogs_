# -*- coding: utf8 -*-
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
plt.style.use("ggplot")

data = np.random.randint(1,10,(20,1))
x = np.array(range(len(data)))

fig = plt.figure()
ax = fig.add_subplot(111)
plt.bar(x, data)
plt.show()
