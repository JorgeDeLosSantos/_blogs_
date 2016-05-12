# -*- coding: utf8 -*-
import wx

class PasswordDialog(wx.Dialog):
	def __init__(self,**kwargs):
		wx.Dialog.__init__(self,parent=None,title="Password Dialog",
						   size=(300,200),**kwargs)
		self.sz = wx.BoxSizer(wx.VERTICAL)
		self.panel = wx.Panel(self, -1)
		
		self.userfield = wx.TextCtrl(self.panel, -1)
		self.passfield = wx.TextCtrl(self.panel, -1, style=wx.TE_PASSWORD)
		self.okbt = wx.Button(self.panel, wx.ID_OK)
		self.cancelbt = wx.Button(self.panel, wx.ID_CANCEL)
		
		self.sz.Add(self.usertxt, 1, wx.EXPAND|wx.ALL, 5)
		self.sz.Add(self.passtxt, 1, wx.EXPAND|wx.ALL, 5)
		self.sz.Add(self.okbt, 1, wx.EXPAND|wx.ALL, 5)
		
		# Configurando sizer
		self.panel.SetSizer(self.sz)


if __name__=='__main__':
	app = wx.App()
	dlg = PasswordDialog()
	if dlg.ShowModal()==wx.ID_OK:
		print 1
	dlg.Destroy()
	app.MainLoop()
	
