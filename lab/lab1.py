"""
---------------------------------------------------------------------

Universidad del Valle de Guatemala
Saúl Contreras	18409
Gráficas por Computadora
Lab 1: Filling any polygon 

This answer to the problem statement in the lab1
---------------------------------------------------------------------
"""

from render import Render

gl = Render()										
gl.CreateWindow(800,800)								

#Polygone 1:
gl.paint([(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)],gl.rgbToColor(0,1,1))

#Polygone 2:
gl.paint([(321, 335), (288, 286), (339, 251), (374, 302)],gl.rgbToColor(1,0,0))

#Polygone 3:
gl.paint([(377, 249), (411, 197), (436, 249)],gl.rgbToColor(0,1,0))

#Polygone 4:
gl.paint([(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52), 
	(750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230),
	(597, 215), (552, 214), (517, 144), (466, 180)],gl.rgbToColor(0,0,0))

#Polygone 5:
gl.paint([(682, 175), (708, 120), (735, 148), (739, 170)],gl.rgbToColor(1,1,1))


gl.finish('lab.bmp')								