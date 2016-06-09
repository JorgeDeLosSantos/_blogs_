# Utilizando estilos en Matplotlib

Por defecto Matplotlib tiene un estilo definido, un aspecto muy característico y facilmente reconocible. Pero también 
permite personalizar los estilos de gráficas de una forma muy sencilla, utilizando hojas de estilos predefinidas y 
que vienen incluidas con Matplotlib, aunque también existe la posibilidad de crearlas, pero de eso hablaremos luego.

Para ver los estilos que tenemos disponibles podemos importar pyplot y posteriormente teclear lo siguiente:

```python
>>> import matplotlib.pyplot as plt
>>> print plt.style.available
[u'labdls-dark',u'grayscale', u'bmh', u'dark_background', u'ggplot', u'fivethirtyeight']
```

Como puede observar lo anterior nos devuelve una lista con los estilos disponibles. El primer elemento de 
la lista es un estilo personalizada, así que seguro no estará en los estilos que le devuelva su consola.

Para utilizar un determinado estilo debe anteponer al código Matplotlib (justo después de las líneas de 
importación de módulos) lo siguiente:

```python
plt.style.use(estilo)
```

Donde estilo es un string con el nombre del estilo a utilizar, por ejemplo:

```python
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = np.linspace(0, 4*np.pi, 100)
y1 = x*np.cos(x)
y2 = x*np.sin(x)
y3 = np.sin(x)+np.cos(x)
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x, y1, label="$x\,cos(x)$")
ax.plot(x, y2, label="$x\,sin(x)$")
ax.plot(x, y3, label="$sin(x)+cos(x)$")
ax.legend()
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Amplitud (mm)")

plt.show()
```

Ahora nuestra gráfica luce un tanto distinta a lo que normalmente estamos acostumbrados en Matplotlib. 
Para dar un vistazo general a cómo se ven los demás estilos puede implementar el siguiente script:

```python
import numpy as np
import matplotlib.pyplot as plt

X = np.random.random((10,3))

fig = plt.figure(figsize=(12,8))
styles = plt.style.available

for k,style in enumerate(styles):
	plt.style.use(style)
	cax = fig.add_subplot(2,3,k)
	cax.set_title(style)
	cax.plot(X)

plt.show()
```

Muy interesantes, pero claro, siempre hará falta un poco de personalización que añada ese toque final. Por ello 
en entradas posteriores hablaremos de cómo crear una hoja de estilos Matplotlib.