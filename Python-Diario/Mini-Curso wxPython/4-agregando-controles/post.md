// # Agregando controles

En las entradas anteriores hemos visto algunos ejemplos de aplicaciones muy sencillas 
que contienen algunos controles, pero aún no hemos *hecho hincapié* en la forma de 
agregar los controles y todas las consideraciones que esto conlleva.

Antes de comenzar hay algunas cuestiones que debemos aclarar un poco. En toda librería 
gráfica existe el concepto de componente y contenedor, o de *padre* e *hijo*, el 
componente u *objeto hijo* será cualquier control gráfico contenido dentro de un 
contenedor (sí, suena raro, pero así es). Normalmente dentro del grupo de contenedores 
se incluyen todos aquellos elementos como los paneles y frames, que sirven para 
organizar el contenido de una interfaz gráfica.

En wxPython existen dos formas de agregar y distribuir los objetos gráficos dentro 
de nuestra interfaz, a saber:

* Posicionamiento absoluto
* Utilizando sizers 

El **posicionamiento absoluto** implica colocar los controles gráficos de manera 
absoluta mediante el argumento `pos`, en el cual se indica mediante una tupla de dos 
elementos la posición en X e Y medida en pixeles. Esta es una forma un tanto sencilla de posicionar 
componentes, pero que en aplicaciones que van más allá de unos cuantos controles 
resulta difícil de implementar.

El **uso de sizers** es, digamos, la forma *correcta* de ir agregando controles a nuestra aplicación, 
quizá al principio pueda resultar un poco más complicada de entender, pero, las ventajas son muy notorias 
desde muy temprano. Sin entrar en muchos detalles técnicos, los **sizers** son *mecanismos de diseño* que 
sirven para posicionar y redimensionar los objetos dentro de una interfaz gráfica.

Bueno, una vez *puestos en la mesa* los puntos anteriores, vamos a ver cómo agregamos controles a una 
interfaz gráfica. Normalmente, para instanciar un control de wxPython, el primer argumento será 
siempre el objeto padre, por ejemplo, veamos que nos dice la ayuda de wxPython sobre la sintaxis 
para crear un Botón:

```python
>>> help(wx.Button.__init__)
Help on method __init__ in module wx._controls:

__init__(self, *args, **kwargs) unbound wx._controls.Button method
    __init__(self, Window parent, int id=-1, String label=EmptyString, 
        Point pos=DefaultPosition, Size size=DefaultSize, 
        long style=0, Validator validator=DefaultValidator, 
        String name=ButtonNameStr) -> Button
```

Como se observa, el primer argumento indicado es el parámetro **self**, el cual no se pasa de manera 
explícita en los argumentos de entrada, seguido por un objeto padre, que es el primer 
argumento real que se pasa al momento de instanciar un objeto gráfico. Luego se debe colocar un 
identificador, que debe ser un entero cualesquiera, pero que normalmente se recomienda utilizar 
el -1 o la constante wx.ID_ANY para dejar que wxPython se encargue de asignar el número correspondiente. 
Luego, el resto de argumentos incluyen algunas cuestiones más propias de cada control. Note que 
también podemos pasar tanto la posición como el tamaño del objeto, mediante los argumentos 
`pos` y `size`, respectivamente. Una linea típica para el caso de un botón sería:

```python
boton = wx.Button(panel, wx.ID_ANY, u"Botón 1", pos=(0,0), size=(80,20))
```

De hecho en la entrada anterior vimos un ejemplo con dos botones posicionados de manera manual:

```python
import wx

class MiFrame(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)

        # Agregando botones
        self.button1 = wx.Button(self, -1, u"Botón A", size=(100,20), pos=(10,10))
        self.button2 = wx.Button(self, -1, u"Botón B", size=(100,20), pos=(10,50))
        
        # Mostrando la interfaz
        self.Show()

            
if __name__=='__main__':
    app = wx.App() 
    fr = MiFrame(None, -1, "wxPython App", size=(300,200))
    app.MainLoop()
```

En este caso, el objeto padre es el Frame mismo, y por ello se pasa el parámetro `self` como 
primer argumento. El -1 refiere al argumento `id`, y el string pasado en cada caso 
corresponde al argumento `label`. Note que se agregan los argumentos `size` y `pos` en forma 
de una tupla, que especifican el tamaño y posición de los botones, respectivamente. La 
posición (o coordenadas de posición) en wxPython se determina a partir de la esquina 
superior izquierda como origen y medida en pixeles.

Veamos un ejemplo más, con algunos otros controles y posicionando de manera manual/absoluta:

```python
import wx

class MiFrame(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)

        # Etiquetas ...
        self.labelA = wx.StaticText(self, wx.ID_ANY, "A", pos=(10,10), size=(80,25))
        self.labelB = wx.StaticText(self, wx.ID_ANY, "B", pos=(10,40), size=(80,25))
        self.labelR = wx.StaticText(self, wx.ID_ANY, "Resultado", pos=(10,70), size=(80,25))
        
        # Inputs
        self.A = wx.TextCtrl(self, wx.ID_ANY, pos=(100,10), size=(180,25))
        self.B = wx.TextCtrl(self, wx.ID_ANY, pos=(100,40), size=(180,25))
        self.R = wx.TextCtrl(self, wx.ID_ANY, pos=(100,70), size=(180,25))

        # Botones
        self.suma = wx.Button(self, wx.ID_ANY, "+", pos=(55,120), size=(40,30))
        self.resta = wx.Button(self, wx.ID_ANY, "-", pos=(105,120), size=(40,30))
        self.multiplicacion = wx.Button(self, wx.ID_ANY, "*", pos=(155,120), size=(40,30))
        self.division = wx.Button(self, wx.ID_ANY, "/", pos=(205,120), size=(40,30))

        self.Centre(True)
        self.Show()
            
if __name__=='__main__':
    app = wx.App() 
    fr = MiFrame(None, -1, "wxPython App", size=(300,200))
    app.MainLoop()
```

Ahora, implementemos este mismo ejemplo utilizando sizers:

```python
import wx

class MiFrame(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        # Sizers
        self.mainsz = wx.BoxSizer(wx.VERTICAL)
        self.inputsz = wx.FlexGridSizer(rows=3, cols=2, hgap=5, vgap=5)
        self.buttonsz = wx.BoxSizer(wx.HORIZONTAL)

        # Etiquetas ...
        self.labelA = wx.StaticText(self, wx.ID_ANY, "A")
        self.labelB = wx.StaticText(self, wx.ID_ANY, "B")
        self.labelR = wx.StaticText(self, wx.ID_ANY, "Resultado")
        
        # Inputs
        self.A = wx.TextCtrl(self, wx.ID_ANY)
        self.B = wx.TextCtrl(self, wx.ID_ANY)
        self.R = wx.TextCtrl(self, wx.ID_ANY)

        # Botones
        self.suma = wx.Button(self, wx.ID_ANY, "+")
        self.resta = wx.Button(self, wx.ID_ANY, "-")
        self.multiplicacion = wx.Button(self, wx.ID_ANY, "*")
        self.division = wx.Button(self, wx.ID_ANY, "/")

        # Agregando a sizers
        for obj in [self.labelA, self.A, self.labelB, self.B, self.labelR, self.R]:
            self.inputsz.Add(obj, 1, wx.EXPAND|wx.ALL, 2)
        self.inputsz.AddGrowableCol(1)

        for obj in [self.suma, self.resta, self.multiplicacion, self.division]:
            self.buttonsz.Add(obj, 1, wx.EXPAND|wx.ALL, 2)
            obj.SetInitialSize((20,-1))

        # Configurando sizers
        self.mainsz.Add(self.inputsz, 2, wx.EXPAND|wx.ALL, 5)
        self.mainsz.Add(self.buttonsz, 1, wx.EXPAND|wx.ALL, 5)
        self.SetSizer(self.mainsz)

        self.Centre(True)
        self.Show()
            
if __name__=='__main__':
    app = wx.App() 
    fr = MiFrame(None, -1, "wxPython App", size=(300,200))
    app.MainLoop()
```

Vaya, que con *sizers* hay que escribir más código, ¿no?. Bueno, posiblemente sí, 
pero ahora, intenta redimensionar la ventana de cada aplicación. Como se dijo, 
utilizar sizers tiene la enorme ventaja de que puedes redimensionar el `Frame` y 
el tamaño y posición de los objetos se ajusta a lo requerido. Además, imagina que 
tienes unas decenas de controles, ¿crees que es sencillo calcular y programar 
cada una de las posiciones y tamaños?, complicado ciertamente.

En la siguiente entrada de este curso estaremos viendo un poco más sobre los *sizers* 
y cómo utilizarlos para organizar controles dentro de una interfaz gráfica wxPython. 

Y bueno, recordarles que las preguntas, comentarios o cualquier otro, serán siempre 
bienvenidos.

<button type="button" style="background-color: rgba(102,217,255,0.6); border-radius: 5px; box-shadow: 2px #ffaaff; padding: 5px;">
<a href="http://www.pythondiario.com/2016/03/mini-curso-de-wxpython-1-introduccion.html#sumario-del-curso" style="color: #505050; 
text-decoration: none;"><strong>Volver al índice</strong></a></button>

