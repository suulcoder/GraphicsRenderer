import math
import random

def color(r,g,b):
  return bytes([b,g,r])

class Shader(object):
	def __init__(self):
		self.red = [3,14,80]
		self.blue = [130,88,44]
		self.blue2 = [255,0,44]
		self.gray = [200,200,200]

	def move(self):
		current = self.next_count
		self.next_count += self.current_count
		self.current_count = current

	def normal(self,x,y):
		return int(math.sqrt(x*x + y*y))

	def drawAmerica(self,x,y):
		return (
			self.normal(x-200,y-230)<35 or
			self.normal(x-230,y-280)<14 or
			self.normal(x-290,y-150)<5 or
			self.normal(x-100,y-190)<39 or
			self.normal(x-410,y-160)<28 or
			self.normal(x-201,y-210)<14 or
			self.normal(x-215,y-120)<5 or
			self.normal(x-201,y-130)<11 or
			self.normal(x-284,y-140)<18 or
			self.normal(x-301,y-210)<14 or
			self.normal(x-315,y-320)<5 or
			self.normal(x-301,y-330)<11 or
			self.normal(x-384,y-340)<18 or
			self.normal(x-210,y-260)<28 or
			self.normal(x-221,y-310)<14 or
			self.normal(x-235,y-320)<29 or
			self.normal(x-241,y-330)<21 or
			self.normal(x-254,y-300)<28 or
			self.normal(x-261,y-310)<24 or
			self.normal(x-215,y-320)<23 or
			self.normal(x-201,y-330)<21 or
			self.normal(x-294,y-310)<28 or
			self.normal(x-221,y-310)<24 or
			self.normal(x-255,y-320)<21 or
			self.normal(x-261,y-330)<21 or
			self.normal(x-274,y-300)<28 or
			self.normal(x-381,y-310)<24 or
			self.normal(x-395,y-320)<25 or
			self.normal(x-301,y-330)<21 or
			self.normal(x-304,y-310)<28 or
			self.normal(x-310,y-310)<28 or
			self.normal(x-321,y-310)<14 or
			self.normal(x-335,y-320)<29 or
			self.normal(x-341,y-330)<21 or
			self.normal(x-354,y-300)<28 or
			self.normal(x-361,y-310)<24 or
			self.normal(x-315,y-320)<23 or
			self.normal(x-301,y-330)<21 or
			self.normal(x-394,y-310)<28 or
			self.normal(x-321,y-310)<24 or
			self.normal(x-355,y-320)<21 or
			self.normal(x-361,y-330)<21 or
			self.normal(x-374,y-300)<28 or
			self.normal(x-381,y-310)<24 or
			self.normal(x-395,y-320)<25 or
			self.normal(x-301,y-330)<21 or
			self.normal(x-304,y-310)<28 or
			self.normal(x-255,y-320)<21 or
			self.normal(x-261,y-330)<21 or
			self.normal(x-274,y-300)<28 or
			self.normal(x-381,y-110)<24 or
			self.normal(x-395,y-120)<25 or
			self.normal(x-301,y-130)<21 or
			self.normal(x-304,y-110)<28 or
			self.normal(x-310,y-110)<28 or
			self.normal(x-321,y-110)<14 or
			self.normal(x-335,y-120)<29 or
			self.normal(x-341,y-130)<21 or
			self.normal(x-354,y-100)<28 or
			self.normal(x-361,y-110)<24 or
			self.normal(x-315,y-120)<23 or
			self.normal(x-301,y-130)<21 or
			self.normal(x-394,y-110)<28 or
			self.normal(x-321,y-110)<24 or
			self.normal(x-355,y-120)<21 or
			self.normal(x-361,y-130)<21 or
			self.normal(x-374,y-100)<28 or
			self.normal(x-381,y-110)<24 or
			self.normal(x-395,y-120)<25 or
			self.normal(x-301,y-130)<21 or
			self.normal(x-304,y-110)<28 or
			self.normal(x-221,y-310)<24 or
			self.normal(x-255,y-320)<21 or
			self.normal(x-261,y-330)<21 or
			self.normal(x-274,y-300)<28 or
			self.normal(x-381,y-310)<24 or
			self.normal(x-395,y-320)<25 or
			self.normal(x-301,y-330)<21 or
			self.normal(x-304,y-310)<28 or
			self.normal(x-310,y-310)<38 or
			self.normal(x-321,y-310)<34 or
			self.normal(x-335,y-320)<39 or
			self.normal(x-341,y-330)<31 or
			self.normal(x-354,y-300)<38 or
			self.normal(x-361,y-310)<34 or
			self.normal(x-315,y-320)<33 or
			self.normal(x-301,y-330)<31 or
			self.normal(x-394,y-310)<8 or
			self.normal(x-321,y-310)<24 or
			self.normal(x-355,y-320)<21 or
			self.normal(x-361,y-330)<21 or
			self.normal(x-374,y-300)<28 or
			self.normal(x-381,y-310)<24 or
			self.normal(x-395,y-320)<25 or
			self.normal(x-301,y-330)<21 or
			self.normal(x-304,y-310)<38 or
			self.normal(x-255,y-320)<31 or
			self.normal(x-261,y-330)<31 or
			self.normal(x-274,y-300)<38 or
			self.normal(x-381,y-110)<34 or
			self.normal(x-395,y-120)<35 or
			self.normal(x-301,y-130)<21 or
			self.normal(x-304,y-110)<28 or
			self.normal(x-310,y-110)<28 or
			self.normal(x-321,y-110)<14 or
			self.normal(x-335,y-120)<29 or
			self.normal(x-341,y-130)<21 or
			self.normal(x-254,y-300)<28 or
			self.normal(x-261,y-310)<24 or
			self.normal(x-215,y-320)<23 or
			self.normal(x-201,y-330)<21 or
			self.normal(x-294,y-310)<28 or
			self.normal(x-221,y-310)<24 or
			self.normal(x-255,y-320)<21 or
			self.normal(x-261,y-330)<21 or
			self.normal(x-274,y-300)<28 or
			self.normal(x-381,y-310)<24 or
			self.normal(x-395,y-320)<25 or
			self.normal(x-301,y-330)<21 or
			self.normal(x-304,y-310)<28 or
			self.normal(x-310,y-310)<28 or
			self.normal(x-321,y-310)<14 or
			self.normal(x-335,y-320)<29 or
			self.normal(x-341,y-330)<21 or
			self.normal(x-354,y-300)<28 or
			self.normal(x-361,y-310)<24 or
			self.normal(x-315,y-320)<23 or
			self.normal(x-301,y-330)<21 or
			self.normal(x-394,y-310)<28 or
			self.normal(x-321,y-310)<24 or
			self.normal(x-355,y-320)<21 or
			self.normal(x-361,y-330)<21 or
			self.normal(x-374,y-300)<28 or
			self.normal(x-381,y-310)<24 or
			self.normal(x-395,y-320)<25 or
			self.normal(x-301,y-330)<21 or
			self.normal(x-304,y-310)<28 or
			self.normal(x-255,y-320)<21 or
			self.normal(x-261,y-330)<21 or
			self.normal(x-274,y-300)<28 or
			self.normal(x-381,y-110)<24 or
			self.normal(x-395,y-120)<25 or
			self.normal(x-301,y-130)<21 or
			self.normal(x-304,y-110)<28 or
			self.normal(x-310,y-110)<28 or
			self.normal(x-321,y-110)<14 or
			self.normal(x-335,y-120)<29 or
			self.normal(x-341,y-130)<21 or
			self.normal(x-354,y-100)<28 or
			self.normal(x-361,y-110)<24 or
			self.normal(x-315,y-120)<23 or
			self.normal(x-301,y-130)<21 or
			self.normal(x-394,y-110)<28 or
			self.normal(x-321,y-110)<24 or
			self.normal(x-355,y-120)<41 or
			self.normal(x-361,y-130)<41 or
			self.normal(x-374,y-100)<48 or
			self.normal(x-381,y-110)<44 or
			self.normal(x-395,y-120)<45 or
			self.normal(x-301,y-130)<41 or
			self.normal(x-304,y-110)<48 or
			self.normal(x-221,y-310)<44 or
			self.normal(x-255,y-320)<41 or
			self.normal(x-261,y-330)<41 or
			self.normal(x-274,y-300)<48 or
			self.normal(x-381,y-310)<44 or
			self.normal(x-395,y-320)<45 or
			self.normal(x-301,y-130)<41 or
			self.normal(x-304,y-110)<48 or
			self.normal(x-310,y-110)<48 or
			self.normal(x-321,y-110)<44 or
			self.normal(x-335,y-120)<49 or
			self.normal(x-341,y-130)<41 or
			self.normal(x-354,y-100)<48 or
			self.normal(x-361,y-110)<44 or
			self.normal(x-315,y-120)<43 or
			self.normal(x-301,y-130)<41 or
			self.normal(x-394,y-110)<8 or
			self.normal(x-355,y-20)<41 or
			self.normal(x-361,y-30)<41 or
			self.normal(x-374,y-70)<48 or
			self.normal(x-381,y-110)<44 or
			self.normal(x-395,y-120)<45 or
			self.normal(x-301,y-130)<41 or
			self.normal(x-304,y-110)<48 or
			self.normal(x-221,y-210)<44 or
			self.normal(x-255,y-220)<41 or
			self.normal(x-261,y-230)<41 or
			self.normal(x-274,y-200)<48 or
			self.normal(x-355,y-20)<41 or
			self.normal(x-361,y-30)<41 or
			self.normal(x-374,y-00)<48 or
			self.normal(x-381,y-10)<44 or
			self.normal(x-395,y-20)<45 or
			self.normal(x-301,y-30)<41 or
			self.normal(x-304,y-10)<48 or
			self.normal(x-221,y-210)<44 or
			self.normal(x-255,y-220)<41 or
			self.normal(x-261,y-230)<41 or
			self.normal(x-274,y-200)<48 or
			self.normal(x-381,y-210)<44 or
			self.normal(x-395,y-220)<45 or
			self.normal(x-301,y-30)<41 
			)

	def Gliese(self,x, y, tx, ty, intensity):
		#Change the intesity to simulate a star on Gliese
		intensity = 9*y*y*intensity/(x*x*40)
		normal=self.normal(x,y)
		if(random.randint(0,normal)<100):
			tx=tx*500
			ty=ty*500
			if x*tx%55>8:
				try:
					return bytes(map(lambda b: round(b*intensity) if b*intensity*(x/400) > 0 else 0, self.blue))
				except:
					pass
			elif tx%144>21:
				try:
					return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.blue2))
				except:
					pass
			else:
				try:
					return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.blue2))
				except:
					pass
		elif(random.randint(0,normal)<200):
			tx=tx*500
			ty=ty*500
			if(x/y<400 or random.randint(0,normal)<100):
				if x*tx%21>13:
					try:
						return bytes(map(lambda b: round(b*intensity) if b*intensity*(x/400) > 0 else 0, self.blue))
					except:
						pass
				elif tx%144>21:
					try:
						return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.gray))
					except:
						pass
				else:
					try:
						return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.blue2))
					except:
						pass
		else:
			tx=tx*500
			ty=ty*500
			if x*tx%55>8:
				if(self.drawAmerica(x,y)):
					try:
						return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.red))
					except:
						pass
				else:
					try:
						return bytes(map(lambda b: round(b*intensity) if b*intensity*(x/400) > 0 else 0, self.blue))
					except:
						pass
			elif tx%89>55:
				try:
					return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.red))
				except:
					pass
			else:
				try:
					return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.blue))
				except:
					pass