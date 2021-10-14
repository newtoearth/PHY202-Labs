import numpy as np

def simpson(f,a,b):
	h = 0.1
	n = (b - a) / h
	i = 0
	b = a + h
	for elem in range(int(n)):
		A = f(a)
		B = f(b)
		C = f((a + b) / 2)
		a += h
		b += h
		i += (h * (A + (4 * C) + B)) / 6
	return i

a,b = map(float,input().strip().split(' '))
I = simpson(np.sin,a,b)
print(I)