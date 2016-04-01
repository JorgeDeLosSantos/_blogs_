# Una aplicación muy básica en wxPython

La aplicación más elemental en wxPython puede lanzarse con apenas 5 líneas de código (incluyendo 
la instrucción de importar el módulo `wx`).


```python
import wx

app = wx.App()
fr = wx.Frame(None,title="Test 01",size=(400,300))
fr.Show()
app.MainLoop()
```

Ahora vamos por pasos, a *despedazar* un poco el código anterior. Primero importamos el módulo 
`wx`, el cual contiene todo (o casi todo, exceptuando controles más especializados y sus derivados) 
lo que podemos utilizar para construir una aplicación. Acto seguido, creamos un objeto de la clase 
`wx.App`, que vendrá a ser la propia aplicación y se encargará de que el usuario pueda interactuar 
con los controles gráficos desplegados en pantalla. Luego, se crea un objeto de la clase `wx.Frame` 
que es en términos simples una *ventana* de las que estamos acostumbrados a ver en todos lados; note 
que a `wx.Frame` se le pasan como argumentos primeramente el valor `None` que hace referencia al 
objeto padre (ninguno en este caso), y los *keyword arguments* `title` y `size` que definen el 
título y tamaño de la ventana, respectivamente. Finalmente se `llama` al método `MainLoop` de 
la clase `wx.App` para inicializar la captura de eventos en nuestra aplicación.

¿Y ahora cómo agregamos controles?

```python
import wx

app = wx.App()
fr = wx.Frame(None,title="Test 01",size=(400,300))
bt = wx.Button(fr, -1, u"Botón 1", pos=(0,0))
txt = wx.TextCtrl(fr, -1, pos=(100,0))
fr.Show()
app.MainLoop()
```

[IMAGEN_01]

En resumen lo que se hace es crear un objeto de clase del control gráfico requerido, pasándole a este como 
argumento de objeto padre la ventana o frame guardado en la variable `fr`. Note que hemos pasado a cada control 
el *keyword argument* `pos` para definir una posición fija dentro del frame. Normalmente en wxPython no 
deberiamos hacer esto, sino utilizar `Sizers` para posicionar los elementos de manera automática, pero bueno, 
para un ejemplo básico lo daremos por bueno.

¿Y cómo definimos un evento?

```python
import wx

def OnClick(event):
	print "Hola wxPython"

app = wx.App()
fr = wx.Frame(None,title="Test 01",size=(400,300))
bt = wx.Button(fr, -1, u"Botón 1", pos=(0,0))
txt = wx.TextCtrl(fr, -1, "",pos=(100,0))
fr.Bind(wx.EVT_BUTTON, OnClick)
fr.Show()
app.MainLoop()
```

Con el método `Bind` agregamos un determinado tipo de evento a ser *capturado* por nuestra aplicación, 
pasando como primer argumento el tipo de evento (en este caso wx.EVT_BUTTON), y como segundo argumento 
un `handler` o una función en la cual habrá de definirse la respuesta de la aplicación al lanzamiento 
del evento. Para el caso anterior lo único que se hace es imprimir en la consola una cadena de texto 
cada que se oprime el botón.

Códigos como los anteriores pueden servir para mostrar una simple ventana o para una demo muy reducida 
de una aplicación wxPython, si quisieramos desarrollar algo más serio con esa *técnica* iríamos directo 
a una infinidad de complicaciones.

Por ello para desarrollar aplicaciones en wxPython se utiliza otra metodología, que consiste en 
crear clases heredadas de las proporcionadas por la librería, y en estás clases heredadas modificar/adicionar 
las características que tendrá nuestro frame o cualquier otro control gráfico. Básicamente esto 
consiste en los siguientes puntos:

1. Heredar una clase de `wx.Frame`
2. Agregar los controles gráficos necesarios a nuestro Frame en su método `__init__` (o pseudoconstructor).
3. Definir los eventos como métodos de la clase que se ha heredado.
4. Crear una instancia de `wx.App` y una de nuestra clase heredada de wx.Frame.
5. Llamar al método `MainLoop` de `wx.App`.

Traducido a código puro y duro:

```python
import wx

class MiFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(400,300))
		# Agregando los controles
		self.bt = wx.Button(self, -1, u"Botón 1", pos=(0,0))
		self.txt = wx.TextCtrl(self, -1, "",pos=(100,0))
		# Eventos
		self.Bind(wx.EVT_BUTTON, self.OnClick)
		# Mostrar la ventana
		self.Show()
		
	def OnClick(self,event):
		print "Hola wxPython"


if __name__=='__main__':
	app = wx.App()
	fr = MiFrame(None, "Test 01")
	app.MainLoop()

```


Por ahora ha sido todo respecto a cómo *construir* una aplicación muy básica, evidentemente hay muchas 
cosas por mejorar en esta aplicación que iremos viendo en entradas posteriores.
