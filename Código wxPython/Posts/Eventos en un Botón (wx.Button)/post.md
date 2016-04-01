# Eventos en un botón (wx.Button)

Los botones son componentes gráficos muy comunes que nos encontramos en cualquier interfaz de usuario y cuyo propósito 
es, generalmente, inicializar o confirmar un evento. En wxPython un botón ordinario se crea utilizando la clase 
`wx.Button`, a la cual habrán de pasarse como argumentos de inicialización mínimos, el objeto padre, un ID, y una cadena 
indicando la etiqueta visible del botón. Por ejemplo:

```python
# -*- coding: utf-8 -*-
import wx

class TestFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(200,200))
		self.boton = wx.Button(self, -1, u"Botón")
		self.Centre(True)
		self.Show()

if __name__=='__main__':
	app = wx.App()
	fr = TestFrame(None, "Test wxButton")
	app.MainLoop()
```

[](img/img_01.png)

Lo anterior crea un botón ocupando todo el espacio disponible en el Frame. Para colocar dos o más botones tendríamos que 
especificar el tamaño y posición de cada uno mediante los *keyword argument* `size` y `pos`. Por ejemplo:

```python
# -*- coding: utf-8 -*-
import wx

class TestFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(200,200))
		
		self.boton1 = wx.Button(self, -1, u"Uno", size=(100,20),
								pos=(50,10))
		self.boton2 = wx.Button(self, -1, u"Dos", size=(100,20),
								pos=(50,50))
		self.boton3 = wx.Button(self, -1, u"Tres", size=(100,20),
								pos=(50,90))
		
		self.Centre(True)
		self.Show()

if __name__=='__main__':
	app = wx.App()
	fr = TestFrame(None, "Test wxButton")
	app.MainLoop()
```

[](img/img_02.png)

Otra manera más conveniente de posicionar los botones o cualquier objeto gráfico sería utilizando sizers, de los 
cuales se estará hablando en posteriores entradas, pero vamos, que por ahora veremos cómo implementar manejo eventos 
en botones.

Así, en wxPython cuando se presiona un botón se *lanza* un evento del tipo `wx.EVT_BUTTON`, por ello lo que debemos 
hacer es utilizar el método `Bind` y agregar eventos de tipo `wx.EVT_BUTTON` al *escuchador* de eventos, asignando 
además un *handler*, que es básicamente una función o método que se encargará de manejar la respuesta de la interfaz 
al evento en cuestión.

Por ejemplo, vamos a imprimir un mensaje en consola cada vez que se presiona cualquiera de los tres botones que 
componen nuestra interfaz de usuario:

```python
# -*- coding: utf-8 -*-
import wx

class TestFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(200,200))
		
		self.boton1 = wx.Button(self, -1, u"Uno", size=(100,20),
								pos=(50,10))
		self.boton2 = wx.Button(self, -1, u"Dos", size=(100,20),
								pos=(50,50))
		self.boton3 = wx.Button(self, -1, u"Tres", size=(100,20),
								pos=(50,90))
		# Conectando evento
		self.Bind(wx.EVT_BUTTON, self.OnClick)
		
		self.Centre(True)
		self.Show()
		
	def OnClick(self,event):
		print u"Has presionado un botón"
		

if __name__=='__main__':
	app = wx.App()
	fr = TestFrame(None, "Test wxButton")
	app.MainLoop()
```

Note que hemos *conectado* los eventos de tipo `wx.EVT_BUTTON` al método `OnClick` que hace las veces de un *handler*. Luego, 
el método `OnClick` simplemente imprime en consola un mensaje.

Ahora, ¿cómo podríamos hacer que para cada botón presionado se tenga una respuesta diferente?. Hay dos formas comunes, a 
saber: especificando un *handler* para cada botón y utilizando el argumento `event` para identificar de dónde proviene 
el evento.

Primero vamos a utilizar un handler para cada botón. Debemos saber entonces que el método `Bind` acepta como tercer argumento 
un `source` o referencia a un objeto gráfico del cual se espera que provenga el evento. Algo como:

```python
self.Bind(wx.EVT_BUTTON, self.OnClick, boton)
```

Pero vamos con el ejemplo que venimos trabajando:

```python
# -*- coding: utf-8 -*-
import wx

class TestFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(200,200))
		
		self.boton1 = wx.Button(self, -1, u"Uno", size=(100,20),
								pos=(50,10))
		self.boton2 = wx.Button(self, -1, u"Dos", size=(100,20),
								pos=(50,50))
		self.boton3 = wx.Button(self, -1, u"Tres", size=(100,20),
								pos=(50,90))
		# Conectando eventos
		self.Bind(wx.EVT_BUTTON, self.OnClick1, self.boton1)
		self.Bind(wx.EVT_BUTTON, self.OnClick2, self.boton2)
		self.Bind(wx.EVT_BUTTON, self.OnClick3, self.boton3)
		
		self.Centre(True)
		self.Show()
		
	def OnClick1(self,event):
		print u"Has presionado el botón 1"
		
	def OnClick2(self,event):
		print u"Has presionado el botón 2"
		
	def OnClick3(self,event):
		print u"Has presionado el botón 3"
		

if __name__=='__main__':
	app = wx.App()
	fr = TestFrame(None, "Test wxButton")
	app.MainLoop()
```

Como puede ver, por cada botón se conecta un evento `wx.EVT_BUTTON` con el handler correspondiente, así cada vez que se presione 
un botón diferente la respuesta obtenida será dependiendo del handler asignado.

Finalmente, la segunda forma consiste en utilizar el segundo parámetro del *handler* asignado para manejar un evento (normalmente y 
por *convención* llamado `event`). ¿Pero qué es el parámetro `event`?, en términos simples es un objeto de la clase 
`wx.CommandEvent` que contiene información acerca del evento lanzado. Implementando esta manera para el ejemplo anterior se tiene:

```python
# -*- coding: utf-8 -*-
import wx

class TestFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(200,200))
		
		self.boton1 = wx.Button(self, -1, u"Uno", size=(100,20),
								pos=(50,10))
		self.boton2 = wx.Button(self, -1, u"Dos", size=(100,20),
								pos=(50,50))
		self.boton3 = wx.Button(self, -1, u"Tres", size=(100,20),
								pos=(50,90))
		# Conectando eventos
		self.Bind(wx.EVT_BUTTON, self.OnClick)
		
		self.Centre(True)
		self.Show()
		
	def OnClick(self,event):
		bt_label = event.GetEventObject().GetLabel()
		print u"Has presionado el botón %s"%(bt_label)

if __name__=='__main__':
	app = wx.App()
	fr = TestFrame(None, "Test wxButton")
	app.MainLoop()
```

El método `GetEventObject` del objeto `event` devuelve la referencia al objeto del cual proviene el evento, y 
posteriormente con el método `GetLabel()` se obtiene simplemente la etiqueta del botón correspondiente para 
imprimirla en pantalla.