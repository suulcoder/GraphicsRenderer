"""
---------------------------------------------------------------------
Universidad del Valle de Guatemala
Saúl Contreras	18409
Gráficas por Computadora
Main: models
This file is an scene built to be the cover of a Science
fiction book:
Lumbre distante
---------------------------------------------------------------------
"""

from render import Render, color
from Texture import Texture
from mathModule import V3, norm
from shaders import mountain, fragment, moon, planet, stars, water
import random
import math

r = Render(800, 800)
out = 'out.bmp'


"""

Firstable we set the camera, and the angle where it is watching

"""

r.lookAt(V3(0, 0, 10), V3(0, 0, 0), V3(0, 1, 0))


"""

Then we Draw the stars in the sky, using a shader that use a random generator of
white points, and that random has lower probability when y is greater. 

"""
stars(r)
		
"""

We draw to moons, using an sphere model, each one has different texture
and differnt shader to produce the effect of an celestial body. This models
were made using bump mapping. 


"""

#Draw the moon Iscaco
t = Texture('./models/iscalo.bmp')
r.active_texture = t
r.active_light = norm(V3(0, 20, 0))
r.load('./models/sphere.obj', [-0.55, 0.70, 0], [0.22, 0.22, 0.22], [0, 0.2, 0])
r.active_shader = moon
r.draw_arrays('TRIANGLES') 

#Draw the moon Urica
t = Texture('./models/urica.bmp')
r.active_texture = t
r.load('./models/sphere.obj', [0.57, 0.80, 0], [0.20, 0.20, 0.20], [0, 0.2, 0])
r.active_shader = planet
r.draw_arrays('TRIANGLES') 


"""

We use model.bmp that is a face, to draw some mountains in the background, in 
this way we use just the back and top part of the face. We generate 30 faces of 
different sizes, to get the effect of mountains Sometimes this will develop a bad
effect because of random

"""

#Draw ground
t = Texture('./models/model.bmp')
r.active_texture = t
r.active_shader = mountain
random.seed(1)
for i in range(0,30):
	size = random.random()/4
	r.load('./models/model.obj', [-i/30, math.sin((30*i))*0.1, 0], [size,size, size], [0, 1.7, 1.1])
	r.draw_arrays('TRIANGLES')

"""

We draw this creature using the brasaleo model to generate the weird creature
using the shader fragment

"""


#Draw a brasaleo
print("brasaleo")
t = Texture('./models/fire2.bmp')
r.active_texture = t
r.active_light = norm(V3(10, 20, 0))
r.load('./models/brasaleo.obj', [-0.75, 0, 1], [0.02, 0.01, 0.01], [0, 0.7, 0])
r.active_shader = fragment
r.draw_arrays('TRIANGLES') 


"""

We draw an effect of reflection in the to simulate water, it change a liite bit the
color, using a shader. 

"""

water(r)



r.display(out)