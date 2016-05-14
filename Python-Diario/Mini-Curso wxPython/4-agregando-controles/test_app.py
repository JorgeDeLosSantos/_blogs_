# -*- coding: utf8 -*-
import wx

class MiFrame(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
<<<<<<< HEAD
        
        self.text = wx.StaticText(self, wx.ID_ANY, "Etiqueta", pos=(10,100), size=(100,-1))
        #~ self.text2 = wx.StaticText(self, wx.ID_ANY, "Etiqueta", pos=(100,100), size=(100,-1))
        self.text.SetBackgroundColour("#ff00ff")
        
        self.Layout()
        self.Fit()
        self.Show()

=======

        # Agregando botones
        self.button = wx.Button(self, -1, u"Botón A", size=(100,20), pos=(10,10))
        self.button = wx.Button(self, -1, u"Botón B", size=(100,20), pos=(10,50))
        
        # Conectando el evento de un botón
        self.Bind(wx.EVT_BUTTON, self.OnClick)
        
        # Mostrando la interfaz
        self.Show()
        
    def OnClick(self,event):
        print(u"Botón presionado: %s"%(event.EventObject.GetLabel()))
>>>>>>> 560f6d83f76c6ea405b09d0a656a5ee5325b4b59

            
if __name__=='__main__':
    app = wx.App() 
    fr = MiFrame(None, -1, "wxPython App", size=(300,200))
    app.MainLoop()
