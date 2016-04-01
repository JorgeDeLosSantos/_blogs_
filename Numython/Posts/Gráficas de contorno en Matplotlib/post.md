# Gráficas de contorno (curvas de nivel) en Matplotlib

Una manera de visualizar una función de dos variables es usar un campo escalar, 
en el que el escalar $ z = f(x,y) $ se asigna al punto $ (x,y) $. Un campo escalar puede caracterizarse
por sus curvas de nivel (o líneas de contorno) a lo largo de las cuales el valor
de $ f(x,y) $ es constante. 

El trazo de gráficas de lineas de contorno o curvas de nivel puede hacerse en Matplotlib utilizando 
la función `contour`, por ejemplo:

```python
import matplotlib.pyplot as plt	
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

x = y = np.linspace(-5, 5, 100)
X,Y = np.meshgrid(x,y)
Z = (-4*X)/(X**2 + Y**2 + 1)

cs = ax.contour(X,Y,Z)
plt.show()
```

[](img/img_01.png)

Podemos aumentar el número de niveles si agregamos un argumento de entrada a la función `contour`, por ejemplo:

```python
cs = ax.contour(X, Y, Z, 20)
```

Con lo anterior tendríamos representados 20 niveles o 20 *planos* de valores constantes $f(x,y)=C$.

[](img/img_02.png)

Se pueden agregar etiquetas a cada curva de nivel si utilizamos el método `clabel`, por ejemplo:

```python
import matplotlib.pyplot as plt	
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

x = y = np.linspace(-5, 5, 100)
X,Y = np.meshgrid(x,y)
Z = (-4*X)/(X**2 + Y**2 + 1)

cs = ax.contour(X, Y, Z, 15)
ax.clabel(cs, fontsize=8)

plt.show()
```

[](img/img_03.png)
