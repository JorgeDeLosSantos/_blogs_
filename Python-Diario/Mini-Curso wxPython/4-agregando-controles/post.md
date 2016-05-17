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

Como se observa, el primer argumento indicado es el parámetro **self**, el cual no se pasa de manera explícita en 
los argumentos de entrada.

<button type="button" style="background-color: rgba(102,217,255,0.6); border-radius: 5px; box-shadow: 2px #ffaaff; padding: 5px;">
<a href="http://www.pythondiario.com/2016/03/mini-curso-de-wxpython-1-introduccion.html#sumario-del-curso" style="color: #505050; 
text-decoration: none;"><strong>Volver al índice</strong></a></button>

