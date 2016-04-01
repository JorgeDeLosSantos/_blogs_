# Personalizando Frames en wxPython

Un frame ordinario en wxPython se puede construir de manera muy sencilla, heredando simplemente 
de `wx.Frame`.

```python
import wx

class TestFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(400,300))
		self.Show()

if __name__=='__main__':
	app = wx.App()
	fr = TestFrame(None, "Mi Frame")
	app.MainLoop()
```

[IMG]

A continuación vamos a ver algunas cuestiones interesantes para crear frames personalizados.

### Cambiando el color de fondo

Para cambiar el color de fondo de un Frame podemos utilizar el método `SetBackgroundColour`, al cual 
debemos pasarle como argumento un objeto de la clase `wx.Colour` o bien una cadena en notación 
hexadecimal para especificar el color.

```python
import wx

class TestFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(400,300))
		# Modificando el color de fondo
		rojo = wx.Colour(255,0,0)
		# rojo = "#ff0000"   # Equivalente en notación hexadecimal
		self.SetBackgroundColour(rojo)
		self.Show()

if __name__=='__main__':
	app = wx.App()
	fr = TestFrame(None, "Mi Frame")
	app.MainLoop()
```

[IMG]

### Colocando un ícono

Para colocar un ícono en la barra superior de nuestro Frame utilizamos el método `SetIcon`, al 
cual debemos pasarle como argumento un objeto de la clase `wx.Icon`. Para instanciar un objeto 
de `wx.Icon` necesitamos simplemente pasar como argumento la ruta de la imagen/ícono.

```python
import wx

class TestFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(400,300))
		# Colocando un ícono
		icono = wx.Icon("icono.png")
		self.SetIcon(icono)
		# ...
		self.Show()

if __name__=='__main__':
	app = wx.App()
	fr = TestFrame(None, "Mi Frame")
	app.MainLoop()
```

[IMG]

### Modificando estilos

**Ventana no redimensionable**

Si queremos tener una ventana con un tamaño fijo, podemos hacerlo modificando el estilo por defecto 
de nuestro Frame. Cuando creamos un Frame por defecto se toma el estilo `wx.DEFAULT_FRAME_STYLE`. 
Para modificarlo debemos pasar el *keyword argument* `style` con una lista de estilos determinados.
Para nuestro caso de una ventana no redimensionable:

```python
import wx

class TestFrame(wx.Frame):
	def __init__(self,parent,title):
		styles = (wx.CLOSE_BOX|wx.CAPTION)
		wx.Frame.__init__(self,parent=parent,title=title,size=(400,300),
						  style=styles)
		self.Show()

if __name__=='__main__':
	app = wx.App()
	fr = TestFrame(None, "Mi Frame")
	app.MainLoop()
```

[IMG]

**Ventana sin barra de título**

Si queremos una ventana sin barra de título, podemos *quitar* el estilo `wx.CAPTION`:

```python
import wx

class TestFrame(wx.Frame):
	def __init__(self,parent,title):
		styles = wx.DEFAULT_FRAME_STYLE & ~ (wx.CAPTION)
		wx.Frame.__init__(self,parent=parent,title=title,size=(400,300),
						  style=styles)
		self.SetBackgroundColour("#ff00ff")
		self.Show()

if __name__=='__main__':
	app = wx.App()
	fr = TestFrame(None, "Mi Frame")
	app.MainLoop()
```

![](img/img_05.png)

El estilo `wx.DEFAULT_FRAME_STYLE & ~ (wx.CAPTION)` toma todos los estilos incluidos en 
`wx.DEFAULT_FRAME_STYLE`, exceptuando a `wx.CAPTION`, un poco de combinación de operaciones lógicas AND-NOT.