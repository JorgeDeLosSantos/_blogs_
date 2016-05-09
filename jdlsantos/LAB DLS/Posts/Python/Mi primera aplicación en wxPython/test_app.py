# -*- coding: utf8 -*-
import wx

class MiAplicacion(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(400,300))
		boton = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		#sizer = wx.BoxSizer(wx.VERTICAL)
		#sizer.Add(boton, 1, wx.ALIGN_LEFT)
		#sizer.Add(texto, 1, wx.ALIGN_LEFT)
		#self.SetSizer(sizer)
		self.Centre(True)
		self.Show()

if __name__=='__main__':
	app = wx.App()
	frame = MiAplicacion(None, u"Mi aplicación")
	app.MainLoop()
