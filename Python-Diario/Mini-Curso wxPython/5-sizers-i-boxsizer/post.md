// # Sizers I. BoxSizer

Como se ha mencionado en entradas anteriores, los *sizers* son algoritmos utilizados 
por wxPython para distribuir controles dentro de un contenedor.

En wxPython se tiene disponibles diversos tipos de *sizers*, listados a continuación:

* **Grid** (`wx.GridSizer`). Distribuye los controles en una rejilla regular de mxn.
* **Flex Grid** (`wx.FlexGridSizer`). Similar a Grid, pero permite mayor flexibilidad respecto al tamaño de los controles.
* **Grid Bag** (`wx.GridBagSizer`). El *sizer* de tipo Grid más flexible en cuanto a tamaño y posición.
* **Box** (`wx.BoxSizer`). Distribuye los controles en una columna o fila dispuesta de manera vertical u horizontal.
* **Static Box** (`wx.StaticBoxSizer`). Similar a Box, pero con una línea que delimita de manera visual.

En esta entrada veremos el uso de *Box Sizer*, que es el *sizer* más simple.

Normalmente para utilizar *sizers*, se debe seguir una metodología como la indicada en 
la siguiente imagen:


Para crear un *Box Sizer* se debe instanciar un objeto de la clase `wx.BoxSizer` como sigue:



```python
boxsz = wx.BoxSizer(orientacion)
```
Donde `orientacion` puede ser una de las constantes: `wx.VERTICAL` y `wx.HORIZONTAL`, mismas que indican 
la orientación de los controles dentro del contenedor:


<button type="button" style="background-color: rgba(102,217,255,0.6); border-radius: 5px; box-shadow: 2px #ffaaff; padding: 5px;">
<a href="http://www.pythondiario.com/2016/03/mini-curso-de-wxpython-1-introduccion.html#sumario-del-curso" style="color: #505050; 
text-decoration: none;"><strong>Volver al índice</strong></a></button>

