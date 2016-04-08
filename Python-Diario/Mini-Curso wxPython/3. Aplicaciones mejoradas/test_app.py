# -*- coding: utf8 -*-
import wx

app = wx.App()
fr = wx.Frame(None, -1, u"Hola wxPython!")
fr.SetSize((300,200))
fr.Show()
app.MainLoop()
