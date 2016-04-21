# Aplicaciones y POO

En la *entrega anterior* vimos como desarrollar una aplicación wxPython muy elemental, con unas cuantas líneas de código. 
Todo esto está muy bien, pero cuando querramos desarrollar una aplicación un poco más compleja vamos a tener muchos 
problemas con ese mismo enfoque. Además, cuando se requiera programar las respuestas a los eventos, se necesita mucho 
*intercambio de información* entre el objeto que lanza el evento y las funciones o rutinas que los manejan (handlers), 
y de esa manera, aun con la *ayuda* de las funciones es un tanto díficil mantener el código legible.

Debido a lo comentado en el párrafo anterior, las aplicaciones en wxPyhon comúnmente se desarrollan utilizando un 
diseño orientado a objetos, donde, típicamente se escriben clases heredadas de los controles gráficos de 
wxPython. 

Lo más común, es crear una clase que herede de `wx.Frame`, y en esta ir agregando todos los controles gráficos que 
necesitemos para que la aplicación sea funcional. Como este mini-curso es de caracter básico/introductorio utilizaremos 
casi siempre la *plantilla* que a continuación se muestra:

```python
import wx

class MiFrame(wx.Frame):
	def __init__(self,*args,**kwargs):
		wx.Frame.__init__(self,*args,**kwargs)
		# Agregamos controles
		# Conectamos eventos
        self.Show() # Mostramos el Frame

	def OnEvent(self,event):
		# Método que "maneja" un evento

if __name__=='__main__':
	app = wx.App()
	fr = MiFrame(None, wx.ID_ANY, "wxPython App", size=(300,200))
	app.MainLoop()
```

Ahora vamos a tratar de explicar un poco lo anterior. 

Primero, definimos una clase `MiFrame` heredada de `wx.Frame`, agregamos el método `__init__` que para efectos de 
este mini-curso será nuestro *constructor* de la clase, y aquí en `__init__` es necesario llamar también al método 
`__init__` de la superclase, pasándole como argumentos aquellos que hemos recibido desde el constructor de 
nuestra clase `MiFrame`. Note que, debido a la sintaxis de Python, el parámetro `self` será siempre el primer 
argumento del método `__init__` de la clase y superclase. Dentro del método `__init__` habrán de agregarse 
todos los controles (que veremos en la siguiente entrega) y hacer las *conexiones* de eventos requeridas. 
El método Show sirve, claro está, para mostrar el Frame en la pantalla.

<blockquote style="border-radius: 5px; font-size: 12px; padding: 5px; 
border-left: thick solid #ddddff; border-right: thick solid #ddddff;
background-color: #fafafa;">

Para llamar al método `__init__` de la superclase, también puede utilizar la otra notación que implica el uso de `super`, algo como:
```python
super(MiFrame, self).__init__(*args,**kwargs)
```
</blockquote>

El método `OnEvent` ejemplifica la estructura de un método que se encarga de *manejar* la respuesta a 
un evento, lo cual estaremos viendo en entradas posteriores.

Finalmente, lo único que hacemos es instanciar un objeto de la clase `MiFrame`, con los mismos argumentos que utilizaríamos 
para uno de `wx.Frame`. Y bueno, lo de la clase `wx.App` ya nos lo sabemos, puesto que lo hemos visto en la entrada anterior.

Para que lo anterior quede un poco más claro vamos a ver ejemplo *reproducible*, para que ustedes puedan escribir (o copiar) el 
código, correrlo y jugar con el, de eso se trata.

```python
import wx

class MiFrame(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)

        # Agregando botones
        self.button = wx.Button(self, -1, u"Botón A", size=(100,20), pos=(10,10))
        self.button = wx.Button(self, -1, u"Botón B", size=(100,20), pos=(10,50))
        
        # Conectando el evento de un botón
        self.Bind(wx.EVT_BUTTON, self.OnClick)
        
        # Mostrando la interfaz
        self.Show()
        
    def OnClick(self,event):
        print(u"Botón presionado: %s"%(event.EventObject.GetLabel()))

            
if __name__=='__main__':
    app = wx.App() 
    fr = MiFrame(None, -1, "wxPython App", size=(300,200))
    app.MainLoop()
```

No deben preocuparse si hay algunas partes del código que puedan resultar incomprensibles ahora, la idea de lo 
anterior es nada más mostrar una mini-estructura de aplicación wxPython, ya iremos viendo y puliendo cada 
uno de esos elementos.

Ya en la siguiente entrada veremos cómo agregar controles a un Frame, y posicionarlos manualmente mediante 
el atributo `pos`, haciendo referencia también otros detalles como el posicionamiento automático mediante 
Sizers (un tema que veremos un poco después de habernos familiarizado más con wxPython). 

Y ya saben: cualquier sugerencia, comentario, duda u otro tipo de colaboración será siempre bienvenida.

<button type="button" style="background-color: rgba(102,217,255,0.6); border-radius: 5px; box-shadow: 2px #ffaaff; padding: 5px;">
<a href="http://www.pythondiario.com/2016/03/mini-curso-de-wxpython-1-introduccion.html#sumario-del-curso" style="color: #505050"><strong>Volver al índice</strong></a></button>

