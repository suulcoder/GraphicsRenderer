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
from Texture import Texture

gl = Render(1024,1024)
gl.load('./models/Bigmax.obj', (40, 0, 0), (12, 12, 20))
gl.display('Bigmax.bmp')