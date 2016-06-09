# Gráficas en coordenadas polares en Matplotlib

Trazar gráficas en coordenadas polares mediante el módulo `pyplot` es muy sencillo, y se procede 
de manera similar que con las funciones en coordenadas rectangulares. Lo único que debemos cambiar 
es el tipo de proyección de el axes en el que vamos a *plotear* nuestras funciones polares. 

Por ejemplo si queremos graficar una espiral de Arquímedes:

$$ 
r(\theta) = a + b\theta 
$$

```python
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0,2*np.pi)
r = 5 + 50*theta

fig = plt.figure()
ax = fig.add_subplot(111, projection="polar")
ax.plot(theta,r)

plt.show()
```

[Gráfica de la espiral]

O una rosa polar:

$$ 
r(\theta) = a \cos(k\theta + \phi_0) 
$$

```python
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0,2*np.pi,1000)
r = 5*np.cos(5*theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection="polar")
ax.plot(theta,r,color="#ffb6c1",linewidth=3)

plt.show()
```

[Gráfica de la rosa polar]

Note que se pueden pasar argumentos de estilo y color a la función `plot` tal y como 
se hace con las gráficas en coordenadas rectangulares. 

Como se observa en los ejemplos anteriores lo único que debemos hacer es adicionar 
el *keyword argument* `projection='polar'` al momento de crear el axes en el cual graficaremos 
nuestra función en coordenadas polares.


