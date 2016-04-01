# -*- coding: utf-8 -*-
import wx

class TestFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(200,200))
		
		self.boton1 = wx.Button(self, -1, u"Uno", size=(100,20),
								pos=(50,10))
		self.boton2 = wx.Button(self, -1, u"Dos", size=(100,20),
								pos=(50,50))
		self.boton3 = wx.Button(self, -1, u"Tres", size=(100,20),
								pos=(50,90))
		# Conectando eventos
		self.Bind(wx.EVT_BUTTON, self.OnClick)
		
		self.Centre(True)
		self.Show()
		
	def OnClick(self,event):
		bt_label = event.GetEventObject().GetLabel()
		print u"Has presionado el botón %s"%(bt_label)

if __name__=='__main__':
	app = wx.App()
	fr = TestFrame(None, "Test wxButton")
	app.MainLoop()
