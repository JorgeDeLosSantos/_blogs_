# -*- coding: utf8 -*-
import wx

class MiFrame(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)

        # Etiquetas ...
        self.labelA = wx.StaticText(self, wx.ID_ANY, "A", pos=(10,10), size=(80,25))
        self.labelB = wx.StaticText(self, wx.ID_ANY, "B", pos=(10,40), size=(80,25))
        self.labelR = wx.StaticText(self, wx.ID_ANY, "Resultado", pos=(10,70), size=(80,25))
        
        # Inputs
        self.A = wx.TextCtrl(self, wx.ID_ANY, pos=(100,10), size=(180,25))
        self.B = wx.TextCtrl(self, wx.ID_ANY, pos=(100,40), size=(180,25))
        self.R = wx.TextCtrl(self, wx.ID_ANY, pos=(100,70), size=(180,25))

        # Botones
        self.suma = wx.Button(self, wx.ID_ANY, "+", pos=(55,120), size=(40,30))
        self.resta = wx.Button(self, wx.ID_ANY, "-", pos=(105,120), size=(40,30))
        self.multiplicacion = wx.Button(self, wx.ID_ANY, "*", pos=(155,120), size=(40,30))
        self.division = wx.Button(self, wx.ID_ANY, "/", pos=(205,120), size=(40,30))

        self.Centre(True)
        self.Show()
            
if __name__=='__main__':
    app = wx.App() 
    fr = MiFrame(None, -1, "wxPython App", size=(300,200))
    app.MainLoop()
