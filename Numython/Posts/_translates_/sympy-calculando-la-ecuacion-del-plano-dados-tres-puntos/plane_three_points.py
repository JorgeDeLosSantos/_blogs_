# -*- coding: utf-8 -*-
from sympy import Matrix, solve, det, latex
from sympy.abc import x,y,z
from sympy.plotting import plot3d

P1 = (1,2,3)
P2 = (0,-1,1)
P3 = (-2,1,-2)

M = Matrix([[x-P1[0]     , y-P1[1]     , z-P1[2]]    ,
		    [P2[0]-P1[0] , P2[1]-P1[1] , P2[2]-P1[2]],
		    [P3[0]-P1[0] , P3[1]-P1[1] , P3[2]-P1[2]]])

sol = solve(det(M), z)
print(u"Ecuación implícita: %s = 0"%det(M))
print(u"Ecuación explícita: z=%s"%(sol[0]))
h = plot3d(sol[0], (x,0,5), (y,0,5), title="$z = %s$"%(latex(sol[0])))
h.save("img_01.png")
h.show()
