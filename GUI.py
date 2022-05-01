# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class WINDOW_CONTRALLER
###########################################################################

class WINDOW_CONTROLLER ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Window Controller", pos = wx.DefaultPosition, size = wx.Size( 303,427 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		MAIN_LAYOUT = wx.FlexGridSizer( 3, 1, 0, 0 )
		MAIN_LAYOUT.SetFlexibleDirection( wx.BOTH )
		MAIN_LAYOUT.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		MAIN_LAYOUT.SetMinSize( wx.Size( 2,2 ) )
		UP_LAYOUT = wx.FlexGridSizer( 4, 3, 0, 0 )
		UP_LAYOUT.SetFlexibleDirection( wx.BOTH )
		UP_LAYOUT.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		UP_LAYOUT.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		A_B = wx.GridSizer( 1, 1, 0, 0 )

		self.TOP_VALUE = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 116,-1 ), wx.TE_CENTER|wx.TE_PROCESS_ENTER )
		A_B.Add( self.TOP_VALUE, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )


		UP_LAYOUT.Add( A_B, 1, wx.EXPAND, 5 )


		UP_LAYOUT.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		B_A = wx.GridSizer( 1, 1, 0, 0 )

		self.LEFT_VALUE = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 74,-1 ), wx.TE_CENTER|wx.TE_PROCESS_ENTER )
		B_A.Add( self.LEFT_VALUE, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )


		UP_LAYOUT.Add( B_A, 1, wx.EXPAND, 5 )

		B_B = wx.GridSizer( 2, 3, 0, 0 )

		self.BTU1 = wx.Button( self, wx.ID_ANY, u"1", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		B_B.Add( self.BTU1, 0, wx.ALL, 5 )

		self.BTU10 = wx.Button( self, wx.ID_ANY, u"10", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		B_B.Add( self.BTU10, 0, wx.ALL, 5 )

		self.BTU100 = wx.Button( self, wx.ID_ANY, u"100", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		B_B.Add( self.BTU100, 0, wx.ALL, 5 )

		self.BTD1 = wx.Button( self, wx.ID_ANY, u"-1", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		B_B.Add( self.BTD1, 0, wx.ALL, 5 )

		self.BTD10 = wx.Button( self, wx.ID_ANY, u"-10", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		B_B.Add( self.BTD10, 0, wx.ALL, 5 )

		self.BTD100 = wx.Button( self, wx.ID_ANY, u"-100", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		B_B.Add( self.BTD100, 0, wx.ALL, 5 )


		UP_LAYOUT.Add( B_B, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		B_C = wx.GridSizer( 1, 1, 0, 0 )

		self.RIGHT_VALUE = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 74,-1 ), wx.TE_CENTER|wx.TE_PROCESS_ENTER )
		B_C.Add( self.RIGHT_VALUE, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )


		UP_LAYOUT.Add( B_C, 1, wx.EXPAND, 5 )

		C_A = wx.GridSizer( 3, 2, 0, 0 )

		self.BLL1 = wx.Button( self, wx.ID_ANY, u"1", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		C_A.Add( self.BLL1, 0, wx.ALL, 5 )

		self.BLR1 = wx.Button( self, wx.ID_ANY, u"-1", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		C_A.Add( self.BLR1, 0, wx.ALL, 5 )

		self.BLL10 = wx.Button( self, wx.ID_ANY, u"10", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		C_A.Add( self.BLL10, 0, wx.ALL, 5 )

		self.BLR10 = wx.Button( self, wx.ID_ANY, u"-10", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		C_A.Add( self.BLR10, 0, wx.ALL, 5 )

		self.BLL100 = wx.Button( self, wx.ID_ANY, u"100", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		C_A.Add( self.BLL100, 0, wx.ALL, 5 )

		self.BLR100 = wx.Button( self, wx.ID_ANY, u"-100", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		C_A.Add( self.BLR100, 0, wx.ALL, 5 )


		UP_LAYOUT.Add( C_A, 1, 0, 5 )

		C_B = wx.GridSizer( 1, 1, 0, 0 )

		self.BOTTOM_VALUE = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 116,-1 ), wx.TE_CENTER|wx.TE_PROCESS_ENTER )
		C_B.Add( self.BOTTOM_VALUE, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )


		UP_LAYOUT.Add( C_B, 1, wx.EXPAND, 5 )

		C_C = wx.GridSizer( 3, 2, 0, 0 )

		self.BRL1 = wx.Button( self, wx.ID_ANY, u"-1", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		C_C.Add( self.BRL1, 0, wx.ALL, 5 )

		self.BRR1 = wx.Button( self, wx.ID_ANY, u"1", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		C_C.Add( self.BRR1, 0, wx.ALL, 5 )

		self.BRL10 = wx.Button( self, wx.ID_ANY, u"-10", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		C_C.Add( self.BRL10, 0, wx.ALL, 5 )

		self.BRR10 = wx.Button( self, wx.ID_ANY, u"10", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		C_C.Add( self.BRR10, 0, wx.ALL, 5 )

		self.BRL100 = wx.Button( self, wx.ID_ANY, u"-100", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		C_C.Add( self.BRL100, 0, wx.ALL, 5 )

		self.BRR100 = wx.Button( self, wx.ID_ANY, u"100", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		C_C.Add( self.BRR100, 0, wx.ALL, 5 )


		UP_LAYOUT.Add( C_C, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )


		UP_LAYOUT.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		D_B = wx.GridSizer( 2, 3, 0, 0 )

		self.BBU1 = wx.Button( self, wx.ID_ANY, u"-1", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		D_B.Add( self.BBU1, 0, wx.ALL, 5 )

		self.BBU10 = wx.Button( self, wx.ID_ANY, u"-10", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		D_B.Add( self.BBU10, 0, wx.ALL, 5 )

		self.BBU100 = wx.Button( self, wx.ID_ANY, u"-100", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		D_B.Add( self.BBU100, 0, wx.ALL, 5 )

		self.BBD1 = wx.Button( self, wx.ID_ANY, u"1", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		D_B.Add( self.BBD1, 0, wx.ALL, 5 )

		self.BBD10 = wx.Button( self, wx.ID_ANY, u"10", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		D_B.Add( self.BBD10, 0, wx.ALL, 5 )

		self.BBD100 = wx.Button( self, wx.ID_ANY, u"100", wx.Point( -1,-1 ), wx.Size( 32,32 ), 0 )
		D_B.Add( self.BBD100, 0, wx.ALL, 5 )


		UP_LAYOUT.Add( D_B, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		UP_LAYOUT.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		MAIN_LAYOUT.Add( UP_LAYOUT, 1, wx.EXPAND, 5 )

		DOWN_LAYOUT = wx.GridSizer( 1, 2, 0, 0 )

		self.xSET_WINDOW = wx.Button( self, wx.ID_ANY, u"Set Window", wx.DefaultPosition, wx.DefaultSize, 0 )
		DOWN_LAYOUT.Add( self.xSET_WINDOW, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.xRESET_WINDOW = wx.Button( self, wx.ID_ANY, u"Reset Window", wx.DefaultPosition, wx.DefaultSize, 0 )
		DOWN_LAYOUT.Add( self.xRESET_WINDOW, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		MAIN_LAYOUT.Add( DOWN_LAYOUT, 1, wx.EXPAND, 5 )

		B_LAYOUT = wx.GridSizer( 1, 1, 0, 0 )

		self.WINDOW_TITLE = wx.StaticText( self, wx.ID_ANY, u"xxx", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WINDOW_TITLE.Wrap( -1 )

		B_LAYOUT.Add( self.WINDOW_TITLE, 0, wx.ALL, 5 )


		MAIN_LAYOUT.Add( B_LAYOUT, 1, wx.EXPAND, 5 )


		self.SetSizer( MAIN_LAYOUT )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.TOP_VALUE.Bind( wx.EVT_TEXT_ENTER, self.SET_TOP )
		self.LEFT_VALUE.Bind( wx.EVT_TEXT_ENTER, self.SET_LEFT )
		self.BTU1.Bind( wx.EVT_BUTTON, self.TOP_SUB_1 )
		self.BTU10.Bind( wx.EVT_BUTTON, self.TOP_SUB_10 )
		self.BTU100.Bind( wx.EVT_BUTTON, self.TOP_SUB_100 )
		self.BTD1.Bind( wx.EVT_BUTTON, self.TOP_ADD_1 )
		self.BTD10.Bind( wx.EVT_BUTTON, self.TOP_ADD_10 )
		self.BTD100.Bind( wx.EVT_BUTTON, self.TOP_ADD_100 )
		self.RIGHT_VALUE.Bind( wx.EVT_TEXT_ENTER, self.SET_RIGHT )
		self.BLL1.Bind( wx.EVT_BUTTON, self.LEFT_SUB_1 )
		self.BLR1.Bind( wx.EVT_BUTTON, self.LEFT_ADD_1 )
		self.BLL10.Bind( wx.EVT_BUTTON, self.LEFT_SUB_10 )
		self.BLR10.Bind( wx.EVT_BUTTON, self.LEFT_ADD_10 )
		self.BLL100.Bind( wx.EVT_BUTTON, self.LEFT_SUB_100 )
		self.BLR100.Bind( wx.EVT_BUTTON, self.LEFT_ADD_100 )
		self.BOTTOM_VALUE.Bind( wx.EVT_TEXT_ENTER, self.SET_BOTTOM )
		self.BRL1.Bind( wx.EVT_BUTTON, self.RIGHT_SUB_1 )
		self.BRR1.Bind( wx.EVT_BUTTON, self.RIGHT_ADD_1 )
		self.BRL10.Bind( wx.EVT_BUTTON, self.RIGHT_SUB_10 )
		self.BRR10.Bind( wx.EVT_BUTTON, self.RIGHT_ADD_10 )
		self.BRL100.Bind( wx.EVT_BUTTON, self.RIGHT_SUB_100 )
		self.BRR100.Bind( wx.EVT_BUTTON, self.RIGHT_ADD_100 )
		self.BBU1.Bind( wx.EVT_BUTTON, self.BOTTOM_SUB_1 )
		self.BBU10.Bind( wx.EVT_BUTTON, self.BOTTOM_SUB_10 )
		self.BBU100.Bind( wx.EVT_BUTTON, self.BOTTOM_SUB_100 )
		self.BBD1.Bind( wx.EVT_BUTTON, self.BOTTOM_ADD_1 )
		self.BBD10.Bind( wx.EVT_BUTTON, self.BOTTOM_ADD_10 )
		self.BBD100.Bind( wx.EVT_BUTTON, self.BOTTOM_ADD_100 )
		self.xSET_WINDOW.Bind( wx.EVT_BUTTON, self.SET_WINDOW )
		self.xRESET_WINDOW.Bind( wx.EVT_BUTTON, self.RESET_WINDOW )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def SET_TOP( self, event ):
		event.Skip()

	def SET_LEFT( self, event ):
		event.Skip()

	def TOP_SUB_1( self, event ):
		event.Skip()

	def TOP_SUB_10( self, event ):
		event.Skip()

	def TOP_SUB_100( self, event ):
		event.Skip()

	def TOP_ADD_1( self, event ):
		event.Skip()

	def TOP_ADD_10( self, event ):
		event.Skip()

	def TOP_ADD_100( self, event ):
		event.Skip()

	def SET_RIGHT( self, event ):
		event.Skip()

	def LEFT_SUB_1( self, event ):
		event.Skip()

	def LEFT_ADD_1( self, event ):
		event.Skip()

	def LEFT_SUB_10( self, event ):
		event.Skip()

	def LEFT_ADD_10( self, event ):
		event.Skip()

	def LEFT_SUB_100( self, event ):
		event.Skip()

	def LEFT_ADD_100( self, event ):
		event.Skip()

	def SET_BOTTOM( self, event ):
		event.Skip()

	def RIGHT_SUB_1( self, event ):
		event.Skip()

	def RIGHT_ADD_1( self, event ):
		event.Skip()

	def RIGHT_SUB_10( self, event ):
		event.Skip()

	def RIGHT_ADD_10( self, event ):
		event.Skip()

	def RIGHT_SUB_100( self, event ):
		event.Skip()

	def RIGHT_ADD_100( self, event ):
		event.Skip()

	def BOTTOM_SUB_1( self, event ):
		event.Skip()

	def BOTTOM_SUB_10( self, event ):
		event.Skip()

	def BOTTOM_SUB_100( self, event ):
		event.Skip()

	def BOTTOM_ADD_1( self, event ):
		event.Skip()

	def BOTTOM_ADD_10( self, event ):
		event.Skip()

	def BOTTOM_ADD_100( self, event ):
		event.Skip()

	def SET_WINDOW( self, event ):
		event.Skip()

	def RESET_WINDOW( self, event ):
		event.Skip()


