# -*- coding: utf8 -*-
import wx


class MiFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(400,300))
		# Agregando los controles
		self.bt = wx.Button(self, -1, u"Botón 1", pos=(0,0))
		self.txt = wx.TextCtrl(self, -1, "",pos=(100,0))
		# Eventos
		self.Bind(wx.EVT_BUTTON, self.OnClick)
		# Mostrar la ventana
		self.Show()
		
	def OnClick(self,event):
		print "Hola wxPython"


if __name__=='__main__':
	app = wx.App()
	fr = MiFrame(None, "Test 01")
	app.MainLoop()
