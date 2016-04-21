# Aplicaciones y POO

<blockquote style="border-radius: 5px; font-size: 12px; padding: 5px; border-left: 
thick solid #0000ff; border-right: thick solid #0000ff;">

</blockquote>

En la *entrega anterior* vimos como desarrollar una aplicación wxPython muy elemental, con unas cuantas líneas de código. 
Todo esto está muy bien, pero cuando querramos desarrollar una aplicación un poco más compleja vamos a tener muchos 
problemas con ese mismo enfoque. Además, cuando se requiera programar las respuestas a los eventos, se necesita mucho 
*intercambio de información* entre el objeto que lanza el evento y las funciones o rutinas que los manejan (handlers), 
y de esa manera, aun con la *ayuda* de las funciones es un tanto díficil mantener el código legible.

Debido a lo comentado en el párrafo anterior, las aplicacione en wxPyhon comúnmente se desarrollan utilizando un 
diseño orientado a objetos, donde, típicamente se escriben clases heredadas de los controles gráficos de 
wxPython. 

Lo más común, es crear una clase que herede de `wx.Frame`, y en esta ir agregando todos los controles gráficos que 
necesitemos para que la aplicación sea funcional. Como este mini-curso es de caracter básico/introductorio utilizaremos 
casi siempre la *plantilla* que a continuación se muestra:

```python
class MiFrame(wx.Frame):
	def __init__(self,*args,**kwargs):
		wx.Frame.__init__(self,*args,**kwargs)
		# Agregamos controles aquí ...
		# Conectamos eventos

	def OnEvent(self,event):
		# 


if __name__=='__main__':
	app = wx.App()
	fr = MiFrame()
	fr.Show()
	app.MainLoop()
```


<button type="button" style="background-color: rgba(102,217,255,0.6); border-radius: 5px; box-shadow: 2px #ffaaff; padding: 5px;">
<a href="http://www.pythondiario.com/2016/03/mini-curso-de-wxpython-1-introduccion.html#sumario-del-curso" style="color: #505050"><strong>Volver al índice</strong></a></button>

