from numpy import matrix
from matrix import Matrix

matrix1 = matrix([
	[0,0,0],
	[1,2,3],
	[2,1,3]
])

matrix2 = matrix([
	[2,0,0],
	[1,2,3],
	[2,1,3]
])

print( (matrix1 @ matrix2).tolist()[0])

matrix1 = Matrix([
	[0,0,0],
	[1,2,3],
	[2,1,3]
])


matrix2 = Matrix([
	[2,0,0],
	[1,2,3],
	[2,1,3]
])
print( matrix1.mul(matrix2).arg[0])