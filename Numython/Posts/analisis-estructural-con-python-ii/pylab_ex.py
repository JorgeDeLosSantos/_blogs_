# -*- coding: utf8 -*-
from pylab import *

x = linspace(0,10)
y1 = exp(0.1*x)*cos(x)
y2 = exp(0.5*x)*sin(x)

subplot(2,1,1)
plot(x,y1,'r')
ylabel("Amplitud (mm)")
grid(True)

subplot(2,1,2)
plot(x,y2,'b')
xlabel("Tiempo (s)")
ylabel("Amplitud (mm)")
grid(True)

savefig("img/img_03.png")
show()
