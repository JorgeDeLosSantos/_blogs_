# -*- coding: utf-8 -*-
import wx
import matplotlib.pyplot as plt
import numpy as np

def OnSelect(event):
	klw = 2
	event.artist.set_lw(event.artist.get_lw() + klw)
	fig.canvas.draw()
	app = wx.App()
	dlg = wx.MessageDialog(None, "Desea borrar",
	'Matplotlib Demo', wx.YES_NO|wx.ICON_QUESTION)
	if dlg.ShowModal() == wx.ID_YES:
		event.artist.remove()
	else:
		event.artist.set_lw(event.artist.get_lw() - klw)
	dlg.Destroy()
	app.MainLoop()
	fig.canvas.draw()

# Definir datos a plotear
X = np.random.random((10,5))
# Crear figure y axes
fig = plt.figure()
ax = fig.add_subplot(111)
# Graficar datos
ax.plot(X, picker=True)
# Conectar evento "pick_event"
pick = fig.canvas.mpl_connect("pick_event", OnSelect)
plt.show()
