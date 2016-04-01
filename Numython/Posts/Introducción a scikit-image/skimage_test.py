# -*- coding: utf8 -*-
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from skimage import io,color

img = io.imread("lenna.png")
img_gris = color.rgb2gray(img)
img_bin = img_gris > 0.5
io.imshow(img_bin, cmap=cm.hot)
io.show()
