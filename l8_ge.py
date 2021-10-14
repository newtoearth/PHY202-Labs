import numpy as np

def gesolver(A,b):
	print(A)
	print('\n')
	n = len(b)
	C = np.zeros(n)
	for i in range(n):
		if A[i][i] == 0:
			print("divide by zero")
			break
		for j in range(i+1,n):
			if i != j:
				r = A[j][i]/A[i][i]
				for k in range(n+1):
					A[j][k] -= r*A[i][k]
				print(A)
				print('\n')

	C[n-1] = A[n-1][n]/A[n-1][n-1]
	A[n-1][n] /= A[n-1][n-1]
	for i in range(n-2,-1,-1):
		C[i] = A[i][n]
		for j in range(i+1,n):
			A[i][n] -= A[i][j]*C[j]
			C[i] -= A[i][j]*C[j]
		C[i] /= A[i][i]
		A[i][n] /= A[i][i]
		print(A)
		print('\n')

	print('Required Result is:')
	for p in range(n):
		print(str(b[p]) + ' = ' + str(C[p]))

A = np.array([[1.0,1.0,-1.0,7.0],[1.0,-1.0,2.0,3.0],[2.0,1.0,1.0,9.0]])
b = np.array(['x','y','z'])
gesolver(A,b)

# x+y-z = 7
# x-y+2z = 3
# 2x+y+z = 9