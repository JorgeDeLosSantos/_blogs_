# -*- coding: utf-8 -*-
import wx

class TestFrame(wx.Frame):
	def __init__(self,*args,**kwargs):
		wx.Frame.__init__(self,*args,**kwargs)
		sizer = wx.BoxSizer(wx.VERTICAL)
		# Datos para los ComboBox
		nombres =  u"Ana|Pablo|Daniela|Jorge|David|Dulce".split("|")
		paises = u"México|Colombia|Chile|Argentina|España|Uruguay".split("|")
	    # Controles gráficos
		self.cbbox_nombres = wx.ComboBox(self, -1, choices=nombres, size=(120,25))
		self.cbbox_paises = wx.ComboBox(self, -1, choices=paises, size=(120,25))
		self.txt = wx.TextCtrl(self, -1, size=(150,25), style=wx.TE_CENTRE)
		self.txt.SetBackgroundColour("#d0fefe")
		# Agregando controles al sizer
		sizer.Add(self.cbbox_nombres, 0, wx.ALIGN_CENTRE|wx.ALL, 10)
		sizer.Add(self.cbbox_paises, 0, wx.ALIGN_CENTRE|wx.ALL, 10)
		sizer.Add(self.txt, 0, wx.ALIGN_CENTRE|wx.ALL, 10)
		# Configurando sizer
		self.SetSizer(sizer)
		# Configurando eventos
		self.Bind(wx.EVT_COMBOBOX, self.OnSelect)
		self.Show()
		
	def OnSelect(self,event):
		nombre = self.cbbox_nombres.GetValue()
		pais = self.cbbox_paises.GetValue()
		statxt = nombre + " es de " + pais
		self.txt.SetLabel(statxt)


if __name__=='__main__':
	app = wx.App()
	fr = TestFrame(None, title="ComboBox Test", size=(250,200))
	app.MainLoop()
	
