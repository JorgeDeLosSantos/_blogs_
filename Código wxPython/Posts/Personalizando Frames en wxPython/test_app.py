# -*- coding: utf8 -*-
import wx

class TestFrame(wx.Frame):
	def __init__(self,parent,title):
		styles = wx.DEFAULT_FRAME_STYLE & ~ (wx.CAPTION)
		wx.Frame.__init__(self,parent=parent,title=title,size=(400,300),
						  style=styles)
		self.SetBackgroundColour("#ff00ff")
		self.Centre(True)
		self.Show()

if __name__=='__main__':
	app = wx.App()
	fr = TestFrame(None, "Mi Frame")
	app.MainLoop()
