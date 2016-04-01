# -*- coding:utf-8 -*-
import glob
from wx.tools.img2py import img2py


if __name__=='__main__':
    #~ img2py("img/icono.png","icono.py")
    for img in glob.glob("img/*.png"):
        img2py(img,"iconos.py", append=True)
