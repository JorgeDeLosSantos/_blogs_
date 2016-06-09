# Funciones definidas a trozos (piecewise) con NumPy

Una función definida a trozos es una función real \\(f\\) de una variable real \\(x\\), cuya definición está dada por varios 
conjuntos disjuntos de su dominio. <sup>[1]</sup>

El ejemplo clásico de una función definida por secciones es la función valor absoluto \\(abs(x)\\), habitualmente definida 
por:

$$
f(x) = \left\{
\begin{matrix}
-x & si \,\, x < 0 \\
x & si \,\, x \geq 0 \\
\end{matrix}\right.
$$

De manera ordinaria, en NumPy, para definir una función en un intervalo tendríamos que crear un vector de \\(n\\) cantidad 
de puntos en ese intervalo, y posteriormente crear la expresión que define la función, por ejemplo, definiendo a 
\\(f(x)=x\\,\\,cos(x)\\)

```python
>>> import numpy as np
>>> x=np.linspace(0,10)
>>> y=x*np.cos(x)
```

Ahora, dada la naturaleza de las funciones por tramos, estás no pueden definirse como en las líneas 
anteriores, puesto que la expresión que las define depende del intervalo. Una opción para crear una función 
a trozos sería definiendo un intervalo para cada expresión y posteriormente concatenar todo en un mismo 
arreglo, tanto para los intervalos como las expresiones.

Por ejemplo, definiendo la función valor absoluto en el intervalo \\((-10,10)\\):

```python
import numpy as np

x1 = np.linspace(-10,0)
x2 = np.linspace(0,10)
y1 = -x1
y2 = x2
x = np.concatenate((x1,x2))
y = np.concatenate((y1,y2))
```

Si, lo anterior puede parecer un poco *tedioso*, así que NumPy también dispone de una función que nos ahorra 
el estar escribiendo mucho código: `piecewise`, la cual nos permite crear un arreglo a partir de otro (intervalo), 
seccionando este acorde a las expresiones/funciones pasadas como argumentos y a las condiciones lógicas para 
definir los subintervalos. En términos simples la sintaxis de `piecewise` es:

```python
np.piecewise(x, logls, funls)
```

Donde `x` es un arreglo que define la variable independiente, `logls` una lista de condiciones lógicas para seccionar 
y definir los subintervalos, y `funls` una lista de funciones o constantes que definen el valor de la función para 
el subintervalo correspondiente.

Siguiendo con nuestro ejemplo de la función valor absoluto, haríamos algo como lo siguiente:

```python
import numpy as np

x = np.linspace(-5, 5)
y = np.piecewise(x, [x<0, x>=0], [lambda x: -x, lambda x: x])
```

Desde luego también se pueden usar funciones ordinarias en lugar de lambdas. 

Para hacer esto un poco más *ilustrativo* vamos a utilizar Matplotlib para trazar la gráfica correspondiente:

```python
import numpy as np
import matplotlib.pyplot as plt	

x = np.linspace(-5, 5)
y = np.piecewise(x, [x<0, x>=0], [lambda x: -x, lambda x: x])

plt.plot(x, y)

plt.show()
```

[](img/img_01.png)



**Referencias:**

\[1\]. [https://es.wikipedia.org/wiki/Funci%C3%B3n_definida_a_trozos](https://es.wikipedia.org/wiki/Funci%C3%B3n_definida_a_trozos)