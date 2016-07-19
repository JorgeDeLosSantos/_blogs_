# -*- coding: utf-8 -*-
from sympy import integrate, latex, cos
from sympy.abc import x,y,z

f = x+cos(x)

fi = integrate(f,x)

print fi
