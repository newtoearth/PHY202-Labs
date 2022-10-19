import numpy as np

f = lambda x : x**2 - 5
h = 0.00001
D = lambda f,x : (f(x+h)-f(x))/h

def n_root(f,a,b):
	xn = b
	while(a < xn):
		if b < a:
			a,b = b,a
		if(abs(f(xn)) < 0.00000001):
			return xn
		if D(f,xn) == 0:
			print("No Root")
			return None
		xn -= f(xn)/D(f,xn)
	return None

x0 = n_root(f,-1,3)

print(x0)
