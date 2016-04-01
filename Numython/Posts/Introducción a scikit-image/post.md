# Introducción a scikit-image, procesamiento de imágenes en Python.

En este post vamos a hacer una pequeña introducción a la librería scikit-image, la cual básicamente 
es una colección de algoritmos para el procesamiento de imágenes en Python.

## Para comenzar

Todas las instrucciones referente a descarga e instalación, así como algunos códigos de ejemplos 
pueden encontrarse en la página oficial: [http://scikit-image.org/](http://scikit-image.org/).

A manera de referencia rápida, puede instalar scikit-image utilizando pip:

```
>> pip install -U scikit-image
```

En general, scikit-image o skimage, trabaja con arrays de numpy, así como también hace uso de algunas 
utilidades gráficas de Matplotlib para la visualización, por ello también es necesario 
tener instaladas las librerías SciPy, Matplotlib, NetWorkX, y PIL/pillow.

## Lo muy básico: cómo leer y mostrar imágenes

Bueno, aquí un primer ejemplo de cómo leer y mostrar una imagen desde un archivo. Tenemos una 
imagen llamada "lenna.png" en el mismo directorio de nuestro código, luego, podemos utilizar el 
módulo `io` de  `scikit-image` para leer y mostrar esta imagen. Básicamente se procede como sigue:

Primero importamos el modulo correspondiente:

```python
from skimage import io
```

Ahora utilizamos la función `imread` del módulo `io` para leer la imagen, y guardamos esto en 
una variable, en la cual se almacenará un array de NumPy con la información de los colores que 
componen la imagen.

````python
img = io.imread('lenna.png')
```

Enseguida utilizamos la función `imshow` para mostrar la imagen que pasemos como argumento 
y la función `show` para mostrar toda la ventana o `figure` que contiene la(s) imágenes 
a desplegar en la pantalla.

```python
io.imshow(img)
io.show()
```

Juntando este mini código nos quedaría algo como lo siguiente:

```python
from skimage import io

img = io.imread("lenna.png")
io.imshow(img)
io.show()
```

Si ejecutamos lo anterior nos mostrará la imagen leída en una ventana o `figure` de Matplotlib, tal 
como se aprecia en la siguiente imagen:

[IMAGEN 1]

Podemos *averiguar* la forma o cantidad de elementos del array `img` utilizando el método `shape`, por ejemplo 
en el script anterior se puede añadir:

```python
print img.shape
```

Y con ello nos mostrará en consola una tupla de 3 elementos (para el caso de esta imagen) con la información 
del número de filas, columnas y *capas* de la matriz. En nuestro ejemplo nos muestra:

```python
(512L, 512L, 3L)
```

Lo cual implica que tenemos una imagen de 512x512 pixeles. El tercer número indica que tenemos tres capas o 
*canales* del módelo de color RGB, en el cual la primer capa representa el rojo, la segunda el verde 
y la tercera el azul. Así, toda la gama de colores para un pixel en específico se puede obtener mediante la 
combinación de estos tres colores primarios.

## Un poco de gris...

Ahora, ya sabemos leer y mostrar imágenes. Vamos a operar un poco y a convertir nuestra matriz RGB de entrada 
en una matriz de intensidades en escala de grises, o en pocas palabras vamos a transformar una matriz 
de color en una en tono de grises. Para ello vamos a importar el módulo `color` y a utilizar la función 
`rgb2gray`:

```python
from skimage import io,color

img = io.imread("lenna.png")
img_gris = color.rgb2gray(img)
io.imshow(img_gris)
io.show()
```

[IMAGEN 2]

¿Y qué pasa si queremos mostrar ambas imágenes en una misma ventana?, bueno, para ello podemos hacer uso de 
la función `subplot` de Matplotlib:

```python
import matplotlib.pyplot as plt
from skimage import io,color

img = io.imread("lenna.png")
img_gris = color.rgb2gray(img)
plt.subplot(211)
io.imshow(img)
plt.subplot(212)
io.imshow(img_gris)
io.show()
```

[IMAGEN 3]

Hasta aquí esta breve introducción a scikit-image, una librería que sin duda vale la pena revisar y que 
proporciona una cantidad razonable de algoritmos que pueden ser muy útiles en el procesamiento digital 
de imágenes. Posteriormente se hablará de algunos tópicos básicos adicionales, como la binarización, segmentación, 
y otras operaciones típicas.