# -*- coding: utf-8 -*-
import wx
import wx.grid as wxgrid

class TestFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(200,200))
		self.panel = wx.Panel(self, -1)
		self.sz = wx.BoxSizer(wx.VERTICAL)
		
		# Grilla
		filas = 2
		columnas = 2
		self.grid = wxgrid.Grid(self.panel, -1)
		self.grid.CreateGrid(filas,columnas)
		self.grid.SetRowLabelSize(60)
		for col in range(columnas):
			self.grid.SetColSize(col, 60)
			self.grid.SetColLabelValue(col, "%s"%(col+1))
		
		# Campo de texto para resultados
		self.res = wx.TextCtrl(self.panel, -1, u"", style=wx.TE_CENTRE)
		
		# Botón para calcular
		self.bt = wx.Button(self.panel, -1, u"Calcular")
		
		# Agregando elementos al sizer
		self.sz.Add(self.grid, 5, wx.EXPAND|wx.ALL, 2)
		self.sz.Add(self.res, 1, wx.EXPAND|wx.ALL, 2)
		self.sz.Add(self.bt, 1, wx.ALIGN_CENTRE|wx.ALL, 2)
		
		# Conectando eventos 
		self.Bind(wx.EVT_BUTTON, self.OnCalc, self.bt)
		self.Bind(wxgrid.EVT_GRID_CELL_CHANGED, self.OnCellEdit)
		
		self.panel.SetSizer(self.sz)
		self.Centre(True)
		self.Show()
		
	def OnCalc(self,event):
		"""
		Ejecuta el cálculo del determinante, utilizando 
		como punto de entrada la matriz obtenida mediante 
		el método GetMatrix. El resultado obtenido se 
		muestra en el TextCtrl destinado para tal uso.
		"""
		M = self.GetMatrix()
		if M is None:
			wx.MessageBox("Rellene todas las celdas...")
			return None
		det = (M[0][0]*M[1][1]) - (M[0][1]*M[1][0])
		res = "det(M) = %s"%(det)
		self.res.SetValue(res)
		
	def GetMatrix(self):
		"""
		Construye una lista de listas para 
		representar una matriz de 2x2.
		"""
		rows = self.grid.GetNumberRows()
		cols = self.grid.GetNumberCols()
		M = []
		for row in range(rows):
			_crow = []
			for col in range(cols):
				cval = self.grid.GetCellValue(row,col)
				if not cval:
					return None
				_crow.append(float(cval))
			M.append(_crow)
		return M
		
	def OnCellEdit(self,event):
		"""
		Verifica que el valor introducido en una 
		celda sea un número, de lo contrario elimina el valor.
		"""
		ii,jj = event.GetRow(), event.GetCol()
		inval = self.grid.GetCellValue(ii,jj)
		try:
			cnum = float(inval)
		except:
			self.grid.SetCellValue(ii,jj,"")
		

if __name__=='__main__':
	app = wx.App()
	fr = TestFrame(None, "Determinante")
	app.MainLoop()
