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

r = Render(800, 600)
t = Texture('./models/model.bmp')
r.load('./models/sphere.obj', (0.7, 0.7, 0), (400, 400, 300), texture=t)
r.display('out.bmp')