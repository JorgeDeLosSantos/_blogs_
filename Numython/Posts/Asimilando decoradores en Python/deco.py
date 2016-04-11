# -*- coding: utf-8 -*-
#~ from sympy.abc import x,y,z
#~ from sympy import *

#~ def sqr(f):
    #~ def wrapper(*args,**kwargs):
        #~ return f(*args,**kwargs)**2
    #~ return wrapper


#~ def expandir(f):
    #~ def wrapper(*args,**kwargs):
        #~ return f(*args,**kwargs) 
    #~ return wrapper


#~ @sqr
#~ def g(x):
    #~ return x


#~ @expandir
#~ @sqr
#~ def h(x):
    #~ return x+1



#~ if __name__=='__main__':
    #~ print g(x)
    #~ print h(x)
