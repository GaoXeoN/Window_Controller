# Windows Controller 1.0
# This script can move windows borders
# to use this script you have to install modules "keyboard" and "wx" (wxWidgets)

# python37 -m pip3.7 install keyboard
# python38 -m pip3.8 install keyboard
# python39 -m pip3.9 install keyboard

import time
import keyboard
import win32gui
import wx
from GUI import WINDOW_CONTROLLER

class Globala_Variabler:
	HWND = 0
	Window_Set = False
	Left = 0
	Right = 0
	Up = 0
	Down = 0

# add the gui and code to it
class WC( WINDOW_CONTROLLER ):

	def SET_WINDOW( self, event ):
		self.Get_Active_Window()

	def RESET_WINDOW( self, event ):
		self.Move_And_Resize_Window( Reset = True )



# set window size and position
	def SET_LEFT( self, event ):
		self.Move_And_Resize_Window( Set_Value = True, Left = self.LEFT_VALUE.GetValue() )

	def SET_TOP( self, event ):
		self.Move_And_Resize_Window( Set_Value = True, Up = self.TOP_VALUE.GetValue() )

	def SET_RIGHT( self, event ):
		self.Move_And_Resize_Window( Set_Value = True, Right = self.RIGHT_VALUE.GetValue() )

	def SET_BOTTOM( self, event ):
		self.Move_And_Resize_Window( Set_Value = True, Down = self.BOTTOM_VALUE.GetValue() )



# buttons for move window left
	def LEFT_ADD_1( self, event ):
		self.Move_And_Resize_Window( Left = 1 )

	def LEFT_ADD_10( self, event ):
		self.Move_And_Resize_Window( Left = 10 )

	def LEFT_ADD_100( self, event ):
		self.Move_And_Resize_Window( Left = 100 )

	def LEFT_SUB_1( self, event ):
		self.Move_And_Resize_Window( Left = -1 )

	def LEFT_SUB_10( self, event ):
		self.Move_And_Resize_Window( Left = -10 )

	def LEFT_SUB_100( self, event ):
		self.Move_And_Resize_Window( Left = -100 )



# buttons for move window up
	def TOP_ADD_1( self, event ):
		self.Move_And_Resize_Window( Up = 1 )

	def TOP_ADD_10( self, event ):
		self.Move_And_Resize_Window( Up = 10 )

	def TOP_ADD_100( self, event ):
		self.Move_And_Resize_Window( Up = 100 )

	def TOP_SUB_1( self, event ):
		self.Move_And_Resize_Window( Up = -1 )

	def TOP_SUB_10( self, event ):
		self.Move_And_Resize_Window( Up = -10 )

	def TOP_SUB_100( self, event ):
		self.Move_And_Resize_Window( Up = -100 )



# buttons for move window right
	def RIGHT_ADD_1( self, event ):
		self.Move_And_Resize_Window( Right = 1 )

	def RIGHT_ADD_10( self, event ):
		self.Move_And_Resize_Window( Right = 10 )

	def RIGHT_ADD_100( self, event ):
		self.Move_And_Resize_Window( Right = 100 )

	def RIGHT_SUB_1( self, event ):
		self.Move_And_Resize_Window( Right = -1 )

	def RIGHT_SUB_10( self, event ):
		self.Move_And_Resize_Window( Right = -10 )

	def RIGHT_SUB_100( self, event ):
		self.Move_And_Resize_Window( Right = -100 )




# buttons for move window down
	def BOTTOM_ADD_1( self, event ):
		self.Move_And_Resize_Window( Down = 1 )

	def BOTTOM_ADD_10( self, event ):
		self.Move_And_Resize_Window( Down = 10 )

	def BOTTOM_ADD_100( self, event ):
		self.Move_And_Resize_Window( Down = 100 )

	def BOTTOM_SUB_1( self, event ):
		self.Move_And_Resize_Window( Down = -1 )

	def BOTTOM_SUB_10( self, event ):
		self.Move_And_Resize_Window( Down = -10 )

	def BOTTOM_SUB_100( self, event ):
		self.Move_And_Resize_Window( Down = -100 )





	def Get_Active_Window( self ):
		global V
		Counter = 5
		while Counter > 0:
			self.Show_Info( Text = "Counting down: " + str( Counter ) )
			Counter -= 1
			time.sleep( 1 )
		try:
			V.HWND = win32gui.GetForegroundWindow()
			X = win32gui.GetWindowRect( V.HWND )
			V.Left = X[ 0 ]
			V.Up = X[ 1 ]
			#V.Right = X[ 2 ]
			#V.Down = X[ 3 ]
			V.Right = X[ 2 ] - X[ 0 ]
			V.Down = X[ 3 ] - X[ 1 ]
			self.LEFT_VALUE.Value = str( V.Left )
			self.TOP_VALUE.Value = str( V.Up )
			self.RIGHT_VALUE.Value = str( V.Right )
			self.BOTTOM_VALUE.Value = str( V.Down )
			V.Window_Set = True
			self.Show_Info()
			return True
		except:
			V.HWND = 0
			V.Window_Set = False
			self.Show_Info()
			return False

	def Move_And_Resize_Window( self, Reset = False, Set_Value = False, Left = 0, Up = 0, Right = 0, Down = 0 ):
		global V
		if( V.Window_Set ):
			if( Reset ):
				V.Left = 0
				V.Up = 0
				V.Right = 500
				V.Down = 500
			elif( Set_Value ):
				if( Left != 0 ):
					V.Right += Left - V.Left
					V.Left = Left
				if( Up != 0 ):
					V.Down += Up - V.Up
					V.Up = Up
				if( Right != 0 ):
					V.Right = Right
				if( Down != 0 ):
					V.Down = Down
			else:
				V.Left += Left
				V.Up += Up
				V.Right -= Left
				V.Down -= Up
				V.Right += Right
				V.Down += Down
			try:
				win32gui.MoveWindow( V.HWND, V.Left, V.Up, V.Right, V.Down, True )
				self.LEFT_VALUE.Value = str( V.Left )
				self.TOP_VALUE.Value = str( V.Up )
				self.RIGHT_VALUE.Value = str( V.Right )
				self.BOTTOM_VALUE.Value = str( V.Down )
				self.Show_Info()
				return True
			except:
				self.Show_Info()
				return False
		else:
			return False

	def Show_Info( self, Text = "" ):
		global V
		if( Text == "" ):
			self.WINDOW_TITLE.Label = "<NO WINDOW SET>"
			if( V.Window_Set ):
				try:
					X = win32gui.GetWindowText( V.HWND )
					if( len( X ) > 0 ):
						self.WINDOW_TITLE.Label = X
					return True
				except:
					self.WINDOW_TITLE.Label = "<NO WINDOW SET>"
					return False
			else:
				return False
		else:
			self.WINDOW_TITLE.Label = Text
			return True



# load all global variables into V
V = Globala_Variabler()

# load the wxWidgets into App
App = wx.App()

# load GUI in to F
F = WC( None )

# show the app (window)
F.Show()

# load the info about selected window
F.Show_Info()

# run the app (wait for user action)
App.MainLoop()
