# Nuestra primera aplicación

> wxPython is the best and most mature cross-platform GUI toolkit, given a number of constraints. The only reason wxPython isn't the standard Python GUI toolkit is that Tkinter was there first. - *Guido van Rossum*

### Para empezar

La mayoría de nosotros asociamos el término app o aplicación gráfica a un programa de computadora que 
se compone normalmente de una ventana y algunos controles gráficos *incrustados* que permiten 
al usuario interactuar con la lógica del programa. Y sí, en la mayoría de los casos esto es cierto, 
sin ser excepción en wxPython. La aplicación más *simple* en wxPython tendría una estructura como 
la siguiente:

```python
import wx

app = wx.App()
# X componente gráfico agregado
app.MainLoop()
```

Ese componente **X** podría ser una ventana o Frame, un cuadro de diálogo, o cualquier otro 
*container* que pueda ser instanciado sin necesidad de un objeto padre como referencia. 

Por ejemplo, podríamos mostrar un pequeño cuadro de diálogo que nos de la bienvenida al curso:

```python
import wx

app = wx.App()
wx.MessageBox(u"¡Bienvenidos al curso de wxPython!","Python Diario")
app.MainLoop()
```

¿Bastante bien, verdad?, y quizá para alguien esa aplicación es todo lo que necesita, 
puede cumplir con la tarea de mostrar un mensaje de forma gráfica, lo cual ya es en 
cierto grado *guay*. Pero podemos hacer mejores cosas, claro que sí, podríamos comenzar 
a *conectar* al usuario con la lógica del programa:

```python
import wx

app = wx.App()
dlg = wx.MessageDialog(None, u"¿Deseas continuar?", u"Python Diario")
if dlg.ShowModal()==wx.ID_OK:
    print(u"Has decidido continuar, gracias.")
else:
    print(u"Has abandonado, vuelve pronto.")
app.MainLoop()
```

Un poco mejor, el código anterior muestra un típico cuadro de diálogo que le pregunta al usuario 
si desea continuar, y dependiendo de la respuesta el programa imprimirá en 
la consola de salida el mensaje correspondiente. No se preocupen por las partes que puedan resultar 
*incomprensibles* ahora, ya veremos esto con bastante detalle cuando lleguemos al tema de 
los cuadros de diálogo.


### El clásico Frame

Bien, ha llegado el momento de presentarles el clásico **frame** de una aplicación wxPython. 
Los frames son las ventanas que estamos muy acostumbrados a ver en cualquier sistema 
operativo actual, en ellos se colocan todos los controles gráficos que componen 
a una aplicación.

En wxPython un frame se crea instanciando un objeto de la clase `wx.Frame`, cuya sintaxis 
mínima es la siguiente:

```python
frame = wx.Frame(parent, id, title)
```

Donde *parent* es el objeto padre, *id* un identificador unico y *title* el título o cadena 
que se mostrará en la parte superior de la ventana. Ahora vamos a explicar un poco 
los conceptos de objeto padre y de identificador.

Con **objeto padre** hacemos referencia a un objeto gráfico de wxPython en 
el cual estará contenido el objeto que se instancia, normalmente para un frame este valor 
suele ser `None` para indicar que no tiene un objeto padre, puesto que normalmente son 
el contenedor de mayor jerarquía en una aplicación.

El **id** o identificador único, es un número entero que sirve para referenciar a un objeto 
gráfico, y como tal este deberá ser único e irrepetible dentro de la aplicación. Normalmente 
se prefiere no asignar estos números de manera manual, sino en cambio dejar que wxPython asigne 
de manera automática estos identificadores, para ello basta con asignar un `-1` al valor del **id** 
o bien asignar la constante `wx.ID_ANY`.

Ahora ya estamos listos para crear nuestra primer ventana:

```python
import wx

app = wx.App()
fr = wx.Frame(None, -1, u"Hola wxPython!")
fr.Show()
app.MainLoop()
```

Bastante bien para un *hola mundo*, ahora viene la parte interesante, vamos a 
*desmenuzar* un poco el código anterior.

Lo primero, y al parecer resulta muy obvio, es importar la librería wxPython, esto lo 
hacemos con `import wx`, con lo cual tenemos disponibles todos los controles básicos 
de la librería, además de muchas clases, funciones y constantes auxiliares, así como 
las clases para controlar y lanzar eventos.

Enseguida instanciamos un objeto de la clase `App`, que no es más que la aplicación 
misma. Debe saber que para utilizar cualquier objeto gráfico de la librería wxPython 
deberá primero inicializar esta clase.

Ya en líneas anteriores explicamos lo referente al Frame, sólo debemos agregar 
que el método Show() se encarga de *mostrar* el Frame en la pantalla del usuario, 
de lo contrario no será visible.

Finalmente *llamamos* al método MainLoop de la clase `App`, con lo cual la aplicación 
se pone en espera de que el usuario interactue con ella, gestionando los eventos y 
respondiendo a ellos dependiendo de lo que se haya programado para cada caso.

Se preguntarán ustedes amables lectores, y ahora, ¿cómo cambiamos el tamaño de la ventana?, 
¿cómo utilizamos un color de fondo diferente?, ¿cómo agregamos un ícono?, ¿cómo agregamos 
controles gráficos?. Si, hay muchas preguntas y pocas respuestas por ahora, pero esa es la 
clave: ser pacientes y constantes. 

Así de manera breve y para que vayamos entrando en la *filosofía* de wxPython les comento 
que hay básicamente dos maneras de especificar y/o modificar las características de un objeto gráfico:

* Al instanciarlo, es posible indicar muchas de sus características mediante *keyword arguments*, 
por ejemplo para el caso del Frame anterior es posible especificarle un tamaño mediante 
el *keyword argument* `size`:

```python
	fr = wx.Frame(None, -1, u"Hola wxPython!", size=(300,200))
```

* Utilizando métodos podemos modificar las propiedades de los objetos, podemos de igual forma 
modificar el tamaño del Frame utilizando el método `SetSize`:

```python
	fr.SetSize((300,200))
```

### Lo bueno, lo mejor y lo que viene...

Lo bueno es que ya hemos creado nuestra primera aplicación de wxPython, aunque sólo sea una 
*ventanita* por algo se empieza, no vamos a correr ahora, pero iremos *de prisa* hacia adelante, 
como dice el refrán: *despacio porque tengo prisa*. Vamos, como todo en la vida pues.

Siempre es bueno decir que lo mejor está por venir, y que así sea. Hasta ahora hemos visto 
una pequeña aplicación pero sin entrar mucho en la programación orientada a objetos, lo cual 
es esencial en wxPython, en la próxima entrega de este mini-curso estaremos hablando de 
cómo diseñar y programar una aplicación de wxPython utilizando el paradigma de la POO, 
de cómo heredar las clases de los objetos gráficos e implementar, claro, un aplicación 
un poco más *"wxPythonica"* (si, esa palabra no existe, pero debería existir ¿no?).

Así que, les recomendaría darle un pequeño repaso a vuestras clases de programación orientada a 
objetos en Python y así recordar algunas cuestiones necesarias para sobrevivir a este curso. Y para no ir 
tan lejos por aquí les dejo una [entrada]( http://www.pythondiario.com/2014/10/clases-y-objetos-en-python-programacion.html) 
que tenemos en el blog que expone los conceptos elementales de la programación orientada a objetos.

Además de invitarlos a que nos dejen sus comentarios, opiniones, sugerencias, y lo que ustedes 
crean conveniente, que estaremos muy agradecidos de vuestra retroalimentación, sin más: *¡sigamos programando!*.

[**Volver al índice**](http://www.pythondiario.com/2016/03/mini-curso-de-wxpython-1-introduccion.html#sumario-del-curso)

