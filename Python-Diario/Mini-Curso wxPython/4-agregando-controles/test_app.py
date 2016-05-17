# -*- coding: utf8 -*-
import wx

class MiFrame(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        
        self.text = wx.StaticText(self, wx.ID_ANY, "Etiqueta", pos=(10,100), size=(100,-1))
        #~ self.text2 = wx.StaticText(self, wx.ID_ANY, "Etiqueta", pos=(100,100), size=(100,-1))
        self.text.SetBackgroundColour("#ff00ff")
        
        self.Centre(True)
        self.Show()


            
if __name__=='__main__':
    app = wx.App() 
    fr = MiFrame(None, -1, "wxPython App", size=(300,200))
    app.MainLoop()
