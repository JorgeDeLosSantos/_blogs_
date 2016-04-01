# Borrar lineas en Matplotlib de manera interactiva

Matplotlib es una librería normalmente utilizada para trazar gráficas que habrán de exportarse como un archivo "estático" 
e incluirse en algún tipo de documento posteriormente. Pero además, Matplotlib también tiene algunas características 
que permiten que el usuario pueda interactuar, tales como los widgets o los eventos definidos por el usuario. Y esta 
última característica vamos a aprovechar en este post para ver cómo poder borrar líneas de una gráfica Matplotlib una vez 
que esta ha sido creada, esto mediante la selección a través del mouse.

Los eventos en Matplotlib se "conectan" utilizando el método `mpl_connect` de la clase `FigureCanvas`, mediante la sintaxis 
siguiente:

```python
hevt = fig.canvas.mpl_connect('tipo_evento', fun)
```

Donde `hevt` es una variable en la cual se guarda la referencia al evento y que puede ser utilizada para desconectarlo cuando 
no lo necesitemos más, `fig` es una instancia de la clase `Figure`, `tipo_evento` es uno de los eventos que pueden ser conectados en Matplotlib, 
cuya lista puede ver [aquí](http://matplotlib.org/users/event_handling.html#event-connections), y `fun` es una función 
en la cual deberá programarse la respuesta de nuestro programa cuando se lance el evento.

Por ahora nos interesa el tipo de evento `pick_event`, el cual se "lanza" cuando un objeto en el canvas actual es seleccionado. 
Así, para conectar nuestro evento haremos algo como lo siguiente:

```python
pick = fig.canvas.mpl_connect("pick_event", OnSelect)
```

Ahora vamos a por todo el código y enseguida explicamos para qué cada cosa:

```python
# -*- coding: utf-8 -*-
import wx
import matplotlib.pyplot as plt
import numpy as np

def OnSelect(event):
	app = wx.App()
	dlg = wx.MessageDialog(None, "Desea borrar",
	'Matplotlib Demo', wx.YES_NO|wx.ICON_QUESTION)
	if dlg.ShowModal() == wx.ID_YES:
		event.artist.remove()
	dlg.Destroy()
	app.MainLoop()
	fig.canvas.draw()

# Definir datos a plotear
X = np.random.random((10,5))
# Crear figure y axes
fig = plt.figure()
ax = fig.add_subplot(111)
# Graficar datos
ax.plot(X, picker=True)
# Conectar evento "pick_event"
pick = fig.canvas.mpl_connect("pick_event", OnSelect)
plt.show()
```

Primero, importamos, claro, los módulos a utilizar. Lo de wxPython es *opcional*, sólo nos servirá para confirmar si realmente 
queremos borrar cierta línea y puede sustituirse con cualquier otra librería gráfica, Tkinter por ejemplo.
Luego, definimos unos datos aleatorios, creamos nuestra `Figure` y nuestro `Axes` de la manera en que se debe, y posteriormente 
*ploteamos* los datos utilizando `plot`, pero adicionando el *keyword argument* `picker=True` para decirle a 
Matplotlib que para nuestro objeto gráfico resultante requerimos que esté disponible para ser seleccionado mediante el mouse. 
Y finalmente conectamos el evento de tipo `"pick_event"` al canvas correspondiente, pasando a la función `OnSelect` como 
la encargada de *dar una respuesta* a ese evento.

La función `OnSelect` bien puede reducirse a dos líneas si es que no requerimos confirmación de borrado, algo como:

```python
def OnSelect(event):
	event.artist.remove()
	fig.canvas.draw()
```

El resto de código es para crear un cuadro de diálogo en wxPython que nos pregunta si realmente queremos borrar la línea 
que hemos seleccionado.

[](img/img_01.png)

Podríamos *mejorar* un poquito nuestro "demo" si por ejemplo cada vez que seleccionamos una línea esta sea modificada para 
distinguirse un poco más del resto, por ejemplo modificar su grosor, y en caso de no confirmar su borrado entonces 
regresar al aspecto original. Agregando algunas líneas nos queda un código más o menos como este:

```python
# -*- coding: utf-8 -*-
import wx
import matplotlib.pyplot as plt
import numpy as np

def OnSelect(event):
	klw = 2
	event.artist.set_lw(event.artist.get_lw() + klw)
	fig.canvas.draw()
	app = wx.App()
	dlg = wx.MessageDialog(None, "Desea borrar",
	'Matplotlib Demo', wx.YES_NO|wx.ICON_QUESTION)
	if dlg.ShowModal() == wx.ID_YES:
		event.artist.remove()
	else:
		event.artist.set_lw(event.artist.get_lw() - klw)
	dlg.Destroy()
	app.MainLoop()
	fig.canvas.draw()

# Definir datos a plotear
X = np.random.random((10,5))
# Crear figure y axes
fig = plt.figure()
ax = fig.add_subplot(111)
# Graficar datos
ax.plot(X, picker=True)
# Conectar evento "pick_event"
pick = fig.canvas.mpl_connect("pick_event", OnSelect)
plt.show()
```

[](img/img_02.png)

Y bueno, con esto finalizamos esta pequeña introducción a las formas interactivas de Matplotlib, desde luego 
existen muchas posibilidades para implementar, de tal modo que nos quede algo más *chulo*.