# Utilizando un ComboBox

Un ComboBox es un control gráfico que despliega una lista de opciones cuando se interactúa con el, permitiendo desde luego la 
selección de sus ítems y consecuentemente el lanzamiento de un evento de tipo `EVT_COMBOBOX`. Resulta lógico pensar que la 
utilidad de un ComboBox se hace notoria cuando se requiere disponer de una serie de opciones en un control que visualmente 
no ocupe mucho espacio.

El ejemplo siguiente es una mini-aplicación wxPython que contiene dos ComboBox y un TextCtrl, que básicamente lo que hace es 
mostrar en el TextCtrl una concatenación de las opciones seleccionadas en ambos ComboBox:

```python
import wx

class TestFrame(wx.Frame):
	def __init__(self,*args,**kwargs):
		wx.Frame.__init__(self,*args,**kwargs)
		sizer = wx.BoxSizer(wx.VERTICAL)
		# Datos para los ComboBox
		nombres =  u"Ana|Pablo|Daniela|Jorge|David|Dulce".split("|")
		paises = u"México|Colombia|Chile|Argentina|España|Uruguay".split("|")
	    # Controles gráficos
		self.cbbox_nombres = wx.ComboBox(self,-1,choices=nombres,size=(120,25))
		self.cbbox_paises = wx.ComboBox(self,-1,choices=paises,size=(120,25))
		self.txt = wx.TextCtrl(self, -1, size=(150,25), style=wx.TE_CENTRE)
		self.txt.SetBackgroundColour("#d0fefe")
		# Agregando controles al sizer
		sizer.Add(self.cbbox_nombres, 0, wx.ALIGN_CENTRE|wx.ALL, 10)
		sizer.Add(self.cbbox_paises, 0, wx.ALIGN_CENTRE|wx.ALL, 10)
		sizer.Add(self.txt, 0, wx.ALIGN_CENTRE|wx.ALL, 10)
		# Configurando sizer
		self.SetSizer(sizer)
		# Configurando eventos
		self.Bind(wx.EVT_COMBOBOX, self.OnSelect)
		self.Show()
		
	def OnSelect(self,event):
		nombre = self.cbbox_nombres.GetValue()
		pais = self.cbbox_paises.GetValue()
		statxt = nombre + " es de " + pais
		self.txt.SetLabel(statxt)


if __name__=='__main__':
	app = wx.App()
	fr = TestFrame(None, title="ComboBox Test", size=(250,200))
	app.MainLoop()
```

Vamos, un poco más despacio y con algunos detalles extras:

Primero (*y como siempre*) importamos el módulo `wx` para tener disponibles las clases que usaremos en el desarrollo de la 
aplicación. Definimos una clase `TestFrame` heredada de `wx.Frame` en la cual colocaremos todos los controles gráficos a 
utilizar.

Enseguida creamos los datos o listas que vamos a utilizar en los ComboBox, ha de saber que el método `split` de la clase 
`str` devuelve una lista de strings resultantes de *cortar* la cadena original en los segmentos delimitados por el 
caracter que se ha pasado como argumento ("|" para este caso).

Luego se crean los controles gráficos (ComboBox y TextCtrl), puede ver que para crear un ComboBox necesita instanciar un 
objeto de la clase `wx.ComboBox`, a la cual como argumentos mínimos se le debe indicar el objeto padre (parent), un id, 
y un lista de valores (choices) que contiene las opciones a desplegar. Adicionalmente puede definir otros *keyword arguments* 
como el tamaño y/o la posición del control.

Una vez se han creado los controles, estos se deben agregarse al sizer de la aplicación para que sean organizados acorde a 
la distribución o algoritmo de posicionamiento seleccionado.

Finalmente, se programa la respuesta que tendrá la aplicación cuando los ComboBox sean manejados por el usuario, para ello 
se asigna el método `OnSelect` como el handler de los eventos de tipo `wx.EVT_COMBOBOX`. Note que el método `OnSelect` 
contiene dos parámetros obligatorios por default, `self` que hace referencia a la clase misma y `event` que contiene 
información acerca del evento lanzado. En este caso el método `OnSelect` lo único que hace es tomar los strings 
seleccionados en cada uno de los ComboBox, y concatenarlos utilizando un nexo cualesquiera, para finalmente 
asignar la cadena resultante al valor del TextCtrl.