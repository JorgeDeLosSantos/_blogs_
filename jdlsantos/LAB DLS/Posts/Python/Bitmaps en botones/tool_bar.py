# -*- coding: utf8 -*-
import wx

class MiAplicacion(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(300,250))
		# Sizer
		self.sz = wx.BoxSizer(wx.VERTICAL)
		# Botones
		for num in range(1,6):
			bt = wx.Button(self, -1, u"Botón "+str(num))
			bt.SetBitmap(wx.Bitmap(r"img/ic_save.png", wx.BITMAP_TYPE_ANY), wx.LEFT)
			self.sz.Add(bt, 1, wx.EXPAND|wx.ALL, 4)
		#Configurar sizer
		self.SetSizer(self.sz)
		self.Centre(True)
		self.Show()

if __name__=='__main__':
	app = wx.App()
	frame = MiAplicacion(None, u"Botones bitmap")
	app.MainLoop()
