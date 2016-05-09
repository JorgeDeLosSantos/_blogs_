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
