"""
---------------------------------------------------------------------

Universidad del Valle de Guatemala
Saúl Contreras	18409
Gráficas por Computadora
SR3: models

This file is a test of the class render.py
---------------------------------------------------------------------
"""
from render import Render

gl = Render()										
gl.CreateWindow(2048,1024)
gl.clearColor(0,0,0)
gl.clear()
gl.color(1,1,1)
gl.load('./models/Bigmax.obj', (65, -5), (14, 14))
gl.finish('Bigmax.bmp')