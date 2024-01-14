from graphics import *   #import the graphics.py module (must be in the same folder this file)


#OPEN THE WINDOW
win = GraphWin("My First Graphics Window", 900, 900)#open a window object called "win" with size and title
win.setBackground("Mint Cream")# Set the background colour of the window

#hold the window until user clicks the mouse
win.getMouse()

#close the window
win.close()

