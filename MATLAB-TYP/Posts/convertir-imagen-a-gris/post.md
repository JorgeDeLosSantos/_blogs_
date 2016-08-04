!# Convertir a una imagen a escala de grises

### La manera rápida

Si cuenta con el *Image Processing Toolbox* MATLAB dispone de una función 
llamada `rgb2gray` que permite convertir una imagen RGB a una en escala de 
grises, ej:

```matlab
X = imread('lenna.png');
XG = rgb2gray(X);
imshow(XG);
```

Como puede notar es muy simple, sólo necesita pasar como argumento la 
matriz que contiene la información de la imagen RGB.

### La otra, un poco de algoritmos...

Si no dispone del toolbox de procesamiento de imagen, entonces puede implementar 
su propio algoritmo para realizar dicha tarea. 

El algoritmo más simple es el del *promedio* (average method), que consiste en 
calcular el promedio de los canales RGB y asignarlos al pixel correspondiente 
en la imagen de grises. Por ejemplo dada una matriz de **MxNx3** correspondiente 
a una imagen, el pixel de la matriz de grises en la posición $(i,j)$ se calcula 
como sigue:

$$
XG_{i,j} = \frac{X_{i,j,1} + X_{i,j,2} + X_{i,j,3}}{3}
$$

Donde `XG` es la matriz de grises, de dimensiones **MxN**. Y $X_{i,j,1}$, $X_{i,j,2}$ 
y $X_{i,j,3}$ las componentes correspondientes a los canales R, G y B, respectivamente.

Implementando esto en MATLAB:

```matlab
X = imread('lenna.png');
XG = uint8(mean(X,3));
imshow(XG);
``` 

¿Bastante simple verdad?, lo que hacemos es hacer el promedio en la dimensión 3, es decir, 
para cada pixel. La conversión a entero de 8-bits (`uint8`) es necesaria para que se muestre 
correctamente cuando utilizamos `imshow`, dado que la función `mean` devuelve una matriz 
de tipo `double`.

Otro método para convertir a escala de grises es el de la luminosidad (luminosity method) 
que consiste en asignar una proporción específica (ponderada) a cada uno de los canales, 
dependiendo la aportación de estos. De hecho MATLAB utiliza este tipo de transformación 
en la función `rgb2gray`. Con este método, la expresión para calcular el valor de un pixel 
de grises viene dado por:

$$
XG_{i,j} = 0.2889\,X_{i,j,1} + 0.5870\,X_{i,j,2} + 0.1140\,X_{i,j,3}
$$

LLevando esto a un código MATLAB:

```matlab
X = imread('img/lenna.png');
k = [0.2989 0.5870 0.1140];
XG = X(:,:,1)*k(1) + X(:,:,2)*k(2) + X(:,:,3)*k(3);
imshow(XG)
```
