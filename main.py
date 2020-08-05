"""
---------------------------------------------------------------------
Universidad del Valle de Guatemala
Saúl Contreras	18409
Gráficas por Computadora
Main: models
This file is a test of the class render.py
---------------------------------------------------------------------
"""

from render import Render

gl = Render(2048,1024)
gl.load('./models/Bigmax.obj', (65, -5, -5), (14, 14, 14))
gl.display('Bigmax.bmp')