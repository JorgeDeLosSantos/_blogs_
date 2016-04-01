# PyAPDL, escribiendo código ANSYS APDL usando Python

[PyAPDL](https://larysa-tech.blogspot.mx/p/pyapdl.html) es una librería escrita en Python aún en desarrollo, cuyo objetivo 
es tener la posibilidad de escribir código APDL (ANSYS Parametric Design Language) usando Python.

### ¿Por qué escribir código Python y no directamente APDL?

Hay muchas cosas que son más sencillas en un lenguaje de alto nivel como Python, escribir bucles, definir funciones, 
crear arreglos, y también la posibilidad de introducir una sintaxis que resulte un poco más descriptiva que la 
usada nativamente por APDL.

Por ejemplo, para definir un keypoint en las coordenadas (0,0,0) en APDL se tendría:

```
K,1,0,0,0
```

Luego, utilizando PyAPDL:

```python
create_keypoint(1,0,0,0)
```

Y bien, por ahora la diferencia consiste en la sintaxis utilizada, normalmente y basándonos en buenas prácticas de 
programación siempre es preferible tener un nombre autodescriptivo para las variables, subrutinas, funciones, clases o cualquier 
otra porción de código en cuestión, así diríamos que `create_keypoint` es más descriptivo que `K`.

Lo anterior está bien, pero Python además nos facilita algunas tareas mediante las estructuras de datos disponibles (diccionarios, 
tuplas, listas...). Por ejemplo, supongamos que se necesitan crear cuatro keypoints que definan un cuadrado unitario, con 
PyAPDL haríamos algo como lo siguiente:

```
kps = {1:(0,0,0),
       2:(1,0,0),
       3:(1,1,0),
       4:(0,1,0)}

for kp in kps:
    create_keypoint(kp, kps[kp])
```

### Instalación y requerimientos

Para utilizar PyAPDL es necesario tener instalados:

* Python 2.X / 3.X
* NumPy

Posteriormente puede seguir las instrucciones que se detallan en el [repositorio en GitHub](https://github.com/JorgeDeLosSantos/pyapdl) 
para instalar de manera correcta la librería.