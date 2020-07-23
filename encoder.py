"""
---------------------------------------------------------------------

Universidad del Valle de Guatemala
Saúl Contreras	18409
Gráficas por Computadora
SR1: Point

This is an ecoder Module it has 3 functions
	char: its util to convert a caracter in to ascii byte
	world: its useful to encode into word byte
	dword: its useful to encode into double world byte

---------------------------------------------------------------------
"""

import struct

def char(myChar):
		return struct.pack('=c', myChar.encode('ascii'))

def word(myChar):
	return struct.pack('=h', myChar)
	
def dword(myChar):
	return struct.pack('=l', myChar)

