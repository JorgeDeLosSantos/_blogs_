# Imágenes en menús de wxPython

Los menús en wxPython se definen de manera muy sencilla creando primeramente la barra de menú principal, 
derivada de la clase `wx.MenuBar`, enseguida se definen los menús principales que compondrán la barra de menú, derivando 
estos de la clase `wx.Menu`, finalmente se agregan los sub-menús que tienen cómo base la clase `wx.MenuItem`.
En el siguiente esquema se muestra la jerarquía de menús en wxPython.

![Jerarquía menús wxPython](img/wxmenu.png)

Un ejemplo muy básico:

```python
self.mb = wx.MenuBar() # Creamos barra de menú
# Creamos el menú archivo
self.archivo = wx.Menu()
# Creamos los MenuItem (Guardar, Abrir)
self.guardar = wx.MenuItem(self.archivo,-1,"Guardar")
self.archivo.AppendItem(self.guardar)
self.abrir = wx.MenuItem(self.archivo,-1,"Abrir","")
self.archivo.AppendItem(self.abrir)
# Agregando el menú "Archivo" a la barra
self.mb.Append(self.archivo, "Archivo")
# Configurando a "mb" como la barra de menú del Frame
self.SetMenuBar(self.mb)
```

En lo anterior se supone que todo ese codigo está inmerso dentro de una clase heredada de `wx.Frame`. Así, se crea una barra 
de menú similar a lo mostrado en la siguiente imagen:

![Imágenes en un menú wxPython](img/img1.png)

Para agregar una imagen al menú, se debe utilizar el método `SetBitmap` de la clase `wx.MenuItem`, pasando como parámetro 
un objeto de la clase `wx.Bitmap`, el cual deberá contener la información necesaria de la imagen o icono a utilizar, 
debe tomarse en cuenta que el método `SetBitmap` deberá "llamarse" antes de agregar el sub-menú al menú padre, de 
lo contrario no se verá reflejado dicho método.

Enseguida se adjunta el código completo de una aplicación wxPython que incluye imágenes en menús.

```python
# -*- coding: utf8 -*-
import wx

class MiAplicacion(wx.Frame):
  def __init__(self,parent,title):
    wx.Frame.__init__(self,parent,title=title,size=(300,200))
    self.createMenu() # Llamamos al método que inicializa el menú
    self.Centre(True)
    self.Show()
    
  def createMenu(self):
    """
    Crea el menú de la aplicación
    """
    # Menú archivo
    self.archivo = wx.Menu()
    # Agregamos el sub-menú Guardar
    self.guardar = wx.MenuItem(self.archivo,-1,"Guardar")
    self.guardar.SetBitmap(wx.Bitmap( u"img/ic_save.png", wx.BITMAP_TYPE_ANY ))
    self.archivo.AppendItem(self.guardar)
    # Agregamos el sub-menú Abrir
    self.abrir = wx.MenuItem(self.archivo,-1,"Abrir")
    self.abrir.SetBitmap(wx.Bitmap( u"img/ic_open.png", wx.BITMAP_TYPE_ANY ))
    self.archivo.AppendItem(self.abrir)
    # Agregamos el sub-menú Imprimir
    self.imprimir = wx.MenuItem(self.archivo,-1,"Imprimir")
    self.imprimir.SetBitmap(wx.Bitmap( u"img/ic_print.png", wx.BITMAP_TYPE_ANY ))
    self.archivo.AppendItem(self.imprimir)
    # Agregamos el sub-menú Salir
    self.salir = wx.MenuItem(self.archivo,-1,"Salir")
    self.salir.SetBitmap(wx.Bitmap( u"img/ic_exit.png", wx.BITMAP_TYPE_ANY ))
    self.archivo.AppendItem(self.salir)
    # Creamos la barra de menú principal y la configuramos
    self.mb = wx.MenuBar()
    self.mb.Append(self.archivo, "Archivo")
    self.SetMenuBar(self.mb)

if __name__=='__main__':
  app = wx.App()
  frame = MiAplicacion(None, u"Imágenes Menú")
  app.MainLoop()
```

![Imágenes en un menú wxPython](img/img2.png)

