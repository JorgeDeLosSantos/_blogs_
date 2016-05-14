# Detección de bordes en imágenes con MATLAB

La detección de bordes en MATLAB es una de las operaciones de procesamiento de imágenes 
más común y básica, cuyo objetivo es determinar las regiones en una imagen que presentan 
cambios significativos de intensidad en los pixeles que la conforman.

Recuerde que una imagen en escala de grises puede expresarse como una función bivariable 
$f(x,y)$, donde x e y son las coordenadas de ubicación (fila, columna). Así una forma 
sencilla de detectar los bordes en una imagen es utilizar el gradiente, mismo que 
determina la tasa de variación en ambas direcciones de una función bivariable, dado por:

$$
\nabla f = \begin{bmatrix} \frac{\partial f}{\partial x} \\ 
                  \frac{\partial f}{\partial y} \end{bmatrix}
$$

Aunque claro, para nuestros propósitos lo que usaremos es la magnitud del gradiente:

$$ |\nabla f|  =  \sqrt{ \left(\frac{\partial f}{\partial x}\right)^2 + \left(\frac{\partial f}{\partial y}\right)^2} $$

Así, para determinar los bordes en una imagen, o lo que sería lo mismo: localizar las regiones en donde la magnitud del 
gradiente es mayor, podemos utilizar la función `gradient`, vea el siguiente ejemplo:

```matlab
X = imread('Lenna.png');
XG = rgb2gray(X);
[dx,dy] = gradient(double(XG));
M = uint8(sqrt(dx.^2+dy.^2));
imshow(M);
```

MATLAB cuenta con una función especial para detectar bordes en una imagen: `edge`, la cual utiliza 
operadores matriciales especiales que transforman una imagen en escala de grises en una imagen binarizada 
con bordes resaltados.

```matlab
X = imread('Lenna.png');
XG = rgb2gray(X);
XB = edge(XG,'sobel');
imshow(XB);
```
