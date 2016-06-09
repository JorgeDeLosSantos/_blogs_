# -*- coding: utf-8 -*-
from sympy import integrate, latex, cos
from sympy.abc import x,y,z

f = x+cos(x)

print latex(integrate(f,x))
