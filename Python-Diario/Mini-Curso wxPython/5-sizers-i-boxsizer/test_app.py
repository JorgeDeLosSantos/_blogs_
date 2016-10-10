# -*- coding: utf8 -*-
import wx

class MiFrame(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        # BoxSizer
        box = wx.BoxSizer(wx.HORIZONTAL)

        self.b1 = wx.Button(self, wx.ID_ANY, u"Botón 1")
        self.b2 = wx.Button(self, wx.ID_ANY, u"Botón 2")
        self.b3 = wx.Button(self, wx.ID_ANY, u"Botón 3")

        box.Add(self.b1, 1, wx.EXPAND)
        box.Add(self.b2, 2, wx.EXPAND)
        box.Add(self.b3, 1, wx.EXPAND)

        self.SetSizer(box)
        self.Centre(True)
        self.Show()
            
if __name__=='__main__':
    app = wx.App() 
    fr = MiFrame(None, -1, "wxPython App", size=(300,200))
    app.MainLoop()