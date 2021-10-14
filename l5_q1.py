import numpy as np

def trapezoidal(f,a,b):
	h = 0.1
	n = (b - a) / h
	i = 0
	b = a + h
	for elem in range(int(n)):
		A = f(a)
		B = f(b)
		a += h
		b += h
		i += 0.5 * h * (A + B)
	return i

a,b = map(float,input().strip().split(' '))
I = trapezoidal(np.sin,a,b)
print(I)