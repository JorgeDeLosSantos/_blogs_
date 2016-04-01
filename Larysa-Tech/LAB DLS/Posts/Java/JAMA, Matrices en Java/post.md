# Introducción a scikit-image, procesamiento de imágenes en Python.

En este post vamos a hacer una pequeña introducción a la librería scikit-image, que básicamente 
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
tener instaladas las librerías SciPy, Matplotlib, NetWorkX, y PIL.

## Lo muy básico: cómo leer y mostrar imágenes

Bueno, aquí un primer ejemplo de cómo leer y mostrar una imagen desde un archivo. Tenemos una 
imagen llamada "lenna.png" en el mismo directorio de nuestro código, luego, podemos utilizar el 
módulo `io` de  `scikit-image` para leer y mostrar esta imagen. Básicamente se procede como sigue:

Primero importamos el modulo correspondiente:

```python
from skimage import io
import os

for x in range(0,10):
	print x
```


