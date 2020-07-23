"""
---------------------------------------------------------------------

Universidad del Valle de Guatemala
Saúl Contreras	18409
Gráficas por Computadora
SR2: Lines

This file is a test of the class render.py
---------------------------------------------------------------------
"""

from render import Render

gl = Render()										
gl.CreateWindow(600,300)								
gl.viewPort(300, 0, 300, 150)						#ViewPort should be the fourth quadrant of the image
gl.line(-1,0,0,1)									#Should draw a line in the left top corner of the view port. 
gl.line(-1,0,0,-1)
gl.line(1,0,0,-1)
gl.line(1,0,0,1)
gl.line(0,1,0,-1)
gl.line(1,0,-1,0)
gl.finish('test.bmp')								