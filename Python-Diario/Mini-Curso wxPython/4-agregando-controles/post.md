// # Agregando controles

En las entradas anteriores hemos visto algunos ejemplos de aplicaciones muy sencillas 
que contienen algunos controles, pero aún no hemos *hecho hincapié* en la forma de 
agregar los controles y todas las consideraciones que esto conlleva.

Antes de comenzar hay algunas cuestiones que debemos aclarar un poco. En toda librería 
gráfica existe el concepto de componente y contenedor, o de *padre* e *hijo*, el 
componente u *objeto hijo* será cualquier control gráfico contenido dentro de un 
contenedor (sí, suena raro, pero así es)


En wxPython existen dos formas de agregar y distribuir los objetos gráficos dentro 
de nuestra aplicación, a saber:

* Posicionamiento absoluto
* Utilizando sizers 

El **posicionamiento absoluto** implica colocar los controles gráficos de manera 
absoluta mediante el argumento `pos`, en el cual se indica mediante una tupla de dos 
elementos la posición en X e Y medida en pixeles. Esta es una forma un tanto sencilla de posicionar 
componentes, pero que en aplicaciones que van más allá de unos cuantos controles 
resulta difícil de implementar.

El **uso de sizers** es, digamos, la forma *correcta* 

<button type="button" style="background-color: rgba(102,217,255,0.6); border-radius: 5px; box-shadow: 2px #ffaaff; padding: 5px;">
<a href="http://www.pythondiario.com/2016/03/mini-curso-de-wxpython-1-introduccion.html#sumario-del-curso" style="color: #505050; 
text-decoration: none;"><strong>Volver al índice</strong></a></button>

