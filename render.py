"""
---------------------------------------------------------------------

Universidad del Valle de Guatemala
Saúl Contreras	18409
Gráficas por Computadora
SR1: Point

Render Class: This class is an BMP image renderer
---------------------------------------------------------------------
"""
import struct
import random
from encoder import *
from mathModule import *
from obj import Obj

def color(r, g, b):
  return bytes([b, g, r])

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)

class Render(object):
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.current_color = WHITE
    self.clear()

  def clear(self):
    self.pixels = [
      [BLACK for x in range(self.width)] 
      for y in range(self.height)
    ]
    self.zbuffer = [
      [-float('inf') for x in range(self.width)]
      for y in range(self.height)
    ]

  def write(self, filename):
    f = open(filename, 'bw')

    # File header (14 bytes)
    f.write(char('B'))
    f.write(char('M'))
    f.write(dword(14 + 40 + self.width * self.height * 3))
    f.write(dword(0))
    f.write(dword(14 + 40))

    # Image header (40 bytes)
    f.write(dword(40))
    f.write(dword(self.width))
    f.write(dword(self.height))
    f.write(word(1))
    f.write(word(24))
    f.write(dword(0))
    f.write(dword(self.width * self.height * 3))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))

    # Pixel data (width x height x 3 pixels)
    for x in range(self.height):
      for y in range(self.width):
        f.write(self.pixels[x][y])

    f.close()

  def display(self, filename='out.bmp'):
    self.write(filename)

    try:
      from wand.image import Image
      from wand.display import display

      with Image(filename=filename) as image:
        display(image)
    except ImportError:
      pass  # do nothing if no wand is installed

  def set_color(self, color):
    self.current_color = color

  def point(self, x, y, color = None):
    try:
      self.pixels[y][x] = color or self.current_color
    except:
      # To avoid index out of range exceptions
      pass

  def triangle(self, A, B, C, color=None, texture=None, texture_coords=(), intensity=1):
    bbox_min, bbox_max = bbox(A, B, C)

    for x in range(bbox_min.x, bbox_max.x + 1):
      for y in range(bbox_min.y, bbox_max.y + 1):
        w, v, u = barycentric(A, B, C, V2(x, y))
        if w < 0 or v < 0 or u < 0:  # 0 is actually a valid value! (it is on the edge)
          continue
        
        if texture:
          tA, tB, tC = texture_coords
          tx = tA.x * w + tB.x * v + tC.x * u
          ty = tA.y * w + tB.y * v + tC.y * u
          
          color = texture.get_color(tx, ty, intensity)

        z = A.z * w + B.z * v + C.z * u

        if x < 0 or y < 0:
          continue

        if x < len(self.zbuffer) and y < len(self.zbuffer[x]) and z > self.zbuffer[x][y]:
          self.point(x, y, color)
          self.zbuffer[x][y] = z

  def transform(self, vertex, translate=(0, 0, 0), scale=(1, 1, 1)):
    return V3(
      round((vertex[0] + translate[0]) * scale[0]),
      round((vertex[1] + translate[1]) * scale[1]),
      round((vertex[2] + translate[2]) * scale[2])
    )
    
  def load(self, filename, translate=(0, 0, 0), scale=(1, 1, 1), texture=None):
    model = Obj(filename)
    light = V3(0,0,1)

    for face in model.vfaces:
        vcount = len(face)

        if vcount == 3:
          f1 = face[0][0] - 1
          f2 = face[1][0] - 1
          f3 = face[2][0] - 1

          a = self.transform(model.vertices[f1], translate, scale)
          b = self.transform(model.vertices[f2], translate, scale)
          c = self.transform(model.vertices[f3], translate, scale)

          normal = norm(cross(sub(b, a), sub(c, a)))
          intensity = dot(normal, light)

          if not texture:
            grey = round(255 * intensity)
            if grey < 0:
              continue
            self.triangle(a, b, c, color=color(grey, grey, grey))
          else:
            t1 = face[0][1] - 1
            t2 = face[1][1] - 1
            t3 = face[2][1] - 1
            tA = V3(*model.tvertices[t1])
            tB = V3(*model.tvertices[t2])
            tC = V3(*model.tvertices[t3])

            self.triangle(a, b, c, texture=texture, texture_coords=(tA, tB, tC), intensity=intensity)
          
        else:
          # assuming 4
          f1 = face[0][0] - 1
          f2 = face[1][0] - 1
          f3 = face[2][0] - 1
          f4 = face[3][0] - 1   

          vertices = [
            self.transform(model.vertices[f1], translate, scale),
            self.transform(model.vertices[f2], translate, scale),
            self.transform(model.vertices[f3], translate, scale),
            self.transform(model.vertices[f4], translate, scale)
          ]

          normal = norm(cross(sub(vertices[0], vertices[1]), sub(vertices[1], vertices[2])))  # no necesitamos dos normales!!
          intensity = dot(normal, light)
          grey = round(255 * intensity)

          A, B, C, D = vertices 

          if not texture:
            grey = round(255 * intensity)
            if grey < 0:
              continue
            self.triangle(A, B, C, color(grey, grey, grey))
            self.triangle(A, C, D, color(grey, grey, grey))            
          else:
            t1 = face[0][1] - 1
            t2 = face[1][1] - 1
            t3 = face[2][1] - 1
            t4 = face[3][1] - 1
            tA = V3(*model.tvertices[t1])
            tB = V3(*model.tvertices[t2])
            tC = V3(*model.tvertices[t3])
            tD = V3(*model.tvertices[t4])
            
            self.triangle(A, B, C, texture=texture, texture_coords=(tA, tB, tC), intensity=intensity)
            self.triangle(A, C, D, texture=texture, texture_coords=(tA, tC, tD), intensity=intensity)
            
